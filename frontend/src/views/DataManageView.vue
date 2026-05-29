<template>
  <div>
    <el-row :gutter="16">
      <el-col :span="8">
        <el-card>
          <div slot="header">用户数据</div>
          <el-table :data="users" height="260">
            <el-table-column prop="id" label="ID" width="60" />
            <el-table-column prop="name" label="姓名" />
            <el-table-column prop="phone" label="手机号" />
          </el-table>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card>
          <div slot="header">车型数据</div>
          <el-table :data="cars" height="260">
            <el-table-column prop="seriesname" label="车型" />
            <el-table-column prop="seriesminprice" label="最低价" />
            <el-table-column prop="average" label="评分" />
          </el-table>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card>
          <div slot="header">租赁订单</div>
          <el-table :data="orders" height="260">
            <el-table-column prop="id" label="订单ID" width="80" />
            <el-table-column prop="status" label="状态" />
            <el-table-column prop="total_amount" label="金额" />
          </el-table>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { getCars, getOrders, getUsers } from '../api'

export default {
  data() {
    return {
      users: [],
      cars: [],
      orders: []
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const [u, c, o] = await Promise.all([getUsers(), getCars(), getOrders()])
      this.users = u.data.data || []
      this.cars = c.data.data || []
      this.orders = o.data.data || []
    }
  }
}
</script>
