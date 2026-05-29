from app.utils.crud import query_all


def _normalize_budget_value(value):
    if value is None:
        return None
    try:
        return float(value)
    except Exception:
        return None


def _in_budget_range(car, budget_min, budget_max):
    car_min = float(car.get('seriesminprice') or 0)
    car_max = float(car.get('seriesmaxprice') or 0)

    if (budget_max is not None and budget_max <= 2000) or (budget_min is not None and budget_min <= 2000):
        car_min = car_min / 1000
        car_max = car_min

    if budget_min is not None and car_max < budget_min:
        return False
    if budget_max is not None and car_min > budget_max:
        return False
    return True


def _seat_score(car_seats, desired_seats):
    try:
        desired = int(desired_seats)
    except Exception:
        return 0

    if desired <= 0:
        return 0

    try:
        seats = int(car_seats)
    except Exception:
        return 0

    diff = abs(seats - desired)
    if diff == 0:
        return 12
    if diff == 1:
        return 8
    if diff == 2:
        return 4
    return 0


def _calc_match_score(car, budget_min, budget_max, use_case='', config_need='', seat_count=None):
    score = 0
    min_price = car['seriesminprice']
    max_price = car['seriesmaxprice']
    use_case_text = (use_case or '').lower()
    config_text = (config_need or '').lower()
    car_feature = (car.get('feature') or '').lower()

    # 1. 预算匹配（核心，保留）
    if budget_min is not None and max_price >= budget_min:
        score += 40
    if budget_max is not None and min_price <= budget_max:
        score += 40
    
    # 2. 车型评分（保留）
    score += int(car.get('average', 0))*0.4

    # ====================== 关联规则 ======================
    # 规则1：商务接待场景 → 商务标签、MPV、豪华车型，都是你有的标签
    if any(x in use_case_text for x in ['商务', '接待', '会议', '高端']):
        if '商务' in car_feature:
            score += 8
        if 'mpv' in car_feature:
            score += 6
        if '豪华' in car_feature:
            score += 4

    # 规则2：长途/自驾场景 → 新能源/混动（省油）、四驱（稳）、SUV（空间），都是你有的
    if any(x in use_case_text for x in ['长途', '自驾', '跨省', '高速']):
        if any(x in car_feature for x in ['新能源', '插电混动', '增程式电动']):
            score += 7
        if '四驱' in car_feature:
            score += 5
        if 'suv' in car_feature:
            score += 3

    # 规则3：多人/全家出行 → MPV、商务大空间，都是你有的
    if any(x in use_case_text for x in ['多人', '全家', '亲友', '团体']):
        if 'mpv' in car_feature:
            score += 10
        if '商务' in car_feature:
            score += 4

    # 规则4：越野/户外场景 → 越野车型、四驱，都是你有的
    if any(x in use_case_text for x in ['越野', '户外', '露营', '山路']):
        if '越野' in car_feature:
            score += 10
        if '四驱' in car_feature:
            score += 6

    # 规则5：日常代步/通勤 → 经济、新能源、小车，都是你有的
    if any(x in use_case_text for x in ['代步', '日常', '通勤', '市区', '短途']):
        if '经济' in car_feature:
            score += 8
        if '新能源' in car_feature:
            score += 5
        if '轿车' in car_feature:
            score += 3

    # 规则6：舒适出行 → 舒适、豪华标签，都是你有的
    if any(x in use_case_text for x in ['舒适', '舒服', '平稳']):
        if '舒适' in car_feature:
            score += 8
        if '豪华' in car_feature:
            score += 4

    # 规则7：性能驾驶 → 后驱/四驱、豪华，都是你有的
    if any(x in use_case_text for x in ['性能', '驾驶', '运动', '提速']):
        if any(x in car_feature for x in ['后驱', '四驱']):
            score += 7
        if '豪华' in car_feature:
            score += 5

    # 规则8：性价比租车 → 经济标签，都是你有的
    if any(x in use_case_text for x in ['性价比', '省钱', '便宜', '实惠']):
        if '经济' in car_feature:
            score += 10

    # 规则9：新能源需求 → 新能源/混动，都是你有的
    if any(x in config_text for x in ['新能源', '电车', '电动车', '混动', '纯电']):
        if any(x in car_feature for x in ['新能源', '插电混动', '增程式电动']):
            score += 12
    # 规则10
    if any(x in use_case_text for x in ['搬家', '拉货', '大件', '运输', '拉东西']):
        if '经济' in car_feature:
            score += 10
        if '货车' in car_feature:
            score += 10
        if '皮卡' in car_feature:
            score += 10

    # ====================== 配置需求匹配，纯feature，无车系名 ======================
    if config_text:
        # 仅匹配你实际有的feature标签，完全不碰车名
        if config_text in car_feature:
            score += 12

    # 座位匹配（保留）
    score += _seat_score(car.get('seat_count'), seat_count)
    return score


def build_recommend_list(budget_min=None, budget_max=None, seat_count=None, use_case='', config_need='', order_by='match_score'):
    sql = """
    SELECT id, seriesid, seriesname, seriesimg, seriesminprice, seriesmaxprice, seat_count, average, feature
    FROM car_series
    """
    cars = query_all(sql)
# 把用户的预算标准化，转成正常的数字
    budget_min = _normalize_budget_value(budget_min)
    budget_max = _normalize_budget_value(budget_max)

    results = []
    for car in cars:
        item = dict(car)
        if not _in_budget_range(item, budget_min, budget_max):
            continue
        item['rental_price_day'] = round((item.get('seriesminprice') or 0) / 1000, 2)#定价
        item['match_score'] = _calc_match_score(item, budget_min, budget_max, use_case, config_need, seat_count)
        item['cost_performance'] = round(item.get('average', 0) * 100000 / max(item['seriesminprice'], 1), 4)
        results.append(item)

    if order_by == 'cost_performance':
        results.sort(key=lambda x: x['cost_performance'], reverse=True)
    else:
        results.sort(key=lambda x: x['match_score'], reverse=True)

    return results