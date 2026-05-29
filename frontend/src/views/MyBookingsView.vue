<template>
  <el-card>
    <div slot="header">我的预约</div>
    <el-table :data="orders">
      <el-table-column prop="id" label="订单ID" width="90" />
      <el-table-column prop="seriesname" label="车型" />
      <el-table-column prop="seat_count" label="座位" width="70" />
      <el-table-column prop="rental_price_day" label="日租价(元)" width="110" />
      <el-table-column prop="start_date" label="开始日期" />
      <el-table-column prop="end_date" label="结束日期" />
      <el-table-column prop="total_amount" label="金额" />
      <el-table-column prop="status" label="状态" />
      <el-table-column label="取还车记录" width="220">
        <template slot-scope="scope">
          <el-button size="mini" type="success" :disabled="scope.row.status !== 'paid'" @click="pickup(scope.row.id)">取车</el-button>
          <el-button
            size="mini"
            type="warning"
            :disabled="scope.row.status !== 'picked_up'"
            @click="returnCar(scope.row.id)"
          >还车</el-button>
        </template>
      </el-table-column>
    </el-table>
  </el-card>
</template>

<script>
import { getRentalOrders, pickupOrder, returnOrder } from '../api'

export default {
  name: 'MyBookingsView',
  data() {
    return {
      orders: []
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const user = JSON.parse(localStorage.getItem('app_user') || '{}')
      const res = await getRentalOrders({ user_id: user.id })
      this.orders = res.data.data || []
    },
    async pickup(id) {
      await pickupOrder(id)
      this.$message.success('取车记录已更新')
      this.loadData()
    },
    async returnCar(id) {
      await returnOrder(id)
      this.$message.success('还车记录已更新')
      this.loadData()
    }
  }
}
</script>
