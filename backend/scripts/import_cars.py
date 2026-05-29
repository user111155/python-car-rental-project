import os#Python内置的操作系统接口模块，专门用来处理文件和目录路径
import sys#Python 内置的系统模块，用来访问 Python 解释器的运行环境
#  获取当前脚本的目录，以及上级的backend目录  
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.dirname(CURRENT_DIR)
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from app.utils.db import get_conn

data = [
    {
        'seriesid': 6962,
        'seriesname': '小米SU7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M03/1C/22/autohomecar__ChxpVWm71bKAIXDYACrJkPzrxfY598.png',
        'seriesminprice': 219900,
        'seriesmaxprice': 303900,
        'average': 4.5135,
        'specids': '[75668, 76173, 75667]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 5769,
        'seriesname': 'Model Y',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M06/77/D5/autohomecar__ChxoHWeS9caAf5JGAAaDqTsVyiE464.png',
        'seriesminprice': 263500,
        'seriesmaxprice': 313500,
        'average': 4.4496,
        'specids': '[76156, 76158, 76157]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 8171,
        'seriesname': '钛7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M01/66/51/autohomecar__ChxknGhZNDeAZ_tCAAcajawlkNE378.png',
        'seriesminprice': 179800,
        'seriesmaxprice': 219800,
        'average': 4.5796,
        'specids': '[73386, 73546, 74645, 74646]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 7806,
        'seriesname': '星愿',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M07/52/53/autohomecar__ChxpV2j18I-AbhS1ACdsTtsNeoQ722.png',
        'seriesminprice': 68800,
        'seriesmaxprice': 98800,
        'average': 4.5656,
        'specids': '[75134, 75146, 75136, 75137, 75147, 75135]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 6643,
        'seriesname': '问界M7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M02/1F/E7/autohomecar__ChtpWGixQfKAQzqhADO6WIGyDZ4979.png',
        'seriesminprice': 249800,
        'seriesmaxprice': 389800,
        'average': 4.5451,
        'specids': '[76252, 74367, 69375, 74565, 73993, 74163, 76945, 76955, 74568, 69377, 76951, 74566, 74571, 74570, 76949, 76948, 76954, 76947, 74161, 76950, 76251, 76944, 76946, 76953, 76952, 74567, 74569, 74162, 69376]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 8433,
        'seriesname': '零跑A10',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M03/75/C0/autohomecar__ChxpVWnFCLeABlmRADCoonpIsWY002.png',
        'seriesminprice': 65800,
        'seriesmaxprice': 86800,
        'average': 0.0,
        'specids': '[77022, 75800, 75799, 75689]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 8511,
        'seriesname': '宋Ultra EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M01/56/B8/autohomecar__ChxpVmmmziyAB7PDAGXLDCr8VSM868.png',
        'seriesminprice': 151900,
        'seriesmaxprice': 179900,
        'average': 0.0,
        'specids': '[76235, 76676, 76723, 76234]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 6762,
        'seriesname': '海鸥',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M06/86/A7/autohomecar__CjIFU2drcTKAVmEvAAbZv39X-1g635.png',
        'seriesminprice': 69800,
        'seriesmaxprice': 85800,
        'average': 4.5098,
        'specids': '[71690, 73635, 71065, 71691]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 5964,
        'seriesname': '秦PLUS',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M0B/58/A2/autohomecar__ChxoHmXVw2qAaWiuAAg1C-bg8-c383.png',
        'seriesminprice': 79800,
        'seriesmaxprice': 179800,
        'average': 4.4114,
        'specids': '[65656, 71689, 71685, 71687, 72524, 76199, 71504, 76177, 72103, 74866, 76109, 71688, 74790, 74863, 71686, 63012, 51966, 72442]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 6651,
        'seriesname': 'MG4',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M04/FA/20/autohomecar__CjIFV2h-B3uAK5ZgAAa68ant0y8517.png',
        'seriesminprice': 68800,
        'seriesmaxprice': 102800,
        'average': 4.4974,
        'specids': '[73923, 72246, 73922, 72245, 74109]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 5346,
        'seriesname': 'Model 3',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M0A/98/B3/autohomecar__CjIFU2VuxAiAMliVAAdeidm7fSE232.png',
        'seriesminprice': 235500,
        'seriesmaxprice': 339500,
        'average': 4.4264,
        'specids': '[75116, 75118, 75117, 75119]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 7724,
        'seriesname': '铂智7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M01/CE/1B/autohomecar__ChxpV2jCkvmAebgpAB-ypM54-w0332.png',
        'seriesminprice': 169800,
        'seriesmaxprice': 229800,
        'average': 0.0,
        'specids': '[76712, 76705, 76713, 72767, 76711]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 8087,
        'seriesname': '海狮06',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M0A/DC/87/autohomecar__ChxpVmjCloKASFuOACCEH6lEguE491.png',
        'seriesminprice': 139800,
        'seriesmaxprice': 179900,
        'average': 4.4975,
        'specids': '[73630, 73633, 76682, 76652, 73631, 72638, 73709, 73632, 76224, 76681]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 8232,
        'seriesname': 'iCAR V27',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M09/C7/26/autohomecar__ChxpVmlx5hiAfJjEAGNBv0U-6xI529.png',
        'seriesminprice': 169800,
        'seriesmaxprice': 196800,
        'average': 4.1428,
        'specids': '[76415, 74039, 76273]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 8462,
        'seriesname': '海豹07 EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M04/C2/E9/autohomecar__ChxpVmmyhkiAe--yACXFPffVKZg472.png',
        'seriesminprice': 169900,
        'seriesmaxprice': 189900,
        'average': 0.0,
        'specids': '[75935, 76710]',
        'create_time': '2026-04-01 02:36:03'
    },
    {
        'seriesid': 6962,
        'seriesname': '小米SU7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M03/1C/22/autohomecar__ChxpVWm71bKAIXDYACrJkPzrxfY598.png',
        'seriesminprice': 219900,
        'seriesmaxprice': 303900,
        'average': 4.5135,
        'specids': '[75668, 76173, 75667]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 5769,
        'seriesname': 'Model Y',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M06/77/D5/autohomecar__ChxoHWeS9caAf5JGAAaDqTsVyiE464.png',
        'seriesminprice': 263500,
        'seriesmaxprice': 313500,
        'average': 4.4496,
        'specids': '[76156, 76158, 76157]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8171,
        'seriesname': '钛7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M01/66/51/autohomecar__ChxknGhZNDeAZ_tCAAcajawlkNE378.png',
        'seriesminprice': 179800,
        'seriesmaxprice': 219800,
        'average': 4.5796,
        'specids': '[73386, 73546, 74645, 74646]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7806,
        'seriesname': '星愿',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M07/52/53/autohomecar__ChxpV2j18I-AbhS1ACdsTtsNeoQ722.png',
        'seriesminprice': 68800,
        'seriesmaxprice': 98800,
        'average': 4.5656,
        'specids': '[75134, 75146, 75136, 75137, 75147, 75135]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 6643,
        'seriesname': '问界M7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M02/1F/E7/autohomecar__ChtpWGixQfKAQzqhADO6WIGyDZ4979.png',
        'seriesminprice': 249800,
        'seriesmaxprice': 389800,
        'average': 4.5451,
        'specids': '[76252, 74367, 69375, 74565, 73993, 74163, 76945, 76955, 74568, 69377, 76951, 74566, 74571, 74570, 76949, 76948, 76954, 76947, 74161, 76950, 76251, 76944, 76946, 76953, 76952, 74567, 74569, 74162, 69376]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8433,
        'seriesname': '零跑A10',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M03/75/C0/autohomecar__ChxpVWnFCLeABlmRADCoonpIsWY002.png',
        'seriesminprice': 65800,
        'seriesmaxprice': 86800,
        'average': 0.0,
        'specids': '[77022, 75800, 75799, 75689]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8511,
        'seriesname': '宋Ultra EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M01/56/B8/autohomecar__ChxpVmmmziyAB7PDAGXLDCr8VSM868.png',
        'seriesminprice': 151900,
        'seriesmaxprice': 179900,
        'average': 0.0,
        'specids': '[76235, 76676, 76723, 76234]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 6762,
        'seriesname': '海鸥',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M06/86/A7/autohomecar__CjIFU2drcTKAVmEvAAbZv39X-1g635.png',
        'seriesminprice': 69800,
        'seriesmaxprice': 85800,
        'average': 4.5098,
        'specids': '[71690, 73635, 71065, 71691]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 5964,
        'seriesname': '秦PLUS',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M0B/58/A2/autohomecar__ChxoHmXVw2qAaWiuAAg1C-bg8-c383.png',
        'seriesminprice': 79800,
        'seriesmaxprice': 179800,
        'average': 4.4114,
        'specids': '[65656, 71689, 71685, 71687, 72524, 76199, 71504, 76177, 72103, 74866, 76109, 71688, 74790, 74863, 71686, 63012, 51966, 72442]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 6651,
        'seriesname': 'MG4',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M04/FA/20/autohomecar__CjIFV2h-B3uAK5ZgAAa68ant0y8517.png',
        'seriesminprice': 68800,
        'seriesmaxprice': 102800,
        'average': 4.4974,
        'specids': '[73923, 72246, 73922, 72245, 74109]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 5346,
        'seriesname': 'Model 3',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M0A/98/B3/autohomecar__CjIFU2VuxAiAMliVAAdeidm7fSE232.png',
        'seriesminprice': 235500,
        'seriesmaxprice': 339500,
        'average': 4.4264,
        'specids': '[75116, 75118, 75117, 75119]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7724,
        'seriesname': '铂智7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M01/CE/1B/autohomecar__ChxpV2jCkvmAebgpAB-ypM54-w0332.png',
        'seriesminprice': 169800,
        'seriesmaxprice': 229800,
        'average': 0.0,
        'specids': '[76712, 76705, 76713, 72767, 76711]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8087,
        'seriesname': '海狮06',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M0A/DC/87/autohomecar__ChxpVmjCloKASFuOACCEH6lEguE491.png',
        'seriesminprice': 139800,
        'seriesmaxprice': 179900,
        'average': 4.4975,
        'specids': '[73630, 73633, 76682, 76652, 73631, 72638, 73709, 73632, 76224, 76681]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8232,
        'seriesname': 'iCAR V27',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M09/C7/26/autohomecar__ChxpVmlx5hiAfJjEAGNBv0U-6xI529.png',
        'seriesminprice': 169800,
        'seriesmaxprice': 196800,
        'average': 4.1428,
        'specids': '[76415, 74039, 76273]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8462,
        'seriesname': '海豹07 EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M04/C2/E9/autohomecar__ChxpVmmyhkiAe--yACXFPffVKZg472.png',
        'seriesminprice': 169900,
        'seriesmaxprice': 189900,
        'average': 0.0,
        'specids': '[75935, 76710]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 5714,
        'seriesname': '宏光MINIEV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M07/B2/39/autohomecar__ChxpV2nKOXeACIocACzeEJiLElE133.png',
        'seriesminprice': 35800,
        'seriesmaxprice': 55800,
        'average': 4.461,
        'specids': '[65441, 76733, 71854, 68994, 66045, 76624, 76519, 71113, 69939, 75655, 66044, 69932]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7793,
        'seriesname': '小米YU7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M08/7F/C9/autohomecar__ChxkjmhebOOAQGGaAAbAi_pZ2Zo916.png',
        'seriesminprice': 253500,
        'seriesmaxprice': 329900,
        'average': 4.526,
        'specids': '[68936, 71839, 71396]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7588,
        'seriesname': '海豹06',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M07/A7/E8/autohomecar__ChxoHmXAj-GASeHTAAXQ1MwtGlE311.png',
        'seriesminprice': 96800,
        'seriesmaxprice': 139800,
        'average': 4.5798,
        'specids': '[76201, 71468, 71469, 75703, 73256, 73276, 76200, 71489, 71467, 75444, 71675, 73251]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8183,
        'seriesname': '理想i6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M0A/B7/A6/autohomecar__ChxpVWjWVjuAftVqACMDgqDSLOQ263.png',
        'seriesminprice': 249800,
        'seriesmaxprice': 269800,
        'average': 4.5258,
        'specids': '[73544, 73545]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8189,
        'seriesname': '缤果S',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M08/FF/AA/autohomecar__ChxpVmite4CARXw5AFgVy8sO7cE462.png',
        'seriesminprice': 66800,
        'seriesmaxprice': 89800,
        'average': 4.528,
        'specids': '[76745, 74366, 74364, 73569, 74365]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7207,
        'seriesname': '问界M9',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M09/96/BE/autohomecar__ChtliGWKs_aAd5wqAAfvNPmxyyo816.png',
        'seriesminprice': 469800,
        'seriesmaxprice': 599800,
        'average': 4.5394,
        'specids': '[76694, 76695, 74949, 76678, 72093, 76691, 74950, 76698, 71905, 72094, 72090, 72092, 72091, 76693, 71840, 76697, 76692, 76696]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 6139,
        'seriesname': '海豚',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M02/B8/EB/autohomecar__ChtlyGeq9jiAReUYAAdKAtoZaRE338.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 129800,
        'average': 4.5412,
        'specids': '[66316, 69005, 69004, 69006, 71049, 71048, 71050]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8003,
        'seriesname': '问界M8',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M02/08/D7/autohomecar__ChtlyGf_VIyAcKebAAYz3Liwnu0090.png',
        'seriesminprice': 359800,
        'seriesmaxprice': 459800,
        'average': 4.5179,
        'specids': '[76961, 73844, 76958, 73980, 72087, 76964, 76969, 76962, 72086, 73981, 72088, 76967, 76968, 76956, 76959, 71397, 72085, 76966, 76963, 73845, 71238, 73842, 73805, 76965]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7578,
        'seriesname': '秦L',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M06/B3/5F/autohomecar__ChxoHWeqtnKAOgObAAehH3gnIrM207.png',
        'seriesminprice': 96800,
        'seriesmaxprice': 153800,
        'average': 4.5719,
        'specids': '[76108, 71455, 70666, 71678, 71532, 71471, 71490, 75413, 75141, 72526, 71472, 76176, 72107]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 5279,
        'seriesname': '宋Pro新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M09/A3/B1/autohomecar__Chto52j7Qb-AQ_1bADGxjSYOOfY268.png',
        'seriesminprice': 102800,
        'seriesmaxprice': 133800,
        'average': 4.5074,
        'specids': '[76542, 76155, 75414, 71682, 71680, 71627, 71681, 75122, 75415, 76242]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7356,
        'seriesname': '钛3',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M05/F6/3B/autohomecar__Chto52m30LuAFOjwADzpx124U6Y492.png',
        'seriesminprice': 133800,
        'seriesmaxprice': 177800,
        'average': 4.5351,
        'specids': '[72391, 76223, 72397, 72398, 68567, 75037, 75046, 76714]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8213,
        'seriesname': '福特智趣烈马',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M08/39/2E/autohomecar__ChxpWGkdmRqASfB4AFAXgTQ0PeQ404.png',
        'seriesminprice': 229800,
        'seriesmaxprice': 282800,
        'average': 4.4723,
        'specids': '[73848, 73847, 75739, 75738, 75737]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7659,
        'seriesname': '腾势Z9GT',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M09/B6/E7/autohomecar__ChxpVmmxV_iAPVqyAC-N69GYikk565.png',
        'seriesminprice': 269800,
        'seriesmaxprice': 414800,
        'average': 4.5736,
        'specids': '[76718, 76720, 69561, 69562, 67581, 67880, 76722, 76721, 69560, 76719]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 6459,
        'seriesname': '岚图梦想家',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M01/CF/7B/autohomecar__ChxpVWjBSIGAGC08ACkqnQ1qab4019.png',
        'seriesminprice': 309900,
        'seriesmaxprice': 709900,
        'average': 4.5158,
        'specids': '[70012, 69686, 71814, 65104, 69675, 76991, 69683, 76646, 74745, 74470, 76992, 71813, 67653, 67217, 65106, 66132, 69684, 76989, 70011, 74744, 74089, 64683, 69685, 76301, 76994, 74740, 69450, 74742, 71815, 65105, 76990, 67216, 74741, 72806, 74743, 76993, 65193, 71816]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7382,
        'seriesname': '零跑C10',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M05/D2/DC/autohomecar__Chtlx2WFZ0qAfTfcAAdfP7WF9sk702.png',
        'seriesminprice': 122800,
        'seriesmaxprice': 142800,
        'average': 4.4824,
        'specids': '[72907, 72249, 72906, 73052, 72908]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7835,
        'seriesname': '极氪9X',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M08/37/B4/autohomecar__Chtk3WhvkKyABCVDAASXH1B6TJs295.png',
        'seriesminprice': 465900,
        'seriesmaxprice': 599900,
        'average': 4.5877,
        'specids': '[74432, 75101, 73246, 74471, 75103]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 6669,
        'seriesname': '腾势D9',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M07/31/CC/autohomecar__ChxoHWXpU8CAcho9AAtC11uVgY8716.png',
        'seriesminprice': 309800,
        'seriesmaxprice': 600600,
        'average': 4.5385,
        'specids': '[74459, 71232, 71229, 66868, 70662, 74462, 70663, 74464, 67047, 66865, 67046, 71230, 71233, 71231, 74461, 66864, 71234]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7538,
        'seriesname': '元UP',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M04/B8/EC/autohomecar__ChtlyGeq9keANi2NAAaoXlveBDQ712.png',
        'seriesminprice': 74800,
        'seriesmaxprice': 119800,
        'average': 4.4709,
        'specids': '[71683, 74038, 71256, 71684]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8241,
        'seriesname': '长安启源Q05',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M00/B3/31/autohomecar__ChxpV2kldtSAH1SAACp13x8PsTI146.png',
        'seriesminprice': 79900,
        'seriesmaxprice': 109900,
        'average': 4.4984,
        'specids': '[75301, 74130, 75784, 74167, 75680, 75783]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 5499,
        'seriesname': '汉',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M05/18/E7/autohomecar__ChsFJ2JSj76AcuOOAAg0TVWXz0E905.png',
        'seriesminprice': 165800,
        'seriesmaxprice': 235800,
        'average': 4.7,
        'specids': '[69144, 75198, 69802, 69815, 75104, 69814, 71535, 71704, 71591, 69813, 71703, 75188, 75106, 71707, 69817, 71533, 72515, 76541, 71705, 69142, 69816, 71534, 75061, 72514, 75199, 69143, 71706, 75192, 71623, 76540]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7165,
        'seriesname': '银河M9',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M07/BA/71/autohomecar__Chto52lwlqWAWObbACeO0fOTje8689.png',
        'seriesminprice': 183800,
        'seriesmaxprice': 248800,
        'average': 4.479,
        'specids': '[74361, 73548, 74360, 74359, 74362, 74263]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7177,
        'seriesname': '豹5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M02/A7/21/autohomecar__ChxpWGim0fqAb67MADfHcVwPq-U415.png',
        'seriesminprice': 239800,
        'seriesmaxprice': 329800,
        'average': 4.5228,
        'specids': '[71789, 71884, 75357, 75356, 75367, 71788, 75358, 71885]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 6298,
        'seriesname': '元PLUS',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M01/45/06/autohomecar__ChxoHmfH_HmASVmOAAeJPWhuAfk369.png',
        'seriesminprice': 115800,
        'seriesmaxprice': 147800,
        'average': 4.5936,
        'specids': '[71427, 71852, 72031, 66990, 71817, 66991, 66992, 66988, 66989, 71918]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8245,
        'seriesname': 'AION i60',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M07/F3/A6/autohomecar__ChtpWGiVyh2AWfEQACVe7z926cE904.png',
        'seriesminprice': 102800,
        'seriesmaxprice': 135800,
        'average': 4.4419,
        'specids': '[76661, 75707, 74159, 75708, 75528, 75527, 75709]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 4427,
        'seriesname': '蔚来ES8',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M03/A9/E4/autohomecar__ChxpVWimcVqAe_qTACXnmr3v5XU235.png',
        'seriesminprice': 406800,
        'seriesmaxprice': 446800,
        'average': 4.5351,
        'specids': '[73547, 74331, 74220]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7674,
        'seriesname': '零跑C16',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M06/2F/84/autohomecar__ChxoHWYppDeAFc9pAAmnWehUZP4049.png',
        'seriesminprice': 151800,
        'seriesmaxprice': 189800,
        'average': 4.5379,
        'specids': '[67739, 68596, 73310, 73313, 73513, 67740, 71295, 68598, 73314, 68595, 68597, 73311, 73312, 73315, 71294, 73512]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 6950,
        'seriesname': '理想L6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M09/5A/8C/autohomecar__Chtk2WgvFLyARrHKAAUPN8FeUIE427.png',
        'seriesminprice': 249800,
        'seriesmaxprice': 279800,
        'average': 4.419,
        'specids': '[72753, 71985]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 5205,
        'seriesname': '零跑C11',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M04/A2/DA/autohomecar__ChxpVmkj88OAXWIFAAqQmCvk_d8687.png',
        'seriesminprice': 148800,
        'seriesmaxprice': 209800,
        'average': 4.5302,
        'specids': '[66883, 73759, 73669, 66912, 66915, 66917, 66916, 73668, 66882, 68433, 66914, 73150, 73151, 66913]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7712,
        'seriesname': '铂智3X',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M01/8C/07/autohomecar__ChxoHmfJpNKADWKXAAgRGSYHIvE058.png',
        'seriesminprice': 109800,
        'seriesmaxprice': 159800,
        'average': 4.5661,
        'specids': '[71013, 71586, 71588, 71589, 71587, 71012, 68066]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7076,
        'seriesname': '魏牌 高山',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M03/2E/7B/autohomecar__ChtlyGfO5bWABmUfAAfsE6XK2v8372.png',
        'seriesminprice': 285800,
        'seriesmaxprice': 353800,
        'average': 4.5507,
        'specids': '[71740, 71739, 74652, 71738]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7353,
        'seriesname': '豹8',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M05/8F/A8/autohomecar__ChxkPmbqblSAR7XAAAh3KmV8NDA939.png',
        'seriesminprice': 379800,
        'seriesmaxprice': 423800,
        'average': 4.5059,
        'specids': '[72020, 69961, 69960, 75366, 71971, 67773, 75365, 72018, 70275, 72019]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8005,
        'seriesname': '唐L',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M06/7E/97/autohomecar__ChxoHWf3KseARHbHAAeigLyPmPM146.png',
        'seriesminprice': 229800,
        'seriesmaxprice': 289800,
        'average': 4.5366,
        'specids': '[71291, 71391, 71390, 71389, 72468, 72208]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 6998,
        'seriesname': '小鹏MONA M03',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M01/A7/1A/autohomecar__Chtk2WbOjc6ANKI3AAi5WZUHzQ0191.png',
        'seriesminprice': 119800,
        'seriesmaxprice': 139800,
        'average': 4.4255,
        'specids': '[73106, 73207, 73107, 73206]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7327,
        'seriesname': '极狐 阿尔法S5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M05/4E/7E/autohomecar__ChtpWGmli6aAf1DXACEQZmkREoo335.png',
        'seriesminprice': 104800,
        'seriesmaxprice': 177800,
        'average': 4.4859,
        'specids': '[76616, 74850, 74848, 76205, 72711, 72708, 76651, 72712, 72710, 74847, 74849, 76573, 76855, 72709, 76653, 76654]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 5761,
        'seriesname': '宋PLUS新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M09/04/73/autohomecar__ChxknGV4DzSAHG4RAAdLphsVYos293.png',
        'seriesminprice': 135800,
        'seriesmaxprice': 180800,
        'average': 4.5259,
        'specids': '[71520, 71656, 71657, 71524, 71470, 71480, 72520, 71525, 71481]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8042,
        'seriesname': '银河星耀8',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M05/8D/0D/autohomecar__ChxoHWe2miGACNluAAUHFKvgX7U086.png',
        'seriesminprice': 125800,
        'seriesmaxprice': 172800,
        'average': 4.5388,
        'specids': '[72250, 72810, 76912, 72251, 71832, 76913, 72809, 72569, 76844, 76843, 71851]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8499,
        'seriesname': 'QQ3 EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M01/A6/9E/autohomecar__ChxpVmmv29KAEOZoACEcZHn47Io753.png',
        'seriesminprice': 58900,
        'seriesmaxprice': 78900,
        'average': 0.0,
        'specids': '[76769, 76577, 76768, 76206]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7740,
        'seriesname': '深蓝S05',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M09/80/1A/autohomecar__ChxoHmZBjWGAFfcqAAdru9xj-NI338.png',
        'seriesminprice': 119900,
        'seriesmaxprice': 149900,
        'average': 4.4913,
        'specids': '[70413, 70411, 68268, 74474, 74326, 75111, 74037, 74063, 74347, 70412, 68267, 74064]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7411,
        'seriesname': '风云T11',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M0B/E3/7F/autohomecar__ChxkPmbR3USAYSOJAAkyne6yMz0106.png',
        'seriesminprice': 189900,
        'seriesmaxprice': 249900,
        'average': 4.5279,
        'specids': '[75221, 75222, 64982, 75223]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8159,
        'seriesname': '腾势N8L',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M06/FD/A8/autohomecar__ChxpWGkDFCeAVFelACdFgita21A750.png',
        'seriesminprice': 299800,
        'seriesmaxprice': 329800,
        'average': 4.5938,
        'specids': '[75025, 73159]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7877,
        'seriesname': '零跑B10',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M00/12/33/autohomecar__Chtk2Wc0Z7yAFFmwAAbWYbMZOGs358.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 149800,
        'average': 4.5308,
        'specids': '[73364, 70078, 72125, 72127, 71066, 72126]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7504,
        'seriesname': '坦克700新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M03/AD/F5/autohomecar__ChxpVmnKOZyAD3ykADmu9mjESTU629.png',
        'seriesminprice': 428000,
        'seriesmaxprice': 700000,
        'average': 4.5494,
        'specids': '[66594, 66140, 65733]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 3430,
        'seriesname': '唐新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M06/8F/C1/autohomecar__ChxkPWcgSDmAKOacAAij6K5NdKY698.png',
        'seriesminprice': 179800,
        'seriesmaxprice': 207800,
        'average': 4.5526,
        'specids': '[74551, 70476, 74600, 71700, 71699, 70475, 74564, 70454, 70416, 71701]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 6091,
        'seriesname': '极氪001',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M08/CD/E7/autohomecar__Chto52jsxTSABtWxADH72vuK3nA506.png',
        'seriesminprice': 269800,
        'seriesmaxprice': 329800,
        'average': 4.5682,
        'specids': '[75071, 75072, 75139, 74180]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7777,
        'seriesname': '极氪7X',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M00/E6/ED/autohomecar__Chto52kAkv-AbhpTADAmq5-A7bU060.png',
        'seriesminprice': 229800,
        'seriesmaxprice': 269800,
        'average': 4.5211,
        'specids': '[75350, 75351, 75352]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8205,
        'seriesname': '尚界H5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M0B/80/62/autohomecar__Chto52jSXryAUcOLAFYXpW7_NlU005.png',
        'seriesminprice': 159800,
        'seriesmaxprice': 199800,
        'average': 4.5156,
        'specids': '[73768, 73871, 74376, 74378, 74375, 74377]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 6576,
        'seriesname': '理想L9',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M0A/A3/57/autohomecar__ChxknGgdcVGAdbReAAfxWHCJjU4265.png',
        'seriesminprice': 409800,
        'seriesmaxprice': 439800,
        'average': 4.466,
        'specids': '[72993, 71988]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 5213,
        'seriesname': '小鹏P7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M01/A6/53/autohomecar__ChxpWGk72QaAdCL5ABik76aebQ4134.png',
        'seriesminprice': 203800,
        'seriesmaxprice': 301800,
        'average': 4.4457,
        'specids': '[76791, 76880, 76879, 74221]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8187,
        'seriesname': '星光730新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M00/D2/66/autohomecar__ChtlxWhZEXWAeBp5AATXoG1pTlo574.png',
        'seriesminprice': 103800,
        'seriesmaxprice': 109800,
        'average': 4.448,
        'specids': '[73563, 73562]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8002,
        'seriesname': '领克900',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M03/AB/19/autohomecar__ChtlxmgCI3-AFpXtAAaVF9ZmwdY453.png',
        'seriesminprice': 309900,
        'seriesmaxprice': 416900,
        'average': 4.5095,
        'specids': '[72146, 72145, 71220, 71395]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8251,
        'seriesname': 'Model Y L',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M05/A6/50/autohomecar__ChxpWGk72NyAOaaTACKu7ouR42c156.png',
        'seriesminprice': 339000,
        'seriesmaxprice': 339000,
        'average': 4.4992,
        'specids': '[73654]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7658,
        'seriesname': '别克GL8新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M04/A3/23/autohomecar__ChxpV2kRwtCAYuiEAAeL78j6C4I209.png',
        'seriesminprice': 229900,
        'seriesmaxprice': 399900,
        'average': 4.3931,
        'specids': '[77038, 73168, 74208, 74209, 72680, 72749, 71053]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7045,
        'seriesname': '五菱缤果',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M03/04/D8/autohomecar__ChxknGV4EEGAdC_6AAfVjvUbzRc807.png',
        'seriesminprice': 56800,
        'seriesmaxprice': 84800,
        'average': 4.3965,
        'specids': '[68464, 72701, 72051, 68463, 68113, 72054, 68465, 72052, 72053]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7851,
        'seriesname': '夏',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M0A/DA/65/autohomecar__ChxpVmkoTFyAQO91AEZ8uHwuCvg976.png',
        'seriesminprice': 206800,
        'seriesmaxprice': 277800,
        'average': 4.5703,
        'specids': '[75559, 75429, 72517, 75560, 75544]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7815,
        'seriesname': '宋L DM-i',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M01/9B/1C/autohomecar__ChxpV2j7ZRCAMxRyADLE-8pojNU527.png',
        'seriesminprice': 135800,
        'seriesmaxprice': 175800,
        'average': 4.5531,
        'specids': '[71473, 71628, 75404, 71676, 75123, 75416, 71603, 71502]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 6544,
        'seriesname': '宝马i3',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M07/34/91/autohomecar__ChxoHmW4xwaAGLJWAAgsDFpWtbM429.png',
        'seriesminprice': 278000,
        'seriesmaxprice': 413900,
        'average': 4.2788,
        'specids': '[76420, 73901, 76421, 75048, 76422, 73900]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7694,
        'seriesname': '海豹06GT',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M00/81/9B/autohomecar__ChxkPWbMXJKAeu-qAAdJ0CbHdbk138.png',
        'seriesminprice': 136800,
        'seriesmaxprice': 186800,
        'average': 4.5804,
        'specids': '[71669, 71667, 71668, 71670]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8215,
        'seriesname': '智己LS9',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M05/46/D7/autohomecar__ChtpWGkJvtmARugCAEoEjBJ1KSc476.png',
        'seriesminprice': 332800,
        'seriesmaxprice': 362800,
        'average': 4.5842,
        'specids': '[75574, 73849]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 7730,
        'seriesname': '智界R7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M08/FF/41/autohomecar__ChxpVWitdtOAUKI1ACzNqmC6e90400.png',
        'seriesminprice': 249800,
        'seriesmaxprice': 319800,
        'average': 4.5206,
        'specids': '[76932, 74052, 74142, 76933, 76936, 74141, 76935, 74139, 74138, 74140, 76934, 76931]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8086,
        'seriesname': '极狐T1',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M00/E9/13/autohomecar__ChxpVWjD6TyABUEYACQIOZtojjo996.png',
        'seriesminprice': 62800,
        'seriesmaxprice': 125800,
        'average': 4.4527,
        'specids': '[74328, 74330, 74329, 74096, 76425, 74327]',
        'create_time': '2026-04-01 02:36:04'
    },
    {
        'seriesid': 8278,
        'seriesname': '零跑Lafa5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M01/CD/7D/autohomecar__ChtpWGknreeAecWwAEekdQVjLiM698.png',
        'seriesminprice': 97800,
        'seriesmaxprice': 121800,
        'average': 4.599,
        'specids': '[75607, 74553, 75606, 75564, 75605]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7864,
        'seriesname': '银河星舰7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M04/4F/96/autohomecar__ChxpWGke3LeABpgvADb0PT-Bd_0876.png',
        'seriesminprice': 97800,
        'seriesmaxprice': 130800,
        'average': 4.6183,
        'specids': '[75753, 75754, 75583, 70654, 70655, 75665, 69919, 70657, 70656]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7981,
        'seriesname': '海豹05 DM-i',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M0A/B8/EF/autohomecar__ChtlyGeq9muABiQYAAYi3DKZli8780.png',
        'seriesminprice': 79800,
        'seriesmaxprice': 103800,
        'average': 4.4975,
        'specids': '[76239, 75124, 76110, 71052]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7873,
        'seriesname': '别克至境世家',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M0B/65/DB/autohomecar__ChxpVmkfy8OAJmkHACX4QXEeItc838.png',
        'seriesminprice': 439900,
        'seriesmaxprice': 489900,
        'average': 0.0,
        'specids': '[75899, 74156, 75717]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7225,
        'seriesname': '风云A9L',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M02/83/83/autohomecar__Chtk2WhuQTOAQV5dAAcNnTbrdRY681.png',
        'seriesminprice': 149900,
        'seriesmaxprice': 236900,
        'average': 4.5856,
        'specids': '[75710, 75712, 75466, 71735, 75711, 70239, 72702, 75467, 75714, 75713, 72247]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7925,
        'seriesname': '奥迪E5 Sportback',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M0A/EE/7F/autohomecar__ChxpVWiUdiKAXw9QACSULRPmhmk137.png',
        'seriesminprice': 235900,
        'seriesmaxprice': 319900,
        'average': 4.5496,
        'specids': '[74119, 74121, 75780, 74120, 72707]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8201,
        'seriesname': '海豹06 DM-i旅行版',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M06/86/EF/autohomecar__ChxkqWhuQb-AHBS3AAi09TA4ZkI864.png',
        'seriesminprice': 109800,
        'seriesmaxprice': 129800,
        'average': 4.5771,
        'specids': '[73388, 72279, 73644]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7899,
        'seriesname': '悦意03',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M00/04/4A/autohomecar__ChxoHmfdEL2ARt9NAAe4yhxVSNI542.png',
        'seriesminprice': 79800,
        'seriesmaxprice': 149900,
        'average': 4.42,
        'specids': '[72077, 76750, 74735, 76753, 76852, 72074, 72075, 76754, 70366, 72076, 76752, 76407, 76751, 72690, 73622]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7717,
        'seriesname': '马自达EZ-60',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M02/F1/06/autohomecar__ChxkPWgCIviAbYL3AAXO0SvQ_a4088.png',
        'seriesminprice': 119900,
        'seriesmaxprice': 166900,
        'average': 4.4945,
        'specids': '[76123, 76130, 72490, 76125, 72679, 72678, 76122, 76124, 76129, 75004, 74883, 75003]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6846,
        'seriesname': '极氪009',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M02/9E/35/autohomecar__ChtlyGd81IqAMqONAAfbiZsZbko909.png',
        'seriesminprice': 439000,
        'seriesmaxprice': 899000,
        'average': 4.5198,
        'specids': '[69218, 68278, 68276, 68275, 72276, 66649, 68277, 69222]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7630,
        'seriesname': '享界S9',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M09/57/4C/autohomecar__ChxpVmke34iAGisLADWxYt7lxsU893.png',
        'seriesminprice': 309800,
        'seriesmaxprice': 379800,
        'average': 4.4991,
        'specids': '[76939, 76938, 75609, 75426, 75603, 75608, 76940, 76942, 75166, 76943, 75610, 76941]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8006,
        'seriesname': '零跑B01',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M0A/2B/F6/autohomecar__Chto52iDWY2AbpGXACmOnYPV8yY751.png',
        'seriesminprice': 89800,
        'seriesmaxprice': 149700,
        'average': 4.5632,
        'specids': '[72909, 71302, 73624, 74314, 73623, 72657, 73966]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6388,
        'seriesname': '问界M5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M06/57/39/autohomecar__ChxoHWYqfW6ADUO1AGR2O2bO6FE939.png',
        'seriesminprice': 229800,
        'seriesmaxprice': 249800,
        'average': 4.5446,
        'specids': '[72006, 72007, 72005]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8140,
        'seriesname': '长安启源A06',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M05/D2/45/autohomecar__ChtpWGjZChKAHXaCACHsf7TINA4231.png',
        'seriesminprice': 109900,
        'seriesmaxprice': 149900,
        'average': 4.5667,
        'specids': '[75033, 75034, 75036, 73155, 76658, 73156, 75035, 75039, 72997]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7650,
        'seriesname': '银河E5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M07/2B/B5/autohomecar__ChxpWGiDWl6AeUbjADKAQ9AuCE4282.png',
        'seriesminprice': 107800,
        'seriesmaxprice': 179800,
        'average': 4.4401,
        'specids': '[73943, 73944, 73952, 73949, 73945, 73702]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7839,
        'seriesname': '腾势N9',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M06/B8/28/autohomecar__ChxkPmcIj8-AXHdBAAZaVdzXixo468.png',
        'seriesminprice': 389800,
        'seriesmaxprice': 449800,
        'average': 4.5809,
        'specids': '[74782, 74580, 74511]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7927,
        'seriesname': '尊界S800',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M06/61/B9/autohomecar__ChtpWGmn8I-ASBsuAB84eN3jrU0785.png',
        'seriesminprice': 708000,
        'seriesmaxprice': 1018000,
        'average': 4.8572,
        'specids': '[76690, 70935, 70658, 73241, 76686, 76688, 71841, 76687, 76689, 71051, 76657, 73082]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8100,
        'seriesname': '别克至境L7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M0B/29/B5/autohomecar__ChxpVWm9HB6ASxwyACt2-yZBYt4869.png',
        'seriesminprice': 173900,
        'seriesmaxprice': 219900,
        'average': 4.5255,
        'specids': '[75045, 72720, 75042, 75044, 75043]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7859,
        'seriesname': '汉L',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M08/7E/82/autohomecar__ChtlyGf3Kq2AbKvzAAa2gTVA09s837.png',
        'seriesminprice': 209800,
        'seriesmaxprice': 279800,
        'average': 4.4943,
        'specids': '[72209, 71393, 71435, 71392, 72523, 71292]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6265,
        'seriesname': '大众ID.3',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M0B/43/BC/autohomecar__CjIFU2V4DPuAe64HAAaKPLlogls618.png',
        'seriesminprice': 129888,
        'seriesmaxprice': 155888,
        'average': 4.2362,
        'specids': '[74902, 74904, 72248, 74903, 73423]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8243,
        'seriesname': '日产N6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M02/15/44/autohomecar__Chto52ktazeAGNTnACph4-mBOi0826.png',
        'seriesminprice': 99900,
        'seriesmaxprice': 129900,
        'average': 4.575,
        'specids': '[74150, 75878, 76611, 75877, 74152, 74151]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7918,
        'seriesname': 'AION UT',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M01/D6/D4/autohomecar__Chtk2WcjQPOAYLEbAAbV7YklfDs086.png',
        'seriesminprice': 69800,
        'seriesmaxprice': 101800,
        'average': 4.5433,
        'specids': '[71303, 76361, 72003, 71304, 72897, 70570]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8138,
        'seriesname': '沃尔沃XC70插电式混动',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M03/A1/12/autohomecar__ChxpV2kkDnKAeIZsACYO1hU0oqI056.png',
        'seriesminprice': 416900,
        'seriesmaxprice': 496900,
        'average': 4.5915,
        'specids': '[72974, 73152, 75022, 74915]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8158,
        'seriesname': '银河A7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M0A/DC/82/autohomecar__ChtlyGhVTDmAEoqrAAcrs1d5rVs681.png',
        'seriesminprice': 89800,
        'seriesmaxprice': 125800,
        'average': 4.5991,
        'specids': '[73916, 73791, 73792, 73915, 73789, 73158, 73790]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7210,
        'seriesname': '坦克300新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M02/95/FF/autohomecar__ChxkmWQ2Ei-AXpQVAE6xm2OjU-w198.png',
        'seriesminprice': 249800,
        'seriesmaxprice': 249800,
        'average': 4.5654,
        'specids': '[71855, 75894]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7298,
        'seriesname': '哈弗猛龙新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M08/99/EE/autohomecar__ChxpWGilh_uAI617ADdH1gTtvGc669.png',
        'seriesminprice': 173800,
        'seriesmaxprice': 208800,
        'average': 4.5481,
        'specids': '[72252, 76660, 74041, 74302, 74301, 74042, 74045, 76659]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7982,
        'seriesname': '海狮05 EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M0A/4C/61/autohomecar__ChxkPWfagHyANQr3AAh61-8NB2s496.png',
        'seriesminprice': 117800,
        'seriesmaxprice': 137800,
        'average': 4.5281,
        'specids': '[71057, 72236, 71072]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7975,
        'seriesname': '长安启源Q07',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M0B/FC/50/autohomecar__ChxkPWgHcwOAI1sUAAVMmhNpziU494.png',
        'seriesminprice': 129800,
        'seriesmaxprice': 176800,
        'average': 4.5262,
        'specids': '[72402, 75175, 72752, 71021, 72403, 75174, 71038, 72401, 75070]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6949,
        'seriesname': '理想L7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M06/1F/55/autohomecar__ChtlxmgvFKaAGmTaAAV94eOnU7w267.png',
        'seriesminprice': 301800,
        'seriesmaxprice': 359800,
        'average': 4.5266,
        'specids': '[72990, 71986, 72989]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8010,
        'seriesname': '极氪007GT',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M09/30/BD/autohomecar__Chtk2Gf_Q4KAEDaNAAUwMw4UDjw027.png',
        'seriesminprice': 202900,
        'seriesmaxprice': 262900,
        'average': 4.4756,
        'specids': '[71419, 71394, 71332, 71418]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8176,
        'seriesname': '领克10',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M07/27/7A/autohomecar__ChxpV2ibAsOAGT3mABwZoE-jBA8685.png',
        'seriesminprice': 173800,
        'seriesmaxprice': 211800,
        'average': 4.5459,
        'specids': '[75978, 74187, 73518, 75976, 74611, 75977, 73568]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8045,
        'seriesname': '乐道L90',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M07/76/69/autohomecar__ChtpWGiJ2a6ALmwNAE67mAl2NS8440.png',
        'seriesminprice': 265800,
        'seriesmaxprice': 316800,
        'average': 4.4286,
        'specids': '[74050, 74043, 76423, 72632, 71906, 74049, 76424, 74044]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8246,
        'seriesname': '昊铂A800',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M06/1B/47/autohomecar__ChxpVWlFC7qAYw0SADYj5c8szUw756.png',
        'seriesminprice': 189800,
        'seriesmaxprice': 299800,
        'average': 0.0,
        'specids': '[76597, 74172, 76596, 76595]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6653,
        'seriesname': '坦克500新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M09/1A/42/autohomecar__ChxpV2iZujWAdoi8AE4NyysA-78039.png',
        'seriesminprice': 335000,
        'seriesmaxprice': 375000,
        'average': 4.5198,
        'specids': '[71272, 73939, 73938, 69708, 67764, 73940, 67304]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6293,
        'seriesname': '大切诺基4xe(进口)',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M02/0C/43/autohomecar__Chtk3WPu6wmAHovPAAXowuhJcg8934.png',
        'seriesminprice': 349000,
        'seriesmaxprice': 439000,
        'average': 4.5714,
        'specids': '[61456, 69973, 61543]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7554,
        'seriesname': '小鹏P7+',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M06/14/A6/autohomecar__ChxpVWlfgemANAt2ACvVPHG54Fo666.png',
        'seriesminprice': 186800,
        'seriesmaxprice': 208800,
        'average': 4.3714,
        'specids': '[75159, 76083, 69103, 72751, 76184, 76185, 66239]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8207,
        'seriesname': '享界S9T',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M0B/7D/66/autohomecar__ChxpWGii_sCAOzt7ADfo7pXe7C4829.png',
        'seriesminprice': 309800,
        'seriesmaxprice': 379800,
        'average': 4.5262,
        'specids': '[76927, 76922, 74281, 74282, 73950, 73951, 76925, 73860, 76926, 73796, 76924, 76923]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7067,
        'seriesname': '小鹏X9',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M01/52/33/autohomecar__ChxpV2ke-FqAfNNNAETDdyAX9rw251.png',
        'seriesminprice': 309800,
        'seriesmaxprice': 369800,
        'average': 4.2858,
        'specids': '[76495, 76498, 75600, 76496, 76662, 76494, 76497, 74165]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7649,
        'seriesname': 'iCAR 超级V23',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M06/C6/3F/autohomecar__Chtk2Wdg396AQzf1AAglIgGekoc604.png',
        'seriesminprice': 109800,
        'seriesmaxprice': 174800,
        'average': 4.4056,
        'specids': '[73869, 71296, 70817, 70737, 74712, 73870, 73846, 76103]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 4881,
        'seriesname': '蔚来ES6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M00/B8/7D/autohomecar__ChxkmmghWiCAJmF9AAawahbad2w219.png',
        'seriesminprice': 338000,
        'seriesmaxprice': 349800,
        'average': 4.5897,
        'specids': '[73039, 75716]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8291,
        'seriesname': '岚图泰山',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M0B/41/C6/autohomecar__Chto52kdmTGAIRZ6ACfVhCzazLI973.png',
        'seriesminprice': 379900,
        'seriesmaxprice': 509900,
        'average': 4.5763,
        'specids': '[75580, 75741, 74688, 75746]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7512,
        'seriesname': '长安UNI-Z新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M0B/6C/21/autohomecar__ChtlxmVUmcCAL0U_AAaz2nx3dKM383.png',
        'seriesminprice': 117900,
        'seriesmaxprice': 135900,
        'average': 4.4285,
        'specids': '[76348, 65784, 76526, 73187, 73188, 76349, 71625, 67464]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 5924,
        'seriesname': '岚图FREE',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M05/8E/FB/autohomecar__ChxkqWh0wJSAKX87AAknKYjKAZU815.png',
        'seriesminprice': 219900,
        'seriesmaxprice': 326900,
        'average': 4.527,
        'specids': '[67798, 73126, 68758, 73795, 68483, 76996, 76995]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7126,
        'seriesname': '阿维塔12',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M06/EA/C5/autohomecar__ChtpWGkB0bCATQdkACrHSyvNEo0381.png',
        'seriesminprice': 269900,
        'seriesmaxprice': 700000,
        'average': 4.5902,
        'specids': '[75318, 75347, 68416, 75348, 75355, 75131, 75319]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6817,
        'seriesname': '深蓝S07',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M02/57/1B/autohomecar__ChxoHWYqfLWAE3cdAAlQMiP2pTE555.png',
        'seriesminprice': 156900,
        'seriesmaxprice': 174900,
        'average': 4.3784,
        'specids': '[74601, 74603, 74401, 74602, 73838, 75979, 75980]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6910,
        'seriesname': '理想L8',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M00/A3/56/autohomecar__ChxknGgdcT6AaHiDAAfxSxdM_fs304.png',
        'seriesminprice': 321800,
        'seriesmaxprice': 379800,
        'average': 4.5017,
        'specids': '[72991, 72992, 71987]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7305,
        'seriesname': '智己LS6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M06/E0/CD/autohomecar__ChtpWGiUF7OAcuQfACusKwW_xkk200.png',
        'seriesminprice': 212900,
        'seriesmaxprice': 284900,
        'average': 4.5557,
        'specids': '[74252, 74590, 74253, 74254, 74219, 74251, 73161, 73163, 75293]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7935,
        'seriesname': '日产N7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M09/7D/A8/autohomecar__ChxoHmgIbgeAcyjZAAaoyubGHyA163.png',
        'seriesminprice': 119900,
        'seriesmaxprice': 149900,
        'average': 4.5075,
        'specids': '[72878, 70809, 72880, 72879, 71933]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7355,
        'seriesname': '智界S7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M06/E1/60/autohomecar__ChxkmWTdj9CAfK8VAAYEPjHzr1E079.png',
        'seriesminprice': 229800,
        'seriesmaxprice': 299800,
        'average': 4.5591,
        'specids': '[76930, 74144, 74093, 74143, 76929, 76928]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7213,
        'seriesname': '坦克400新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M0B/62/D8/autohomecar__ChxpV2kMZLGAXopgAEKQ9oAiYnc983.png',
        'seriesminprice': 285800,
        'seriesmaxprice': 319800,
        'average': 4.588,
        'specids': '[67337, 67336, 74994, 74947, 71836]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6394,
        'seriesname': '海豹',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M05/4C/0E/autohomecar__Chtk2WasoV6AHYWGAAYRhXkxZxQ248.png',
        'seriesminprice': 175800,
        'seriesmaxprice': 239800,
        'average': 4.2688,
        'specids': '[71666, 71663, 71664, 71665]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7125,
        'seriesname': '极狐 阿尔法T5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M01/E0/71/autohomecar__ChxpVmjuEq2AOD6vADIXb1gcEIM766.png',
        'seriesminprice': 113800,
        'seriesmaxprice': 158800,
        'average': 4.5346,
        'specids': '[75230, 75229, 75225, 74716, 75228, 74154, 75227]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6674,
        'seriesname': '长安Lumin',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M09/32/31/autohomecar__ChxoHWgCI9CASsXYAAYTmKfMAyo989.png',
        'seriesminprice': 37900,
        'seriesmaxprice': 65900,
        'average': 4.25,
        'specids': '[72689, 68902, 71768, 69480, 75369, 65300, 72535, 71769, 64154, 76406, 72361, 68900, 75364, 68901, 75496, 68899]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7243,
        'seriesname': '领克08 EM-P',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M07/10/1C/autohomecar__ChxpVmjIAhKAP7PCADR5Wzb5X6Y228.png',
        'seriesminprice': 175800,
        'seriesmaxprice': 248800,
        'average': 4.3792,
        'specids': '[69386, 74351, 76131, 73823, 73863, 69384, 69385, 69401, 73864, 69383, 69400]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8211,
        'seriesname': '银河星耀6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M00/91/AF/autohomecar__Chtk2Gh46emAOFFIAASxi3H6sgY867.png',
        'seriesminprice': 74800,
        'seriesmaxprice': 105800,
        'average': 4.554,
        'specids': '[75008, 75498, 75007, 75499, 75009, 73899, 73839]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7687,
        'seriesname': '乐道L60',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M03/C1/D4/autohomecar__ChxkmWhT0W6AdPN3AAa0qcDXya8068.png',
        'seriesminprice': 206900,
        'seriesmaxprice': 255900,
        'average': 4.4833,
        'specids': '[75882, 74840, 74785, 74841, 74784, 76333, 75881]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7727,
        'seriesname': '理想i8',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M0A/BB/17/autohomecar__Chxkjmh4yh2AM4VIAAa9JM9S8a4722.png',
        'seriesminprice': 339800,
        'seriesmaxprice': 339800,
        'average': 4.5641,
        'specids': '[74102]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8203,
        'seriesname': '红旗HS6 PHEV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M01/6D/10/autohomecar__ChxpV2jR9GyAammbAEqbOnss2u0346.png',
        'seriesminprice': 178800,
        'seriesmaxprice': 228800,
        'average': 4.5036,
        'specids': '[74898, 74897, 73760]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7752,
        'seriesname': '阿维塔06',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M03/DD/2E/autohomecar__ChtlyGfaKHSARvDzAAbPE9aX2Dc205.png',
        'seriesminprice': 209900,
        'seriesmaxprice': 279900,
        'average': 4.5365,
        'specids': '[72351, 74455, 75530, 71036, 75531, 72200, 71035, 71023]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6903,
        'seriesname': '丰田bZ3',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M08/DF/F5/autohomecar__ChxpWGlaKm6AQlB8AFQImfrL2PM734.png',
        'seriesminprice': 109800,
        'seriesmaxprice': 199800,
        'average': 4.5191,
        'specids': '[76002, 66582, 76119, 76120, 66581, 66470, 76121]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6979,
        'seriesname': '魏牌 蓝山',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M06/4F/28/autohomecar__ChxpVWkywS2AFwutAD6-Fe2tVTY386.png',
        'seriesminprice': 299800,
        'seriesmaxprice': 326800,
        'average': 4.5222,
        'specids': '[75880, 75474, 75475]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7231,
        'seriesname': '奔腾小马',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M07/9E/9D/autohomecar__ChxpV2kRh1aAWgO2ADL_X0ZP77Y495.png',
        'seriesminprice': 34900,
        'seriesmaxprice': 53900,
        'average': 4.601,
        'specids': '[73960, 71999, 74070, 73972, 76340, 73965, 73971, 70540, 70539, 69985, 70541, 71998, 73973]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7162,
        'seriesname': '小鹏G6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M05/14/B6/autohomecar__Chto52lfgj2AdCzaAENFaqjPMFg869.png',
        'seriesminprice': 176800,
        'seriesmaxprice': 198800,
        'average': 4.2958,
        'specids': '[72159, 71058, 75160, 76162, 76186, 71059]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6924,
        'seriesname': '熊猫',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M0B/3F/43/autohomecar__CjIFV2SiOP6AanH4AArwD9j35Tg115.png',
        'seriesminprice': 46900,
        'seriesmaxprice': 53900,
        'average': 4.5328,
        'specids': '[74021, 70184, 72345, 70183, 67838]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8106,
        'seriesname': '捷途山海L7 PLUS',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M05/84/27/autohomecar__ChxpVWii9puAfKbhACwJ4ODURvA345.png',
        'seriesminprice': 119900,
        'seriesmaxprice': 165900,
        'average': 4.5537,
        'specids': '[72796, 73162, 74247, 74268, 74265, 74410, 74269, 74266, 74267, 74264]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8422,
        'seriesname': 'AION UT super',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M09/54/93/autohomecar__ChtpWGkLFj2AEIBTACbSaLgkQ7U082.png',
        'seriesminprice': 89900,
        'seriesmaxprice': 93800,
        'average': 4.5703,
        'specids': '[76360, 76908, 75586]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7652,
        'seriesname': '阿维塔07',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M07/D4/E1/autohomecar__ChxoHWY9td2AUPaCAAdo30mtSUI095.png',
        'seriesminprice': 219900,
        'seriesmaxprice': 289900,
        'average': 4.5243,
        'specids': '[74558, 74886, 74557, 74560, 74885, 74873, 74554, 74559, 74555, 74872, 74876]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6851,
        'seriesname': '海狮07 EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M09/4E/67/autohomecar__ChtlxWVaxciAFYGFAAId8duUm4o278.png',
        'seriesminprice': 189800,
        'seriesmaxprice': 239800,
        'average': 4.5383,
        'specids': '[71693, 71695, 71692, 68250, 71694, 66476, 66475, 58503]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7209,
        'seriesname': '长安启源A07',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M0A/30/F5/autohomecar__ChxkjmWFaXiAaafdAAa0Ibm_vnI141.png',
        'seriesminprice': 119900,
        'seriesmaxprice': 165900,
        'average': 4.4286,
        'specids': '[70405, 74615, 71711, 74924, 74617, 71712, 74614, 71717, 71714, 71715, 71709, 71710, 71716, 74616, 71713]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 5576,
        'seriesname': '领克07 EM-P',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M07/FE/C2/autohomecar__ChtpWGjHxNOATPnuACKVDwOSTlM557.png',
        'seriesminprice': 155800,
        'seriesmaxprice': 175800,
        'average': 4.4475,
        'specids': '[74717, 76808, 73833, 74718]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7990,
        'seriesname': 'firefly萤火虫',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M0A/B5/8F/autohomecar__ChxkPmdo_leAE5XbAAeihT-TACo170.png',
        'seriesminprice': 119800,
        'seriesmaxprice': 137800,
        'average': 4.5707,
        'specids': '[72534, 72533, 76901]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7491,
        'seriesname': '极氪007',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M04/2B/65/autohomecar__CjIFU2V3yGKAYqDvAAYbfFIiKq8035.png',
        'seriesminprice': 209900,
        'seriesmaxprice': 299900,
        'average': 4.5243,
        'specids': '[69447, 69444, 69446, 69445, 69463]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6939,
        'seriesname': '理想MEGA',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M0B/07/6C/autohomecar__ChtlyGgdj7aAHYKBAAabT4lHk2Q899.png',
        'seriesminprice': 529800,
        'seriesmaxprice': 559800,
        'average': 4.6232,
        'specids': '[71989, 72579]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 5515,
        'seriesname': '零跑T03',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M0B/45/40/autohomecar__Chtk3WQIIZmABkn0AAIq67kU2c4010.png',
        'seriesminprice': 59900,
        'seriesmaxprice': 69900,
        'average': 4.5438,
        'specids': '[71891, 71892]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7442,
        'seriesname': '风云T9',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M0B/01/70/autohomecar__CjIFV2WbtsaAZpydAAHmBvSCWXc177.png',
        'seriesminprice': 132900,
        'seriesmaxprice': 193900,
        'average': 4.539,
        'specids': '[72557, 72556, 72555, 72552, 72559, 72554, 72553, 72558]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7306,
        'seriesname': '蔚来ET5T',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M06/D4/78/autohomecar__ChxknGgvFHOAUW1zAAbmlR9Bjl4366.png',
        'seriesminprice': 298000,
        'seriesmaxprice': 316000,
        'average': 4.5515,
        'specids': '[73120, 75991, 73727]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7822,
        'seriesname': '海豹07 DM-i',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M09/B6/7A/autohomecar__ChxkPmay7YuAVLozAAgJCDY_Gl4807.png',
        'seriesminprice': 139800,
        'seriesmaxprice': 195800,
        'average': 4.4559,
        'specids': '[74335, 73552, 71658, 71662, 71660, 71661, 71659, 74310, 73553]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7979,
        'seriesname': '深蓝S09',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M02/32/2F/autohomecar__ChxoHWgCI5yAOFJTAAUnMKW_QcE832.png',
        'seriesminprice': 239900,
        'seriesmaxprice': 309900,
        'average': 4.4409,
        'specids': '[72761, 74607, 72759, 74591, 74592, 76918, 72760]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 5976,
        'seriesname': 'AION Y',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M05/1E/69/autohomecar__ChtliGM2rW2AAKCrAAkX86oWZF0331.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 145800,
        'average': 4.5047,
        'specids': '[73267, 66737, 66735, 62285, 62284, 66308, 61848, 71126, 71124, 68111, 63780, 73268, 73270, 73269, 68112]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7220,
        'seriesname': '宋L EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M08/03/33/autohomecar__ChxknGV4DDmAKTvOAAbB-qWMreE491.png',
        'seriesminprice': 189800,
        'seriesmaxprice': 249800,
        'average': 4.5821,
        'specids': '[71679, 69743, 71503, 71536, 71508, 69744, 68095, 69742]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 6453,
        'seriesname': '蔚来ET5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M04/5A/5B/autohomecar__ChxkPmgvFGKAB140AAeerK1gKW4061.png',
        'seriesminprice': 298000,
        'seriesmaxprice': 316000,
        'average': 4.8571,
        'specids': '[75990, 73119, 73726]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7398,
        'seriesname': 'eπ007',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M07/AE/DD/autohomecar__ChxpVmkRrlmAINlrAC6d1Swt3Pk953.png',
        'seriesminprice': 115900,
        'seriesmaxprice': 265900,
        'average': 4.4993,
        'specids': '[75525, 73278, 73279, 74020, 74018, 73570, 75505, 75523, 75638, 75636, 73103, 75637]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7915,
        'seriesname': '小米SU7 Ultra',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M0B/12/12/autohomecar__ChxkPmc0Z4CAI0-4AAeGn_xFc70936.png',
        'seriesminprice': 529900,
        'seriesmaxprice': 529900,
        'average': 4.4822,
        'specids': '[70545]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7116,
        'seriesname': '仰望U9',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M00/CE/2E/autohomecar__ChtlyGXYCaWAVjVrAAdbV4R__DQ904.png',
        'seriesminprice': 1800000,
        'seriesmaxprice': 1800000,
        'average': 4.8572,
        'specids': '[62533]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7807,
        'seriesname': '海狮05 DM-i',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M00/8D/FA/autohomecar__Chtk2WaUgPCAZrCMAAXX-gjU2KU194.png',
        'seriesminprice': 102800,
        'seriesmaxprice': 142800,
        'average': 4.5168,
        'specids': '[70057, 71671, 71672, 69114, 71674, 70058, 69115, 71673]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7696,
        'seriesname': '北京越野BJ40增程',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M09/EB/EA/autohomecar__Chtk2WdiOyCAYvRBAAmQmXOLGLQ897.png',
        'seriesminprice': 179800,
        'seriesmaxprice': 279800,
        'average': 4.4852,
        'specids': '[75442, 75694, 67937, 76435, 71138, 75693, 74593]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7713,
        'seriesname': '丰田bZ5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M02/40/E0/autohomecar__CjIFVWhH6RiAZQp9AAYe6Y5HNzs943.png',
        'seriesminprice': 129800,
        'seriesmaxprice': 199800,
        'average': 4.5501,
        'specids': '[72883, 72743, 72882, 72739, 73111, 72884]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 5785,
        'seriesname': 'ID.4 CROZZ',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M02/64/AF/autohomecar__ChxpV2kMe9eAIypNADfm2Fi5XRw165.png',
        'seriesminprice': 149900,
        'seriesmaxprice': 243600,
        'average': 4.6277,
        'specids': '[71288, 70812, 74408, 71287, 74409, 74341, 71289]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8023,
        'seriesname': '纵横G700',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M07/65/B9/autohomecar__ChxpWGjRC-yAU15OADettNaWwRI061.png',
        'seriesminprice': 329900,
        'seriesmaxprice': 424900,
        'average': 4.5861,
        'specids': '[71510, 72866, 75798, 74880, 73550, 74783, 74881, 74436, 74878, 74879]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 7860,
        'seriesname': 'AION RT',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M02/69/A4/autohomecar__Chtk2Wb2FNWARkC8AAdl-0bNVfo970.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 165800,
        'average': 4.6026,
        'specids': '[70612, 71792, 70133, 74871, 69916, 69915, 70134, 74916, 74884, 74727]',
        'create_time': '2026-04-01 02:36:05'
    },
    {
        'seriesid': 8244,
        'seriesname': '深蓝L06',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M03/1F/84/autohomecar__Chto52kEofmAdOE1ACYQV0twxFU087.png',
        'seriesminprice': 134900,
        'seriesmaxprice': 156900,
        'average': 4.2806,
        'specids': '[75493, 75492, 74149, 75494]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 8436,
        'seriesname': '银河V900',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M03/AA/86/autohomecar__ChxpV2lvPuqAPCYbAFYXaaE0-_k352.png',
        'seriesminprice': 299800,
        'seriesmaxprice': 369800,
        'average': 4.8571,
        'specids': '[76085, 75725, 75735, 76594]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7043,
        'seriesname': '别克E5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M06/FE/A5/autohomecar__CjIFVmhVMQOATS3OAAbPxPYlWLk006.png',
        'seriesminprice': 169900,
        'seriesmaxprice': 211900,
        'average': 4.3843,
        'specids': '[66832, 68969, 73521, 73522, 60605, 72253]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7728,
        'seriesname': '岚图知音',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M07/9C/4C/autohomecar__ChxpVWiMjl6Aa1PKACaEH_-KV7Q300.png',
        'seriesminprice': 196900,
        'seriesmaxprice': 242900,
        'average': 4.5213,
        'specids': '[68301, 68150, 74448, 73955, 73154, 68300]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 8014,
        'seriesname': '小鹏G7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M06/0E/F1/autohomecar__ChxpWGlfdTyAIhhGACuPkLAHM8Q479.png',
        'seriesminprice': 195800,
        'seriesmaxprice': 225800,
        'average': 4.3626,
        'specids': '[76139, 74686, 71365, 73373, 76188, 73712, 76187]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 2357,
        'seriesname': 'Model S',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M02/A2/87/autohomecar__ChxpV2kkItuAV3GGACDDNJllssU883.png',
        'seriesminprice': 842900,
        'seriesmaxprice': 842900,
        'average': 4.8571,
        'specids': '[75788]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7170,
        'seriesname': '银河E8',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M00/EB/45/autohomecar__ChxknGV3yJWAFnjFAAdm5mgiFto615.png',
        'seriesminprice': 149800,
        'seriesmaxprice': 198800,
        'average': 4.519,
        'specids': '[75958, 72042, 72039, 74706, 72040, 74707, 72041]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7456,
        'seriesname': 'eπ008',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M04/A7/F6/autohomecar__ChxoHmXAkBmACWpsAAYHVPTP2Fg492.png',
        'seriesminprice': 169900,
        'seriesmaxprice': 203600,
        'average': 4.5567,
        'specids': '[73818, 73816, 73817, 73910, 73911, 73909, 71969, 73908, 73815]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7400,
        'seriesname': '星海V9',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M03/54/40/autohomecar__Chto52i1WM2Af6WgAFPKcAolq5I502.png',
        'seriesminprice': 179900,
        'seriesmaxprice': 359900,
        'average': 4.5124,
        'specids': '[76102, 74113, 74112, 74412, 74114, 76982, 76502, 76800, 77025, 76527, 74413, 74111, 74115]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7391,
        'seriesname': '仰望U7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M08/9D/67/autohomecar__ChxpWGmump-AD4DeADRnXH1fk5g314.png',
        'seriesminprice': 628000,
        'seriesmaxprice': 888000,
        'average': 4.5163,
        'specids': '[70708, 76729, 76728, 76727, 70710, 64659, 70709, 76730, 75167]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 6492,
        'seriesname': '小鹏G9',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M09/7D/3F/autohomecar__ChxoHWfUDRyAemybAAlC9uPMxAM596.png',
        'seriesminprice': 248800,
        'seriesmaxprice': 278800,
        'average': 4.5909,
        'specids': '[76194, 72158, 75170, 71061, 76192, 71060]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7514,
        'seriesname': '智己L6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M0A/44/9C/autohomecar__Chtk2GgF9BOAT-3ZAAdOw3R2xy0547.png',
        'seriesminprice': 219900,
        'seriesmaxprice': 305900,
        'average': 4.58,
        'specids': '[72625, 71063, 65923, 72624, 67623, 66442, 72489, 67624, 68475]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 6353,
        'seriesname': '深蓝SL03',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M03/57/32/autohomecar__ChtlyGYqfdmARfRkAAgQ_zaC-v4243.png',
        'seriesminprice': 129900,
        'seriesmaxprice': 146900,
        'average': 4.1429,
        'specids': '[72282, 72284, 70106, 70107]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7812,
        'seriesname': '领克Z20',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M00/3B/2A/autohomecar__ChxkPmblQVWAREBaAAZjmyKsUDc151.png',
        'seriesminprice': 109900,
        'seriesmaxprice': 150900,
        'average': 4.5018,
        'specids': '[70771, 73953, 69213, 73165, 75691, 70772]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7003,
        'seriesname': '仰望U8',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M09/1C/30/autohomecar__Chto52m71WeAZCLoADZSBg_KVsc763.png',
        'seriesminprice': 1008000,
        'seriesmaxprice': 1098000,
        'average': 4.5977,
        'specids': '[60268, 76716]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7838,
        'seriesname': '腾势Z9',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M00/69/68/autohomecar__ChxkPmdOb2WAe1GBAAdLDEzn6Zg780.png',
        'seriesminprice': 334800,
        'seriesmaxprice': 414800,
        'average': 4.5549,
        'specids': '[69566, 69565, 69563, 69564, 69559]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7692,
        'seriesname': '马自达EZ-6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M09/6A/01/autohomecar__ChxkPWcrYJ-AApi2AAZSGMS4BTI322.png',
        'seriesminprice': 119800,
        'seriesmaxprice': 162800,
        'average': 4.5921,
        'specids': '[75513, 75518, 75510, 75511, 75516, 75515, 75514, 75512, 75509, 75508, 75517]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 8544,
        'seriesname': '博越REV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M04/4E/1F/autohomecar__ChxpVmnBL-uAPxeEACa2UEaeO_M366.png',
        'seriesminprice': 113900,
        'seriesmaxprice': 126900,
        'average': 0.0,
        'specids': '[76749, 76748, 76558]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7028,
        'seriesname': '极氪X',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M05/62/77/autohomecar__ChxpVWkLDlCAeZryADKGpna4_-0357.png',
        'seriesminprice': 149000,
        'seriesmaxprice': 199000,
        'average': 4.4413,
        'specids': '[70576, 68920, 75578, 69933, 68922, 75557, 75579, 68921]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 6002,
        'seriesname': '红旗E-QM5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M0A/90/AF/autohomecar__Chtk3WCd0Y2AKjBnAAcJzLq4tp0660.png',
        'seriesminprice': 89800,
        'seriesmaxprice': 239800,
        'average': 4.3241,
        'specids': '[72244, 67711, 73233, 56058, 73232, 73234, 67051, 75361, 75625, 67710, 67709]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 8464,
        'seriesname': 'FOR ME',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M0B/B4/CA/autohomecar__Chto52lUwh2ALEfPAC2xtFHOY6E920.png',
        'seriesminprice': 508000,
        'seriesmaxprice': 558000,
        'average': 0.0,
        'specids': '[76605, 75937]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7364,
        'seriesname': '纳米01',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M06/94/A8/autohomecar__ChtlxWWFZ46AafJ4AAfAeIN0Yx8951.png',
        'seriesminprice': 59800,
        'seriesmaxprice': 139800,
        'average': 4.4022,
        'specids': '[73723, 67531, 75038, 75269, 69722, 75151, 75270, 75271, 75268, 71111, 75272, 67530, 69720, 75150, 69721, 67950]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 8091,
        'seriesname': '猛士M817',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M07/9A/7F/autohomecar__ChtlyGh-9UGAbaIqAAi1kufvFrA072.png',
        'seriesminprice': 301900,
        'seriesmaxprice': 369900,
        'average': 4.5982,
        'specids': '[73093, 73367, 75791, 75060]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 5823,
        'seriesname': '欧拉好猫',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M05/A4/08/autohomecar__ChxkmWhL8cKAOwdAAAaUfMTkisQ392.png',
        'seriesminprice': 83800,
        'seriesmaxprice': 103800,
        'average': 4.6059,
        'specids': '[73411, 73265, 72277]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 8266,
        'seriesname': '仰望U8 L',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M09/03/CC/autohomecar__ChxpV2iucqGAD7AUADo-v_6ZUM0933.png',
        'seriesminprice': 1280000,
        'seriesmaxprice': 1300000,
        'average': 4.5849,
        'specids': '[72672, 76715]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7158,
        'seriesname': '银河L7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M03/71/E0/autohomecar__ChtlyGgHVBeAQLFKAAYy9jru0-0873.png',
        'seriesminprice': 115800,
        'seriesmaxprice': 148800,
        'average': 4.4242,
        'specids': '[70348, 71500, 71763, 71762]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 6337,
        'seriesname': '驱逐舰05',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M08/35/2F/autohomecar__ChxoHmW4yg6ABc33AAYuGIYuF_g057.png',
        'seriesminprice': 79800,
        'seriesmaxprice': 136800,
        'average': 4.5209,
        'specids': '[66738, 73237, 66740, 66739, 66741, 69284, 73236, 69283, 66742, 66734]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 2664,
        'seriesname': 'Model X',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M06/BF/84/autohomecar__ChxpWGkmhgyALr7XACVlyrKrPk4973.png',
        'seriesminprice': 882900,
        'seriesmaxprice': 882900,
        'average': 4.5715,
        'specids': '[75786]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7167,
        'seriesname': '银河L6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M06/45/32/autohomecar__CjIFU2V4EJyAa0qEAAZj03xUyII345.png',
        'seriesminprice': 79800,
        'seriesmaxprice': 106800,
        'average': 4.4871,
        'specids': '[71464, 71463, 71465, 71466, 70353]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7897,
        'seriesname': '五菱之光新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M0B/43/FA/autohomecar__Chtk2WcPXPeAWqYGAAfGmEGwVQQ329.png',
        'seriesminprice': 47800,
        'seriesmaxprice': 57800,
        'average': 4.3911,
        'specids': '[1020015, 1021329, 1019511]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7576,
        'seriesname': '电动MINI COOPER',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M05/CF/B4/autohomecar__ChxpV2k_z4KABQtyAC5vywbiTHM572.png',
        'seriesminprice': 209800,
        'seriesmaxprice': 259800,
        'average': 4.1724,
        'specids': '[76770, 75460, 75210, 76006, 76005, 75209]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7345,
        'seriesname': '捷途旅行者C-DM',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M05/2D/3F/autohomecar__Chto52kcMTSAbspAAC5gUoYvGps757.png',
        'seriesminprice': 159900,
        'seriesmaxprice': 239900,
        'average': 4.5099,
        'specids': '[64751, 72572, 67385, 72570, 72270, 75722, 67386, 75721, 75661, 75723, 73284, 75724, 72110, 75599, 64117, 72571]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 4344,
        'seriesname': '奔驰S级新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g2/M09/5A/AD/autohomecar__ChwFql9QXhCAGvKxAAmJJujfBso894.png',
        'seriesminprice': 1308300,
        'seriesmaxprice': 1308300,
        'average': 0.0,
        'specids': '[71822]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 8084,
        'seriesname': '奔驰CLA新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M0A/63/16/autohomecar__ChxpVmkLGemAFWyyACjulfRjgtk170.png',
        'seriesminprice': 249000,
        'seriesmaxprice': 285600,
        'average': 0.0,
        'specids': '[73788, 72614]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7349,
        'seriesname': '五菱星光',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M00/67/0E/autohomecar__CjIFVGWFaLqAdRSrAAbResIjDJI329.png',
        'seriesminprice': 79800,
        'seriesmaxprice': 125800,
        'average': 4.562,
        'specids': '[72744, 64200, 67978, 72748, 64254, 72715, 64256, 72746, 67977, 72745, 67975, 72747, 67976, 64255]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7329,
        'seriesname': '传祺E8新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M00/F3/38/autohomecar__ChxkmWWFZa2AdKq6AAfJm9TZz4U546.png',
        'seriesminprice': 232800,
        'seriesmaxprice': 238800,
        'average': 4.1429,
        'specids': '[63806, 69510]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 8210,
        'seriesname': '星途ET5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M03/EE/7D/autohomecar__ChxpVWkW8ROAKM-DACWr-tZuIxc947.png',
        'seriesminprice': 144900,
        'seriesmaxprice': 164900,
        'average': 4.4767,
        'specids': '[73836, 74024]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7035,
        'seriesname': '星纪元 ES',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M03/76/24/autohomecar__ChxoHmfTma-AEbedAAadGJrPuFE948.png',
        'seriesminprice': 152800,
        'seriesmaxprice': 299900,
        'average': 4.5681,
        'specids': '[69189, 68911, 71803, 71935, 69557, 72732, 72733, 74869, 74870, 71148, 69923, 71791, 69187, 69188, 68910, 68909, 72731, 69922]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 5845,
        'seriesname': '领克Z10',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M00/12/21/autohomecar__ChxkPmZqvNeAEjTQAAhlAT-80yI259.png',
        'seriesminprice': 186800,
        'seriesmaxprice': 262800,
        'average': 4.3629,
        'specids': '[68725, 69474, 70966, 68107, 69475]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7546,
        'seriesname': '蔚来ET9',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M06/6A/0B/autohomecar__CjIFV2WI6u-AWg1cAAdrtbOuYnk309.png',
        'seriesminprice': 768000,
        'seriesmaxprice': 818000,
        'average': 0.0,
        'specids': '[73852, 66170, 71239]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 4218,
        'seriesname': '小蚂蚁',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M08/42/C5/autohomecar__ChxpVmlkwAqAXZlAAAbm5d71hgA316.png',
        'seriesminprice': 54900,
        'seriesmaxprice': 76900,
        'average': 4.48,
        'specids': '[70211, 72981, 70210, 70212, 76079, 70205, 76080, 70209]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 8103,
        'seriesname': 'EO 羿欧',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M04/72/40/autohomecar__CjIFVGgayICAd_RXAAmBM53Hclo234.png',
        'seriesminprice': 119800,
        'seriesmaxprice': 184800,
        'average': 4.5714,
        'specids': '[75220, 75481, 75329, 75479, 75480, 75041]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 6309,
        'seriesname': 'QQ冰淇淋',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M06/5B/DE/autohomecar__ChtpWGlnXByAR2g4AAe1c42v4_o931.png',
        'seriesminprice': 36900,
        'seriesmaxprice': 49900,
        'average': 4.6428,
        'specids': '[76070, 72662, 70920, 76075, 76253, 76074, 72954]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 5622,
        'seriesname': 'AION V',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M02/14/E3/autohomecar__ChxpV2iwHzSAC66XACoTUeQ6RQk999.png',
        'seriesminprice': 109800,
        'seriesmaxprice': 193600,
        'average': 4.5521,
        'specids': '[71766, 69771, 68294, 68094, 69246, 69772, 69245, 69243, 69733, 74372, 69244, 74653, 74342, 74373, 74371]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7569,
        'seriesname': '深蓝G318',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M09/A0/B9/autohomecar__CjIFU2gCDf-AN0teAAcM3bB6pyo292.png',
        'seriesminprice': 185900,
        'seriesmaxprice': 229900,
        'average': 4.5117,
        'specids': '[71844, 76988, 71843, 72682]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 4867,
        'seriesname': 'Taycan',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M03/55/08/autohomecar__ChxoHmXvGHaAdy5_AAX-jGq-xwU778.png',
        'seriesminprice': 918000,
        'seriesmaxprice': 1568000,
        'average': 4.4607,
        'specids': '[75245, 75247, 75244, 75242, 75246, 75243, 75241]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7738,
        'seriesname': '深蓝L07',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M02/E9/C0/autohomecar__ChxpVmiUGZSACy8MADIyWm1PhJQ689.png',
        'seriesminprice': 145900,
        'seriesmaxprice': 170900,
        'average': 4.6124,
        'specids': '[71649, 74014, 71638, 74012, 74211, 74212, 74015, 71637, 74013, 71639, 71651, 71647, 71648, 71650, 71646]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7223,
        'seriesname': '宝马iX1',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M01/F4/8E/autohomecar__ChxkjmTsQ7iACytkAAkpFnY5exo153.png',
        'seriesminprice': 228000,
        'seriesmaxprice': 268000,
        'average': 4.3714,
        'specids': '[76385, 76387, 74389, 76388, 74388, 74391, 76386, 74390]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 6504,
        'seriesname': '奥迪Q4 e-tron',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M03/43/8D/autohomecar__CjIFU2V4DJKAZ3PJAAl2nZpvFD4657.png',
        'seriesminprice': 289900,
        'seriesmaxprice': 367100,
        'average': 4.5796,
        'specids': '[65051, 65050, 65049, 65047]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7718,
        'seriesname': '长安凯程V919',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M05/69/D4/autohomecar__Chtlx2hHkpSAKPo_AAjOlZnlmdI051.png',
        'seriesminprice': 82900,
        'seriesmaxprice': 225900,
        'average': 4.5004,
        'specids': '[1022607, 1020934, 1018481, 1020948, 1021188, 1022606, 1021317, 1022191, 1020941, 1020938, 1020935, 1020936, 1021316, 1020939, 1021318, 1021169, 1021314, 1022605, 1020933, 1020940, 1021315, 1020937, 1021313, 1021310]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7781,
        'seriesname': '五菱宏光新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M03/86/85/autohomecar__ChtlyGeHVMmAVHkZAAfRUDdDRC4950.png',
        'seriesminprice': 68800,
        'seriesmaxprice': 79800,
        'average': 4.1429,
        'specids': '[1020475, 1019172, 1018930, 1019398, 1022510, 1020477, 1022511]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 5511,
        'seriesname': 'ID.4 X',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M01/2A/DD/autohomecar__ChxpV2iDTGGAKBNzADZW79RTcQ0140.png',
        'seriesminprice': 159888,
        'seriesmaxprice': 211888,
        'average': 4.2972,
        'specids': '[73088, 73087, 73086, 73085]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 8184,
        'seriesname': '比亚迪M9',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M04/42/4E/autohomecar__Chtk2GhZNBGATw5WAAYlE90_vTE104.png',
        'seriesminprice': 229800,
        'seriesmaxprice': 249800,
        'average': 0.0,
        'specids': '[74491, 73549]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7711,
        'seriesname': '捷途山海L7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M04/76/80/autohomecar__Chtk2Wb2iomAd7x8AAh0YAGz67Y968.png',
        'seriesminprice': 114900,
        'seriesmaxprice': 227800,
        'average': 4.1235,
        'specids': '[76868, 69116, 76869, 76870, 76867, 68062, 72045, 69701, 69702, 73329, 76872, 69703, 73331, 72044, 69704, 69700, 73332, 75411, 75410, 76871, 69705, 73330]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 6161,
        'seriesname': '零跑C01',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M07/DE/AB/autohomecar__ChtlxWSiN22AOgguAAaO0K90Hww115.png',
        'seriesminprice': 136800,
        'seriesmaxprice': 199800,
        'average': 4.5446,
        'specids': '[66880, 66923, 66879, 66920, 68431, 66919, 66924]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7127,
        'seriesname': '雅阁新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M01/17/EF/autohomecar__ChxkmWQlIY6AQzlDAAZgDjcahtE466.png',
        'seriesminprice': 238800,
        'seriesmaxprice': 238800,
        'average': 4.1056,
        'specids': '[72263]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7928,
        'seriesname': '传祺向往S7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M0B/41/04/autohomecar__ChxkPWc2vAGAIHjvAAdt7wnoDOI585.png',
        'seriesminprice': 159800,
        'seriesmaxprice': 229800,
        'average': 4.4953,
        'specids': '[70665, 71237, 72101, 72114, 72115, 75006, 75005]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7572,
        'seriesname': '五菱缤果PLUS',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M0A/3E/20/autohomecar__ChxoHWWlBduAEnW-AAZZwAIPGsE313.png',
        'seriesminprice': 75800,
        'seriesmaxprice': 98800,
        'average': 4.3105,
        'specids': '[69389, 66471, 69984, 69983, 66414]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 8216,
        'seriesname': '星光560新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M09/D7/D1/autohomecar__ChxkPmh46ciAbz5KAAbFUs9tT2U377.png',
        'seriesminprice': 91800,
        'seriesmaxprice': 98800,
        'average': 4.5114,
        'specids': '[73862, 73861]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 6898,
        'seriesname': '腾势N7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M05/7A/44/autohomecar__ChtlyGem9ZKAFtc9AAdGCEvPQSM822.png',
        'seriesminprice': 259800,
        'seriesmaxprice': 289800,
        'average': 4.5238,
        'specids': '[71806, 71807, 71605]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 8039,
        'seriesname': '传祺向往M8',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M09/5B/90/autohomecar__ChxpVWj18LeAfRD9ADGVHNhOs3I556.png',
        'seriesminprice': 269900,
        'seriesmaxprice': 409900,
        'average': 3.8374,
        'specids': '[73053, 73141, 76099, 74025, 75302, 76101, 71799, 76100, 75055]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7520,
        'seriesname': '铂智4X',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M08/28/35/autohomecar__ChxknGVgFxmACoeqAAj7xtYhrwQ913.png',
        'seriesminprice': 179800,
        'seriesmaxprice': 238800,
        'average': 4.4728,
        'specids': '[70806, 65874, 65873, 65872, 65875, 70807, 70805, 70808]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7977,
        'seriesname': '海狮07 DM-i',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M03/18/6F/autohomecar__ChxkPmdX0UKAbpNBAAWmShvgI9E821.png',
        'seriesminprice': 169800,
        'seriesmaxprice': 205800,
        'average': 4.5714,
        'specids': '[71069, 71041, 72650]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 6369,
        'seriesname': 'smart精灵#1',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M0B/C5/7C/autohomecar__ChxkjmUROuOAdnNlAASIB0rqqQo183.png',
        'seriesminprice': 154900,
        'seriesmaxprice': 249900,
        'average': 4.4562,
        'specids': '[73148, 72269, 72267, 72268]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 6334,
        'seriesname': '领克09 EM-P',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M07/28/78/autohomecar__CjIFU2V60S-AeCX-AAgE7AeOZ8Q996.png',
        'seriesminprice': 275800,
        'seriesmaxprice': 347800,
        'average': 4.4729,
        'specids': '[66226, 72580, 66225, 66224, 66165, 63330]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 6336,
        'seriesname': '奥迪Q5 e-tron',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M00/03/EA/autohomecar__ChxkqWIURVeAN8nkAAcEu2xVP_A031.png',
        'seriesminprice': 298500,
        'seriesmaxprice': 432500,
        'average': 4.7114,
        'specids': '[62278, 62275, 62270, 68572, 62269, 62274, 62277, 62273, 62268, 62272, 62267, 62271, 62276, 68571]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7275,
        'seriesname': '沃尔沃EX30',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M07/C2/48/autohomecar__ChxkmmSBQuqAdhGpAAYhNhD1ev4097.png',
        'seriesminprice': 200800,
        'seriesmaxprice': 263800,
        'average': 4.5731,
        'specids': '[76893, 76891, 67888, 67889, 71736, 76892, 67887, 63050]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7563,
        'seriesname': '五菱扬光',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M03/19/9A/autohomecar__CjIFV2Wea_-AKFH5AAhtwEE8V30242.png',
        'seriesminprice': 73800,
        'seriesmaxprice': 125800,
        'average': 4.0639,
        'specids': '[1019180, 1021520, 1018835, 1018836]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 8259,
        'seriesname': '岚图追光 L',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M02/DF/A1/autohomecar__ChxpVWkVohGAL3VwAECmjydDaDE365.png',
        'seriesminprice': 279900,
        'seriesmaxprice': 339900,
        'average': 4.5467,
        'specids': '[75370, 74090, 76999]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 6354,
        'seriesname': '阿维塔11',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M05/57/5F/autohomecar__ChxoHWYqfoKAPOBmAAfnk2Orxfw220.png',
        'seriesminprice': 289900,
        'seriesmaxprice': 429900,
        'average': 4.5518,
        'specids': '[72861, 72865, 72821, 72863, 72864, 72862]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7413,
        'seriesname': '奥迪Q6L e-tron',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M07/E9/AB/autohomecar__ChxpVmiUGKWAT0krAFSommA6MZo972.png',
        'seriesminprice': 369800,
        'seriesmaxprice': 399800,
        'average': 4.4702,
        'specids': '[65052, 73243]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7208,
        'seriesname': '大众ID.7 VIZZION',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M01/AA/C4/autohomecar__ChxknGVlX06AXfyvAAmeZixDd3o085.png',
        'seriesminprice': 227777,
        'seriesmaxprice': 262777,
        'average': 4.4619,
        'specids': '[65987, 62442, 62621, 66190]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 4776,
        'seriesname': '微蓝6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g6/M00/72/C3/autohomecar__Chxkj2DnuyyASLi9AAnDGTd0Dqo361.png',
        'seriesminprice': 112800,
        'seriesmaxprice': 168900,
        'average': 4.3196,
        'specids': '[68668, 68957, 65235, 65234, 68958]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7150,
        'seriesname': '哈弗枭龙MAX',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M00/7D/CB/autohomecar__ChtlyGgIbYeAZGw0AAYZAFOQUnA783.png',
        'seriesminprice': 131800,
        'seriesmaxprice': 169800,
        'average': 4.5149,
        'specids': '[72294, 72296, 70352, 72153, 72295]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 8161,
        'seriesname': '荣威M7 DMH',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M06/C0/52/autohomecar__ChtpWGjBMFCAfgvAACt_uhsJFVU032.png',
        'seriesminprice': 97800,
        'seriesmaxprice': 209800,
        'average': 4.5215,
        'specids': '[74337, 75588, 73167, 75590, 75589, 74336]',
        'create_time': '2026-04-01 02:36:06'
    },
    {
        'seriesid': 7344,
        'seriesname': '宝马i5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M0A/2F/61/autohomecar__Chto52kcUf2AZHvmAC0N-u-hBo4943.png',
        'seriesminprice': 368000,
        'seriesmaxprice': 539900,
        'average': 3.7858,
        'specids': '[76448, 76449, 74522, 74524, 74523, 76450]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6639,
        'seriesname': '吉利几何E萤火虫',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M06/E1/43/autohomecar__Chtk3WTsWraAFYcuAAi03cu074U117.png',
        'seriesminprice': 59800,
        'seriesmaxprice': 89800,
        'average': 4.5015,
        'specids': '[67050, 64039, 65581, 64038, 63999]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6671,
        'seriesname': '护卫舰07',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M07/44/1B/autohomecar__CjIFU2V4DeOAcTi_AAfhONI4fzg254.png',
        'seriesminprice': 179800,
        'seriesmaxprice': 259800,
        'average': 4.4451,
        'specids': '[67250, 67272, 67273, 67274, 67271]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 5967,
        'seriesname': 'RAV4荣放双擎E+',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M04/7C/32/autohomecar__ChwFj2IYlH-AONK-AAcm_d0dxAA519.png',
        'seriesminprice': 256800,
        'seriesmaxprice': 297800,
        'average': 4.5351,
        'specids': '[69868, 69870]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7628,
        'seriesname': '与众06',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M06/CB/76/autohomecar__ChxkPmaXrbmAVzaOAAe0BlreatU982.png',
        'seriesminprice': 189900,
        'seriesmaxprice': 249900,
        'average': 4.5243,
        'specids': '[72631, 72629, 72599, 72630]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 5569,
        'seriesname': '蔚来EC6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M0A/B8/7F/autohomecar__ChxkmmghWjWAYWF_AAlrF1dx5wQ939.png',
        'seriesminprice': 358000,
        'seriesmaxprice': 370000,
        'average': 4.5257,
        'specids': '[73728, 73022]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 8209,
        'seriesname': '风云X3',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M02/E5/F7/autohomecar__ChtpWGiUdeCARqmFAC3egiHZJds455.png',
        'seriesminprice': 89900,
        'seriesmaxprice': 129900,
        'average': 4.597,
        'specids': '[75109, 73832, 76427, 73831]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7506,
        'seriesname': '捷途山海T1',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M07/7C/40/autohomecar__ChxkPmcfUk2ALGm9AAol4mQ9LzM824.png',
        'seriesminprice': 134900,
        'seriesmaxprice': 179900,
        'average': 4.5191,
        'specids': '[75317, 73185, 70523, 73183, 73184, 72109, 69469, 73182, 75497, 67849, 70522]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7671,
        'seriesname': '五菱星光S',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M04/64/60/autohomecar__ChtlyGYfXzeAO3ASAAeLhc09A_0982.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 129800,
        'average': 4.5472,
        'specids': '[73580, 73535, 73506, 74240, 73532, 74066]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 4324,
        'seriesname': 'Cayenne新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M03/D2/C8/autohomecar__Chtlx2WFZKiANXOvAAlQi3gOOcs679.png',
        'seriesminprice': 878000,
        'seriesmaxprice': 1998000,
        'average': 4.1512,
        'specids': '[62501, 68385, 64514, 62500, 68386, 65015, 64513, 65016, 68384, 68382, 68383, 68381]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7631,
        'seriesname': '极氪MIX',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M0B/FC/5B/autohomecar__Chtk2WcY9juAfUWRAAkhf9BXs-A251.png',
        'seriesminprice': 279900,
        'seriesmaxprice': 299900,
        'average': 4.5174,
        'specids': '[67165, 67799]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7154,
        'seriesname': '风云A8',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M02/C5/34/autohomecar__CjIFVWWKOROAXsw5AAcC31Auhi0872.png',
        'seriesminprice': 79900,
        'seriesmaxprice': 109900,
        'average': 4.5502,
        'specids': '[72545, 73318, 73040, 72544, 73012]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 4904,
        'seriesname': '帕萨特新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M07/68/07/autohomecar__ChtpWGkgNeeAeXY6AD9SOy6EZ0o187.png',
        'seriesminprice': 217150,
        'seriesmaxprice': 242150,
        'average': 4.4155,
        'specids': '[72659, 59533, 59532]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 4768,
        'seriesname': '奔驰E级新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M03/0D/7C/autohomecar__ChwFj2IhdT2ACJtaAAve4Qv2wMw350.png',
        'seriesminprice': 538600,
        'seriesmaxprice': 538600,
        'average': 4.1939,
        'specids': '[68559, 65775]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6649,
        'seriesname': 'ELETRE',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M03/DB/C4/autohomecar__ChxknGJDj6qAf3HRAAhUxEbY2M8745.png',
        'seriesminprice': 558000,
        'seriesmaxprice': 863000,
        'average': 4.3372,
        'specids': '[74751, 74857, 74867, 74858]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 8083,
        'seriesname': '传祺向往S9',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M01/59/C6/autohomecar__ChxknGgAe4qAIUI-AAbbV3vtmEk853.png',
        'seriesminprice': 229900,
        'seriesmaxprice': 309900,
        'average': 4.5478,
        'specids': '[73964, 76873, 72600, 73962, 73963]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7276,
        'seriesname': '大拿V1',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M05/B6/77/autohomecar__ChxkPmay7WmAT2jmAAiQjAIdjsc962.png',
        'seriesminprice': 88800,
        'seriesmaxprice': 165800,
        'average': 4.5287,
        'specids': '[1020363, 1017521, 1022771, 1022179, 1020364, 1022180, 1017022, 1022770, 1022769, 1020365, 1022772]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7574,
        'seriesname': '宝骏悦也Plus',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M09/A5/CF/autohomecar__ChxpVmkkHFyAZ-tUADkB_Usfus0648.png',
        'seriesminprice': 76800,
        'seriesmaxprice': 116800,
        'average': 4.5557,
        'specids': '[73023, 74136, 71898, 70711, 66436, 73028, 67689, 73003, 73027]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7677,
        'seriesname': '广汽本田P7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M07/07/94/autohomecar__ChtlyGf_Q-eAXIxVAAYqQCalptA626.png',
        'seriesminprice': 199900,
        'seriesmaxprice': 249900,
        'average': 4.5588,
        'specids': '[67766, 72619, 71067]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6013,
        'seriesname': '智己LS7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M0A/07/FC/autohomecar__ChtliGPh5omAEvOrAAY4alzhLhQ625.png',
        'seriesminprice': 339800,
        'seriesmaxprice': 359800,
        'average': 4.6429,
        'specids': '[69131, 68650, 68651]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 8290,
        'seriesname': '欧拉5 EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M09/DF/D1/autohomecar__ChxpWGlBJb-AFgJNAC5jDSMGtjA922.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 133800,
        'average': 4.5967,
        'specids': '[75671, 75669, 75670, 74705, 75672]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7378,
        'seriesname': 'EMEYA',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M0A/4C/D7/autohomecar__ChxkPmc3I5eAEp5qAAZB7PgEjAY852.png',
        'seriesminprice': 528000,
        'seriesmaxprice': 1008000,
        'average': 4.5192,
        'specids': '[74860, 71734, 71751, 71754, 71752, 71753, 74859, 71749, 74750, 74861]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 2761,
        'seriesname': '秦新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M0B/8D/8B/autohomecar__CjIFVWSiOAeAYYHnAAciw7xT3vs956.png',
        'seriesminprice': 168800,
        'seriesmaxprice': 168800,
        'average': 4.2857,
        'specids': '[72914, 72915]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7174,
        'seriesname': '星纪元 ET',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M06/68/6B/autohomecar__ChxoHWfSp4aAd8fkAAa_3L5qO50376.png',
        'seriesminprice': 189800,
        'seriesmaxprice': 319800,
        'average': 4.5498,
        'specids': '[72698, 67723, 70759, 66648, 72696, 67721, 72695, 67724, 67722, 72697, 70758, 73272, 66464, 69435, 66463, 67720, 72494]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 4349,
        'seriesname': '奔驰C级新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M0A/86/DD/autohomecar__Chxky2P3ET-AAuY-AAfFZG03th0823.png',
        'seriesminprice': 410600,
        'seriesmaxprice': 410600,
        'average': 3.9285,
        'specids': '[71974, 69745]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6915,
        'seriesname': '岚图追光',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M08/B9/BB/autohomecar__CjIFU2VvMTCAfz2DAAgYgvxWS1A129.png',
        'seriesminprice': 252800,
        'seriesmaxprice': 385900,
        'average': 4.5501,
        'specids': '[60990, 59292, 76997, 59291, 66115]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 5275,
        'seriesname': '红旗H5 PHEV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M08/B9/BC/autohomecar__ChxoHmfX32-AL6-SAAaaIpI7_24770.png',
        'seriesminprice': 185800,
        'seriesmaxprice': 199800,
        'average': 4.4999,
        'specids': '[71054, 72495]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6035,
        'seriesname': 'ID.6 X',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M06/89/51/autohomecar__ChsEdmLo_QaACwEcAAqAIqjYMhI457.png',
        'seriesminprice': 259888,
        'seriesmaxprice': 293888,
        'average': 4.42,
        'specids': '[62714, 62715, 62716]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7863,
        'seriesname': '风云A8L',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M0A/D0/51/autohomecar__ChxkPmdhPeaACF98AAdGCp0tUcw257.png',
        'seriesminprice': 129900,
        'seriesmaxprice': 149900,
        'average': 4.5973,
        'specids': '[70998, 71146, 69918]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7684,
        'seriesname': 'smart精灵#5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M08/D1/D0/autohomecar__Chto52j_NN6AIh1VACI9XRjtrds577.png',
        'seriesminprice': 189900,
        'seriesmaxprice': 379900,
        'average': 4.5057,
        'specids': '[75056, 68745, 75430, 73835, 68743, 75431, 68746, 69690, 70524, 68744]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7018,
        'seriesname': '远程超级VAN',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M0B/FA/CB/autohomecar__ChtlyGYNBnuAQF8ZAAd82o8X-B8979.png',
        'seriesminprice': 123900,
        'seriesmaxprice': 328000,
        'average': 0.0,
        'specids': '[1020599, 1022749, 1020580, 1023021, 1021967, 1023122, 1020578, 1020576, 1021935, 1022746, 1020583, 1020600, 1020581, 1021934, 1023120, 1020582, 1020601, 1022748, 1021966, 1021964, 1022196, 1020584, 1023121, 1023020, 1020603, 1022745, 1021456, 1021965, 1022744, 1021933, 1022747, 1023022]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6626,
        'seriesname': '远程星享V',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M01/F7/0E/autohomecar__ChxkqWITWtWAcNPsAEp4xZW8cF8596.png',
        'seriesminprice': 94900,
        'seriesmaxprice': 175800,
        'average': 4.5714,
        'specids': '[1017508, 1015553, 1013948, 1015546, 1023196, 1013941, 1015543, 1015551, 1023197, 1015552, 1013946, 1023199, 1016210, 1013943, 1015554, 1015541, 1021372, 1015545, 1021373, 1021377, 1013938, 1019616, 1021043, 1021366, 1013949, 1021369, 1016204, 1013944, 1015550, 1013939, 1021375, 1018889, 1013947, 1021374, 1021370, 1023330, 1021376, 1019339, 1016209, 1013937, 1016202, 1021371, 1013950, 1015548, 1018457, 1015540, 1013951, 1015542, 1016206, 1022568, 1015424, 1016211, 1018456, 1021368, 1023198, 1022569, 1021044, 1023329, 1016208, 1015555, 1016205, 1013952, 1015547, 1016203, 1016207, 1021367, 1013945, 1013942, 1015549, 1015423, 1013940, 1015544]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6907,
        'seriesname': '猛士917',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M09/57/4D/autohomecar__ChxoHWYqfgOALp8gAAnKbBiGiyY563.png',
        'seriesminprice': 637700,
        'seriesmaxprice': 1098000,
        'average': 4.7143,
        'specids': '[76231, 68096, 68771, 62651, 76232, 67780, 73741, 61005, 68053]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 5264,
        'seriesname': '蔚来ET7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M03/9D/5D/autohomecar__ChtlyGYmKa6AdbpxAAdm2lumxBM417.png',
        'seriesminprice': 428000,
        'seriesmaxprice': 458000,
        'average': 4.53,
        'specids': '[67323, 66797]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6150,
        'seriesname': '奔驰EQB',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M08/36/8E/autohomecar__ChxkPWarVWWAGAMxAAaV978IS9c170.png',
        'seriesminprice': 352000,
        'seriesmaxprice': 428000,
        'average': 3.9683,
        'specids': '[69333, 69332]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7898,
        'seriesname': '风云T8',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M0B/A5/78/autohomecar__ChtlyGeIwLeABHbuAAi3pFsV3h0138.png',
        'seriesminprice': 103900,
        'seriesmaxprice': 150900,
        'average': 4.5124,
        'specids': '[70365, 71399, 71909, 71402, 71401, 71405, 71404, 71403, 71400, 71406, 70356, 71407]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 8149,
        'seriesname': '东风风神L8',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M03/2F/7B/autohomecar__ChxpVmia_niAXZTdAEzxRSSp-hI294.png',
        'seriesminprice': 129900,
        'seriesmaxprice': 239900,
        'average': 4.5208,
        'specids': '[76359, 74177, 73138, 74179, 74178]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 8015,
        'seriesname': '比亚迪e7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M08/29/1B/autohomecar__ChxpV2iDLa-AVrhzADB6_aF9_qY343.png',
        'seriesminprice': 103800,
        'seriesmaxprice': 139800,
        'average': 4.5051,
        'specids': '[74242, 73073, 73072, 74243, 71398, 74241]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7633,
        'seriesname': '风云T10',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M03/AD/7A/autohomecar__Chtk2WZ8xcuAcLhKAAm1NMLoT1Y727.png',
        'seriesminprice': 189900,
        'seriesmaxprice': 229900,
        'average': 4.6199,
        'specids': '[72560, 72561, 72562]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6640,
        'seriesname': '奔驰EQE',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g29/M04/76/BE/autohomecar__Chxkm2MNeJqAfdRjAAjCm8i_FVs906.png',
        'seriesminprice': 478000,
        'seriesmaxprice': 627000,
        'average': 4.348,
        'specids': '[75858, 70754, 69750, 75857, 70753, 75856]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7832,
        'seriesname': '蓝电E5 PLUS',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M01/1C/36/autohomecar__Chtk2WdX6f6AagRyAAaTArMS8Kk769.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 168800,
        'average': 4.535,
        'specids': '[73064, 75519, 73679, 73061, 71018, 73060, 73008, 75491, 73000, 73678, 72692, 74792, 72693, 72889, 72890, 73062, 73059, 74791, 75522, 71017, 73063, 72451]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7797,
        'seriesname': '极狐 考拉S',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M0A/4B/9A/autohomecar__ChtpWGlmBdyACXuDAC5lKHlslGE445.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 109800,
        'average': 4.524,
        'specids': '[76263, 76276]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6900,
        'seriesname': '哈弗大狗 PLUS 新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M07/46/F2/autohomecar__ChxpV2i1bZGAYRN8ACxxC1j0vjQ351.png',
        'seriesminprice': 162800,
        'seriesmaxprice': 183800,
        'average': 4.5313,
        'specids': '[74343, 64937, 61646, 59026, 67307, 72641]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6055,
        'seriesname': 'ID.6 CROZZ',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g8/M0A/25/7E/autohomecar__ChsEwGB8EwOAa-DrAAZilvWfpPY783.png',
        'seriesminprice': 205900,
        'seriesmaxprice': 283900,
        'average': 4.6014,
        'specids': '[67825, 64678, 67824, 67826]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6427,
        'seriesname': '宝马i7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M05/D9/B8/autohomecar__ChwFkmOIKOaAf4GYAAZCIPuatfU681.png',
        'seriesminprice': 808000,
        'seriesmaxprice': 1328000,
        'average': 0.0,
        'specids': '[62415, 76468, 62417, 62416, 76469, 62414, 76471, 60892, 76470, 76472, 56703, 76473]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7737,
        'seriesname': '奔驰GLC新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M05/E2/16/autohomecar__ChxpV2kW8aSABvKKADwLBa3_YqQ717.png',
        'seriesminprice': 518000,
        'seriesmaxprice': 518000,
        'average': 4.2857,
        'specids': '[68264]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6276,
        'seriesname': '法拉利296',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M08/30/80/autohomecar__ChxkmWKqoZSAJ8rZAAYj-anVoYo415.png',
        'seriesminprice': 2988000,
        'seriesmaxprice': 4398800,
        'average': 0.0,
        'specids': '[72903, 56694, 51891, 72904]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7537,
        'seriesname': '翼真L380',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M02/5B/37/autohomecar__ChtlyGYfKhOAX01dAAhZtiwF0sM637.png',
        'seriesminprice': 299900,
        'seriesmaxprice': 599900,
        'average': 4.5581,
        'specids': '[71879, 71881, 71878, 72133, 71880]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6421,
        'seriesname': '闪灵',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M0A/BC/26/autohomecar__CjIFVmQ-XvOAGGV5AAbGkFX38nQ533.png',
        'seriesminprice': 5750000,
        'seriesmaxprice': 5750000,
        'average': 0.0,
        'specids': '[53557]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 8301,
        'seriesname': '埃尚',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M08/2E/A7/autohomecar__Chto52jKf46AasO2ACQnPQdfEqU985.png',
        'seriesminprice': 39800,
        'seriesmaxprice': 52800,
        'average': 0.0,
        'specids': '[75377, 74768, 75378, 75379]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6012,
        'seriesname': '智己L7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M03/A4/E4/autohomecar__ChxpVWkkDuqAdnpLADEmZIPYL2U941.png',
        'seriesminprice': 279900,
        'seriesmaxprice': 419900,
        'average': 3.8571,
        'specids': '[66716, 66715, 77018, 66834, 66850]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 5238,
        'seriesname': '比亚迪e2',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M00/A8/9D/autohomecar__Chto52kRToKAWQfBAFt67ITwowM545.png',
        'seriesminprice': 89800,
        'seriesmaxprice': 147800,
        'average': 4.3843,
        'specids': '[67156, 67157, 63011]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6404,
        'seriesname': 'IQ锐歌',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M0B/C8/8F/autohomecar__ChtliGK12bGAD1W0AAnjge9mL9A785.png',
        'seriesminprice': 297700,
        'seriesmaxprice': 419700,
        'average': 4.3276,
        'specids': '[65853, 53345, 57121, 57120]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7705,
        'seriesname': '红旗天工05',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M0A/51/D1/autohomecar__ChxoHWekUs6AYgwmAAYOjIOzSUE664.png',
        'seriesminprice': 159800,
        'seriesmaxprice': 222800,
        'average': 4.5188,
        'specids': '[71948, 71604, 71949, 70751, 71947]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 8208,
        'seriesname': '风云X3L',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M09/9E/EF/autohomecar__ChxpVmj7HK2AEJTwADJyxV3jgg4621.png',
        'seriesminprice': 119900,
        'seriesmaxprice': 159900,
        'average': 4.5671,
        'specids': '[73829, 74132, 73828, 73830]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7214,
        'seriesname': '瑞虎9 C-DM',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M07/3D/2B/autohomecar__ChxkPWblWD2AIqBrAAeze2Ia-vA547.png',
        'seriesminprice': 165900,
        'seriesmaxprice': 185900,
        'average': 4.5771,
        'specids': '[70996, 75028, 67796, 70995, 75027, 69941, 67797, 74625, 69940]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7676,
        'seriesname': '东风本田S7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M0A/8B/E0/autohomecar__ChxoHWfJoriAfM4jAAXxiufQ13M936.png',
        'seriesminprice': 199900,
        'seriesmaxprice': 249900,
        'average': 0.0,
        'specids': '[67767, 71976]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7301,
        'seriesname': '荣威D7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M03/D2/DD/autohomecar__Chtlx2WFZ9uAeXBpAAcKMs74iwo726.png',
        'seriesminprice': 123800,
        'seriesmaxprice': 200800,
        'average': 4.514,
        'specids': '[70660, 70574, 70652, 63814, 63813, 68177, 70661, 70659, 70575, 71617, 65418]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 5715,
        'seriesname': '五菱荣光EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M06/9D/49/autohomecar__ChxpV2mumSyALQ1yAEvMwN_aYBo073.png',
        'seriesminprice': 69800,
        'seriesmaxprice': 69800,
        'average': 4.75,
        'specids': '[1023123]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 5892,
        'seriesname': '本田CR-V新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M04/CB/AC/autohomecar__ChxkjmQJVPCAcf3jAAbCESD_VF4043.png',
        'seriesminprice': 225900,
        'seriesmaxprice': 269900,
        'average': 4.6374,
        'specids': '[59442, 59426, 59443]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 5557,
        'seriesname': '领克06 EM-P',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M02/54/AE/autohomecar__CjIFWGVJmKSAElc9AAgMNEA2oag289.png',
        'seriesminprice': 147800,
        'seriesmaxprice': 156800,
        'average': 4.5266,
        'specids': '[70140, 70141]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 4609,
        'seriesname': '沃尔沃XC60插电式混动',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M05/29/27/autohomecar__Chxky2hdFUeANw1xAAfW_VEhBR8940.png',
        'seriesminprice': 523900,
        'seriesmaxprice': 603900,
        'average': 4.4286,
        'specids': '[73217, 73578, 73353]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7673,
        'seriesname': '红旗HS3 PHEV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M02/6B/00/autohomecar__CjIFU2f3Yc-AH18jAAb6eDxOSOk934.png',
        'seriesminprice': 159800,
        'seriesmaxprice': 161800,
        'average': 4.5509,
        'specids': '[67738, 74444, 73604, 74443, 73371]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6011,
        'seriesname': '魏牌 摩卡新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M08/04/C7/autohomecar__Chtk2WZex-2AazMgABki4gWQ4JU905.png',
        'seriesminprice': 238800,
        'seriesmaxprice': 238800,
        'average': 4.4519,
        'specids': '[65484]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7229,
        'seriesname': '山海炮 Hi4-T',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M0B/AF/50/autohomecar__CjIFU2gIzPKAfZnuAAZu1ml-cgA039.png',
        'seriesminprice': 226800,
        'seriesmaxprice': 249800,
        'average': 4.5635,
        'specids': '[1020878, 1020879, 1020909]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6619,
        'seriesname': 'AION S Plus',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M00/8B/BA/autohomecar__CjIFVWR4e9mAGN57AAbyvefxGg4100.png',
        'seriesminprice': 118800,
        'seriesmaxprice': 156800,
        'average': 4.4426,
        'specids': '[70842, 70845, 73754, 70843, 73755, 70844]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 5026,
        'seriesname': 'AION S',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M00/9A/35/autohomecar__ChsEdmNGiPeARhVLAAfS3QdHZjY746.png',
        'seriesminprice': 139800,
        'seriesmaxprice': 146800,
        'average': 4.4715,
        'specids': '[62283, 64646, 73757, 64648, 74298, 64645, 64647, 73756]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7365,
        'seriesname': '沃尔沃EM90',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M00/DA/29/autohomecar__CjIFV2VTHj-AODFlAAW7xrn6PiQ164.png',
        'seriesminprice': 818000,
        'seriesmaxprice': 818000,
        'average': 4.5811,
        'specids': '[64393]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 8191,
        'seriesname': '睿蓝蓝气球',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M05/02/2F/autohomecar__ChtpWGjIAfKAYWrMAAaZyGzDWu8070.png',
        'seriesminprice': 46900,
        'seriesmaxprice': 50900,
        'average': 4.6593,
        'specids': '[73572, 74728]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6975,
        'seriesname': '奔驰EQE SUV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M03/03/70/autohomecar__ChxknGV4DMSARwkNAAhv2oNgDJA190.png',
        'seriesminprice': 486000,
        'seriesmaxprice': 630600,
        'average': 3.6429,
        'specids': '[68010, 68008, 75757, 68009, 75756, 75755]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 8458,
        'seriesname': '多拉大面',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M0B/4D/89/autohomecar__ChxpWGkywKqAVFmuACtRw7bPcn0612.png',
        'seriesminprice': 76800,
        'seriesmaxprice': 106800,
        'average': 0.0,
        'specids': '[1022654, 1022644, 1022653, 1022643, 1022648, 1022649, 1022645, 1022647, 1022646, 1022655, 1022652, 1022651, 1022650]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 4942,
        'seriesname': '宝马iX',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M03/E0/2C/autohomecar__ChxkmWSiMW6Abz3pAAfAmbQtS_U359.png',
        'seriesminprice': 746900,
        'seriesmaxprice': 846900,
        'average': 4.1429,
        'specids': '[63896, 63899]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 5824,
        'seriesname': '极狐 阿尔法S',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M05/4F/A6/autohomecar__CjIFU2V4LSaACAdRAAhhABoVEmQ885.png',
        'seriesminprice': 209800,
        'seriesmaxprice': 329800,
        'average': 4.5005,
        'specids': '[63475, 62488, 64146, 67998, 63158, 63488, 66557, 63489, 66504, 66556]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6936,
        'seriesname': '宝骏悦也',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M09/94/61/autohomecar__ChxknGRi9DWARS7wAAb0YKyTqXg587.png',
        'seriesminprice': 80800,
        'seriesmaxprice': 90800,
        'average': 4.4544,
        'specids': '[67240, 75495, 67241]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6149,
        'seriesname': '奔驰EQA',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M08/36/87/autohomecar__ChxkPmarVVeAW6cFAAX-Fuyjvlg431.png',
        'seriesminprice': 322000,
        'seriesmaxprice': 322000,
        'average': 2.8571,
        'specids': '[69334]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6869,
        'seriesname': '传祺E9',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M06/F0/AB/autohomecar__ChxkPmcy6xWAfZEOAAdi0URpA7E069.png',
        'seriesminprice': 322800,
        'seriesmaxprice': 392800,
        'average': 4.5506,
        'specids': '[70712, 70713, 70697]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7044,
        'seriesname': 'smart精灵#3',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M01/43/81/autohomecar__CjIFU2V4DH6AD0KMAAiQIf8lMEc679.png',
        'seriesminprice': 164900,
        'seriesmaxprice': 259900,
        'average': 4.4395,
        'specids': '[73742, 75797, 73765, 73766, 73767]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 4746,
        'seriesname': '途观L新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M00/0D/8B/autohomecar__ChwFj2IhdeKAA22WAAtkv4Nl2WU334.png',
        'seriesminprice': 261050,
        'seriesmaxprice': 272050,
        'average': 4.3889,
        'specids': '[59087, 59086]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7036,
        'seriesname': 'Macan新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M07/D8/91/autohomecar__ChxoHmYnm_qAC1nZAAgrgww-TbE002.png',
        'seriesminprice': 598000,
        'seriesmaxprice': 968000,
        'average': 0.0,
        'specids': '[75262, 75261, 75260]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 5955,
        'seriesname': '比亚迪e9',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M05/03/D2/autohomecar__ChwFkGGB-ayAJ3jQAAe8T2tb6ZM094.png',
        'seriesminprice': 169800,
        'seriesmaxprice': 169800,
        'average': 4.0714,
        'specids': '[73582]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7590,
        'seriesname': '红旗HS7 PHEV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M06/14/CC/autohomecar__ChxkPWaN6GyARCbmAAoeiVgZQIo814.png',
        'seriesminprice': 290800,
        'seriesmaxprice': 345800,
        'average': 4.3252,
        'specids': '[76117, 76118, 76116, 76113, 76115, 76114]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 4337,
        'seriesname': '沃尔沃XC90插电式混动',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M06/DE/81/autohomecar__ChxkPmf-GX6AAwXPAAh9CByilYs157.png',
        'seriesminprice': 795900,
        'seriesmaxprice': 894900,
        'average': 4.8571,
        'specids': '[75646, 75647]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 6121,
        'seriesname': '五菱NanoEV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g7/M11/26/F2/autohomecar__ChsEvmFP6NKAMyXHAAqcpQrmlvY928.png',
        'seriesminprice': 56800,
        'seriesmaxprice': 66800,
        'average': 3.8854,
        'specids': '[55597, 53480, 53787, 50664, 53479, 60051]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7380,
        'seriesname': '红旗HQ9 PHEV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M02/62/B3/autohomecar__ChxoHmYEzl6ATo_hAAuY0t6l4Bo711.png',
        'seriesminprice': 358800,
        'seriesmaxprice': 538800,
        'average': 0.0,
        'specids': '[67489, 67490, 64594, 72857]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7698,
        'seriesname': '极氪001 FR',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M0B/66/9D/autohomecar__ChxoHWZGwFqAcCHoAAfGlhi4l0c712.png',
        'seriesminprice': 769000,
        'seriesmaxprice': 769000,
        'average': 0.0,
        'specids': '[69466]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 4864,
        'seriesname': '沃尔沃S90插电式混动',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M08/63/AD/autohomecar__ChxkmWg5c9qAddu5AAWpquz9V2Q815.png',
        'seriesminprice': 499900,
        'seriesmaxprice': 613900,
        'average': 3.5714,
        'specids': '[72936, 73229, 72935]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7395,
        'seriesname': '昊铂HT',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M0A/BF/B1/autohomecar__ChtliGUxCoOAIKv2AAgdycuc9wo534.png',
        'seriesminprice': 189900,
        'seriesmaxprice': 229900,
        'average': 4.5493,
        'specids': '[72932, 73708, 72930, 72931]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 5062,
        'seriesname': '迈腾GTE插电混动',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M04/C0/09/autohomecar__ChsEel4fu7iAO3fIAAfrhGdVMLw518.png',
        'seriesminprice': 237900,
        'seriesmaxprice': 252900,
        'average': 4.4555,
        'specids': '[54801, 54800]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 4322,
        'seriesname': 'Panamera新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M0B/4B/34/autohomecar__ChxknGVgh3eAbWOPAAeXAgsW6aU728.png',
        'seriesminprice': 1288000,
        'seriesmaxprice': 2248000,
        'average': 4.6628,
        'specids': '[67462, 64338, 75075, 75074, 67460, 66022, 67461]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7323,
        'seriesname': '东风风神L7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M0B/C3/B5/autohomecar__ChxoHmYL4a6ATMzHAAeckTSLjb8023.png',
        'seriesminprice': 94900,
        'seriesmaxprice': 224500,
        'average': 4.4445,
        'specids': '[63737, 73080, 72593, 73078, 72597, 74201, 76847, 73079, 76529, 72594, 69731, 67988, 67931, 72592, 67989, 72596, 72860, 76530, 72627, 71798, 72591, 72590, 75565, 72595, 69102, 76846, 71797, 76914]',
        'create_time': '2026-04-01 02:36:07'
    },
    {
        'seriesid': 7936,
        'seriesname': '奥迪Q6L Sportback e-tron',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M00/58/8F/autohomecar__ChxpWGiHSLGAZwjeADYAlchaK78465.png',
        'seriesminprice': 389800,
        'seriesmaxprice': 419800,
        'average': 4.4179,
        'specids': '[70766, 73244]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7980,
        'seriesname': '荣威D6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M06/18/71/autohomecar__ChxkPmdX0XOAMXsFAASf7KYZlHM866.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 139800,
        'average': 4.5579,
        'specids': '[71044, 72730, 71043, 72734, 72736, 72735]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 8108,
        'seriesname': '锋坦Frontier Pro PHEV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M0A/8D/E3/autohomecar__ChxoHmgJ2TKAZnwtAAWd5Qlr1GY101.png',
        'seriesminprice': 189900,
        'seriesmaxprice': 249900,
        'average': 4.4805,
        'specids': '[75186, 75862, 72757, 75863]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7629,
        'seriesname': '星海S7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M06/BC/45/autohomecar__ChxoHWXxP32AbWirAATTgK7NPnQ292.png',
        'seriesminprice': 119900,
        'seriesmaxprice': 219900,
        'average': 4.5714,
        'specids': '[76372, 75500, 67159, 75503, 73595, 75690, 76899, 76347, 69419, 76371, 71901, 72362, 70954, 71123, 74877, 75501, 75502, 69511, 74445]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7575,
        'seriesname': '长安启源E07',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M09/41/3B/autohomecar__ChtlyGWlFkmAOARlAAdxt3QvkQ8654.png',
        'seriesminprice': 219900,
        'seriesmaxprice': 309900,
        'average': 4.5023,
        'specids': '[74487, 74482, 75666, 74484, 74486, 74485, 74483]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7176,
        'seriesname': 'Revuelto',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M05/8C/E1/autohomecar__ChxoHme2mmKANDb-AAY2kDfm2uo599.png',
        'seriesminprice': 6294994,
        'seriesmaxprice': 6294994,
        'average': 0.0,
        'specids': '[61868]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6029,
        'seriesname': '福特电马',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M04/EB/2D/autohomecar__ChxknGV3yFGAFzL2AAgrx6BJjWI976.png',
        'seriesminprice': 239800,
        'seriesmaxprice': 359800,
        'average': 4.479,
        'specids': '[65382, 66124, 66122, 66123, 66121]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7929,
        'seriesname': '昊铂HL',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M02/49/6E/autohomecar__ChxkPWc3BLGAV1CfAAllMb1e9Qs294.png',
        'seriesminprice': 269800,
        'seriesmaxprice': 319800,
        'average': 4.5036,
        'specids': '[74308, 74304, 74303, 71037, 71448, 70668, 74307, 72204]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6719,
        'seriesname': '五菱Air ev晴空',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M0B/AA/DF/autohomecar__ChxkjmL5rj6ANnguAAcu_8oqjIw739.png',
        'seriesminprice': 57800,
        'seriesmaxprice': 69800,
        'average': 4.443,
        'specids': '[60697, 60696, 56673, 60475]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 3682,
        'seriesname': 'Mirai',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g21/M0E/9F/FB/autohomecar__ChwFRF_a8eaAYJa7AAYoyVwSU-w910.png',
        'seriesminprice': 748000,
        'seriesmaxprice': 748000,
        'average': 0.0,
        'specids': '[59751]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 8089,
        'seriesname': '风云X3 PLUS',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M0B/44/93/autohomecar__ChxpWGi1P1yAPJN6ADiPqQjXqpg872.png',
        'seriesminprice': 109900,
        'seriesmaxprice': 139900,
        'average': 4.5049,
        'specids': '[74205, 74249, 72648, 74248]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 8062,
        'seriesname': '逸动PHEV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M04/A4/C9/autohomecar__Chtk2GfdPk-ATKu5AAbqxxNDBI8080.png',
        'seriesminprice': 84900,
        'seriesmaxprice': 99900,
        'average': 4.4286,
        'specids': '[72238, 72237, 72164]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6303,
        'seriesname': '宝马XM',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g29/M06/F9/57/autohomecar__ChwFk2Mzs8OABblBAAhJpVp7wYk845.png',
        'seriesminprice': 1290000,
        'seriesmaxprice': 2450000,
        'average': 0.0,
        'specids': '[73374, 62467]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 8026,
        'seriesname': '纳米06',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M0A/8C/CE/autohomecar__ChtlyGe2mQWADlsjAAXhyx_Tm-I504.png',
        'seriesminprice': 89900,
        'seriesmaxprice': 149800,
        'average': 4.541,
        'specids': '[72892, 71748, 72482, 73619, 72891, 72483, 73620]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7513,
        'seriesname': '北京越野BJ60增程',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M02/EF/1C/autohomecar__CjIFV2VVdNGASH4yAAfX8QipHQo047.png',
        'seriesminprice': 259800,
        'seriesmaxprice': 304800,
        'average': 4.0,
        'specids': '[69521, 75866, 65789, 72462, 72461, 69522]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7332,
        'seriesname': 'IQ傲歌',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M06/B4/C3/autohomecar__ChxoHWYWMi2ALkmxAAdlflAUw4A688.png',
        'seriesminprice': 239700,
        'seriesmaxprice': 269700,
        'average': 4.5305,
        'specids': '[67520, 67519]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7753,
        'seriesname': '欧陆插电混动',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M04/57/42/autohomecar__Chtk2WdNbkuATcM-AAflknbUn04162.png',
        'seriesminprice': 2929000,
        'seriesmaxprice': 4456000,
        'average': 0.0,
        'specids': '[75079, 75083, 75082, 75078, 75076, 75080, 75081, 75077]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 5480,
        'seriesname': '宝马i4',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M07/4A/F9/autohomecar__ChxkPmc3EUuAX5jVAAXL_SJ6LIw849.png',
        'seriesminprice': 429900,
        'seriesmaxprice': 469900,
        'average': 4.4286,
        'specids': '[68076, 70764]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 8214,
        'seriesname': '锐胜M8新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M06/1D/29/autohomecar__Chto52kEgESAXGzZAENp4KO7hgU460.png',
        'seriesminprice': 159800,
        'seriesmaxprice': 269800,
        'average': 4.8571,
        'specids': '[76857, 75194, 75925, 75240, 75678, 75918, 75563, 75567, 75568, 75924, 75921, 75571, 75561, 75919, 75920, 75572, 75922, 73850, 75923, 75926, 75679, 75573, 75570, 75183, 75562, 75569]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6641,
        'seriesname': '荣威iMAX8新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M09/14/7B/autohomecar__CjIFVmS1AUmAbSHDAApsq15EKIo792.png',
        'seriesminprice': 199900,
        'seriesmaxprice': 319800,
        'average': 4.5229,
        'specids': '[75432, 71618, 70650, 66374, 67814, 76677, 70651, 75558]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7805,
        'seriesname': 'MG ES5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M05/7B/19/autohomecar__Chtk2WcSC5KAEe5iAAcz4rIeIK0090.png',
        'seriesminprice': 136900,
        'seriesmaxprice': 196900,
        'average': 4.6032,
        'specids': '[72344, 69101, 70618]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6525,
        'seriesname': '雷克萨斯RZ',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M08/44/52/autohomecar__CjIFU2V4DmqAGRVMAAWXKnF3vq8585.png',
        'seriesminprice': 355900,
        'seriesmaxprice': 459900,
        'average': 4.2052,
        'specids': '[60660, 66189, 66188, 60659]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 5382,
        'seriesname': '奔驰EQS',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M05/23/68/autohomecar__ChxpWGkcNQ2ABG93AEPdRBpwex0365.png',
        'seriesminprice': 881000,
        'seriesmaxprice': 1339000,
        'average': 4.7143,
        'specids': '[61683, 74778, 61685, 61684]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7352,
        'seriesname': '起亚EV5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M06/F1/BE/autohomecar__ChxknGVpwgqARCYOAAdodrFlI_w340.png',
        'seriesminprice': 149800,
        'seriesmaxprice': 255800,
        'average': 4.5868,
        'specids': '[67790, 70714, 70777, 70779, 70778, 70781, 70780, 70782, 70776, 70787, 70775, 70774]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 5755,
        'seriesname': 'MG Cyberster',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M09/00/05/autohomecar__Chtlx2TsapiAKWjiAAe7G_xNO8w646.png',
        'seriesminprice': 319800,
        'seriesmaxprice': 365800,
        'average': 4.6092,
        'specids': '[66580, 62447, 62448, 72665, 73652, 73651, 58304]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7452,
        'seriesname': 'AION S MAX',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M04/03/42/autohomecar__ChxknGV4DFqAbNXDAAjQcSobfwQ179.png',
        'seriesminprice': 118800,
        'seriesmaxprice': 191600,
        'average': 4.5162,
        'specids': '[68803, 65446, 65367, 69151, 65443, 66176, 65445, 65444, 68804, 66175, 68805]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7923,
        'seriesname': '长安CS55PLUS PHEV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M02/54/A8/autohomecar__ChxpVWkJv2SAF4urADiQHGpJ4tw886.png',
        'seriesminprice': 104900,
        'seriesmaxprice': 112900,
        'average': 4.8571,
        'specids': '[75529, 72165, 70635]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 8058,
        'seriesname': '多米',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M03/9B/7D/autohomecar__ChxknGgazeSASw8GAAZ0R1YCdzQ377.png',
        'seriesminprice': 59900,
        'seriesmaxprice': 69900,
        'average': 4.619,
        'specids': '[72240, 72241]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 5262,
        'seriesname': 'AION LX',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M07/8E/37/autohomecar__ChxkmmG5hQeAQAqRAAevj7PFpKM567.png',
        'seriesminprice': 286600,
        'seriesmaxprice': 469600,
        'average': 4.6457,
        'specids': '[55278, 55280, 55088, 55279]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 8053,
        'seriesname': '极狐 阿尔法S6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M03/00/B9/autohomecar__ChxoHWfc0IuAZr2IAAdklQ5mL8M405.png',
        'seriesminprice': 195800,
        'seriesmaxprice': 249800,
        'average': 4.5714,
        'specids': '[72430, 72144, 72449, 72431, 72447, 73216]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 5994,
        'seriesname': '皓影新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M03/7C/0A/autohomecar__ChxkPmcfUVeAWj0cAAhMRr5HLXU242.png',
        'seriesminprice': 225900,
        'seriesmaxprice': 269900,
        'average': 4.7142,
        'specids': '[70328, 70327, 70329]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6994,
        'seriesname': '蔚来EC7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M02/A5/84/autohomecar__ChtliGOm9HCAcLbSAAbHXxDmFng627.png',
        'seriesminprice': 458000,
        'seriesmaxprice': 490000,
        'average': 4.8571,
        'specids': '[66826, 66805]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 5425,
        'seriesname': '红旗E-HS9',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M07/56/98/autohomecar__ChsEnF8rtVSAftDZAAnoB12Rakk422.png',
        'seriesminprice': 589800,
        'seriesmaxprice': 779800,
        'average': 4.5523,
        'specids': '[67053, 69767, 67055, 69768, 69770, 67052, 67054, 69769]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7227,
        'seriesname': '星途揽月C-DM',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M04/7D/42/autohomecar__ChxoHWfUDVSAYGiyAAeC5l9D-js681.png',
        'seriesminprice': 209900,
        'seriesmaxprice': 233900,
        'average': 4.4856,
        'specids': '[70370, 71903, 71904, 70371]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 8324,
        'seriesname': '大拿V1L',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M0B/F3/9E/autohomecar__ChxpVmjvdwCAc0RqAAkEl05gWiQ084.png',
        'seriesminprice': 124800,
        'seriesmaxprice': 173800,
        'average': 0.0,
        'specids': '[1022779, 1022782, 1022172, 1022781, 1022175, 1022178, 1022177, 1022173, 1022176, 1022171, 1022174, 1022780]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 8289,
        'seriesname': '法拉利849',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M03/BC/C7/autohomecar__ChtpWGjA6NeAYvrIAC9qzc8gu00171.png',
        'seriesminprice': 5168000,
        'seriesmaxprice': 5638000,
        'average': 0.0,
        'specids': '[74650, 74649]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7141,
        'seriesname': 'Urus SE',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M06/7C/D7/autohomecar__ChxoHmgIWteAOcawAAfz29YAirk772.png',
        'seriesminprice': 2971000,
        'seriesmaxprice': 2971000,
        'average': 0.0,
        'specids': '[67935]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6322,
        'seriesname': '欧拉好猫GT',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M04/82/B8/autohomecar__ChwFjmEItc2AFfgjAApJmqjcwVk751.png',
        'seriesminprice': 96800,
        'seriesmaxprice': 106800,
        'average': 4.6494,
        'specids': '[72278, 73412]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7084,
        'seriesname': '昊铂GT',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M04/03/DC/autohomecar__ChxknGV4Db6AJNJeAAcWy0I3aFo611.png',
        'seriesminprice': 153800,
        'seriesmaxprice': 219900,
        'average': 4.3843,
        'specids': '[75486, 75490, 75489, 73363, 75487]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6374,
        'seriesname': '奔驰G级新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M00/47/81/autohomecar__ChxkPWc29K-AM3HBAAhRBh81Px0076.png',
        'seriesminprice': 2170000,
        'seriesmaxprice': 2170000,
        'average': 0.0,
        'specids': '[67883]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7393,
        'seriesname': '探界者Plus',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M09/CB/97/autohomecar__ChxoHmYnUlyAEG23AAocCUPBntc450.png',
        'seriesminprice': 149900,
        'seriesmaxprice': 179900,
        'average': 0.0,
        'specids': '[67454, 66461, 64732, 66457]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7215,
        'seriesname': '瑶光C-DM',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M0A/09/D9/autohomecar__ChxkPmc0FgmAcH8IAAg_XbU3m6w048.png',
        'seriesminprice': 139900,
        'seriesmaxprice': 218800,
        'average': 4.6077,
        'specids': '[73515, 70135, 70136, 74781, 74990, 73323, 74991]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6714,
        'seriesname': 'ARIYA艾睿雅',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M09/43/7A/autohomecar__CjIFU2V4DGyAbhd4AAeK5QGzDc0789.png',
        'seriesminprice': 199900,
        'seriesmaxprice': 282900,
        'average': 4.5705,
        'specids': '[63862, 63863, 63861, 63864, 63860]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7120,
        'seriesname': '极狐 考拉',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M01/9F/4D/autohomecar__ChxoHWY8dOqAV-6UAAh6Om5S_Gs667.png',
        'seriesminprice': 131800,
        'seriesmaxprice': 169800,
        'average': 4.6022,
        'specids': '[64415, 64417, 64416, 61229]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7858,
        'seriesname': '瑞虎8 PLUS C-DM',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M00/25/D9/autohomecar__ChxkPmbkF8uAJxeFAAfvOLR2yfk255.png',
        'seriesminprice': 129900,
        'seriesmaxprice': 158900,
        'average': 0.0,
        'specids': '[69845, 69860, 69858, 69859, 69843, 69844]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7934,
        'seriesname': 'E福顺',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M03/DA/BA/autohomecar__Chtk2GfqBP2AXCBMAAUEYwHtJXU796.png',
        'seriesminprice': 80800,
        'seriesmaxprice': 135000,
        'average': 4.8571,
        'specids': '[1023127, 1023124, 1023125, 1023129, 1019942, 1022960, 1019935, 1019944, 1019939, 1023131, 1023130, 1022484, 1019941, 1020055, 1019945, 1019937, 1022959, 1019940, 1019936, 1020054, 1019943, 1023128, 1023126, 1022483, 1020053, 1019946, 1019938]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6621,
        'seriesname': '元宝',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M01/C4/45/autohomecar__CjIFVmR4DreAQFYBAAwuLQ2tMeY424.png',
        'seriesminprice': 29700,
        'seriesmaxprice': 51900,
        'average': 0.0,
        'specids': '[62191, 63308, 63309, 57976, 60503, 57975, 63301, 63302, 63307, 63306, 55456]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7065,
        'seriesname': '奔驰S级AMG新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M04/A2/5A/autohomecar__ChxpV2kkIFiAZcwEAD2GAfrJqf0953.png',
        'seriesminprice': 2674800,
        'seriesmaxprice': 2853000,
        'average': 0.0,
        'specids': '[67865, 71117]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7963,
        'seriesname': '吉利雷达金刚',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M0B/0F/4E/autohomecar__Chtk2WdJqoqAfI2KAAZGrRRYe7I137.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 248800,
        'average': 4.5792,
        'specids': '[1019771, 1019769, 1022723, 1023294, 1023291, 1022197, 1019770, 1023287, 1023290, 1019681, 1021058, 1023289, 1019768, 1023296, 1021172, 1023292, 1019682, 1021171, 1023295, 1021059, 1019767, 1019766, 1023288, 1021755, 1019684, 1023297, 1021112, 1021170, 1019683, 1021143]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6287,
        'seriesname': '飞驰插电混动',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M08/82/05/autohomecar__Chto52kNsU6ARreYADuyfm-CdSw648.png',
        'seriesminprice': 2530000,
        'seriesmaxprice': 3936000,
        'average': 0.0,
        'specids': '[64368, 75098, 75097, 64366, 75100, 75099, 70180, 64369, 64367]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7221,
        'seriesname': '瑞风RF8 PHEV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M0A/6D/96/autohomecar__ChtliGWFaAuAC10BAAjq9wxWXqw098.png',
        'seriesminprice': 199900,
        'seriesmaxprice': 369900,
        'average': 4.526,
        'specids': '[69912, 65876, 69913, 76757, 69909, 66612, 71872, 76766, 69911, 63745, 76286, 76767]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7947,
        'seriesname': '宝马i4 M',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M04/FC/AA/autohomecar__ChtpWGl4iiOAUzwiAD9AMZavZv4408.png',
        'seriesminprice': 448000,
        'seriesmaxprice': 448000,
        'average': 0.0,
        'specids': '[76477, 73219]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7143,
        'seriesname': '迈巴赫S级新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M06/A0/3E/autohomecar__CjIFVWWFZ2uAOIrIAAZUDWG5Pa8152.png',
        'seriesminprice': 2016000,
        'seriesmaxprice': 2016000,
        'average': 0.0,
        'specids': '[61518]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 8056,
        'seriesname': '极狐 阿尔法T6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M02/31/AB/autohomecar__ChxoHWhwWfSANCyfAAZU3-Dzz2c192.png',
        'seriesminprice': 195800,
        'seriesmaxprice': 215800,
        'average': 4.5782,
        'specids': '[77036, 72155, 72440]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7397,
        'seriesname': '捷途山海L9',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M03/8D/13/autohomecar__ChxoHWe2mk2AD-gYAAYx0UgY5Ko113.png',
        'seriesminprice': 164900,
        'seriesmaxprice': 242900,
        'average': 4.5294,
        'specids': '[72375, 65747, 65745, 72370, 72436, 72371, 72435, 72374, 72369, 65741, 65742, 72373, 65748, 71805, 64744, 65743, 72372, 65746]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6124,
        'seriesname': '欧拉闪电猫',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M01/57/49/autohomecar__ChxoHWYqffCAIhYqAGbD69FN_vs424.png',
        'seriesminprice': 189800,
        'seriesmaxprice': 272800,
        'average': 4.4489,
        'specids': '[56142, 57667, 55717, 65520, 60377, 65502, 65521]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7331,
        'seriesname': '传祺ES9',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M0A/1F/41/autohomecar__ChxkmWTsW2eADS5WAAa5NxjaGdE122.png',
        'seriesminprice': 229800,
        'seriesmaxprice': 229800,
        'average': 4.4319,
        'specids': '[68760]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 4346,
        'seriesname': '奔驰GLE新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M02/A6/1D/autohomecar__ChxpVWkkIC-AEHeZAFEv-30SGTc020.png',
        'seriesminprice': 824800,
        'seriesmaxprice': 824800,
        'average': 4.6307,
        'specids': '[70273]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6770,
        'seriesname': '奔驰C级AMG新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M0A/1A/F9/autohomecar__ChxpV2iB_nuASLA5AFLi3mIPasg712.png',
        'seriesminprice': 1191800,
        'seriesmaxprice': 1191800,
        'average': 0.0,
        'specids': '[67866]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6152,
        'seriesname': '本田e:NS1',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g29/M01/E8/C6/autohomecar__Chxkm2HbxASATKwTAAb0DefIRRo627.png',
        'seriesminprice': 175000,
        'seriesmaxprice': 218000,
        'average': 4.4458,
        'specids': '[56791, 53666, 56138, 56565]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7826,
        'seriesname': '宝骏享境',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M04/35/62/autohomecar__Chtk2Gds8K6AJjCtAAaQfrweViA116.png',
        'seriesminprice': 129800,
        'seriesmaxprice': 188800,
        'average': 4.5683,
        'specids': '[73541, 73538, 69410, 69409, 72484, 71451, 73540, 73539]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7704,
        'seriesname': '红旗天工06',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M05/CD/37/autohomecar__ChtlyGfqMXiALqm-AAYot12G3Tw220.png',
        'seriesminprice': 179800,
        'seriesmaxprice': 262800,
        'average': 3.8572,
        'specids': '[72381, 70750, 72379, 72385, 71047, 72390, 72383]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7924,
        'seriesname': '大通G50插电混动',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M04/8D/DC/autohomecar__ChxkPmcte9OAIGOxAAV1XXV7um8527.png',
        'seriesminprice': 139800,
        'seriesmaxprice': 159800,
        'average': 4.5403,
        'specids': '[75451, 70639, 75373, 75372, 72143]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6735,
        'seriesname': '长安UNI-V 智电iDD',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M03/37/8A/autohomecar__ChxoHmXpbpGAChG0AAX7gOl8rDU060.png',
        'seriesminprice': 114900,
        'seriesmaxprice': 151900,
        'average': 4.4835,
        'specids': '[66462, 61517, 66840, 66841, 62842]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7866,
        'seriesname': '电动MINI JCW',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M05/07/69/autohomecar__ChxoHmf_Q7SAbwLRAAYk4X8R7GA887.png',
        'seriesminprice': 299800,
        'seriesmaxprice': 299800,
        'average': 0.0,
        'specids': '[76007, 75213]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7787,
        'seriesname': '宝马M5新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M00/A2/27/autohomecar__ChtpWGkkHeOAa4UlAC4MI3Ohvgg493.png',
        'seriesminprice': 1468900,
        'seriesmaxprice': 1468900,
        'average': 0.0,
        'specids': '[68878]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7362,
        'seriesname': '瑞驰新能源EC75',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M0B/73/81/autohomecar__ChtliGTjM4SAbhvGAAZAHc9HF54425.png',
        'seriesminprice': 79900,
        'seriesmaxprice': 129900,
        'average': 4.2858,
        'specids': '[1022045, 1020022, 1022051, 1022705, 1019585, 1022706, 1022052, 1019582, 1020020, 1020018, 1021181, 1021178, 1020019, 1022053, 1020017, 1022046, 1020016, 1020021, 1022047, 1022707, 1021180, 1022050, 1019584, 1019588, 1022049, 1019586, 1020023, 1021179, 1022048, 1019587, 1019583, 1022704]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6345,
        'seriesname': '欧拉芭蕾猫',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M02/05/07/autohomecar__ChtliGLOKe2AQPV6AAnxkHjc6TI251.png',
        'seriesminprice': 149800,
        'seriesmaxprice': 179800,
        'average': 4.533,
        'specids': '[62619, 62582, 62620]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7245,
        'seriesname': '红旗EH7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M05/C2/60/autohomecar__ChxkPmb6deGAA9CUAAXJdk186LA372.png',
        'seriesminprice': 208800,
        'seriesmaxprice': 309800,
        'average': 4.6086,
        'specids': '[69713, 69710, 65253, 72813, 69711, 65254, 72816, 72812, 72815, 69709, 67298, 69712, 66954, 72814, 67297]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 6977,
        'seriesname': '蓝电E5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M08/62/71/autohomecar__ChtliGOuQVSAVxMMAAyVJA5QVQM540.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 153900,
        'average': 4.5234,
        'specids': '[67644, 67646, 63922, 65760, 65759, 60084, 67645, 67642, 63923, 67647, 67643, 62031]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 5977,
        'seriesname': '威兰达新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M06/B0/A7/autohomecar__Chtk3WCYyWaARigrAAn2MNAdh3I000.png',
        'seriesminprice': 267800,
        'seriesmaxprice': 301800,
        'average': 4.5639,
        'specids': '[68622, 68623, 68621]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 4343,
        'seriesname': '逸动新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g29/M07/CF/00/autohomecar__ChwFk2HpOBaAO2fNAAdFx-7-Gqk940.png',
        'seriesminprice': 149900,
        'seriesmaxprice': 149900,
        'average': 4.5032,
        'specids': '[66339, 66340]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7741,
        'seriesname': '宝骏云海',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M0B/A2/2E/autohomecar__ChxpWGkkHNKAFczAACQwQL3i_mg121.png',
        'seriesminprice': 109800,
        'seriesmaxprice': 165800,
        'average': 3.9762,
        'specids': '[68269, 73995, 73878, 68296, 74131, 74312, 68297, 73261, 73879, 73199, 68295, 73192]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7978,
        'seriesname': '悦意07',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M05/15/A6/autohomecar__ChxkPWdXszKAQ8kjAAW1XuJvb9s207.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 139900,
        'average': 4.5117,
        'specids': '[73132, 72913, 74948, 71040, 73131]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 7680,
        'seriesname': '探索06 C-DM',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M0A/57/12/autohomecar__ChtlyGYqfQKARbVtAAhAlf50f5c890.png',
        'seriesminprice': 119900,
        'seriesmaxprice': 139900,
        'average': 4.2254,
        'specids': '[67835, 71257, 67891]',
        'create_time': '2026-04-01 02:36:08'
    },
    {
        'seriesid': 5477,
        'seriesname': '长安睿行EM60',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M07/BD/AA/autohomecar__ChxpVWnLf3CAdtBeAFT_RecjbuM907.png',
        'seriesminprice': 66900,
        'seriesmaxprice': 172900,
        'average': 4.5448,
        'specids': '[1015265, 1023511, 1016626, 1023315, 1023505, 1021290, 1016621, 1023516, 1015266, 1021770, 1021284, 1023518, 1023515, 1023509, 1023508, 1021288, 1020212, 1023316, 1021287, 1023317, 1018521, 1023319, 1020211, 1023507, 1021807, 1023519, 1016627, 1015268, 1021289, 1023321, 1020209, 1016623, 1023506, 1020210, 1023517, 1020213, 1019827, 1019826, 1023512, 1023520, 1023510, 1023314, 1016625, 1016624, 1021806, 1015267, 1020208, 1020249, 1021283, 1020247, 1015264, 1023513, 1021286, 1015794, 1023320, 1023318, 1016628, 1020248, 1021808, 1016622, 1021769, 1021285, 1021932, 1023514, 1021809, 1016620, 1016619]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6702,
        'seriesname': '锐胜王牌M7新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M00/E0/A3/autohomecar__ChxkmWSiOKyAMethAALU6Bt1d5s351.png',
        'seriesminprice': 82800,
        'seriesmaxprice': 249800,
        'average': 4.5668,
        'specids': '[69645, 64377, 69553, 74419, 69550, 69552, 69886, 69544, 69547, 74417, 71249, 70885, 74837, 70886, 74838, 70882, 75554, 74836, 75552, 70881, 69545, 74835, 69555, 69646, 64374, 69543, 74415, 74834, 64376, 69542, 74833, 69554, 69548, 73029, 76296, 71248, 74416, 74418, 69549, 69551, 70884, 69541, 76297, 74414, 70883, 69546, 75553]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7178,
        'seriesname': '英仕派新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M07/89/CB/autohomecar__ChxkjmR3DyiAWgJUAAh19j9SoTk091.png',
        'seriesminprice': 268800,
        'seriesmaxprice': 268800,
        'average': 4.5629,
        'specids': '[73519]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6376,
        'seriesname': '迈巴赫EQS SUV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M05/C4/AF/autohomecar__ChxkmWQ9TnOAZu-dAAoKknxBty0195.png',
        'seriesminprice': 1486000,
        'seriesmaxprice': 1595000,
        'average': 0.0,
        'specids': '[74463, 68011]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 5061,
        'seriesname': '探岳GTE插电混动',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M06/6E/15/autohomecar__Chto52kgNmyAQYvHAFT9zJBMLiU781.png',
        'seriesminprice': 242900,
        'seriesmaxprice': 242900,
        'average': 4.4233,
        'specids': '[66573]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 5574,
        'seriesname': '牧马人新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M01/76/72/autohomecar__ChwFjmC9zByABAyzAAt01hUgvlA998.png',
        'seriesminprice': 499900,
        'seriesmaxprice': 579900,
        'average': 4.4413,
        'specids': '[73666, 63916, 63419]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7751,
        'seriesname': '吉利幸福号',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M0A/8F/C9/autohomecar__Chtk2WcgSCqAB_F_AAonLiVOe5s799.png',
        'seriesminprice': 169900,
        'seriesmaxprice': 229900,
        'average': 0.0,
        'specids': '[68364, 69319, 68365, 69320]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6155,
        'seriesname': '宝骏KiWi EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M07/B7/EA/autohomecar__ChxknGL9n7qAOoRVAAlSWX2DFWs343.png',
        'seriesminprice': 87800,
        'seriesmaxprice': 102800,
        'average': 4.4785,
        'specids': '[59206, 59194, 59193, 59207, 57662, 59205]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6778,
        'seriesname': '五菱征程新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M07/D7/95/autohomecar__CjIFU2UD8gmADbCLAAZcvDoH0vQ329.png',
        'seriesminprice': 145800,
        'seriesmaxprice': 155800,
        'average': 0.0,
        'specids': '[64810, 64808, 64807, 57594, 64809]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 5825,
        'seriesname': '比亚迪D1',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M00/5D/64/autohomecar__ChtliGSiNYqABUaUAAcAgqN7c1U152.png',
        'seriesminprice': 160800,
        'seriesmaxprice': 169800,
        'average': 4.5,
        'specids': '[63696, 60414]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 4983,
        'seriesname': '吉利几何A',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g3/M08/9D/16/autohomecar__ChsEkV1JJdmAIR_GAAf8zKmm0mU464.png',
        'seriesminprice': 143800,
        'seriesmaxprice': 207800,
        'average': 4.2429,
        'specids': '[56972, 69609, 58890, 60307, 56559, 64209, 56556, 68263, 56557, 56558, 56555]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 5371,
        'seriesname': '比亚迪e3',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M05/2B/84/autohomecar__ChtpWGiDVGmAPcGFAC3LVrTMMp8591.png',
        'seriesminprice': 154800,
        'seriesmaxprice': 155800,
        'average': 4.531,
        'specids': '[51306, 52635]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7632,
        'seriesname': '电动MINI ACEMAN',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M0B/AF/D7/autohomecar__Chtk2WbO-IKAA2g9AAiZ7-tMjP0815.png',
        'seriesminprice': 229900,
        'seriesmaxprice': 259900,
        'average': 4.4195,
        'specids': '[75219, 75218]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7211,
        'seriesname': '大家7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M00/A7/B6/autohomecar__ChtlxmVbCCaAUkpyAAYK3H4RbCU193.png',
        'seriesminprice': 189900,
        'seriesmaxprice': 259800,
        'average': 4.5828,
        'specids': '[72058, 72064, 72061, 72095, 72056, 72057, 72055, 72059, 72062, 72063, 72060, 72096, 72097]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6767,
        'seriesname': '雷克萨斯RX新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M00/13/AC/autohomecar__Chxky2PskOSATVu9AAkIRCB2Mvk267.png',
        'seriesminprice': 549000,
        'seriesmaxprice': 549000,
        'average': 4.5714,
        'specids': '[70425]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6861,
        'seriesname': '瑞虎7 PLUS新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M03/2C/75/autohomecar__ChwFj2NZ6cyAI5wCAAwwGBLrULY543.png',
        'seriesminprice': 129900,
        'seriesmaxprice': 166900,
        'average': 4.6364,
        'specids': '[64342, 61853, 64344, 64343, 58643, 61854]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 8043,
        'seriesname': '示界06',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M0B/66/45/autohomecar__Chtk2WfiGkyACz-BAAbzrc_Qt7w762.png',
        'seriesminprice': 125800,
        'seriesmaxprice': 125800,
        'average': 4.4989,
        'specids': '[71834]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6913,
        'seriesname': '红旗天工08',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M0B/11/F8/autohomecar__ChxkPmc0Zx2AHvgGAAcY-b9ByZ0018.png',
        'seriesminprice': 215900,
        'seriesmaxprice': 339800,
        'average': 4.6173,
        'specids': '[71320, 72838, 71322, 72443, 72840, 72837, 71321, 72839, 66466, 66441, 72444]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 8095,
        'seriesname': '捷途X70 PLUS C-DM',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M01/30/AF/autohomecar__ChtlyGgCCMGAT-xaAAX9y4Fugts056.png',
        'seriesminprice': 139900,
        'seriesmaxprice': 151900,
        'average': 0.0,
        'specids': '[72480, 72479, 72686, 72685]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6684,
        'seriesname': 'Grecale格雷嘉新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M0A/3D/95/autohomecar__ChxknGI5ya-AZKVmAAbwCLGUNGQ904.png',
        'seriesminprice': 898800,
        'seriesmaxprice': 898800,
        'average': 0.0,
        'specids': '[70990]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7542,
        'seriesname': '猛士M800',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M04/EB/3B/autohomecar__ChxknGV3yHCAUih_AAne_l3yf8U178.png',
        'seriesminprice': 879000,
        'seriesmaxprice': 979000,
        'average': 0.0,
        'specids': '[66144, 69780]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 4714,
        'seriesname': '添越插电混动',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M09/4A/9C/autohomecar__ChwFjmC3RgCAeumWAAoFOABhjXQ530.png',
        'seriesminprice': 2630000,
        'seriesmaxprice': 3308000,
        'average': 0.0,
        'specids': '[65995, 65993, 65994, 68020]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7216,
        'seriesname': '风云T6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M07/D1/26/autohomecar__ChxkPmZ057WAIEg6AAe4RDn-CNc954.png',
        'seriesminprice': 129900,
        'seriesmaxprice': 156900,
        'average': 0.0,
        'specids': '[67526, 65773, 67527]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6008,
        'seriesname': '奔腾NAT',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M08/22/BD/autohomecar__ChwFkGBzsm6AZTgFAAbrqpTMf5g503.png',
        'seriesminprice': 139800,
        'seriesmaxprice': 162800,
        'average': 3.2858,
        'specids': '[61508, 61512, 61511, 61503, 61513, 61507, 61595, 61502, 61596, 61510, 64912, 61504, 70955, 61594]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 8233,
        'seriesname': '跨越星光 EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M08/9B/6D/autohomecar__ChxpVmiMfkCAGbX2AEvyc7WP0wQ030.png',
        'seriesminprice': 99900,
        'seriesmaxprice': 165900,
        'average': 4.6076,
        'specids': '[1021918, 1023149, 1021908, 1021920, 1021911, 1021921, 1023151, 1023154, 1021906, 1021904, 1021923, 1023145, 1022106, 1021909, 1021919, 1021914, 1022110, 1021915, 1021916, 1021929, 1023152, 1023148, 1021917, 1022108, 1022111, 1021913, 1021910, 1023153, 1021922, 1021930, 1023147, 1022109, 1022107, 1023150, 1021925, 1021927, 1023146, 1021912, 1021905, 1021907, 1021926, 1021924, 1021931, 1021928]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7271,
        'seriesname': '宝骏云朵',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M02/4C/94/autohomecar__ChxknGRbORqAC4WcAAc1A7hyr4c400.png',
        'seriesminprice': 95800,
        'seriesmaxprice': 145800,
        'average': 4.5042,
        'specids': '[65043, 63943, 65947, 63927, 63023, 63941, 63942]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7744,
        'seriesname': '领睿新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M06/6B/89/autohomecar__ChxpVmkgGpGAMrAWAE4oFqVYrKY979.png',
        'seriesminprice': 168800,
        'seriesmaxprice': 199800,
        'average': 4.4789,
        'specids': '[70796, 70797, 68273, 70798]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 831,
        'seriesname': '比亚迪e6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M07/07/8B/autohomecar__Chtk2WcZremABwfxAAhQZW1JVY4082.png',
        'seriesminprice': 269800,
        'seriesmaxprice': 269800,
        'average': 4.1986,
        'specids': '[70470, 70469]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7956,
        'seriesname': '宝马iX M60',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M01/EF/DD/autohomecar__ChxkPmdIROaAH1xYAAnLGvvqLp8798.png',
        'seriesminprice': 1009900,
        'seriesmaxprice': 1009900,
        'average': 0.0,
        'specids': '[63897]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7388,
        'seriesname': '世极',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M04/A4/D4/autohomecar__ChxpVWkkDkmADBraAFlXI-PEmck713.png',
        'seriesminprice': 1980000,
        'seriesmaxprice': 1980000,
        'average': 0.0,
        'specids': '[65900]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6188,
        'seriesname': '创维EV6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M07/94/1D/autohomecar__ChtpWGkQjc6AbTamADvPiqqMPQM260.png',
        'seriesminprice': 98800,
        'seriesmaxprice': 259800,
        'average': 3.8571,
        'specids': '[76327, 76328, 75853, 75852, 69256, 67330, 68846, 74091, 76368, 73466, 69255, 74734, 70394, 73744, 76369, 70444, 67284, 65932]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6707,
        'seriesname': '瑞虎8 PRO新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M08/D2/61/autohomecar__Chtk3WPp5gqAITnwAAb3OdDlohU053.png',
        'seriesminprice': 137900,
        'seriesmaxprice': 198900,
        'average': 4.7143,
        'specids': '[64072, 64073, 70598, 64074, 69364]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7723,
        'seriesname': '五菱E5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M05/7C/05/autohomecar__ChxoHWYrTlaAO0VFAAdaZDIPtac282.png',
        'seriesminprice': 159800,
        'seriesmaxprice': 169800,
        'average': 0.0,
        'specids': '[68093, 68092]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7238,
        'seriesname': '捷途山海L6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M04/3E/E3/autohomecar__ChxkPWa6-DeAcL4gAAhZ-WAtg5g504.png',
        'seriesminprice': 123900,
        'seriesmaxprice': 144900,
        'average': 4.487,
        'specids': '[65436, 69615, 69495]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 8073,
        'seriesname': '捷途X90 C-DM',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M08/10/1A/autohomecar__ChxknGfuYW-ANZftAAj83-0TIQM791.png',
        'seriesminprice': 159900,
        'seriesmaxprice': 243900,
        'average': 0.0,
        'specids': '[72429, 73797, 73799, 73798, 72500, 73800, 72501, 72502]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7592,
        'seriesname': 'vala pro',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M01/13/C9/autohomecar__Chtk2WcM-nKAM6VrAAeNSVRrsWs053.png',
        'seriesminprice': 268000,
        'seriesmaxprice': 268000,
        'average': 0.0,
        'specids': '[76033, 70313]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7489,
        'seriesname': '菱势黄金仓',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M09/4C/C1/autohomecar__ChxkqWVN5HyASzpGAAic5JxrF8w466.png',
        'seriesminprice': 73800,
        'seriesmaxprice': 188000,
        'average': 4.2858,
        'specids': '[1017944, 1017310, 1021094, 1020799, 1020800, 1017943, 1021093, 1017875, 1017311, 1021472, 1021174, 1017942, 1021150]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7088,
        'seriesname': '奇瑞舒享家',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M0B/63/26/autohomecar__ChxkqWT5PxWAa5tLAAYUQw_dLIc230.png',
        'seriesminprice': 129900,
        'seriesmaxprice': 172900,
        'average': 4.3251,
        'specids': '[64087, 65430, 64740, 64739, 69594, 69595, 64738, 65431, 64088, 61003, 67672]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 4892,
        'seriesname': '长安睿行EM80',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M00/BF/76/autohomecar__ChtpWGnLf2CADS-rAFQSYFHWEn0133.png',
        'seriesminprice': 69900,
        'seriesmaxprice': 192800,
        'average': 4.5871,
        'specids': '[1023491, 1016612, 1016609, 1020202, 1023495, 1020246, 1023488, 1016611, 1021802, 1023309, 1015275, 1016613, 1016426, 1023494, 1021281, 1015274, 1021282, 1020201, 1021273, 1020245, 1021275, 1016618, 1015272, 1023492, 1020846, 1020200, 1016425, 1023311, 1016430, 1021274, 1015273, 1021276, 1021277, 1016433, 1023502, 1016431, 1020207, 1021280, 1023312, 1021269, 1021805, 1023306, 1023489, 1023493, 1021272, 1020204, 1016427, 1017438, 1016615, 1021803, 1020847, 1016614, 1023310, 1023504, 1023307, 1016617, 1021804, 1016608, 1016428, 1021270, 1020244, 1016610, 1020199, 1021268, 1016616, 1015271, 1023487, 1021279, 1016429, 1023490, 1023498, 1021256, 1023503, 1020205, 1023308, 1020250, 1016432, 1023501, 1023496, 1023499, 1016434, 1015793, 1023497, 1021271, 1023313, 1021278, 1020206, 1020848, 1020845, 1019932, 1020203, 1023500, 1017439]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 5146,
        'seriesname': 'Valhalla',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M01/D0/E4/autohomecar__ChxpVWknrxOATlAuAC3tjl9xWfA866.png',
        'seriesminprice': 10688000,
        'seriesmaxprice': 11788000,
        'average': 0.0,
        'specids': '[71084, 76743]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7950,
        'seriesname': '宝马M760Le',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M06/A5/F1/autohomecar__ChxpVmkkHgyASLNaAC5JqZU2FCY856.png',
        'seriesminprice': 1598000,
        'seriesmaxprice': 1598000,
        'average': 0.0,
        'specids': '[62587]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7949,
        'seriesname': '宝马i7 M70L',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M03/EE/56/autohomecar__Chtk2WdINjCAT9apAAc8H8TqN3Q453.png',
        'seriesminprice': 1598000,
        'seriesmaxprice': 1598000,
        'average': 0.0,
        'specids': '[62588, 76478]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 8017,
        'seriesname': '羿驰05',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M04/55/15/autohomecar__ChxoHmeE7W2AdPMTAAOkEtEl1d4963.png',
        'seriesminprice': 129800,
        'seriesmaxprice': 179800,
        'average': 4.6684,
        'specids': '[71425, 76866, 71426, 76864, 74720, 76865, 71424]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 4840,
        'seriesname': '领克01 EM-P',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M01/3F/37/autohomecar__CjIFV2SiN7uAMqo_AAlB8Kq2PRw188.png',
        'seriesminprice': 195800,
        'seriesmaxprice': 223800,
        'average': 4.4987,
        'specids': '[58998, 58997, 58249]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7920,
        'seriesname': '五菱扬光电卡',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M00/5B/75/autohomecar__Chtk2WcqzsWAB0laAAWpHAStM_o021.png',
        'seriesminprice': 84800,
        'seriesmaxprice': 91800,
        'average': 0.0,
        'specids': '[1019589, 1019590]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7948,
        'seriesname': '宝马i5 M60',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M09/ED/CF/autohomecar__ChxkPWdIMmaAFgJ8AAiIyRYl9Og856.png',
        'seriesminprice': 558000,
        'seriesmaxprice': 558000,
        'average': 0.0,
        'specids': '[76480, 63217]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7434,
        'seriesname': '长安猎手',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M05/B8/0B/autohomecar__CjIFU2WDmHSADOHzAAkTJm1XJEc825.png',
        'seriesminprice': 127900,
        'seriesmaxprice': 219900,
        'average': 4.4912,
        'specids': '[1017566, 1021107, 1022155, 1023227, 1020334, 1021105, 1017158, 1021106, 1017160, 1017159, 1017565, 1017161, 1017567]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 4418,
        'seriesname': '菱智新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M01/72/F1/autohomecar__CjIFVmgtqKSAUWsXAAmEMEALsWY872.png',
        'seriesminprice': 109800,
        'seriesmaxprice': 196900,
        'average': 4.5657,
        'specids': '[74722, 75892, 74510, 76265, 76270, 73091, 76267, 73092, 76266, 76272, 73090, 75893, 76269, 76271, 76268, 73611, 73612, 73089]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6720,
        'seriesname': '易至EV2',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M04/26/B7/autohomecar__ChsFWWNjrruAEsouAFCKj9YdOlg936.png',
        'seriesminprice': 39900,
        'seriesmaxprice': 51900,
        'average': 4.3572,
        'specids': '[74272, 74271, 74270, 69777, 69776]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6261,
        'seriesname': '雷克萨斯NX新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M0A/8F/1E/autohomecar__ChsFJ2J8tcSAV5FrAAfRHWTbEtk070.png',
        'seriesminprice': 429800,
        'seriesmaxprice': 509800,
        'average': 4.5,
        'specids': '[74355, 74356]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6148,
        'seriesname': '大家9',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M08/21/D8/autohomecar__ChsEdmLCeuOAFO9KAAfv7DneaAs593.png',
        'seriesminprice': 269900,
        'seriesmaxprice': 409900,
        'average': 4.483,
        'specids': '[68885, 75903, 66215, 73676, 69656, 68884, 73675, 74450, 66216, 73674, 69655, 69657]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7099,
        'seriesname': '启辰VX6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M00/06/04/autohomecar__ChxkPmdJVJ2AHOWAAAen_4C-WXg953.png',
        'seriesminprice': 134900,
        'seriesmaxprice': 199800,
        'average': 4.5478,
        'specids': '[73811, 69819, 73808, 69238, 70351, 70414, 69818, 73812, 71137, 70238, 73809, 70350, 73810, 69497]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 5590,
        'seriesname': '极狐 阿尔法T',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M07/36/5A/autohomecar__ChsEl1-2HPaAMcpHAAezzWrfQoU765.png',
        'seriesminprice': 254800,
        'seriesmaxprice': 280800,
        'average': 4.5993,
        'specids': '[63485, 62487]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6862,
        'seriesname': '吉利几何M6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M07/FF/73/autohomecar__ChwFj2OYPNaARAUxAAmTDpYRKqI582.png',
        'seriesminprice': 149800,
        'seriesmaxprice': 189800,
        'average': 4.5385,
        'specids': '[59104, 58650, 59529, 59528]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7409,
        'seriesname': '大拿M1',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M09/AC/D8/autohomecar__Chtk2Wb5THCAREJMAAcVPxpje1c649.png',
        'seriesminprice': 176800,
        'seriesmaxprice': 197800,
        'average': 0.0,
        'specids': '[1022777, 1020391, 1020392, 1021421, 1021418, 1022776, 1022774, 1020390, 1022778, 1021419, 1022773, 1021420, 1022775, 1019222]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 5986,
        'seriesname': 'Artura',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M07/92/87/autohomecar__Chtlx2SelKeAZ_VMAAbxOvx3YHk382.png',
        'seriesminprice': 2380000,
        'seriesmaxprice': 2788000,
        'average': 0.0,
        'specids': '[66871, 66874, 58448]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7244,
        'seriesname': '猎光e:NS2',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M03/78/DF/autohomecar__Chtk2WZ6kNKAd_8hAAkisiQ2VdU776.png',
        'seriesminprice': 189800,
        'seriesmaxprice': 209800,
        'average': 0.0,
        'specids': '[68031, 66473, 68033, 68032]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6845,
        'seriesname': '凯翼拾月',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M07/A0/39/autohomecar__CjIFVWWFZweAYFFuAAhpzg5qfzY703.png',
        'seriesminprice': 50900,
        'seriesmaxprice': 99800,
        'average': 4.6667,
        'specids': '[73498, 66172, 63412, 71372, 66171, 74200, 71374, 73497, 71375, 65158, 73501, 73500, 73499, 73502, 73496, 73495, 67553]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6863,
        'seriesname': '吉利几何G6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M04/A8/F9/autohomecar__ChtliGNp8FaANLhTAAYWwbDRjoo323.png',
        'seriesminprice': 119800,
        'seriesmaxprice': 185800,
        'average': 4.4936,
        'specids': '[66498, 64554, 64693, 65460, 64336, 64692, 66499]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6820,
        'seriesname': '吉利雷达地平线',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M09/19/32/autohomecar__ChwFj2LyPzGAUMF5AAz9vobv6pQ411.png',
        'seriesminprice': 136800,
        'seriesmaxprice': 241800,
        'average': 4.5147,
        'specids': '[1020915, 1017910, 1023293, 1018103, 1019124, 1021173, 1021760, 1018105, 1018104, 1018102, 1021144, 1022722, 1021761]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6637,
        'seriesname': '奔驰EQS SUV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M00/31/0F/autohomecar__ChwFkmOjxF-AO-NMAAilO9n5csg829.png',
        'seriesminprice': 910500,
        'seriesmaxprice': 910500,
        'average': 4.127,
        'specids': '[74777]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 4668,
        'seriesname': 'Nexo',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M05/0A/62/autohomecar__ChtlyGfuWOmASN_6AAYSRbxPUW0499.png',
        'seriesminprice': 800000,
        'seriesmaxprice': 800000,
        'average': 0.0,
        'specids': '[60766]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 5759,
        'seriesname': '锐际新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M09/16/44/autohomecar__CjIFWGSiODqAKT-lAAnpVmawXXM872.png',
        'seriesminprice': 210000,
        'seriesmaxprice': 210000,
        'average': 4.4285,
        'specids': '[45547]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6431,
        'seriesname': '风光MINIEV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M01/5D/6E/autohomecar__ChtliGSiNpyASWhhAAkLTgXZoz0788.png',
        'seriesminprice': 32600,
        'seriesmaxprice': 59100,
        'average': 4.3644,
        'specids': '[57762, 53670, 55282, 57763, 57268, 58659, 58434, 55274, 55273, 57764]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6366,
        'seriesname': 'AMG GT新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M03/57/21/autohomecar__ChxoHmYqfnuAItRiAAf-QoaeeKo652.png',
        'seriesminprice': 2285500,
        'seriesmaxprice': 2285500,
        'average': 0.0,
        'specids': '[71311]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7325,
        'seriesname': 'IONIQ 5 N(艾尼氪5N)',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M03/E3/06/autohomecar__ChxkPmbR1eiAM1MrAAZ4ldYusc0540.png',
        'seriesminprice': 388800,
        'seriesmaxprice': 413000,
        'average': 0.0,
        'specids': '[68470, 75728]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 8124,
        'seriesname': '长安猎手 K50',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M07/2C/45/autohomecar__CjIFVmgR8O6AHEuqAAen-Fiw9Zg962.png',
        'seriesminprice': 127900,
        'seriesmaxprice': 229900,
        'average': 4.2972,
        'specids': '[1021741, 1021740, 1023215, 1021247, 1023217, 1023214, 1021747, 1021743, 1020911, 1021249, 1021739, 1021250, 1023213, 1023216, 1021248, 1020914, 1021742, 1021251]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 5396,
        'seriesname': '畅巡',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M04/D5/CE/autohomecar__ChcCQF3xoUGAXMMfAAaIz0hFKWs851.png',
        'seriesminprice': 182900,
        'seriesmaxprice': 197900,
        'average': 4.5116,
        'specids': '[63638, 63637, 64614, 63639, 64613]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7743,
        'seriesname': '领裕新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M05/80/16/autohomecar__ChxoHmZBjU6AE1R2AASJdoUDR54190.png',
        'seriesminprice': 206800,
        'seriesmaxprice': 238800,
        'average': 4.4782,
        'specids': '[70789, 68272, 70790]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6462,
        'seriesname': '奔驰EQE AMG',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M03/A2/4B/autohomecar__ChxpV2kkH1CAMgiEAE2OVkV6Cu8353.png',
        'seriesminprice': 862000,
        'seriesmaxprice': 862000,
        'average': 0.0,
        'specids': '[62689]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6925,
        'seriesname': '飞凡F7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M05/03/AD/autohomecar__ChxknGV4DUeAAh6NAAWlX7f5uRU846.png',
        'seriesminprice': 182900,
        'seriesmaxprice': 182900,
        'average': 4.542,
        'specids': '[73600]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6647,
        'seriesname': '五菱E10',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M02/64/CD/autohomecar__ChxkqWIPDCaAQQPBAAftosDy4NE322.png',
        'seriesminprice': 36800,
        'seriesmaxprice': 39800,
        'average': 0.0,
        'specids': '[1015572, 1013388]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6072,
        'seriesname': '飞凡R7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M05/8D/7E/autohomecar__CjIFVWSiNouAPL7NAAcHrFUgO8c809.png',
        'seriesminprice': 179900,
        'seriesmaxprice': 209900,
        'average': 4.5156,
        'specids': '[73603, 70803, 73602]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6264,
        'seriesname': '长安UNI-K 智电iDD',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M05/61/2A/autohomecar__ChwFjmDIIy6ACHLeAAjLMPpBjV0227.png',
        'seriesminprice': 187900,
        'seriesmaxprice': 215900,
        'average': 4.493,
        'specids': '[66351, 66352, 66354, 66353]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7904,
        'seriesname': '睿蓝8',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M09/41/0B/autohomecar__Chtk2Wc2u-mACcgXAArgGHxRSP4970.png',
        'seriesminprice': 127800,
        'seriesmaxprice': 231800,
        'average': 4.5581,
        'specids': '[71271, 70749, 76341, 76342, 76291, 70426]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7186,
        'seriesname': '钇为3',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M08/F9/A7/autohomecar__ChxkqWWFaQeAFHiZAAgcKkapzPU843.png',
        'seriesminprice': 69900,
        'seriesmaxprice': 149900,
        'average': 4.393,
        'specids': '[67507, 68176, 70165, 67503, 67508, 67506, 72826, 67282, 72827, 72828, 67504, 72829, 67505, 72830, 70744]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 8430,
        'seriesname': '极石ADAMAS',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M06/BF/6D/autohomecar__ChxpVmkTC7yAe_SwACLyo0q-CAY989.png',
        'seriesminprice': 349900,
        'seriesmaxprice': 359900,
        'average': 0.0,
        'specids': '[73854, 73853]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 4240,
        'seriesname': '荣威RX5新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g29/M03/DC/AA/autohomecar__ChwFk2LRHcOAHUqGAAm9WGunoDg830.png',
        'seriesminprice': 147900,
        'seriesmaxprice': 169800,
        'average': 4.5435,
        'specids': '[58308, 56999, 72224, 58309]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7540,
        'seriesname': '风行游艇新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M04/6C/11/autohomecar__Chtk2Wfjp8CAdg6iAAk72jXYn2s398.png',
        'seriesminprice': 154900,
        'seriesmaxprice': 159900,
        'average': 0.0,
        'specids': '[75677, 66142]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6340,
        'seriesname': '跨越星V5 EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g29/M03/13/10/autohomecar__ChwFk2EU3u-AP4a7AAZw6zGzPqg218.png',
        'seriesminprice': 67800,
        'seriesmaxprice': 98000,
        'average': 4.7142,
        'specids': '[1020272, 1020330, 1020274, 1020620, 1020621, 1020326, 1020279, 1020619, 1020276, 1020277, 1020327, 1020275, 1020278, 1020269, 1020622, 1020280, 1020329, 1020324, 1020273, 1020271, 1020325, 1020323, 1020328, 1020270]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6135,
        'seriesname': '领克05 EM-P',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M07/CB/0F/autohomecar__ChwFjmC0jNCAN0zsAAr5xicovBw272.png',
        'seriesminprice': 223800,
        'seriesmaxprice': 223800,
        'average': 4.56,
        'specids': '[58252]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 8411,
        'seriesname': '麒领',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M04/46/E9/autohomecar__ChxpVWkIeqWAZFEOAI9g3lgrnzg341.png',
        'seriesminprice': 199800,
        'seriesmaxprice': 259800,
        'average': 0.0,
        'specids': '[1022663, 1022664, 1022662]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7577,
        'seriesname': '知豆彩虹',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M01/A6/EC/autohomecar__ChxoHWYV7bqAKomvAAZqFMSYInc782.png',
        'seriesminprice': 31900,
        'seriesmaxprice': 60900,
        'average': 4.5506,
        'specids': '[66472, 67817, 67816, 67818, 72675, 72676, 72677, 67125]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6654,
        'seriesname': 'Polestar 4',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M07/93/D0/autohomecar__CjIFVGTsWxyACstzAAdF4RiRQ24598.png',
        'seriesminprice': 338000,
        'seriesmaxprice': 399900,
        'average': 4.5729,
        'specids': '[73083, 65829, 65831, 73084]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7198,
        'seriesname': '曹操60',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M09/BC/C2/autohomecar__CjIFVGQlFwuAJ3tQAAceHjqW2HE224.png',
        'seriesminprice': 119800,
        'seriesmaxprice': 169800,
        'average': 0.0,
        'specids': '[64282, 64283, 70010, 70008, 70009, 64284]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 4554,
        'seriesname': '荣威Ei5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M0B/16/3D/autohomecar__CjIFWGSiOCKAcQiPAAYaA7wXHqQ374.png',
        'seriesminprice': 152800,
        'seriesmaxprice': 166800,
        'average': 4.75,
        'specids': '[50230, 50211, 50047]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 7407,
        'seriesname': '灵悉L',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M06/0D/01/autohomecar__ChxkPWbi0xiAGJRVAAd7edco6Oc059.png',
        'seriesminprice': 149800,
        'seriesmaxprice': 155800,
        'average': 4.7142,
        'specids': '[75408, 75409]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 5241,
        'seriesname': '炮新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g15/M09/7B/89/autohomecar__ChwEoWDlaEGAeNxzAAmX9Wu9ano199.png',
        'seriesminprice': 251800,
        'seriesmaxprice': 267800,
        'average': 0.0,
        'specids': '[1010268, 1010261, 1010260, 1010267]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 5708,
        'seriesname': '五菱EV50',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M00/2F/A4/autohomecar__ChwFkF8WsnuAbODbAA_rLL2V89g952.png',
        'seriesminprice': 124800,
        'seriesmaxprice': 143800,
        'average': 4.375,
        'specids': '[1013674, 1012036, 1012042, 1017056, 1012038, 1012040, 1012037, 1012045, 1012035, 1014238, 1012044, 1013673, 1014239, 1012039, 1012034, 1012043, 1012041]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 6204,
        'seriesname': '五菱电卡',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M03/72/BE/autohomecar__ChwFjmCYq2CAA_uHAAf4tE3KHbI039.png',
        'seriesminprice': 120800,
        'seriesmaxprice': 143800,
        'average': 0.0,
        'specids': '[1011623, 1011626, 1011616, 1014241, 1011621, 1011615, 1011620, 1011613, 1011611, 1011609, 1011612, 1011608, 1011610, 1011625, 1011618, 1011622, 1011617, 1011619, 1011614, 1011624, 1014240]',
        'create_time': '2026-04-01 02:36:09'
    },
    {
        'seriesid': 8060,
        'seriesname': 'Summer',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M05/F1/97/autohomecar__ChxoHWfbq3yAfE7jAAc1xcsl0_0976.png',
        'seriesminprice': 328000,
        'seriesmaxprice': 328000,
        'average': 0.0,
        'specids': '[72266]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7895,
        'seriesname': '长安欧尚520',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M02/43/FB/autohomecar__ChxkPWcPXT2AduhcAAaSeIMBCQs367.png',
        'seriesminprice': 166800,
        'seriesmaxprice': 166800,
        'average': 0.0,
        'specids': '[70347]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7394,
        'seriesname': '荣威D5X DMH',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M03/79/84/autohomecar__CjIFU2UBkv-AKnqeAAZZW1g6Goc631.png',
        'seriesminprice': 129800,
        'seriesmaxprice': 146800,
        'average': 4.4717,
        'specids': '[68007, 66355, 68006]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6593,
        'seriesname': '星途追风C-DM',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M06/E2/FB/autohomecar__ChwFj2Ie2B6AWW7FAAnCqebcr2o382.png',
        'seriesminprice': 139800,
        'seriesmaxprice': 195800,
        'average': 4.5714,
        'specids': '[69670, 66555, 66554]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 5058,
        'seriesname': '北京EU5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M09/B1/B1/autohomecar__ChsEel8rzlmAKVqcAAXqOCuyu2s190.png',
        'seriesminprice': 129900,
        'seriesmaxprice': 171900,
        'average': 4.4029,
        'specids': '[71281, 54792, 41487, 46593, 41484, 57094, 45873, 47027, 71280, 59567, 41486, 41485, 47026, 57093]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 5724,
        'seriesname': '凌宝BOX',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M0A/22/1E/autohomecar__ChwFkmKisaCAJgJXAAmqbzE9eco106.png',
        'seriesminprice': 41900,
        'seriesmaxprice': 61900,
        'average': 4.5714,
        'specids': '[73036, 73035, 69789, 70602, 69788]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7059,
        'seriesname': '大力牛魔王D01',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M01/3D/00/autohomecar__ChtliGOs_I6APBlUAAd8Odj5VD4969.png',
        'seriesminprice': 28800,
        'seriesmaxprice': 69800,
        'average': 4.6468,
        'specids': '[1015054, 1016281, 1016669, 1016670, 1020241, 1016283, 1014992, 1015053, 1014853, 1016282, 1014993]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 4421,
        'seriesname': '东风风神E70',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M02/0E/8B/autohomecar__ChsEbGMHL4SATk34AAg2lVVgDeQ589.png',
        'seriesminprice': 142800,
        'seriesmaxprice': 153800,
        'average': 4.5,
        'specids': '[62156, 57965, 60273, 62154, 62244, 62155, 62204, 60276, 60274, 57964, 57966, 62245, 62243]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6670,
        'seriesname': '长安欧尚Z6新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M0A/5D/87/autohomecar__ChtliGSiN8iAONKgAAjlQXnXR_8328.png',
        'seriesminprice': 155800,
        'seriesmaxprice': 175800,
        'average': 4.365,
        'specids': '[63338, 63339, 63337]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6231,
        'seriesname': '奔驰EQS AMG',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M07/E7/8D/autohomecar__ChsFJ2KUrdiAKy-cAAYfpjkeSfM333.png',
        'seriesminprice': 1566000,
        'seriesmaxprice': 1566000,
        'average': 0.0,
        'specids': '[61343]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6050,
        'seriesname': '起亚EV6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M02/6E/0B/autohomecar__CjIFWGTxhg6ARqLUAAbX6lAuGss487.png',
        'seriesminprice': 282800,
        'seriesmaxprice': 439800,
        'average': 0.0,
        'specids': '[64480, 61943, 63789, 64435]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7865,
        'seriesname': '电动MINI JCW ACEMAN',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M02/35/ED/autohomecar__Chtk2Wbk_VyAY-eIAAYXKTQfwvQ371.png',
        'seriesminprice': 320900,
        'seriesmaxprice': 320900,
        'average': 0.0,
        'specids': '[75212]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6633,
        'seriesname': '风行雷霆',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g29/M08/F6/8A/autohomecar__ChwFk2N_Zv2AJIesAAl5LscPPWo628.png',
        'seriesminprice': 129900,
        'seriesmaxprice': 229900,
        'average': 3.9306,
        'specids': '[65688, 60708, 55558, 62093, 62094, 67789, 60689, 60688, 65411]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6955,
        'seriesname': '羿驰01',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M00/85/3E/autohomecar__ChxpVWiK0yqAP-XHAFtzQ3OseaU479.png',
        'seriesminprice': 229800,
        'seriesmaxprice': 229800,
        'average': 0.0,
        'specids': '[59735]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 5774,
        'seriesname': '五菱荣光小卡专用车',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M00/82/13/autohomecar__ChsEe17Xe1WAXmpqAArwU8zaHOs087.png',
        'seriesminprice': 49600,
        'seriesmaxprice': 159500,
        'average': 0.0,
        'specids': '[1016920]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6980,
        'seriesname': '奔驰EQE SUV AMG',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M0B/E1/C8/autohomecar__ChxkqWNM6mOANKp-AAojdg30CcY606.png',
        'seriesminprice': 863400,
        'seriesmaxprice': 863400,
        'average': 0.0,
        'specids': '[69663]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 8271,
        'seriesname': '威麟R08 EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M08/FC/AB/autohomecar__ChtpWGl4ikGAc0dSAGCgJJgAZDw830.png',
        'seriesminprice': 127800,
        'seriesmaxprice': 279800,
        'average': 0.0,
        'specids': '[1023257, 1023090, 1022956, 1022957, 1023089, 1023255, 1022963, 1023258, 1023088, 1023259, 1023256, 1022961, 1022962, 1022958]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7159,
        'seriesname': 'E全顺',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M02/7D/9A/autohomecar__ChtlyGYFRF2AeSclAAeX7ya6jVM290.png',
        'seriesminprice': 199800,
        'seriesmaxprice': 452900,
        'average': 0.0,
        'specids': '[1017865, 1017873, 1017868, 1015834, 1017869, 1017157, 1017867, 1015253, 1017864, 1017874, 1017872, 1015247, 1017871, 1017862, 1017866, 1015251, 1015249, 1017863, 1021177, 1017870]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6934,
        'seriesname': '昊铂SSR',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M0A/94/98/autohomecar__ChtlxWWFZhCAAEfEAAZacCZfxGU328.png',
        'seriesminprice': 1286000,
        'seriesmaxprice': 1686000,
        'average': 0.0,
        'specids': '[65157, 59535, 59534]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6667,
        'seriesname': '江豚',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M02/35/45/autohomecar__ChxoHWW4yeyAICQ8AAdKigxb8fA756.png',
        'seriesminprice': 133800,
        'seriesmaxprice': 162800,
        'average': 0.0,
        'specids': '[1015037, 1015034, 1013955, 1015036, 1015035, 1015033, 1015038, 1013956, 1013561, 1015039, 1013954]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 8580,
        'seriesname': '创维鸿途',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M06/B3/B9/autohomecar__ChxpWGnKVt-AQiyzAD8VB4J647I032.png',
        'seriesminprice': 160800,
        'seriesmaxprice': 291800,
        'average': 0.0,
        'specids': '[1023458, 1023462, 1023456, 1023457, 1023461, 1023460, 1023459]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 5801,
        'seriesname': '荣威i6 MAX新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g3/M0B/E3/CD/autohomecar__ChsEkV9qsPyAeWQfAAdeugMZhpI338.png',
        'seriesminprice': 152800,
        'seriesmaxprice': 259800,
        'average': 4.375,
        'specids': '[56385, 56384, 71032, 69451, 56760, 56758, 65195, 55324]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6497,
        'seriesname': '机甲龙',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M0B/C2/15/autohomecar__Chtlx2SiNuCAd50vAAah_rxFz2Q005.png',
        'seriesminprice': 488000,
        'seriesmaxprice': 488000,
        'average': 0.0,
        'specids': '[54461]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7508,
        'seriesname': '捷途X70 C-DM',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M01/95/BE/autohomecar__ChxoHmXW7ImACIzKAAhAk-6JjfE515.png',
        'seriesminprice': 165900,
        'seriesmaxprice': 189900,
        'average': 0.0,
        'specids': '[69981, 69986, 69987, 69982]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 8016,
        'seriesname': '郑州日产Z9 GE PHEV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M03/30/3B/autohomecar__Chtk2GhT0VOAT7XSAAY10QzOxa4803.png',
        'seriesminprice': 156900,
        'seriesmaxprice': 259900,
        'average': 4.4836,
        'specids': '[1020906, 1021364, 1021159, 1021160, 1020908, 1021166, 1021235, 1021161, 1020010, 1021727, 1021162, 1021163, 1020907]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 5403,
        'seriesname': '艾瑞泽e',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M05/23/0C/autohomecar__ChsEmF1bkbOARvFOAAbBMN-w2Tg846.png',
        'seriesminprice': 152800,
        'seriesmaxprice': 157800,
        'average': 4.75,
        'specids': '[64229, 64230]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6506,
        'seriesname': '瑞风E3',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M06/0E/F2/autohomecar__ChxpWGlfdVSALwlHAD6JAirN1hU842.png',
        'seriesminprice': 139900,
        'seriesmaxprice': 208800,
        'average': 4.4956,
        'specids': '[76196, 69907, 65386, 72105, 76195, 66893, 72104, 54576, 76168, 57562, 76197, 72106, 69908, 65387, 61170]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6686,
        'seriesname': '创维HT-i',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M0B/A1/E5/autohomecar__ChxpVWkQjjeAGD4wADlAszdQT4w600.png',
        'seriesminprice': 116800,
        'seriesmaxprice': 299800,
        'average': 4.7143,
        'specids': '[76615, 68531, 76332, 70525, 70395, 76367, 71219, 67037, 76331, 69282, 76330, 74094, 75402]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6436,
        'seriesname': '凌宝uni',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M06/CF/CA/autohomecar__ChwFkmKGDzSALtnGAAcN4cvjSo4494.png',
        'seriesminprice': 29800,
        'seriesmaxprice': 41800,
        'average': 0.0,
        'specids': '[70984, 70981, 61317, 56710, 53675, 62058, 70982, 70983, 70985]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7247,
        'seriesname': 'SKY EV01',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M0A/B3/92/autohomecar__Chtlx2VAeT-AB0iCAAYD0aemzs8232.png',
        'seriesminprice': 149900,
        'seriesmaxprice': 189900,
        'average': 0.0,
        'specids': '[71622, 72194, 74507, 68738, 69454, 74508, 72193, 69455, 68815, 68812]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 8457,
        'seriesname': '星海T5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M02/2E/B4/autohomecar__ChtpWGkv9paAb-m8AGRDkzmF6Fc103.png',
        'seriesminprice': 153900,
        'seriesmaxprice': 161900,
        'average': 0.0,
        'specids': '[76455, 76456, 75887, 75886]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7104,
        'seriesname': '启辰大V DD-i',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M0A/4C/FE/autohomecar__ChxpV2lmGSWAWVj6ACA-23gqYbQ872.png',
        'seriesminprice': 129900,
        'seriesmaxprice': 149900,
        'average': 4.7143,
        'specids': '[71961, 76259, 71977, 76292, 70355, 76293]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 8136,
        'seriesname': '瑞驰R5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M08/9C/87/autohomecar__ChxknGgbBGGAc3edAAWAuBS-vpc835.png',
        'seriesminprice': 78900,
        'seriesmaxprice': 127900,
        'average': 0.0,
        'specids': '[1022038, 1022702, 1022041, 1022037, 1022043, 1020959, 1020958, 1020957, 1020954, 1020949, 1020963, 1022701, 1022042, 1022040, 1022044, 1020950, 1020956, 1020960, 1020961, 1020962, 1020955, 1020953, 1020951, 1022703, 1020964, 1020952, 1022036, 1022700, 1022039]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6788,
        'seriesname': '睿蓝7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M03/F2/43/autohomecar__ChxkmmT1gfOABtDoAAjCK5w6_Bg317.png',
        'seriesminprice': 115700,
        'seriesmaxprice': 173700,
        'average': 4.478,
        'specids': '[70407, 64347, 61798, 66588, 68656, 68147, 64935, 70406, 67906, 69258]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7112,
        'seriesname': '好运',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M08/B5/82/autohomecar__ChxkPWdo_kCAPcjFAAkbVBpLc3c967.png',
        'seriesminprice': 69900,
        'seriesmaxprice': 186800,
        'average': 4.5801,
        'specids': '[1020526, 1023298, 1020522, 1020524, 1017393, 1020523, 1020393, 1019719, 1015945, 1020521, 1020525, 1023300, 1019720, 1020527]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 5861,
        'seriesname': '枫叶80v',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M06/C0/42/autohomecar__ChwFlGBIi6SASMNJAAjh1F84jOM996.png',
        'seriesminprice': 89800,
        'seriesmaxprice': 159800,
        'average': 4.2778,
        'specids': '[58763, 47130, 58764, 58781, 51454, 58780, 58782, 58779]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 5183,
        'seriesname': '启辰D60EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M06/09/04/autohomecar__ChwFkmNOQuuAChUhAAbmm0LQysc517.png',
        'seriesminprice': 139800,
        'seriesmaxprice': 158050,
        'average': 4.583,
        'specids': '[58556, 60148, 60147, 60151, 58554, 60139, 60144, 54823, 55657, 46380, 60140, 54821, 60150, 58557, 60152, 58555, 46382, 60145, 60149, 54822, 46381]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 4949,
        'seriesname': '易至EV3',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M00/BB/42/autohomecar__ChxkmWUULjqAaFdZAAwQIJvCg6k681.png',
        'seriesminprice': 62800,
        'seriesmaxprice': 66800,
        'average': 4.8571,
        'specids': '[71423, 71422]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 5973,
        'seriesname': '花仙子',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M03/DC/EC/autohomecar__ChxkjmNggf-AAJMaAAceEG0XYSc809.png',
        'seriesminprice': 59900,
        'seriesmaxprice': 74900,
        'average': 4.5893,
        'specids': '[62428, 62427, 62429, 62426]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 5078,
        'seriesname': 'Polestar 2',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M00/C4/6A/autohomecar__Chxky2SiNwSAHjrCAAb6hDTnpO8277.png',
        'seriesminprice': 299800,
        'seriesmaxprice': 358800,
        'average': 4.4257,
        'specids': '[61373, 62513, 62514]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 5494,
        'seriesname': '新途EV80',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g1/M06/F9/49/autohomecar__ChsEmV2yYySAEuU8AAZNp2-oP24896.png',
        'seriesminprice': 186800,
        'seriesmaxprice': 249800,
        'average': 0.0,
        'specids': '[1018097, 1021409, 1018098, 1021408, 1021410, 1021411]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7579,
        'seriesname': '鑫源E3',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M03/F7/7E/autohomecar__ChtlyGWuCJ2ATyMAAAWZezCWdy0539.png',
        'seriesminprice': 79800,
        'seriesmaxprice': 85800,
        'average': 4.602,
        'specids': '[1017630, 1017631, 1020153, 1020368, 1020154]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7497,
        'seriesname': '依维柯聚星新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M07/02/FA/autohomecar__ChxkjmVLKqGAM1YLAAmao-MCi5M552.png',
        'seriesminprice': 178800,
        'seriesmaxprice': 265800,
        'average': 0.0,
        'specids': '[1019280, 1020801, 1019266, 1019278, 1019268, 1019274, 1019275, 1019277, 1019271, 1019269, 1019272, 1019281, 1019282, 1019273, 1019270, 1019267, 1019276, 1019279]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6677,
        'seriesname': 'GranTurismo 新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M06/E5/58/autohomecar__ChwFkmNBUeqATDVgAAeAdxXlvV4033.png',
        'seriesminprice': 1988000,
        'seriesmaxprice': 1988000,
        'average': 0.0,
        'specids': '[56139]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6310,
        'seriesname': '橙仕01',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M00/44/F2/autohomecar__ChwFjmD5NC6ADI0fAATyRYnrDJY054.png',
        'seriesminprice': 39800,
        'seriesmaxprice': 72000,
        'average': 4.75,
        'specids': '[1014109, 1019000, 1014108, 1012574, 1012582, 1015502, 1014107, 1018999, 1012581, 1015501, 1012575, 1012576, 1014105, 1012579, 1015498, 1015497, 1011855, 1014106, 1012580, 1013384]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7930,
        'seriesname': '瑞风M3 PHEV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M07/D8/47/autohomecar__ChxkPmcxv9SAFDRaAArRqtTwMow472.png',
        'seriesminprice': 114900,
        'seriesmaxprice': 134900,
        'average': 0.0,
        'specids': '[70691, 70693, 70690, 70688, 70694, 70696]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7735,
        'seriesname': '江豚E5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M09/05/EB/autohomecar__ChtlyGY-0SSAS457AACcazS4XLQ607.jpg',
        'seriesminprice': 56900,
        'seriesmaxprice': 135800,
        'average': 0.0,
        'specids': '[1019491, 1019492, 1021037, 1021036, 1018948, 1018607, 1021034, 1018608, 1018947, 1021035]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6868,
        'seriesname': '跨越星V7 EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M01/F6/B0/autohomecar__ChwFj2NGXMCACRvtAAt6VJ2V-og905.png',
        'seriesminprice': 103900,
        'seriesmaxprice': 165800,
        'average': 0.0,
        'specids': '[1020267, 1020282, 1020295, 1020298, 1020281, 1020290, 1020626, 1020320, 1020268, 1020284, 1020264, 1020297, 1020300, 1020261, 1020302, 1020293, 1020304, 1020314, 1020310, 1020260, 1020289, 1020315, 1020301, 1020288, 1020283, 1020627, 1020266, 1020311, 1020625, 1020307, 1020321, 1020308, 1020427, 1020333, 1020286, 1020316, 1020265, 1020318, 1020319, 1020306, 1020623, 1020294, 1020313, 1020292, 1020331, 1020303, 1020332, 1020317, 1020322, 1020296, 1020312, 1020428, 1020291, 1020287, 1020309, 1020263, 1020624, 1020299, 1020305, 1020262, 1020285]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 8279,
        'seriesname': '宝骏E6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M03/7A/38/autohomecar__ChxpV2i6pVeAVR2DACVl_y_Q9r0009.png',
        'seriesminprice': 149800,
        'seriesmaxprice': 149800,
        'average': 0.0,
        'specids': '[74556]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 8525,
        'seriesname': '领汇e5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M01/C4/F0/autohomecar__ChxpWGlyEh6AYcFzACbJAk4B19Y747.png',
        'seriesminprice': 95800,
        'seriesmaxprice': 129800,
        'average': 0.0,
        'specids': '[77049, 77012, 76402]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7402,
        'seriesname': '五菱荣光新卡EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M0A/33/70/autohomecar__CjIFVWUJPuCAZRJ0AAhk5tRU97c467.png',
        'seriesminprice': 147800,
        'seriesmaxprice': 155800,
        'average': 0.0,
        'specids': '[1016966, 1016968, 1016962, 1016963, 1016965, 1016964, 1016969, 1016967]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7940,
        'seriesname': '风景i',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M0B/BB/09/autohomecar__ChxkPmc8OTiAD3FvAAl3VKenZ-w828.png',
        'seriesminprice': 102800,
        'seriesmaxprice': 175800,
        'average': 0.0,
        'specids': '[1021455, 1020151, 1020152, 1023285, 1020872, 1019671, 1022265, 1020873, 1020876, 1020858, 1021622, 1020871, 1020875, 1020860, 1021452, 1020859, 1019667, 1020149, 1020150, 1021621, 1021454, 1022264, 1020862, 1022266, 1020861, 1022619, 1020874, 1022617, 1022618, 1020877, 1020857, 1021620, 1021453]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 4479,
        'seriesname': '瑞驰新能源EC35',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M02/42/94/autohomecar__ChsEoF54JyCAC3GHAA2KdeeWQpI447.png',
        'seriesminprice': 79900,
        'seriesmaxprice': 85900,
        'average': 0.0,
        'specids': '[1018686, 1018687, 1018692]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 8034,
        'seriesname': '先锋官V EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M08/09/B9/autohomecar__ChxoHWfuSyGAJ0DmAAaTnCk3LQk724.png',
        'seriesminprice': 232800,
        'seriesmaxprice': 355800,
        'average': 0.0,
        'specids': '[1020235, 1020233, 1022841, 1022842, 1020232, 1022844, 1020234, 1022843]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 8315,
        'seriesname': '睿立达V8E',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M03/94/86/autohomecar__Chto52jozP-ABmqtABZwigHmk50253.png',
        'seriesminprice': 85800,
        'seriesmaxprice': 100800,
        'average': 0.0,
        'specids': '[1023026, 1023025, 1022955, 1022154, 1023023, 1023028, 1023027, 1023024, 1022954]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7270,
        'seriesname': '蓝电E3',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M04/60/32/autohomecar__CjIFVGVe_VmAYgpGAAhZnSS_LgI568.png',
        'seriesminprice': 139800,
        'seriesmaxprice': 145800,
        'average': 0.0,
        'specids': '[66069, 63022]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7880,
        'seriesname': 'Lorinser 星际战车',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M03/EB/D7/autohomecar__ChtlxmhrpMeAZQJRAAkExnUcIbI753.png',
        'seriesminprice': 879000,
        'seriesmaxprice': 1288000,
        'average': 0.0,
        'specids': '[70087, 70086, 72803, 72782]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 8225,
        'seriesname': '荣威E6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M04/5A/E6/autohomecar__ChxpVWiHTq2ACQiLACPBpdsLqgg631.png',
        'seriesminprice': 168800,
        'seriesmaxprice': 176800,
        'average': 0.0,
        'specids': '[76012, 73991, 73992, 73990]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7300,
        'seriesname': '菱势黄金卡',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M01/96/EF/autohomecar__CjIFVGSC8u2APooOAAa65JOrogo001.png',
        'seriesminprice': 89800,
        'seriesmaxprice': 180800,
        'average': 0.0,
        'specids': '[1018527, 1020155, 1021401, 1020156, 1020421, 1016710, 1016237, 1016709, 1016349, 1016712, 1016708, 1021400, 1016713, 1020423, 1020422, 1016348, 1020157, 1016711, 1021399, 1019103]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 8277,
        'seriesname': '星海X5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M06/6D/E2/autohomecar__ChxpV2i5YE2AO6CFAD1GuoB5kmc917.png',
        'seriesminprice': 151900,
        'seriesmaxprice': 169900,
        'average': 0.0,
        'specids': '[75634, 74550, 74549, 76458, 76457]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6005,
        'seriesname': '羿',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M03/14/5C/autohomecar__ChxknGJGyyWAd5hqAAkdscHjQDA210.png',
        'seriesminprice': 118800,
        'seriesmaxprice': 199800,
        'average': 4.7143,
        'specids': '[61408, 61405, 70870, 61406, 63075, 68045, 63076, 68046, 61494, 63077, 62225, 61407, 70869, 63078, 61404]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6866,
        'seriesname': '五菱荣光小卡EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M08/09/F0/autohomecar__ChxkmmL8ffGAU4t5AAZsBSs4260266.png',
        'seriesminprice': 113800,
        'seriesmaxprice': 125800,
        'average': 0.0,
        'specids': '[1014258, 1016961, 1014264, 1016960, 1016957, 1014265, 1014266, 1016959, 1016958]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 8573,
        'seriesname': '祥菱U8',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M03/61/EC/autohomecar__ChxpV2nCUDiAVTHqAAA3tw-pJAc539.png',
        'seriesminprice': 110000,
        'seriesmaxprice': 119900,
        'average': 0.0,
        'specids': '[1023371, 1023372, 1023374, 1023375, 1023376, 1023370, 1023373, 1023377, 1023368, 1023369]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6522,
        'seriesname': '雷丁芒果Pro',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M06/7C/7E/autohomecar__ChtlyGeTMUeAUznuAAgiXgtKno4360.png',
        'seriesminprice': 53900,
        'seriesmaxprice': 53900,
        'average': 4.5065,
        'specids': '[71521]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7077,
        'seriesname': '凯翼昆仑新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M02/BF/C3/autohomecar__ChwFkGOUCpiAEcqsAAoL-4Qqrl0505.png',
        'seriesminprice': 109900,
        'seriesmaxprice': 182900,
        'average': 4.3372,
        'specids': '[76290, 71499, 74772, 71491, 74769, 71495, 74775, 74773, 71497, 76288, 74776, 71492, 76289, 74770, 74771, 71494, 76287, 71496, 71498, 74774, 71493]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7580,
        'seriesname': '鑫源E3L',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M09/21/37/autohomecar__ChxkPmdYH4mAemeZAALoMDScpNc338.png',
        'seriesminprice': 95800,
        'seriesmaxprice': 129800,
        'average': 4.8571,
        'specids': '[1019186, 1018683, 1019581, 1019183, 1019182, 1018684]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7998,
        'seriesname': '乐福',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M04/B0/E9/autohomecar__ChxkPmdo2MSAEVHQAAeK54TV4EE946.png',
        'seriesminprice': 95000,
        'seriesmaxprice': 198000,
        'average': 4.5714,
        'specids': '[1021654, 1019761, 1021141, 1020537, 1022152, 1020069, 1020078, 1020068, 1021641, 1021124, 1022754, 1021626, 1020533, 1021129, 1020546, 1020544, 1021117, 1020074, 1021627, 1020197, 1020548, 1021629, 1021636, 1020072, 1020539, 1022755, 1021651, 1020070, 1021119, 1021632, 1020542, 1021130, 1021134, 1022146, 1021637, 1022147, 1020075, 1021631, 1022756, 1020073, 1021138, 1021132, 1020076, 1019765, 1021652, 1020530, 1020077, 1020545, 1019762, 1021628, 1020067, 1021635, 1021648, 1022752, 1022149, 1021653, 1020079, 1020538, 1021646, 1020529, 1021125, 1021135, 1021126, 1019764, 1021644, 1021114, 1021120, 1021142, 1021639, 1021131, 1020536, 1020535, 1021136, 1020528, 1021115, 1022153, 1020071, 1020540, 1021649, 1021643, 1021121, 1022757, 1021140, 1021122, 1020543, 1020541, 1021650, 1021638, 1020531, 1022151, 1021123, 1021630, 1021645, 1021127, 1020532, 1021137, 1020196, 1021640, 1020065, 1021647, 1022148, 1022753, 1021116, 1022150, 1020198, 1020547, 1021133, 1019763, 1021642, 1021633, 1020066, 1021128, 1021118, 1021634, 1020534]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6097,
        'seriesname': '小虎EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M03/A8/59/autohomecar__ChwFj2N-EKGAbcz6AAeFL5SE9p8848.png',
        'seriesminprice': 41900,
        'seriesmaxprice': 55900,
        'average': 4.625,
        'specids': '[52016, 52015, 56372, 56371, 58912, 52014]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 8406,
        'seriesname': '峰渡行',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M0B/46/E5/autohomecar__Chto52kIeayAP8fEAFheQFjya3Q797.png',
        'seriesminprice': 299800,
        'seriesmaxprice': 299800,
        'average': 0.0,
        'specids': '[1022661]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6813,
        'seriesname': '欧麦加',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M08/51/8F/autohomecar__ChsEbGLCv8KAVGTMAAULIUgFWUw090.png',
        'seriesminprice': 46800,
        'seriesmaxprice': 59800,
        'average': 4.8571,
        'specids': '[61878, 61879, 61876, 61877]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6682,
        'seriesname': '五菱EV80',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M00/85/15/autohomecar__ChwFj2I1a2KAHI_7AAcwFX-gAzA222.png',
        'seriesminprice': 213000,
        'seriesmaxprice': 213000,
        'average': 0.0,
        'specids': '[1013675]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7964,
        'seriesname': '骏驰EA',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M02/55/3E/autohomecar__Chtk2WdNWwqAPMj9AAhSk4N_VJg400.png',
        'seriesminprice': 38800,
        'seriesmaxprice': 45000,
        'average': 0.0,
        'specids': '[73143, 70968]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 5589,
        'seriesname': 'e爱丽舍',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g3/M00/54/D3/autohomecar__ChwFlV9QYYeAbeU1AAheGUlWmmE170.png',
        'seriesminprice': 139800,
        'seriesmaxprice': 179800,
        'average': 0.0,
        'specids': '[75731, 68213, 68212, 75732]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 5918,
        'seriesname': 'SS DOLPHIN',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M08/E7/C9/autohomecar__ChsEf19v-HWAPWu9AAevUHmA3OQ001.png',
        'seriesminprice': 700000,
        'seriesmaxprice': 700000,
        'average': 0.0,
        'specids': '[47951]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 6760,
        'seriesname': '新海狮EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M07/83/A1/autohomecar__ChwFlGKOL4SAUP-GAAqEyQWXvPw929.png',
        'seriesminprice': 139800,
        'seriesmaxprice': 140300,
        'average': 4.5661,
        'specids': '[1021360, 1021361]',
        'create_time': '2026-04-01 02:36:10'
    },
    {
        'seriesid': 7267,
        'seriesname': '远程星智',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M04/D7/B9/autohomecar__Chxky2WFaTuAFM--AArX_EYwARM036.png',
        'seriesminprice': 265300,
        'seriesmaxprice': 334100,
        'average': 0.0,
        'specids': '[1019539]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8007,
        'seriesname': 'E福顺小卡',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M02/A2/68/autohomecar__ChxoHWd9B-OAYW9SAAdl1KBYk-8129.png',
        'seriesminprice': 85900,
        'seriesmaxprice': 112000,
        'average': 0.0,
        'specids': '[1019984, 1019989, 1019993, 1019986, 1019985, 1019983, 1019988, 1019987, 1019992, 1019990, 1019982, 1019991]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 4918,
        'seriesname': '长安星卡EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M08/65/FA/autohomecar__ChtlyGelpM6ARboUAAac1GHi5sQ933.png',
        'seriesminprice': 74900,
        'seriesmaxprice': 136800,
        'average': 0.0,
        'specids': '[1018289, 1015259, 1018295, 1018291, 1018286, 1015258, 1011777, 1015364, 1018287, 1018290, 1011776, 1015365, 1018293, 1018292, 1018294, 1018288]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8227,
        'seriesname': '祥菱U7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M02/99/DB/autohomecar__ChxpVmk6cy-AfbSHACs7F4uWVps910.png',
        'seriesminprice': 97000,
        'seriesmaxprice': 114400,
        'average': 0.0,
        'specids': '[1023323, 1023359, 1023322, 1023326, 1023325, 1023356, 1023354, 1023355, 1021468, 1023358, 1023324, 1023357]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8452,
        'seriesname': 'vala home',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M00/D4/21/autohomecar__ChxpVmk_1AuAMxwkADji62ts0U0509.png',
        'seriesminprice': 169900,
        'seriesmaxprice': 169900,
        'average': 0.0,
        'specids': '[1022611]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7296,
        'seriesname': '远程星享F1E',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M00/05/CB/autohomecar__ChxkmWR_BO-AE-dLAAQlc-AzLV0431.png',
        'seriesminprice': 129900,
        'seriesmaxprice': 177800,
        'average': 0.0,
        'specids': '[1016215, 1016217, 1016219, 1016213, 1016216, 1016212, 1017904, 1016220, 1019540, 1016214, 1017907, 1017905, 1016218, 1017906]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7217,
        'seriesname': '江淮QX PHEV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M05/06/87/autohomecar__Chxky2Tsan2AOjSPAAhH2WGXt1Y914.png',
        'seriesminprice': 89900,
        'seriesmaxprice': 186900,
        'average': 4.5257,
        'specids': '[67485, 68772, 72538, 72536, 72537]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7528,
        'seriesname': '启辰大V氢境',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M05/0B/44/autohomecar__CjIFU2VpT6yAOK1NAAh6JK_aNJ4585.png',
        'seriesminprice': 998800,
        'seriesmaxprice': 998800,
        'average': 0.0,
        'specids': '[66080]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 5882,
        'seriesname': '新途EV90',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M09/1C/D6/autohomecar__ChsEemAGcO2ABcS2AAmXeAHQu48633.png',
        'seriesminprice': 249000,
        'seriesmaxprice': 729800,
        'average': 0.0,
        'specids': '[1019999, 1012942, 1019997, 1012964, 1012963, 1019998, 1012940, 1020002, 1012967, 1020001, 1013999, 1012943, 1019996, 1012941, 1020000, 1012948, 1012939]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8066,
        'seriesname': '红旗金葵花国悦新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M03/1E/E0/autohomecar__CjIFU2fj1gCANwPLAAisjcjtvlk683.png',
        'seriesminprice': 706800,
        'seriesmaxprice': 711800,
        'average': 0.0,
        'specids': '[1020495, 1020496]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 5075,
        'seriesname': '大将军EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M08/AD/8E/autohomecar__ChxknGVv7EaAA5qnAAkmqZ96LnY552.png',
        'seriesminprice': 119800,
        'seriesmaxprice': 368800,
        'average': 4.6305,
        'specids': '[1020243, 1020024, 1013287, 1022273, 1020728, 1021810, 1021814, 1022275, 1020727, 1013669, 1021811, 1018877, 1018878, 1022895, 1022896, 1021815, 1022894, 1020729, 1020730, 1013670, 1021812, 1021813, 1022274]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 5583,
        'seriesname': '悦虎',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M08/8B/98/autohomecar__ChwFjl6qpiCACMrqAAo3M8L1lmE967.png',
        'seriesminprice': 63800,
        'seriesmaxprice': 86990,
        'average': 4.1554,
        'specids': '[63628, 63629, 63630, 63633, 63634, 63631, 63632]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 5993,
        'seriesname': 'Modern in',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g13/M10/13/BB/autohomecar__ChwEn2CLlteABN8dAAbnrPiX05A749.png',
        'seriesminprice': 139800,
        'seriesmaxprice': 249800,
        'average': 0.0,
        'specids': '[57194, 57401, 57193, 57195, 61204, 61700, 57402, 61205]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7401,
        'seriesname': '大力牛魔王D02',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M04/D7/94/autohomecar__CjIFU2UD8fiAH008AAPXxVcj7ks409.png',
        'seriesminprice': 30500,
        'seriesmaxprice': 69800,
        'average': 0.0,
        'specids': '[1019517, 1019515, 1019516, 1019514, 1020242, 1019519, 1019518]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8549,
        'seriesname': '菱势黄金大卡',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M0A/93/49/autohomecar__ChxpV2mK74mANm2tAEVQ7dPjyzQ636.png',
        'seriesminprice': 168000,
        'seriesmaxprice': 168000,
        'average': 0.0,
        'specids': '[1023062]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7726,
        'seriesname': '江豚E7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M08/32/26/autohomecar__ChxoHmYvdTuAa6G4AAbjzUOLimI111.png',
        'seriesminprice': 82900,
        'seriesmaxprice': 175800,
        'average': 0.0,
        'specids': '[1019397, 1021041, 1020387, 1018501, 1021040, 1021039, 1019396, 1020388, 1018500, 1021038]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 5939,
        'seriesname': 'LEVC TX',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g29/M01/57/04/autohomecar__ChwFk2L80tOATxquAAogDDghsQk848.png',
        'seriesminprice': 339800,
        'seriesmaxprice': 369800,
        'average': 0.0,
        'specids': '[60007, 60009, 60010, 60008, 60011, 60012]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6400,
        'seriesname': 'Polestar 3',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M05/F7/62/autohomecar__ChwFkmNHrDyALidjAAevO4nIStc887.png',
        'seriesminprice': 698000,
        'seriesmaxprice': 798000,
        'average': 0.0,
        'specids': '[60028, 53318]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8575,
        'seriesname': '金龙V8',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M02/61/65/autohomecar__ChtpWGnCUEqANXAQACiSWLRyxkM247.png',
        'seriesminprice': 108800,
        'seriesmaxprice': 139800,
        'average': 0.0,
        'specids': '[1023396, 1023397, 1023398]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 5189,
        'seriesname': '北京EU7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M01/92/1E/autohomecar__ChwFkWGJ5COAJZqqAAgbtA_44yE636.png',
        'seriesminprice': 159900,
        'seriesmaxprice': 175900,
        'average': 4.1429,
        'specids': '[54776, 54777, 54775]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7438,
        'seriesname': '悦01',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M08/AC/91/autohomecar__ChtlxWWc9PmAXr-GAAoTww59X3w572.png',
        'seriesminprice': 59800,
        'seriesmaxprice': 79800,
        'average': 0.0,
        'specids': '[65259, 66370, 66368, 66369, 66367, 66371]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8218,
        'seriesname': '羿驰05S',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M08/9F/CA/autohomecar__Chto52jUrOSAdm-FAFbNrwcqQlY815.png',
        'seriesminprice': 97800,
        'seriesmaxprice': 169800,
        'average': 4.8571,
        'specids': '[73867, 74944, 74945, 73868, 74946, 75380, 75381]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6172,
        'seriesname': '北京EU5 PLUS',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M03/B6/8D/autohomecar__Chtk3WCuBriAFDu2AAPV9DVxQao654.png',
        'seriesminprice': 129900,
        'seriesmaxprice': 185900,
        'average': 4.75,
        'specids': '[64186, 66279, 65693, 64270, 64269, 64267, 65694, 64268, 64266]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 2576,
        'seriesname': '九龙A6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M00/28/29/autohomecar__wKgHIVqnPUeAEoaSAAb7B4wVLL4593.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 272800,
        'average': 3.75,
        'specids': '[1003797]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6622,
        'seriesname': '家宝',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M05/69/36/autohomecar__Chtk3WPgXFKAObGkAAfDDYw3H7I664.png',
        'seriesminprice': 39800,
        'seriesmaxprice': 56900,
        'average': 0.0,
        'specids': '[63310, 61442, 61440, 63312, 61441, 63311]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8222,
        'seriesname': '新途远界',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M07/2C/00/autohomecar__ChxpVWiDWbOActvTADp9HuiaLhQ296.png',
        'seriesminprice': 329800,
        'seriesmaxprice': 729800,
        'average': 0.0,
        'specids': '[1021751, 1021531, 1021530, 1021528, 1021527, 1021445, 1021446, 1021529]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6743,
        'seriesname': '海马7X新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M0A/E9/31/autohomecar__ChxkqWSiNseAADQ-AAdRXk093YU560.png',
        'seriesminprice': 219800,
        'seriesmaxprice': 259800,
        'average': 0.0,
        'specids': '[57176, 59783, 59782]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 5027,
        'seriesname': '广汽本田VE-1',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g5/M08/FC/B1/autohomecar__ChxkkGEt186AKO7YAAgegs5NUD0230.png',
        'seriesminprice': 159800,
        'seriesmaxprice': 186799,
        'average': 4.75,
        'specids': '[59220, 59224, 59221, 59222, 59226, 59225, 59223]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6215,
        'seriesname': '枫叶60s',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M08/44/F3/autohomecar__ChwFj2IVrAyAfxnhAE036ZU8ty0732.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 163800,
        'average': 0.0,
        'specids': '[56363, 69612, 56367, 66523, 62520, 62519, 71629, 56364, 62521, 56366, 66522]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7912,
        'seriesname': '菱势黄金小卡',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M03/28/FF/autohomecar__ChxkPmcbTpOAa7wFAAa4YgvzoMI941.png',
        'seriesminprice': 88000,
        'seriesmaxprice': 195800,
        'average': 0.0,
        'specids': '[1020425, 1020426, 1019553, 1021154, 1021158, 1019554, 1021473, 1019552, 1021474, 1020424, 1021156]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7589,
        'seriesname': '江淮X8 E家',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M00/D4/F8/autohomecar__ChtlyGXBlDyAenHdAAdnJP0bsLE937.png',
        'seriesminprice': 99800,
        'seriesmaxprice': 199800,
        'average': 3.8572,
        'specids': '[66658, 70053, 72542, 66656, 72540, 66657, 70280, 70056, 70055, 70054, 72541, 70051, 70052, 70281, 70282, 72539]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7240,
        'seriesname': '大道EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M03/BD/79/autohomecar__CjIFVmQ-hqqAYZK1AAb8Su-Ttj0763.png',
        'seriesminprice': 182800,
        'seriesmaxprice': 299800,
        'average': 0.0,
        'specids': '[1020824, 1017957, 1015914, 1020826, 1017958, 1020825]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6391,
        'seriesname': '风光E380',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M05/E9/0E/autohomecar__ChxknGNjfIWAHy3-AE-JX6meXok121.png',
        'seriesminprice': 129100,
        'seriesmaxprice': 169100,
        'average': 4.4569,
        'specids': '[60417, 65064, 53203, 65065, 65066, 62949, 60421, 62952, 60420, 60418, 62951, 65062, 62953, 62950, 65063, 65067]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 5432,
        'seriesname': '海豚EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M0B/41/FE/autohomecar__ChwFjmDB5fWADKpdAAfGrBAWfzE758.png',
        'seriesminprice': 123000,
        'seriesmaxprice': 176800,
        'average': 0.0,
        'specids': '[1022532, 1022528, 1014287, 1022527, 1022533, 1022534, 1022535, 1010904, 1014285, 1020336, 1022529, 1020335, 1015032, 1010903, 1010902, 1022530, 1014288, 1014286, 1010905, 1022531]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 5378,
        'seriesname': '远程星享E6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M0B/35/66/autohomecar__ChxoHWW4yrCAa9UWAApPWqx1lc0607.png',
        'seriesminprice': 184800,
        'seriesmaxprice': 258800,
        'average': 0.0,
        'specids': '[1013471, 1015433, 1013472, 1013474, 1013473]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6792,
        'seriesname': '睿蓝9',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g29/M05/E6/67/autohomecar__Chxkm2OAJn6AUSeKAAchvU6Zovc679.png',
        'seriesminprice': 159900,
        'seriesmaxprice': 197900,
        'average': 4.4779,
        'specids': '[61623, 61622, 61621, 61624, 66007]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7852,
        'seriesname': '意路达',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M01/DD/35/autohomecar__Chtk2WbgN6KAVTNCAAd0PGTrNm4318.png',
        'seriesminprice': 138800,
        'seriesmaxprice': 138800,
        'average': 0.0,
        'specids': '[1019338]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7505,
        'seriesname': '悍途新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M02/64/3D/autohomecar__ChxoHmYfX0qAGLP1AAqjtH3ieXw694.png',
        'seriesminprice': 179800,
        'seriesmaxprice': 319800,
        'average': 0.0,
        'specids': '[1021664, 1021405, 1021666, 1021665]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8127,
        'seriesname': '上汽大通MAXUS 生活家PHEV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M0A/03/3D/autohomecar__Chtk2WgKCeOAQPTsAAxahE1GQjI560.png',
        'seriesminprice': 639800,
        'seriesmaxprice': 729800,
        'average': 0.0,
        'specids': '[1021095, 1020913]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8236,
        'seriesname': '东风风神L7X',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M06/C1/B0/autohomecar__Chto52iQbYSAcJ3uAEoujW2QrYY823.png',
        'seriesminprice': 186900,
        'seriesmaxprice': 234500,
        'average': 0.0,
        'specids': '[74085, 74086, 74084]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7783,
        'seriesname': '小象X3',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M04/B3/1C/autohomecar__Chtk2WZz97mAIcwyAAa7rVY9VbI393.png',
        'seriesminprice': 59900,
        'seriesmaxprice': 106900,
        'average': 0.0,
        'specids': '[1019500, 1018958, 1019503, 1018957, 1019498, 1018956, 1019499, 1019497, 1019501, 1019496, 1019502]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7350,
        'seriesname': '瑞风E4',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M09/62/97/autohomecar__ChxoHmgGAEWAAWC2AAmnZtD-sFE120.png',
        'seriesminprice': 179800,
        'seriesmaxprice': 199800,
        'average': 0.0,
        'specids': '[76151, 68510, 68509, 76606, 76607, 76150]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 5990,
        'seriesname': '华晨新日i03',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M0A/85/3A/autohomecar__ChwFjmDazPuAdOLiAAg1MNA937Q598.png',
        'seriesminprice': 43900,
        'seriesmaxprice': 98800,
        'average': 3.25,
        'specids': '[60629, 53789, 60631, 60632, 60630, 60633]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 4614,
        'seriesname': '风行S50EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g10/M02/2B/34/autohomecar__ChsFVWBtdmeAe9BwAAhMGrm3nSU370.png',
        'seriesminprice': 150900,
        'seriesmaxprice': 169900,
        'average': 0.0,
        'specids': '[62365, 64351, 64727, 62726, 64350, 64723, 62364]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 4917,
        'seriesname': '长安之星9EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M01/6E/57/autohomecar__ChwFjmB1DjKAcge7AArnJc2oUIg309.png',
        'seriesminprice': 132800,
        'seriesmaxprice': 168900,
        'average': 0.0,
        'specids': '[1015792, 1011844, 1013008, 1018099, 1011845, 1014165, 1011848, 1011846, 1011847]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7124,
        'seriesname': '云兔',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M0A/B0/B6/autohomecar__ChtlxmTZwyKAFeYhAAdMODtfK1g819.png',
        'seriesminprice': 69800,
        'seriesmaxprice': 93800,
        'average': 3.7143,
        'specids': '[61316, 63926, 65013, 61266, 65012]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6927,
        'seriesname': '江南U2',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M02/60/4E/autohomecar__ChxkqWMbPZ6AXMZ_AAf7WsKEAbQ830.png',
        'seriesminprice': 56800,
        'seriesmaxprice': 98800,
        'average': 0.0,
        'specids': '[61578, 61577, 61574, 61576, 59428, 61575]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7155,
        'seriesname': '跨越者D5 新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M04/F9/99/autohomecar__ChxkqWWFZyqAU0HAAAdFEmk6eow418.png',
        'seriesminprice': 152800,
        'seriesmaxprice': 200800,
        'average': 0.0,
        'specids': '[1023341, 1023342, 1017129, 1021320, 1019506, 1019508, 1023343, 1023340, 1023339, 1023338, 1019507, 1023337, 1021321, 1023336, 1023046, 1023047, 1023045, 1015216, 1023344, 1023334, 1023048, 1023049, 1023335, 1019509, 1023345]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6341,
        'seriesname': 'YOUNG光小新',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g29/M09/38/B2/autohomecar__ChwFk2EWFIGAfTEiAAbzj1jR5jY981.png',
        'seriesminprice': 65800,
        'seriesmaxprice': 84800,
        'average': 3.2322,
        'specids': '[58031, 58030, 52623, 58028, 58029, 52622, 66163, 58032]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6096,
        'seriesname': 'Lorinser LX',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M02/E3/B7/autohomecar__ChxpVWlBICKAL767AEARq-JhtbQ704.png',
        'seriesminprice': 499000,
        'seriesmaxprice': 499000,
        'average': 0.0,
        'specids': '[50453]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7050,
        'seriesname': '未奥BOMA',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M07/CA/25/autohomecar__ChxknGVpTU6AAkZgAAgfQ8QwjrQ520.png',
        'seriesminprice': 39900,
        'seriesmaxprice': 51900,
        'average': 0.0,
        'specids': '[63733, 63730, 63732, 63731]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8067,
        'seriesname': '睿立达V5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M07/5E/2B/autohomecar__ChxoHmfjxMGAACkWAATEopTTtx0571.png',
        'seriesminprice': 79800,
        'seriesmaxprice': 116000,
        'average': 0.0,
        'specids': '[1022071, 1022070, 1020499, 1022068, 1022069]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7558,
        'seriesname': '图雅诺大V新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M01/FE/91/autohomecar__ChtlxWWOjUiAUbz2AAiMHyd8zY8859.png',
        'seriesminprice': 152800,
        'seriesmaxprice': 237800,
        'average': 4.8571,
        'specids': '[1017586, 1018496, 1018497]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 5224,
        'seriesname': '启辰T60EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M0B/5C/60/autohomecar__ChcCP14djO6AYhVtAAfi7BTIP1M954.png',
        'seriesminprice': 189800,
        'seriesmaxprice': 189800,
        'average': 4.5328,
        'specids': '[61745]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 5764,
        'seriesname': '远志M1',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M08/B8/74/autohomecar__ChsEoF9oDp6AQvVlAAwAA1ey5Cg447.png',
        'seriesminprice': 174800,
        'seriesmaxprice': 318800,
        'average': 4.7143,
        'specids': '[68332, 73275, 68338, 68352, 68343, 68340, 68342, 68345, 68347, 68336, 68339, 68333, 68330, 68344, 68346, 68328, 68348, 68331, 73274, 68351, 68350, 68353, 68335, 68341, 68329, 68349, 68337, 68334]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 5289,
        'seriesname': '依维柯欧胜新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g27/M09/2E/79/autohomecar__ChsEnVy5MImAabRcAAdcMnR8yBg508.png',
        'seriesminprice': 248900,
        'seriesmaxprice': 309900,
        'average': 0.0,
        'specids': '[1015565, 1018285, 1015566, 1018282, 1016351, 1018284, 1018283, 1015567, 1016350, 1015568]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7772,
        'seriesname': '钇为花仙子',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M09/98/28/autohomecar__Chtk2WZoETuAIv9VAAk2UZ0d118679.png',
        'seriesminprice': 59900,
        'seriesmaxprice': 65900,
        'average': 4.5164,
        'specids': '[68673, 68674]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 4461,
        'seriesname': '东风小康EC36',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M03/73/EE/autohomecar__ChxknGJNJfKAfD-LAAqI5hwCxjY677.png',
        'seriesminprice': 129800,
        'seriesmaxprice': 129800,
        'average': 3.875,
        'specids': '[1013779, 1013778]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8574,
        'seriesname': '卡文乐途',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M0A/BC/6F/autohomecar__ChxpVWnLbPmAR2c0ACo_LqV0zRA282.png',
        'seriesminprice': 289000,
        'seriesmaxprice': 401000,
        'average': 0.0,
        'specids': '[1023390, 1023394, 1023387, 1023388, 1023393, 1023389, 1023391, 1023392, 1023395]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6115,
        'seriesname': '凌宝COCO',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M06/21/85/autohomecar__ChwFlGN0UNqAXhL-AAo47Bkdado937.png',
        'seriesminprice': 36800,
        'seriesmaxprice': 39800,
        'average': 0.0,
        'specids': '[60005, 60006]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7239,
        'seriesname': '长安览拓者新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M07/88/4D/autohomecar__ChxkjmQ-XwSAJC4eAAhkEM-beH8164.png',
        'seriesminprice': 279900,
        'seriesmaxprice': 279900,
        'average': 0.0,
        'specids': '[1015892]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7259,
        'seriesname': '祥菱V1 EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M05/D2/E8/autohomecar__Chtlx2WFaNqANZbiAAupW_2bMi0086.png',
        'seriesminprice': 140000,
        'seriesmaxprice': 160000,
        'average': 0.0,
        'specids': '[1015959, 1015961, 1015958, 1015956, 1015957, 1015960]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7756,
        'seriesname': '菱势电卡',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M0B/A1/9C/autohomecar__ChtlyGZNylKATrprAAT3V4G3w8Y877.png',
        'seriesminprice': 131800,
        'seriesmaxprice': 131800,
        'average': 0.0,
        'specids': '[1018681]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 5004,
        'seriesname': '瑞驰新能源EC31',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g1/M09/77/F1/autohomecar__ChsEmV08K5iAUKJ1AAj0Es9YcuQ656.png',
        'seriesminprice': 62900,
        'seriesmaxprice': 123900,
        'average': 0.0,
        'specids': '[1019029, 1019030, 1019031, 1018839, 1018688, 1018689, 1018838]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8272,
        'seriesname': '克蒂昆仑',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M09/44/3F/autohomecar__ChtpWGi1N5mAErh_AFi2vMdhgFw648.png',
        'seriesminprice': 529900,
        'seriesmaxprice': 529900,
        'average': 0.0,
        'specids': '[74506]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8274,
        'seriesname': '凯翼昆仑L8',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M02/E1/1C/autohomecar__ChtpWGjaJp6ASDY0AEQvk3wIgxY007.png',
        'seriesminprice': 196800,
        'seriesmaxprice': 246800,
        'average': 0.0,
        'specids': '[74527, 74526, 74528]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7324,
        'seriesname': '乐行E路达',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M04/9D/30/autohomecar__ChtliGSry4GAKyJvAAmKpNalEbA161.png',
        'seriesminprice': 183300,
        'seriesmaxprice': 369800,
        'average': 0.0,
        'specids': '[1023186, 1023181, 1023193, 1016447, 1023246, 1023247, 1016445, 1016442, 1023183, 1023189, 1016440, 1023190, 1023184, 1016446, 1023185, 1023195, 1023188, 1023191, 1016438, 1023182, 1023194, 1023245, 1023187, 1016437, 1016441, 1023192, 1017476, 1017477, 1017478, 1016444, 1016439, 1016443]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7809,
        'seriesname': '星际X新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M06/90/52/autohomecar__Chtk2WaUktqAX3zBAAa4A-h4urw520.png',
        'seriesminprice': 299800,
        'seriesmaxprice': 322800,
        'average': 0.0,
        'specids': '[1019727, 1019729, 1021476]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6420,
        'seriesname': '远程锋锐',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g7/M0A/83/B6/autohomecar__ChsEvmFS5TqACisqAAoAr662Blc599.png',
        'seriesminprice': 189800,
        'seriesmaxprice': 271800,
        'average': 0.0,
        'specids': '[1015558, 1015434, 1015562, 1015561, 1013451, 1015560, 1015435, 1015557, 1014252, 1014254, 1015425, 1014253, 1014794, 1015559, 1015564, 1013452, 1014779, 1015426, 1015563, 1012163, 1014796, 1015436, 1015427, 1014795, 1015556]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7119,
        'seriesname': 'SWM斯威大虎EDi',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M08/6A/90/autohomecar__Chtk3WPgczGAdyUAAAJff65F7WE508.png',
        'seriesminprice': 99900,
        'seriesmaxprice': 139900,
        'average': 4.5106,
        'specids': '[61453, 61452, 61225, 61450, 61449, 61448, 65134, 61451, 61454]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6787,
        'seriesname': 'SEM DELICA',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M00/38/79/autohomecar__ChsFJ2KxLgOAVLlsAAihVNIwOs8872.png',
        'seriesminprice': 168800,
        'seriesmaxprice': 268800,
        'average': 0.0,
        'specids': '[1016831, 1014080, 1014079, 1015042]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8389,
        'seriesname': '金杯海狮王EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M04/9B/0D/autohomecar__ChtpWGj7ZJCAMuTfAFZ0VbS_fm4257.png',
        'seriesminprice': 118800,
        'seriesmaxprice': 156300,
        'average': 0.0,
        'specids': '[1022360, 1022362, 1022363, 1022284, 1022277, 1022282, 1022283, 1022281, 1022359, 1022280, 1022642, 1022364, 1022278, 1022276, 1022279, 1022285, 1022361]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 8037,
        'seriesname': '睿立达V7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M01/09/7C/autohomecar__ChxoHmfuSxOAWUAYAAavJNOXx7k657.png',
        'seriesminprice': 85800,
        'seriesmaxprice': 136000,
        'average': 0.0,
        'specids': '[1022076, 1022072, 1020498, 1022074, 1022075, 1022073]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 7263,
        'seriesname': '新海豚EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M06/DB/17/autohomecar__ChxkjmRLgCeAR_AMAAW76sUChQQ020.png',
        'seriesminprice': 141800,
        'seriesmaxprice': 149800,
        'average': 4.529,
        'specids': '[1015975, 1021348, 1018298, 1021443, 1015980, 1021442, 1015978, 1021441, 1015976, 1015977, 1021349, 1021350, 1015979]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6844,
        'seriesname': '轩度EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M06/5C/4D/autohomecar__Chtk2Wa8gGGAMaTpAAVDwkHW-tk885.png',
        'seriesminprice': 149900,
        'seriesmaxprice': 169900,
        'average': 0.0,
        'specids': '[76492, 74429, 67752, 74428, 69471]',
        'create_time': '2026-04-01 02:36:11'
    },
    {
        'seriesid': 6413,
        'seriesname': '炫界Pro EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M04/64/81/autohomecar__ChxknGI8NauAPT0fAAazpgmZDNM260.png',
        'seriesminprice': 119900,
        'seriesmaxprice': 176600,
        'average': 4.4863,
        'specids': '[64851, 64869, 64868, 64867]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 4278,
        'seriesname': '御风EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M01/29/5A/autohomecar__ChcCr1qnPm-AT7geAAcHrF4lbyo946.png',
        'seriesminprice': 188000,
        'seriesmaxprice': 480000,
        'average': 0.0,
        'specids': '[1022195, 1006521, 1006523, 1004932, 1022194, 1011552, 1006522]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8576,
        'seriesname': '东风福瑞通',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M05/BD/A6/autohomecar__ChxpVWnLfxiAIcrVACcD-j7J9qU935.png',
        'seriesminprice': 83800,
        'seriesmaxprice': 106000,
        'average': 0.0,
        'specids': '[1023472, 1023471, 1023463, 1023466, 1023464, 1023469, 1023468, 1023465, 1023470, 1023467]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7933,
        'seriesname': 'E顺达',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M07/31/05/autohomecar__Chtk2Wc13oWALy6IAAhzID__5C8614.png',
        'seriesminprice': 101200,
        'seriesmaxprice': 134900,
        'average': 0.0,
        'specids': '[1019981, 1023155, 1019971, 1019959, 1019961, 1023157, 1019642, 1019960, 1019974, 1019962, 1019980, 1019963, 1019968, 1019972, 1019970, 1019964, 1019977, 1019973, 1023159, 1019978, 1019966, 1023158, 1019969, 1019979, 1019965, 1019976, 1023176, 1023160, 1019975, 1019967]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7641,
        'seriesname': 'E路顺V6',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M09/41/36/autohomecar__ChxoHmX5VLmAEWGkAAjCMqB0UfE810.png',
        'seriesminprice': 153800,
        'seriesmaxprice': 153800,
        'average': 0.0,
        'specids': '[1018082]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 6488,
        'seriesname': '风行S60EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M03/4E/D8/autohomecar__ChwFlGJf5fuAc4cEAAdfbQjtBHw177.png',
        'seriesminprice': 155900,
        'seriesmaxprice': 165900,
        'average': 0.0,
        'specids': '[68392, 68393]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 6704,
        'seriesname': '智蓝精灵E7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M03/A7/99/autohomecar__ChwFj2JGZtaAciBCAAhT6Hhp0Yo608.png',
        'seriesminprice': 118500,
        'seriesmaxprice': 181300,
        'average': 4.8571,
        'specids': '[1018893, 1018891, 1016717, 1016716, 1018894, 1018896, 1016719, 1016718, 1018895]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7343,
        'seriesname': '雷驰·仁T10',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M06/AD/CF/autohomecar__ChxkjmUw3QCAMS90AAjeH_d7_ig571.png',
        'seriesminprice': 39800,
        'seriesmaxprice': 77000,
        'average': 0.0,
        'specids': '[1017183, 1016633, 1021293, 1021294, 1016639, 1016636, 1016640, 1021292, 1016637, 1017181, 1021291, 1016634, 1017182, 1016635, 1016638]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7138,
        'seriesname': '翼放EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M00/9C/2E/autohomecar__Chxky2PhsdWAXBmIAAMHszBjb3M392.png',
        'seriesminprice': 227500,
        'seriesmaxprice': 255000,
        'average': 0.0,
        'specids': '[1015101, 1015102]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 4878,
        'seriesname': '迈图',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g30/M04/64/E0/autohomecar__wKgHPlsxnC2AYPG6AAdAIHScCts912.png',
        'seriesminprice': 69000,
        'seriesmaxprice': 89000,
        'average': 0.0,
        'specids': '[1006524, 1006525]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7338,
        'seriesname': '长安神骐T30EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M03/D2/EB/autohomecar__Chtlx2WFaaGAMChtAApbfw6HpQI846.png',
        'seriesminprice': 119900,
        'seriesmaxprice': 139800,
        'average': 4.4314,
        'specids': '[1016601, 1016604, 1016605, 1016599, 1016603, 1016600, 1016597, 1021798, 1016602, 1016596, 1018489, 1021800, 1016598, 1021799, 1018020, 1016607, 1019198, 1018490, 1021801, 1018491, 1016606]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8144,
        'seriesname': '凯翼江豚E5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M08/0B/5C/autohomecar__Chtk2WgkU-6ACaWGAAZSrlpHPNo956.png',
        'seriesminprice': 64900,
        'seriesmaxprice': 99300,
        'average': 0.0,
        'specids': '[1021051, 1021045, 1021050, 1021049, 1021046, 1021048, 1021047, 1021052]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 6661,
        'seriesname': '御风EM26',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M09/2F/2B/autohomecar__ChxkqWIlrr6AGO8mAA3SHy8jcAw434.png',
        'seriesminprice': 171100,
        'seriesmaxprice': 176200,
        'average': 0.0,
        'specids': '[1015535, 1013522]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7581,
        'seriesname': '吉祥AIR',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M0A/6D/29/autohomecar__ChtlyGW_Wp6ALhcoAAaAHUGyvR4330.png',
        'seriesminprice': 147800,
        'seriesmaxprice': 159800,
        'average': 0.0,
        'specids': '[66525, 71997]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8539,
        'seriesname': '睿立达V6E',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M0B/59/5B/autohomecar__Chto52mDB0-AMID2AF1Bdu8jY8Q564.png',
        'seriesminprice': 83800,
        'seriesmaxprice': 86300,
        'average': 0.0,
        'specids': '[1023039, 1023038]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7763,
        'seriesname': '小象X7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M02/A2/04/autohomecar__ChtlyGZNzRuAbwpbAAVcQ7jciNo302.png',
        'seriesminprice': 176800,
        'seriesmaxprice': 186800,
        'average': 0.0,
        'specids': '[1018738, 1018732, 1018734, 1018739, 1018733, 1018736, 1018737, 1018735]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7447,
        'seriesname': '大力牛魔王D05',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M08/25/09/autohomecar__Chtk3WU2UjWAKjhfAAWGPqmPGbI220.png',
        'seriesminprice': 58300,
        'seriesmaxprice': 91800,
        'average': 0.0,
        'specids': '[1019528, 1019523, 1017193, 1017604, 1017197, 1017195, 1017602, 1017607, 1017196, 1019527, 1017194, 1017605, 1019524, 1017198, 1017606, 1017603, 1019520, 1019526, 1019521, 1019525, 1019522]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8250,
        'seriesname': '宇通天骏V6E',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M01/36/2B/autohomecar__ChxpV2icXtqAeAaQAC_tC31I4hk082.png',
        'seriesminprice': 366800,
        'seriesmaxprice': 381800,
        'average': 0.0,
        'specids': '[1021618, 1021619]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8308,
        'seriesname': '星塔EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M05/DD/F0/autohomecar__Chto52jZDEqAZ_ywAE5nXDZOw5U440.png',
        'seriesminprice': 165800,
        'seriesmaxprice': 189800,
        'average': 0.0,
        'specids': '[1022261, 1022088, 1022257, 1022084, 1022083, 1022080, 1022077, 1022082, 1022256, 1022263, 1022260, 1022079, 1022259, 1022258, 1022078, 1022086, 1022081, 1022087, 1022085, 1022262]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 5483,
        'seriesname': '长安神骐T10EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g3/M0A/D7/C5/autohomecar__ChcCRV2wFmuAC8m2AAajH4Qr2xU821.png',
        'seriesminprice': 77900,
        'seriesmaxprice': 172900,
        'average': 0.0,
        'specids': '[1011840, 1011843, 1011838, 1011839, 1011841, 1011842, 1015795, 1019569]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 4995,
        'seriesname': '域虎EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M04/AF/B1/autohomecar__ChcCP10QoJ6ADMmAAAaiumJmGrY590.png',
        'seriesminprice': 316800,
        'seriesmaxprice': 383800,
        'average': 0.0,
        'specids': '[1014389, 1014388, 1013803, 1014150, 1014387]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 6292,
        'seriesname': '风景智蓝G7新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M04/AA/C1/autohomecar__ChwFlGIxlHaASlrdAAn2ejPJAu8586.png',
        'seriesminprice': 130200,
        'seriesmaxprice': 177500,
        'average': 4.375,
        'specids': '[1017696, 1014406, 1017691, 1017702, 1017700, 1017697, 1014407, 1016730, 1014405, 1014402, 1016728, 1016729, 1017698, 1017703, 1014403, 1016724, 1017692, 1017701, 1016727, 1017705, 1017688, 1017699, 1017690, 1017704, 1014404, 1017689, 1016725, 1017693, 1012157, 1017687, 1017686, 1016731, 1017694, 1017695, 1012158, 1016726]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8247,
        'seriesname': '图雅诺X8新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M07/3D/CA/autohomecar__ChxpVmicVH6AP9z-ACrG3pqQ1gk810.png',
        'seriesminprice': 338800,
        'seriesmaxprice': 368300,
        'average': 0.0,
        'specids': '[1021991, 1021553, 1023286, 1021554]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 6486,
        'seriesname': '江淮T8新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M07/E3/0E/autohomecar__ChwFkmGN9aeAMBChAAvGDFnWWnI419.png',
        'seriesminprice': 169800,
        'seriesmaxprice': 169800,
        'average': 0.0,
        'specids': '[1021406]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7151,
        'seriesname': '锐捷',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M08/9B/AE/autohomecar__ChxkmmWFZ_aAQxQsAAd1OC-4X5g945.png',
        'seriesminprice': 173800,
        'seriesmaxprice': 179800,
        'average': 0.0,
        'specids': '[1015212, 1015213]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7573,
        'seriesname': '爱跑',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M04/ED/F0/autohomecar__ChxkPmbhK9OAMwuiAAajYQwHI-U210.png',
        'seriesminprice': 152900,
        'seriesmaxprice': 189900,
        'average': 0.0,
        'specids': '[72142, 67263, 67262, 67260, 68847]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8075,
        'seriesname': '图雅诺X5新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M08/09/D3/autohomecar__ChtpWGiuylCAD8pQAGRzKNvfl18044.png',
        'seriesminprice': 175600,
        'seriesmaxprice': 175600,
        'average': 0.0,
        'specids': '[1021686]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7545,
        'seriesname': '御风EM27',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M00/5C/AC/autohomecar__ChxknGV_p5WAI7mVAA4EwnlSfGw589.png',
        'seriesminprice': 104000,
        'seriesmaxprice': 120000,
        'average': 0.0,
        'specids': '[1018566, 1018565, 1018563, 1018558, 1018562, 1018559, 1018564, 1018567, 1018560, 1018561, 1017546]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8282,
        'seriesname': '瑞驰C3',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M04/89/DA/autohomecar__ChxpVWi6rj-ADr9SAB-BttSVL4g178.png',
        'seriesminprice': 79900,
        'seriesmaxprice': 131900,
        'average': 0.0,
        'specids': '[1021833, 1021826, 1021834, 1021822, 1021828, 1021831, 1021830, 1021823, 1021825, 1021832, 1021829, 1021820, 1021824, 1021821, 1021827]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7584,
        'seriesname': '钱多多',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M07/AC/52/autohomecar__ChxoHWW7PHCAWEe9AAlk1ddciwE790.png',
        'seriesminprice': 110500,
        'seriesmaxprice': 115500,
        'average': 4.8571,
        'specids': '[1018892, 1018890]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 6277,
        'seriesname': '跨越王X1 EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g24/M03/43/A8/autohomecar__ChwFjmDZcGyAX9_tAAxDjQ2r31o317.png',
        'seriesminprice': 142800,
        'seriesmaxprice': 175800,
        'average': 0.0,
        'specids': '[1017320, 1017316, 1017319, 1017318, 1011794, 1017317, 1017315]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8281,
        'seriesname': '瑞驰C5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M0B/7A/A7/autohomecar__ChxpV2i6rimAGXYrACgJ9mImTmY476.png',
        'seriesminprice': 89900,
        'seriesmaxprice': 150900,
        'average': 0.0,
        'specids': '[1021860, 1021838, 1021854, 1021835, 1021857, 1021886, 1021891, 1021869, 1021851, 1021850, 1021856, 1021892, 1021903, 1021846, 1021865, 1021901, 1021880, 1021848, 1021864, 1021878, 1021858, 1021870, 1021893, 1021837, 1021899, 1021855, 1021867, 1021863, 1021884, 1021896, 1021853, 1021861, 1021895, 1021890, 1021887, 1021875, 1021877, 1021840, 1021881, 1021872, 1021897, 1021845, 1021844, 1021866, 1021902, 1021868, 1021852, 1021873, 1021849, 1021898, 1021841, 1021883, 1021871, 1021900, 1021847, 1021862, 1021842, 1021836, 1021889, 1021874, 1021876, 1021859, 1021839, 1021894, 1021843]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7315,
        'seriesname': '星际EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M0A/35/5F/autohomecar__ChxoHWW4ypGAWnQbAAcSdiXAul0249.png',
        'seriesminprice': 249800,
        'seriesmaxprice': 309800,
        'average': 0.0,
        'specids': '[1022724, 1022726, 1022725, 1022727]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7255,
        'seriesname': '鑫源T3L EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g26/M05/D8/EE/autohomecar__CjIFVmRCZkqADooWAAVyq577uSY237.png',
        'seriesminprice': 79900,
        'seriesmaxprice': 145800,
        'average': 0.0,
        'specids': '[1015948, 1015949, 1022200, 1019393, 1022202, 1015947, 1020567, 1022201, 1019395, 1019394]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 6951,
        'seriesname': '枫叶80v PRO',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g29/M02/D3/F2/autohomecar__Chxkm2MtTpSAeZIdAAaIk0BDGDA150.png',
        'seriesminprice': 162800,
        'seriesmaxprice': 178800,
        'average': 0.0,
        'specids': '[57915, 57914]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 5833,
        'seriesname': '思皓E50A',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g29/M0B/A1/4B/autohomecar__ChwFk2K5dfKAEYOpAAoe5kQK0vg334.png',
        'seriesminprice': 152900,
        'seriesmaxprice': 189800,
        'average': 4.3183,
        'specids': '[50745, 52756, 58156, 61168, 57937]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7736,
        'seriesname': '江豚E6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M04/A1/0E/autohomecar__ChxoHmZNx0CAJdaJAAX_rGA0NKo211.png',
        'seriesminprice': 154800,
        'seriesmaxprice': 162800,
        'average': 0.0,
        'specids': '[1018615, 1018614, 1018609, 1018612, 1018611, 1018610, 1018613]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 5223,
        'seriesname': '江淮iEV7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g3/M04/FA/6D/autohomecar__ChsEm1ytr_2AT4HfAASOK4gnvi0893.png',
        'seriesminprice': 116500,
        'seriesmaxprice': 120500,
        'average': 4.4615,
        'specids': '[67237, 67236, 67238]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 4320,
        'seriesname': '云度π1',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M04/54/72/autohomecar__wKgHHlteoOOAcK2rAAY9zv2hQys488.png',
        'seriesminprice': 79800,
        'seriesmaxprice': 79800,
        'average': 4.8571,
        'specids': '[60294]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7260,
        'seriesname': '时代EV6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g27/M02/AF/1B/autohomecar__CjIFVWRGWTiAdygSAAcvu-Xc4B8627.png',
        'seriesminprice': 169800,
        'seriesmaxprice': 176800,
        'average': 0.0,
        'specids': '[1015972, 1015973]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8145,
        'seriesname': '凯翼江豚E7',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M01/0B/5C/autohomecar__Chtk2WgkU9OACn65AAernYJUOEA654.png',
        'seriesminprice': 83400,
        'seriesmaxprice': 148000,
        'average': 0.0,
        'specids': '[1021084, 1021772, 1021771, 1021082, 1021055, 1021085, 1021053, 1021083, 1021086, 1021042, 1021057, 1021056, 1021054]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7627,
        'seriesname': '锐骐7新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M02/08/E9/autohomecar__ChxoHmX4JGSAR0PXAAgdi20LnkE024.png',
        'seriesminprice': 189800,
        'seriesmaxprice': 299800,
        'average': 0.0,
        'specids': '[1020867, 1021758, 1020870, 1021757, 1021759, 1020866, 1020864, 1020865, 1020868, 1020869]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 4915,
        'seriesname': '东风·瑞泰特EM10',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g2/M07/97/B5/autohomecar__ChcCRF1RBAiASkuNAAwSeDnbTPs694.png',
        'seriesminprice': 79800,
        'seriesmaxprice': 79800,
        'average': 4.375,
        'specids': '[1006691]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 5790,
        'seriesname': '宇通T7新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M06/E4/DD/autohomecar__ChsEnl8YAmaANU7GAA8wQ-8KO0Q701.png',
        'seriesminprice': 880000,
        'seriesmaxprice': 880000,
        'average': 0.0,
        'specids': '[1021439]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7144,
        'seriesname': '蓝猫',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M01/00/52/autohomecar__Chxkmmg4YoiAVAQXAAXrS3lPXI8804.png',
        'seriesminprice': 86800,
        'seriesmaxprice': 186800,
        'average': 0.0,
        'specids': '[1016910, 1021147, 1016911, 1017861, 1017200, 1016663, 1017499, 1016912, 1017498, 1016661, 1016908, 1017199, 1018332, 1016909, 1015211, 1016662, 1017860, 1016659, 1017201, 1016907, 1016660, 1021146]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 5312,
        'seriesname': '锐骐6新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M00/29/D5/autohomecar__ChwFkl8X_omAPrXOAA9ndqMPD2Q294.png',
        'seriesminprice': 189800,
        'seriesmaxprice': 269800,
        'average': 0.0,
        'specids': '[1015417, 1015415, 1015412, 1018051, 1015416, 1018050, 1018049, 1022008]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7562,
        'seriesname': '活越神童01',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g28/M00/ED/EB/autohomecar__CjIFVGWWlMmAPgWZAARQLwOYbzg699.png',
        'seriesminprice': 39800,
        'seriesmaxprice': 98800,
        'average': 0.0,
        'specids': '[1017592, 1017591, 1019505]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7734,
        'seriesname': '新豹T3 EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M01/D9/02/autohomecar__ChtlyGY9zRKAF04KAAee3Ms3ZSY106.png',
        'seriesminprice': 151800,
        'seriesmaxprice': 187800,
        'average': 0.0,
        'specids': '[1020400, 1020404, 1020403, 1020401, 1018606, 1020402, 1018604, 1018605, 1020405]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7974,
        'seriesname': '予风黄金仓',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M03/FD/8C/autohomecar__ChxkPWdWX2iAQxbFAAqkNQEXqAI572.png',
        'seriesminprice': 93800,
        'seriesmaxprice': 139800,
        'average': 0.0,
        'specids': '[1021175, 1019710, 1021152, 1019709, 1020420, 1020798, 1021092, 1020797, 1021091]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8515,
        'seriesname': '华东祥云 插电混动',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M0A/42/E2/autohomecar__Chto52lkwVqAYkxWAEqyniIKYXw104.png',
        'seriesminprice': 398000,
        'seriesmaxprice': 398000,
        'average': 0.0,
        'specids': '[76283]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7794,
        'seriesname': '橙仕X5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M08/4C/01/autohomecar__ChxkPWaDzrOAMJLDAATChuSgC98888.png',
        'seriesminprice': 54800,
        'seriesmaxprice': 65800,
        'average': 0.0,
        'specids': '[1019022, 1019015, 1019026, 1019024, 1019014, 1019023, 1019016, 1019018, 1019019, 1019025, 1019020, 1019013, 1019017]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7966,
        'seriesname': '骏驰ET',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M0A/55/2B/autohomecar__ChxkPmdNWtyAY0AmAAfc0GT--e8339.png',
        'seriesminprice': 36800,
        'seriesmaxprice': 41800,
        'average': 0.0,
        'specids': '[73142, 70969]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 6967,
        'seriesname': '飞碟EF3',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M05/EC/3D/autohomecar__ChwFkmND4_6AYz48AAfAmoFdb8o505.png',
        'seriesminprice': 162000,
        'seriesmaxprice': 208000,
        'average': 0.0,
        'specids': '[1018651, 1018637, 1018650, 1018635, 1018652, 1018636, 1014470]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8548,
        'seriesname': '菱势黄金小卡Plus',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M09/93/83/autohomecar__ChtpWGmK_3SAcvvnAAA2x9IhKis773.png',
        'seriesminprice': 148000,
        'seriesmaxprice': 148000,
        'average': 0.0,
        'specids': '[1023063]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7778,
        'seriesname': 'TAGA达咖纯电',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M0B/10/48/autohomecar__ChxknGfuaUqATildAAm3dXcULIg519.png',
        'seriesminprice': 236300,
        'seriesmaxprice': 262300,
        'average': 0.0,
        'specids': '[1021210, 1021211, 1021229, 1021213, 1021212]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8495,
        'seriesname': '途逸T7E',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M08/18/F4/autohomecar__ChtpWGlFC5yAYKOqADDPKSmI6ps963.png',
        'seriesminprice': 68000,
        'seriesmaxprice': 68000,
        'average': 0.0,
        'specids': '[1022699]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7204,
        'seriesname': '鑫源T5L EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M06/31/04/autohomecar__CjIFU2WFZVGAFJ0YAA0Bg71oN3M636.png',
        'seriesminprice': 168800,
        'seriesmaxprice': 199800,
        'average': 0.0,
        'specids': '[1020916, 1020920, 1020452, 1020921, 1020923, 1020924, 1020919, 1020925, 1020922, 1020918, 1020917]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7871,
        'seriesname': '雷驰·信V70',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M0A/08/35/autohomecar__Chtk2WbxBD2AOXRIAASm1-FzNNA222.png',
        'seriesminprice': 148800,
        'seriesmaxprice': 148800,
        'average': 0.0,
        'specids': '[1019487]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8329,
        'seriesname': '金杯海狮EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M09/DE/F0/autohomecar__Chto52kAMX-ASRnbAIAIMoekjj0137.png',
        'seriesminprice': 142800,
        'seriesmaxprice': 150800,
        'average': 0.0,
        'specids': '[1022270, 1022271]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7779,
        'seriesname': '枫叶80v L',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g32/M09/DE/09/autohomecar__ChxkPWZpjA6AP2A5AAdx1XLJwZI535.png',
        'seriesminprice': 161700,
        'seriesmaxprice': 178700,
        'average': 0.0,
        'specids': '[68707, 68705, 68704, 68706]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 5016,
        'seriesname': '九龙EM3',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g3/M08/45/CE/autohomecar__ChcCRVvwFLmAeZu3AAkgTEtA-Hg168.png',
        'seriesminprice': 85800,
        'seriesmaxprice': 101800,
        'average': 0.0,
        'specids': '[1008497, 1006956]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 6808,
        'seriesname': '安凯快乐运',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M03/65/D8/autohomecar__ChxkqWK8GvmAS5avAArbXhkvwms875.png',
        'seriesminprice': 142800,
        'seriesmaxprice': 142800,
        'average': 0.0,
        'specids': '[1014104]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7373,
        'seriesname': '恺达EX6',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M06/EC/82/autohomecar__Chtk3WTu_NiAUl-kAAWLqyMufoU336.png',
        'seriesminprice': 153800,
        'seriesmaxprice': 206000,
        'average': 0.0,
        'specids': '[1019094, 1019095, 1016898, 1016897, 1019096, 1016899, 1016900, 1016901, 1016896]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 4612,
        'seriesname': '图雅诺智蓝新能源',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M07/44/06/autohomecar__ChwFj2IxkGqAWUcCAAlD85iIaL0667.png',
        'seriesminprice': 235700,
        'seriesmaxprice': 282800,
        'average': 0.0,
        'specids': '[1017660, 1012160, 1016723, 1016722, 1016721, 1017661, 1017662, 1012161, 1012159, 1017663, 1016720]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7011,
        'seriesname': '跨越王X3 EV',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M03/10/55/autohomecar__ChxkmmU2VYKAekTHAAjTqTXUJps814.png',
        'seriesminprice': 179800,
        'seriesmaxprice': 195800,
        'average': 0.0,
        'specids': '[1020376, 1020378, 1020377, 1020380, 1020384, 1014696, 1014697, 1019579, 1020381, 1020379, 1020374, 1019610, 1020382, 1014698, 1019612, 1020383, 1020373, 1020375, 1019611]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 6816,
        'seriesname': '安凯Q5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g28/M07/59/C3/autohomecar__ChsFWWLD0R6AYsuEAAm8Ks8IqIg767.png',
        'seriesminprice': 336000,
        'seriesmaxprice': 346000,
        'average': 0.0,
        'specids': '[1014152, 1014151]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7748,
        'seriesname': '飞碟U5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M01/B6/FA/autohomecar__ChxoHmZCzl2AdeaSAAf6-mFreUg888.png',
        'seriesminprice': 138000,
        'seriesmaxprice': 148000,
        'average': 0.0,
        'specids': '[1018649, 1018648]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 5832,
        'seriesname': '思皓E40X',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g25/M07/BA/60/autohomecar__ChsEel-ELJqAA2yKAAwTyTwyXQ0473.png',
        'seriesminprice': 160800,
        'seriesmaxprice': 170800,
        'average': 4.875,
        'specids': '[55895, 55894]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7585,
        'seriesname': '江淮卡拉',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M09/E8/05/autohomecar__ChxoHmW3ZJiAeV0aAAcWLwtb9ew622.png',
        'seriesminprice': 82800,
        'seriesmaxprice': 86800,
        'average': 0.0,
        'specids': '[1017852, 1017851]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8556,
        'seriesname': '金琥EV80',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M02/97/F5/autohomecar__ChxpV2muNuyAPXR5AFLk6RbK3jI006.png',
        'seriesminprice': 117800,
        'seriesmaxprice': 138000,
        'average': 0.0,
        'specids': '[1023133, 1023134, 1023135]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7758,
        'seriesname': '瑞驰新能源ES50',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M03/54/8C/autohomecar__ChtlyGZMDA-Ab875AAaItxjmTrY285.png',
        'seriesminprice': 83900,
        'seriesmaxprice': 83900,
        'average': 0.0,
        'specids': '[1018691]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 6324,
        'seriesname': '瑞驰新能源EC71',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g4/M07/6A/B5/autohomecar__ChwElmEJDnaAHtUCAAVNZ7JkJhM422.png',
        'seriesminprice': 74900,
        'seriesmaxprice': 135900,
        'average': 0.0,
        'specids': '[1016705, 1019034, 1016703, 1019033, 1019032, 1018840, 1016704]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7762,
        'seriesname': '小象X5',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g31/M0B/A1/DF/autohomecar__ChxoHmZNzQqAY8vxAAdk8OSjo5o731.png',
        'seriesminprice': 152800,
        'seriesmaxprice': 159800,
        'average': 0.0,
        'specids': '[1018715, 1018716, 1018714]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7525,
        'seriesname': '锐菱',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g30/M01/0B/37/autohomecar__CjIFU2VpT4uAGClFAAjA6CK6TCY234.png',
        'seriesminprice': 77800,
        'seriesmaxprice': 79800,
        'average': 0.0,
        'specids': '[1017472, 1017471, 1017470]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 6401,
        'seriesname': '瑞驰新能源EC72',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g6/M04/88/C1/autohomecar__Chxkj2FCuNuAOTVCAAdkKjq_SHE347.png',
        'seriesminprice': 83900,
        'seriesmaxprice': 83900,
        'average': 0.0,
        'specids': '[1018842]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7118,
        'seriesname': '小象EV',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M07/46/16/autohomecar__ChtliGO35_CAWgOPAAjzCvb00ho226.png',
        'seriesminprice': 152800,
        'seriesmaxprice': 187800,
        'average': 0.0,
        'specids': '[1015028, 1017529, 1015029, 1017528, 1015030, 1017530]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7164,
        'seriesname': '风景智蓝G5新能源',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g24/M05/AE/76/autohomecar__Chtk3WP8WP6AJLhVAApSDJ4IPSA010.png',
        'seriesminprice': 138600,
        'seriesmaxprice': 176700,
        'average': 0.0,
        'specids': '[1017680, 1015328, 1017685, 1017681, 1017677, 1017684, 1017679, 1015329, 1017678, 1017682, 1017683, 1017676]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7533,
        'seriesname': '创维D10',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M01/3B/29/autohomecar__ChxkPWa6yhuAfPF1AAjO2cCS8BM358.png',
        'seriesminprice': 198000,
        'seriesmaxprice': 228000,
        'average': 0.0,
        'specids': '[1019383, 1019035, 1019175]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7282,
        'seriesname': '悦ER',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M07/B5/74/autohomecar__ChtlyGWndCaAVraNAAd-dlLSHpU567.png',
        'seriesminprice': 145000,
        'seriesmaxprice': 148800,
        'average': 0.0,
        'specids': '[1016016, 1019580]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8228,
        'seriesname': '乐迪',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M07/1E/9E/autohomecar__ChtpWGjKWFGAZGYMACc67PbuJJk347.png',
        'seriesminprice': 149100,
        'seriesmaxprice': 159100,
        'average': 0.0,
        'specids': '[1022021, 1022015, 1022023, 1022014, 1022011, 1022016, 1021526, 1022020, 1022009, 1022013, 1022017, 1022018, 1022025, 1022024, 1022026, 1022010, 1022012, 1022019]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 6646,
        'seriesname': '橙仕X2',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g25/M07/64/14/autohomecar__ChxkqWIPCHuAM5JtAE3vcf6ZkTc914.png',
        'seriesminprice': 60800,
        'seriesmaxprice': 81800,
        'average': 0.0,
        'specids': '[1013385, 1014114, 1014112, 1013386, 1014110, 1014111, 1014113]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8475,
        'seriesname': '雷驰T10 Pro',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g34/M00/92/FE/autohomecar__ChxpV2k6HIqAM-FZAABOurjQyzw294.png',
        'seriesminprice': 55800,
        'seriesmaxprice': 69800,
        'average': 0.0,
        'specids': '[1022666, 1022667, 1022665, 1022669, 1022670, 1022671, 1022668, 1022672]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8394,
        'seriesname': '骐蔚熊猫宏运',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g34/M08/EA/D0/autohomecar__ChxpV2kB0Z6AYREWAHMGAePKgg0572.png',
        'seriesminprice': 190800,
        'seriesmaxprice': 195800,
        'average': 0.0,
        'specids': '[1022381, 1022382]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7765,
        'seriesname': 'Van宝路',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g32/M06/68/DD/autohomecar__Chtk2WZhJuGAGD6OAAY2rw9JwWw193.png',
        'seriesminprice': 119800,
        'seriesmaxprice': 209800,
        'average': 0.0,
        'specids': '[1019097, 1021032, 1019101, 1019102, 1018812, 1018811, 1021033, 1020014, 1019099, 1019098, 1020013, 1020431, 1020012, 1019100, 1020432, 1021031, 1020430, 1018813]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 6947,
        'seriesname': '枫叶60s PRO',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g26/M0A/66/4A/autohomecar__ChwFkGMr-UGAA9ecAAa95NP47-k810.png',
        'seriesminprice': 139800,
        'seriesmaxprice': 139800,
        'average': 0.0,
        'specids': '[59676, 59678]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8221,
        'seriesname': '中通T7',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M0B/93/39/autohomecar__ChxoHmh9_IeACoNUAAf6JncjXj8088.png',
        'seriesminprice': 152800,
        'seriesmaxprice': 152800,
        'average': 0.0,
        'specids': '[1021444]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 7750,
        'seriesname': '飞碟HW5',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g31/M07/B7/0B/autohomecar__ChxoHmZCzraAKPTFAAZt3ahN65A481.png',
        'seriesminprice': 218000,
        'seriesmaxprice': 268000,
        'average': 0.0,
        'specids': '[1018666, 1018663, 1018664, 1018665]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 5894,
        'seriesname': '飞碟Q2T',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g2/M0B/C0/35/autohomecar__ChwFql9heL6AfuVrABB3PDXUlbI192.png',
        'seriesminprice': 128000,
        'seriesmaxprice': 188000,
        'average': 0.0,
        'specids': '[1018655, 1018658, 1014469, 1018660, 1018659, 1018656, 1018654, 1018653, 1010169, 1018662, 1018661, 1010168, 1014468, 1018657]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8408,
        'seriesname': '跃进大拿T2',
        'seriesimg': '//car3.autoimg.cn/cardfs/series/g33/M01/1F/7F/autohomecar__ChxpVmkEo1yATnzbAFxSc_NZ8X4910.png',
        'seriesminprice': 140700,
        'seriesmaxprice': 154500,
        'average': 0.0,
        'specids': '[1022407, 1022403, 1022400, 1022404, 1022409, 1022401, 1022406, 1022402, 1022410, 1022408, 1022411, 1022405]',
        'create_time': '2026-04-01 02:36:12'
    },
    {
        'seriesid': 8409,
        'seriesname': '跃进大拿T1',
        'seriesimg': '//car2.autoimg.cn/cardfs/series/g33/M00/1F/7C/autohomecar__ChxpVmkEouOADmgpAG2b61FnlV8679.png',
        'seriesminprice': 189400,
        'seriesmaxprice': 228800,
        'average': 0.0,
        'specids': '[1022420, 1022427, 1022426, 1022424, 1022428, 1022412, 1022414, 1022421, 1022416, 1022415, 1022418, 1022422, 1022413, 1022423, 1022425, 1022417, 1022429, 1022419]',
        'create_time': '2026-04-01 02:36:12'
    }
]


def import_car_series(json_path):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO car_series
            (seriesid, seriesname, seriesimg, seriesminprice, seriesmaxprice, average, specids, create_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            for car in data:
                cursor.execute(sql, (
                    car.get('seriesid'),
                    car.get('seriesname'),
                    car.get('seriesimg'),
                    car.get('seriesminprice'),
                    car.get('seriesmaxprice'),
                    car.get('average'),
                    car.get('specids'),
                    car.get('create_time')
                ))
        conn.commit()
    finally:
        conn.close()


import requests


def download_image(url, code):
    # 发送HTTP请求获取图片数据
    response = requests.get(url)
    # 检查请求是否成功
    if response.status_code == 200:
        # 将图片数据写入文件
        save_path = f"E:/GraduationDesign/汽车租赁服务用户需求与车型推荐关联系统/backend/static/{code}.jpg"
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print("图片下载成功！")
    else:
        print(f"无法下载图片，HTTP响应码：{response.status_code}")


if __name__ == '__main__':
    for item in data:
        download_image(f"https:{item.get('seriesimg')}",item.get("seriesid"))
