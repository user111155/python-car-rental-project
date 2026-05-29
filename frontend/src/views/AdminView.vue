<template>
  <div>
    <el-tabs v-model="activeTab">
      <el-tab-pane label="租赁车型管理" name="cars">
        <el-row :gutter="16">
          <el-col v-for="car in cars" :key="car.id" :xs="24" :sm="12" :md="8" :lg="6" style="margin-bottom: 16px">
            <el-card shadow="hover" class="car-card">
              <img :src="getCarImage(car)" class="car-image" @error="onImgError($event, car)" />
              <div class="car-name">{{ car.seriesname }}</div>
              <div class="car-price">{{ car.seriesminprice }} - {{ car.seriesmaxprice }} 万</div>
              <div v-if="Number(car.average) > 0" class="car-score">
                <span class="score-label">口碑分</span>
                <el-rate :value="Number(car.average)" disabled allow-half text-color="#ff9900" />
                <span class="score-value">{{ Number(car.average).toFixed(2) }}</span>
              </div>
              <div v-else class="car-no-score">暂未评分</div>
              <div class="car-rent">租赁价：{{ car.rental_price_day }} 元/天</div>
              <div class="car-stock">库存：{{ car.stock_count }} 台 | 状态：{{ car.vehicle_status === 'available' ? '可租赁' : car.vehicle_status === 'maintenance' ? '维护中' : '已售罄' }}</div>
              <div style="margin-top: 10px">
                <el-button size="mini" type="primary" @click="openEditStock(car)">编辑库存</el-button>
                <el-button size="mini" type="danger" @click="deleteCar(car.id)">删除</el-button>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-tab-pane>
      <el-tab-pane label="用户预约列表" name="bookings">
        <el-card>
          <el-table :data="orderList">
            <el-table-column prop="id" label="订单ID" width="80" />
            <el-table-column prop="username" label="用户名" />
            <el-table-column prop="seriesname" label="车型" />
            <el-table-column prop="start_date" label="开始日期" />
            <el-table-column prop="end_date" label="结束日期" />
            <el-table-column prop="status" label="状态" width="110" />
            <el-table-column label="操作" width="120">
              <template slot-scope="scope">
                <el-button size="mini" type="success" @click="setOrderStatus(scope.row.id, 'completed')">标记完成</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </el-tab-pane>
      <el-tab-pane label="用车需求统计列表" name="requirements">
        <el-card>
          <el-table :data="requirementsStats">
            <el-table-column prop="use_case" label="用途" />
            <el-table-column prop="config_need" label="配置需求" />
            <el-table-column prop="total" label="需求数量" width="100" />
            <el-table-column prop="avg_duration_days" label="平均时长(天)" width="120" />
            <el-table-column prop="avg_budget_min" label="平均预算下限" />
            <el-table-column prop="avg_budget_max" label="平均预算上限" />
          </el-table>
        </el-card>
      </el-tab-pane>
      <el-tab-pane label="用户中心模块" name="users">
        <el-card class="stats-card">
          <div class="stats-rings">
            <div v-for="item in statItems" :key="item.key" class="stats-item">
              <div class="ring-wrap">
                <svg viewBox="0 0 100 100" class="ring-svg">
                  <circle class="ring-bg" cx="50" cy="50" r="38" />
                  <circle
                    class="ring-fg"
                    cx="50"
                    cy="50"
                    r="38"
                    :stroke="item.color"
                    :stroke-dasharray="circleLength"
                    :stroke-dashoffset="circleLength * (1 - calcProgress(item.value))"
                  />
                </svg>
                <div class="ring-content">
                  <div class="ring-value">{{ item.value }}</div>
                  <div class="ring-label">{{ item.label }}</div>
                </div>
              </div>
            </div>
          </div>
        </el-card>
        <el-card style="margin-top: 16px">
          <div slot="header" class="user-header">
            <span>用户列表</span>
            <el-button size="mini" type="primary" @click="openCreateUser">新增用户</el-button>
          </div>
          <el-table :data="users">
            <el-table-column prop="id" label="ID" width="60" />
            <el-table-column prop="username" label="用户名" />
            <el-table-column prop="name" label="姓名" />
            <el-table-column prop="phone" label="手机号" />
            <el-table-column prop="role" label="角色" width="100" />
            <el-table-column label="操作" width="180">
              <template slot-scope="scope">
                <el-button size="mini" @click="openEditUser(scope.row)">编辑</el-button>
                <el-button size="mini" type="danger" @click="deleteUser(scope.row.id)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </el-tab-pane>
    </el-tabs>

    <!-- 编辑库存的弹窗 -->
    <el-dialog title="编辑车型库存" :visible.sync="stockDialogVisible" width="420px">
      <el-form :model="stockForm" label-width="80px">
        <el-form-item label="库存数量">
          <el-input v-model.number="stockForm.stock_count" type="number" min="0" placeholder="请输入可租赁的车辆数量" />
        </el-form-item>
        <el-form-item label="车辆状态">
          <el-select v-model="stockForm.vehicle_status" style="width: 100%">
            <el-option label="可租赁" value="available" />
            <el-option label="维护中" value="maintenance" />
            <el-option label="已售罄" value="sold_out" />
          </el-select>
        </el-form-item>
      </el-form>
      <span slot="footer">
        <el-button @click="stockDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="saveStock">保存</el-button>
      </span>
    </el-dialog>

    <!-- 原来的用户编辑弹窗 -->
    <el-dialog :title="isEditUser ? '编辑用户' : '新增用户'" :visible.sync="userDialogVisible" width="420px">
      <el-form :model="userForm" label-width="80px">
        <el-form-item label="用户名">
          <el-input v-model="userForm.username" :disabled="isEditUser" />
        </el-form-item>
        <el-form-item label="姓名">
          <el-input v-model="userForm.name" />
        </el-form-item>
        <el-form-item label="手机号">
          <el-input v-model="userForm.phone" />
        </el-form-item>
        <el-form-item v-if="!isEditUser" label="密码">
          <el-input v-model="userForm.password" type="password" show-password />
        </el-form-item>
        <el-form-item label="角色">
          <el-select v-model="userForm.role" style="width: 100%">
            <el-option label="用户" value="user" />
            <el-option label="管理员" value="admin" />
          </el-select>
        </el-form-item>
      </el-form>
      <span slot="footer">
        <el-button @click="userDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="saveUser">保存</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
import {
  getAdminCars,
  getAdminOrderList,
  getAdminRequirementStats,
  getAdminStats,
  getAdminUsers,
  createAdminUser,
  updateAdminUser,
  deleteAdminUser,
  deleteAdminCar,
  updateAdminOrderStatus,
  updateAdminCarStatus
} from '../api'
export default {
  data() {
    return {
      staticBase: process.env.NODE_ENV === 'development' ? 'http://127.0.0.1:5000/static' : '/static',
      activeTab: 'cars',
      stats: {},
      users: [],
      cars: [],
      orderList: [],
      requirementsStats: [],
      userDialogVisible: false,
      isEditUser: false,
      userForm: {
        id: null,
        username: '',
        name: '',
        phone: '',
        password: '',
        role: 'user'
      },
      // 新增的库存弹窗相关变量
      stockDialogVisible: false,
      currentCarId: null,
      stockForm: {
        stock_count: 0,
        vehicle_status: 'available'
      }
    }
  },
  computed: {
    statItems() {
      return [
        { key: 'user_total', label: '总用户数', value: Number(this.stats.user_total || 0), color: '#2f8cff' },
        { key: 'car_total', label: '总车型数', value: Number(this.stats.car_total || 0), color: '#00c48c' },
        { key: 'order_total', label: '总订单数', value: Number(this.stats.order_total || 0), color: '#f5b800' }
      ]
    },
    maxStatValue() {
      const values = this.statItems.map(item => item.value)
      return Math.max(...values, 1)
    },
    circleLength() {
      return 2 * Math.PI * 38
    }
  },
  mounted() {
    this.loadData()
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
      event.target.src = 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="320" height="160"><rect width="100%" height="100%" fill="%23f5f7fa" /><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="%2390999c" font-size="16">No Image</text></svg>'
    },
    calcProgress(value) {
      const ratio = Number(value || 0) / this.maxStatValue
      return Math.max(0.25, Math.min(1, ratio))
    },
    async loadData() {
      const [inventoryRes, statsRes] = await Promise.all([
        getAdminRequirementStats(),
        getAdminStats()
      ])
      const [usersRes, carsRes, orderListRes] = await Promise.all([
        getAdminUsers(),
        getAdminCars(),
        getAdminOrderList()
      ])
      this.requirementsStats = inventoryRes.data.data || []
      this.stats = statsRes.data.data || {}
      this.users = usersRes.data.data || []
      this.cars = carsRes.data.data || []
      this.orderList = orderListRes.data.data || []
    },
    async setOrderStatus(id, status) {
      await updateAdminOrderStatus(id, { status })
      this.$message.success('订单状态已更新')
      this.loadData()
    },
    async deleteCar(id) {
      await deleteAdminCar(id)
      this.$message.success('车型已删除')
      this.loadData()
    },
    // 新增的打开编辑库存弹窗的方法
    openEditStock(car) {
      this.currentCarId = car.id
      this.stockForm = {
        stock_count: car.stock_count,
        vehicle_status: car.vehicle_status
      }
      this.stockDialogVisible = true
    },
    // 新增的保存库存的方法
    async saveStock() {
      await updateAdminCarStatus(this.currentCarId, this.stockForm)
      this.$message.success('库存已更新')
      this.stockDialogVisible = false
      this.loadData() // 重新加载数据，让页面显示最新的库存
    },
    openCreateUser() {
      this.isEditUser = false
      this.userForm = {
        id: null,
        username: '',
        name: '',
        phone: '',
        password: '',
        role: 'user'
      }
      this.userDialogVisible = true
    },
    openEditUser(row) {
      this.isEditUser = true
      this.userForm = {
        id: row.id,
        username: row.username,
        name: row.name,
        phone: row.phone,
        password: '',
        role: row.role || 'user'
      }
      this.userDialogVisible = true
    },
    async saveUser() {
      if (this.isEditUser) {
        await updateAdminUser(this.userForm.id, {
          name: this.userForm.name,
          phone: this.userForm.phone,
          role: this.userForm.role
        })
      } else {
        await createAdminUser(this.userForm)
      }
      this.$message.success('用户保存成功')
      this.userDialogVisible = false
      this.loadData()
    },
    async deleteUser(id) {
      await deleteAdminUser(id)
      this.$message.success('用户已删除')
      this.loadData()
    }
  }
}
</script>
<style scoped>
.car-card {
  min-height: 420px;
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
.car-score,
.car-meta {
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
.car-stock {
  margin-top: 6px;
  color: #00c48c;
  font-weight: 500;
}
.score-label,
.score-value {
  font-weight: 600;
}
.car-no-score {
  margin-top: 6px;
  color: #909399;
}
.user-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.stats-card {
  padding: 4px 0;
}
.stats-rings {
  display: flex;
  justify-content: flex-start;
  gap: 24px;
  flex-wrap: wrap;
}
.stats-item {
  width: 120px;
}
.ring-wrap {
  position: relative;
  width: 110px;
  height: 110px;
}
.ring-svg {
  width: 110px;
  height: 110px;
  transform: rotate(-90deg);
}
.ring-bg,
.ring-fg {
  fill: none;
  stroke-width: 8;
}
.ring-bg {
  stroke: #e9eef7;
}
.ring-fg {
  stroke-linecap: round;
  transition: stroke-dashoffset 0.35s ease;
}
.ring-content {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.ring-value {
  font-size: 18px;
  font-weight: 700;
  color: #1f2d3d;
  line-height: 1;
}
.ring-label {
  margin-top: 6px;
  font-size: 12px;
  color: #8c97a8;
}
</style>