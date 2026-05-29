<template>
  <div>
    <el-alert :title="hintText" type="info" :closable="false" style="margin-bottom: 16px" />
    
    <!-- 新增：排序选择器 -->
    <div style="margin-bottom: 16px; text-align: right;">
      <span>排序方式：</span>
      <el-select v-model="order_by" @change="onOrderChange" placeholder="请选择">
        <el-option label="按匹配度排序" value="match_score"></el-option>
        <el-option label="按性价比排序" value="cost_performance"></el-option>
      </el-select>
    </div>

    <el-row :gutter="16">
      <el-col v-for="item in list" :key="item.id" :xs="24" :sm="12" :md="8" :lg="6" style="margin-bottom: 16px">
        <el-card class="car-card" shadow="hover">
          <img :src="getCarImage(item)" class="car-image" @error="onImgError($event, item)" />
          <div class="car-name">{{ item.seriesname }}</div>
          <div class="car-price">{{ item.seriesminprice }} - {{ item.seriesmaxprice }} 万</div>
          <div class="car-rent">租赁价：{{ item.rental_price_day }} 元/天</div>
          <div v-if="Number(item.average) > 0" class="car-score">
            <span class="score-label">口碑分</span>
            <el-rate :value="Number(item.average)" disabled allow-half text-color="#ff9900" />
            <span class="score-value">{{ Number(item.average).toFixed(2) }}</span>
          </div>
          <div v-else class="car-no-score">暂未评分</div>
          <div class="btn-row">
            <el-button type="primary" size="mini" @click="openBook(item)">预约</el-button>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-dialog title="预约车型" :visible.sync="dialogVisible" width="420px">
      <el-form :model="form" label-width="80px">
        <el-form-item label="车型">
          <el-input v-model="form.car_name" disabled />
        </el-form-item>
        <el-form-item label="开始日期">
          <el-date-picker v-model="form.start_date" type="date" value-format="yyyy-MM-dd" style="width: 100%" />
        </el-form-item>
        <el-form-item label="结束日期">
          <el-date-picker v-model="form.end_date" type="date" value-format="yyyy-MM-dd" style="width: 100%" />
        </el-form-item>
        <el-form-item label="总金额">
          <el-input-number v-model="form.total_amount" :min="0" :step="100" />
        </el-form-item>
      </el-form>
      <span slot="footer">
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="openPayment">确认预约</el-button>
      </span>
    </el-dialog>

    <el-dialog title="支付页面" :visible.sync="paymentVisible" width="420px">
      <div class="pay-card">
        <div class="pay-row"><span>车型：</span><strong>{{ paymentForm.car_name }}</strong></div>
        <div class="pay-row"><span>开始：</span><strong>{{ paymentForm.start_date }}</strong></div>
        <div class="pay-row"><span>结束：</span><strong>{{ paymentForm.end_date }}</strong></div>
        <div class="pay-row pay-amount"><span>支付金额：</span><strong>￥{{ paymentForm.total_amount }}</strong></div>
      </div>
      <span slot="footer">
        <el-button @click="paymentVisible = false">取消支付</el-button>
        <el-button type="success" :loading="paying" @click="submitPayment">支付</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { getRecommend, getRequirements, previewRentalPayment, payRentalBooking } from '../api'

export default {
  data() {
    return {
      staticBase: process.env.NODE_ENV === 'development' ? 'http://127.0.0.1:5000/static' : '/static',
      hintText: '正在按照你的用车需求推荐车型',
      // 新增：排序方式变量，默认按匹配度
      order_by: 'match_score',
      form: {
        user_id: 1,
        car_id: 1,
        car_name: '',
        start_date: '',
        end_date: '',
        total_amount: 1000
      },
      paymentForm: {
        user_id: 1,
        car_id: 1,
        car_name: '',
        start_date: '',
        end_date: '',
        total_amount: 0
      },
      list: [],
      dialogVisible: false,
      paymentVisible: false,
      paying: false
    }
  },
  mounted() {
    this.fetchRecommend()
  },
  methods: {
    getCarImage(car) {
      return `${this.staticBase}/${car.seriesid}.jpg`
    },
    onImgError(event, car) {
      if (car && car.seriesimg && event.target.src !== car.seriesimg) {
        event.target.src = car.seriesimg
        return
      }
      event.target.src = 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="320" height="160"><rect width="100%" height="100%" fill="%23f5f7fa"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="%2390999c" font-size="16">No Image</text></svg>'
    },
    // 新增：排序方式变化时，重新加载推荐
    onOrderChange() {
      this.fetchRecommend()
    },
    async fetchRecommend() {
      const user = JSON.parse(localStorage.getItem('app_user') || '{}')
      const reqRes = await getRequirements({ user_name: user.username })
      const reqList = reqRes.data.data || []
      if (!reqList.length) {
        // 这里把写死的order_by改成用变量
        const allRes = await getRecommend({ order_by: this.order_by })
        const allList = allRes.data.data || []
        this.list = allList.slice(0, 20)
        this.hintText = `你还没有提交需求，已按${this.order_by === 'match_score' ? '匹配度' : '性价比'}推荐20款车型`
        return
      }
      const latestReq = reqList[0]
      const payload = {
        use_case: latestReq.use_case,
        budget_min: latestReq.budget_min,
        budget_max: latestReq.budget_max,
        seat_count: latestReq.seat_count,
        config_need: latestReq.config_need,
        // 这里把写死的order_by改成用变量
        order_by: this.order_by
      }
      const res = await getRecommend(payload)
      this.list = res.data.data || []
      this.hintText = `已根据你最新提交的需求，按${this.order_by === 'match_score' ? '匹配度' : '性价比'}进行推荐`
    },
    openBook(row) {
      const user = JSON.parse(localStorage.getItem('app_user') || '{}')
      this.form.user_id = user.id
      this.form.car_id = row.id
      this.form.car_name = row.seriesname
      this.form.start_date = ''
      this.form.end_date = ''
      this.form.total_amount = Number(row.rental_price_day || 100)
      this.dialogVisible = true
    },
    calcAmount() {
      if (this.form.start_date && this.form.end_date) {
        const dayMs = 24 * 60 * 60 * 1000
        const days = Math.max(1, Math.floor((new Date(this.form.end_date) - new Date(this.form.start_date)) / dayMs) + 1)
        const car = this.list.find(c => c.id === this.form.car_id) || {}
        this.form.total_amount = days * Number(car.rental_price_day || 100)
      }
    },
    async openPayment() {
      if (!this.form.start_date || !this.form.end_date) {
        this.$message.warning('请选择预约日期')
        return
      }
      this.calcAmount()
      const res = await previewRentalPayment(this.form)
      this.paymentForm = { ...(res.data.data || this.form) }
      this.dialogVisible = false
      this.paymentVisible = true
    },
    async submitPayment() {
      this.paying = true
      try {
        await payRentalBooking(this.paymentForm)
        this.$message.success('支付成功，已加入我的预约')
        this.paymentVisible = false
      } finally {
        this.paying = false
      }
    }
  }
}
</script>

<style scoped>
.car-card {
  min-height: 360px;
}
.car-image {
  width: 100%;
  height: 170px;
  object-fit: contain;
  object-position: center;
  background: #f5f7fa;
  border-radius: 4px;
}
.car-name {
  font-size: 16px;
  margin-top: 10px;
  line-height: 1.4;
  min-height: 44px;
}
.car-price {
  color: #e67e22;
  margin-top: 6px;
}
.car-score {
  margin-top: 6px;
  color: #606266;
  display: flex;
  align-items: center;
  gap: 6px;
}
.car-rent {
  margin-top: 6px;
  color: #409eff;
  font-weight: 600;
}
.btn-row {
  margin-top: 12px;
}
.score-label,
.score-value {
  font-weight: 600;
}
.car-no-score {
  margin-top: 6px;
  color: #909399;
}
.pay-card {
  padding: 8px 4px;
}
.pay-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 12px;
  color: #606266;
}
.pay-amount {
  font-size: 18px;
  color: #e67e22;
  font-weight: 700;
}
</style>