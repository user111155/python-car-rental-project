<template>
  <div class="big-screen">
    <div class="screen-overlay"></div>
    <div class="screen-content">
      <div class="screen-header">
        <div class="title">汽车租赁运营可视化大屏</div>
        <div class="subtitle">实时概览 · 需求洞察 · 订单分布</div>
      </div>

      <el-row :gutter="16" class="kpi-row">
        <el-col :xs="24" :sm="8" v-for="item in kpiList" :key="item.key">
          <div class="kpi-card">
            <div class="kpi-label">{{ item.label }}</div>
            <div class="kpi-value">{{ item.value }}</div>
            <div class="kpi-trend">{{ item.hint }}</div>
          </div>
        </el-col>
      </el-row>

      <el-row :gutter="16" class="chart-row">
        <el-col :xs="24" :md="12">
          <div class="panel">
            <div class="panel-title">订单状态分布</div>
            <div ref="orderStatusChart" class="chart-box"></div>
          </div>
        </el-col>
        <el-col :xs="24" :md="12">
          <div class="panel">
            <div class="panel-title">热门车型 Top 8</div>
            <div ref="hotCarChart" class="chart-box"></div>
          </div>
        </el-col>
      </el-row>

      <el-row :gutter="16" class="chart-row">
        <el-col :xs="24" :md="16">
          <div class="panel">
            <div class="panel-title">车型平均租期分布</div>
            <div ref="weekTrendChart" class="chart-box"></div>
          </div>
        </el-col>
        <el-col :xs="24" :md="8">
          <div class="panel">
            <div class="panel-title">用车需求场景占比</div>
            <div ref="requirementChart" class="chart-box"></div>
          </div>
        </el-col>
      </el-row>

      <el-row :gutter="16" class="chart-row">
        <el-col :xs="24" :md="12">
          <div class="panel">
            <div class="panel-title">订单金额趋势（近7日）</div>
            <div ref="orderAmountChart" class="chart-box"></div>
          </div>
        </el-col>
        <el-col :xs="24" :md="12">
          <div class="panel">
            <div class="panel-title">订单金额分布（分段）</div>
            <div ref="orderAmountDistChart" class="chart-box"></div>
          </div>
        </el-col>
      </el-row>

      <el-row :gutter="16" class="table-row">
        <el-col :span="24">
          <div class="panel">
            <div class="panel-title">车型运营看板</div>
            <el-table :data="simulatedCars" height="260" size="small" class="screen-table">
              <el-table-column prop="name" label="车型" min-width="160" />
              <el-table-column prop="utilization" label="利用率" width="100" />
              <el-table-column prop="avgRentDays" label="平均租期(天)" width="120" />
              <el-table-column prop="satisfaction" label="满意度" width="100" />
              <el-table-column prop="income" label="预估日营收(元)" width="140" />
            </el-table>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts'
import { getAdminStats, getAdminCars, getAdminOrderList, getAdminRequirementStats } from '../api'

export default {
  data() {
    return {
      stats: {
        user_total: 0,
        car_total: 0,
        order_total: 0
      },
      cars: [],
      orders: [],
      requirementStats: [],
      simulatedCars: [],
      chartInstances: []
    }
  },
  computed: {
    kpiList() {
      return [
        {
          key: 'user_total',
          label: '总用户数',
          value: this.stats.user_total || 0,
          hint: '较昨日 +4.3%'
        },
        {
          key: 'car_total',
          label: '总车型数',
          value: this.stats.car_total || 0,
          hint: '车型库稳定'
        },
        {
          key: 'order_total',
          label: '总订单数',
          value: this.stats.order_total || 0,
          hint: '本周转化上升'
        }
      ]
    }
  },
  mounted() {
    this.loadData()
    window.addEventListener('resize', this.handleResize)
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize)
    this.chartInstances.forEach(item => item && item.dispose())
    this.chartInstances = []
  },
  methods: {
    async loadData() {
      const [statsRes, carsRes, ordersRes, requirementRes] = await Promise.all([
        getAdminStats(),
        getAdminCars(),
        getAdminOrderList(),
        getAdminRequirementStats()
      ])
      this.stats = statsRes.data.data || this.stats
      this.cars = carsRes.data.data || []
      this.orders = ordersRes.data.data || []
      this.requirementStats = requirementRes.data.data || []
      this.buildSimulatedData()
      this.$nextTick(() => {
        this.initCharts()
      })
    },
    buildSimulatedData() {
      const carTotal = Number(this.stats.car_total || this.cars.length || 0)
      const maxCount = Math.max(Math.min(carTotal, 12), 1)
      const source = (this.cars || []).slice(0, maxCount)

      this.simulatedCars = source.map((car, index) => {
        const avgRentDays = 2 + (index % 4)
        const basePrice = Number(car.rental_price_day || 260)
        const utilizationValue = Math.max(54, 90 - index * 3)
        const utilization = `${utilizationValue}%`
        const income = basePrice * avgRentDays * (utilizationValue / 100)
        return {
          name: car.seriesname,
          utilization,
          avgRentDays,
          satisfaction: `${(4.2 + ((index % 5) * 0.1)).toFixed(1)}`,
          income: Number(income).toFixed(2)
        }
      })
    },
    handleResize() {
      this.chartInstances.forEach(item => item && item.resize())
    },
    createChart(refName) {
      const el = this.$refs[refName]
      if (!el) return null
      const instance = echarts.init(el)
      this.chartInstances.push(instance)
      return instance
    },
    initCharts() {
      this.chartInstances.forEach(item => item && item.dispose())
      this.chartInstances = []

      this.renderOrderStatusChart()
      this.renderHotCarChart()
      this.renderWeekTrendChart()
      this.renderRequirementChart()
      this.renderOrderAmountTrendChart()
      this.renderOrderAmountDistributionChart()
    },
    renderOrderStatusChart() {
      const chart = this.createChart('orderStatusChart')
      if (!chart) return

      const totalOrders = Number(this.stats.order_total || this.orders.length || 0)
      const statusMap = { pending: 0, active: 0, completed: 0, canceled: 0 }

      this.orders.forEach(item => {
        const status = (item.status || '').toLowerCase()
        if (statusMap[status] !== undefined) {
          statusMap[status] += 1
        }
      })

      const counted = statusMap.pending + statusMap.active + statusMap.completed + statusMap.canceled
      if (totalOrders > counted) {
        statusMap.pending += totalOrders - counted
      }

      chart.setOption({
        color: ['#f8c24c', '#43d39e', '#49a8ff', '#ff6f91'],
        tooltip: { trigger: 'item' },
        series: [
          {
            type: 'pie',
            radius: ['42%', '68%'],
            center: ['50%', '52%'],
            label: { color: '#dbe9ff' },
            data: [
              { name: '待处理', value: statusMap.pending },
              { name: '进行中', value: statusMap.active },
              { name: '已完成', value: statusMap.completed },
              { name: '已取消', value: statusMap.canceled }
            ]
          }
        ]
      })
    },
    renderHotCarChart() {
      const chart = this.createChart('hotCarChart')
      if (!chart) return

      const topCars = this.simulatedCars.slice(0, Math.min(8, this.simulatedCars.length))
      chart.setOption({
        grid: { left: 80, right: 20, top: 24, bottom: 24 },
        xAxis: {
          type: 'value',
          axisLine: { lineStyle: { color: '#5d7aa8' } },
          splitLine: { lineStyle: { color: 'rgba(109, 147, 196, 0.2)' } }
        },
        yAxis: {
          type: 'category',
          data: topCars.map(item => item.name).reverse(),
          axisLine: { lineStyle: { color: '#5d7aa8' } },
          axisLabel: { color: '#dbe9ff' }
        },
        tooltip: { trigger: 'axis' },
        series: [
          {
            type: 'bar',
            data: topCars.map(item => Number(item.income)).reverse(),
            barWidth: 14,
            itemStyle: {
              borderRadius: [0, 8, 8, 0],
              color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                { offset: 0, color: '#34d7ff' },
                { offset: 1, color: '#3a7bff' }
              ])
            }
          }
        ]
      })
    },
    renderWeekTrendChart() {
      const chart = this.createChart('weekTrendChart')
      if (!chart) return

      const rentMap = { '1-2天': 0, '3-4天': 0, '5天及以上': 0 }
      this.simulatedCars.forEach(item => {
        if (item.avgRentDays <= 2) {
          rentMap['1-2天'] += 1
        } else if (item.avgRentDays <= 4) {
          rentMap['3-4天'] += 1
        } else {
          rentMap['5天及以上'] += 1
        }
      })

      chart.setOption({
        tooltip: { trigger: 'axis' },
        grid: { left: 44, right: 20, top: 24, bottom: 26 },
        xAxis: {
          type: 'category',
          data: Object.keys(rentMap),
          axisLine: { lineStyle: { color: '#5d7aa8' } },
          axisLabel: { color: '#dbe9ff' }
        },
        yAxis: {
          type: 'value',
          axisLine: { lineStyle: { color: '#5d7aa8' } },
          splitLine: { lineStyle: { color: 'rgba(109, 147, 196, 0.2)' } },
          axisLabel: { color: '#dbe9ff' }
        },
        series: [
          {
            type: 'bar',
            data: Object.values(rentMap),
            barWidth: 32,
            itemStyle: {
              borderRadius: [8, 8, 0, 0],
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: '#5fe3c1' },
                { offset: 1, color: '#2f7ff5' }
              ])
            }
          }
        ]
      })
    },
    renderRequirementChart() {
      const chart = this.createChart('requirementChart')
      if (!chart) return

      const fallbackData = [
        { use_case: '通勤代步', total: 12 },
        { use_case: '家庭出游', total: 9 },
        { use_case: '商务接待', total: 7 },
        { use_case: '长途旅行', total: 5 }
      ]
      const source = this.requirementStats.length ? this.requirementStats : fallbackData

      chart.setOption({
        tooltip: { trigger: 'item' },
        series: [
          {
            type: 'pie',
            radius: ['35%', '68%'],
            center: ['50%', '52%'],
            label: { color: '#dbe9ff', formatter: '{b}\n{d}%' },
            data: source.slice(0, 6).map(item => ({
              name: item.use_case,
              value: Number(item.total || 1)
            }))
          }
        ]
      })
    },
    getPaidOrders() {
      return (this.orders || []).filter(o => String(o.status || '').toLowerCase() === 'paid')
    },
    getLast7DaysKeys() {
      const keys = []
      const now = new Date()
      for (let i = 6; i >= 0; i -= 1) {
        const d = new Date(now.getFullYear(), now.getMonth(), now.getDate() - i)
        const m = String(d.getMonth() + 1).padStart(2, '0')
        const day = String(d.getDate()).padStart(2, '0')
        keys.push(`${d.getFullYear()}-${m}-${day}`)
      }
      return keys
    },
    renderOrderAmountTrendChart() {
      const chart = this.createChart('orderAmountChart')
      if (!chart) return

      const days = this.getLast7DaysKeys()
      const paidOrders = this.getPaidOrders()
      const amountByDay = {}
      days.forEach(k => {
        amountByDay[k] = 0
      })

      paidOrders.forEach(o => {
        const key = String(o.start_date || '').slice(0, 10)
        if (amountByDay[key] !== undefined) {
          amountByDay[key] += Number(o.total_amount || 0)
        }
      })

      const seriesData = days.map(k => Number(amountByDay[k] || 0))

      chart.setOption({
        grid: { left: 44, right: 16, top: 26, bottom: 28 },
        tooltip: { trigger: 'axis' },
        xAxis: {
          type: 'category',
          data: days.map(k => k.slice(5)),
          axisLine: { lineStyle: { color: '#5d7aa8' } },
          axisLabel: { color: '#dbe9ff' }
        },
        yAxis: {
          type: 'value',
          axisLine: { lineStyle: { color: '#5d7aa8' } },
          splitLine: { lineStyle: { color: 'rgba(109, 147, 196, 0.2)' } },
          axisLabel: { color: '#dbe9ff' }
        },
        series: [
          {
            type: 'line',
            data: seriesData,
            smooth: true,
            showSymbol: false,
            lineStyle: { width: 3, color: '#43d39e' },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: 'rgba(67, 211, 158, 0.45)' },
                { offset: 1, color: 'rgba(67, 211, 158, 0.02)' }
              ])
            }
          }
        ]
      })
    },
    renderOrderAmountDistributionChart() {
      const chart = this.createChart('orderAmountDistChart')
      if (!chart) return

      const paidOrders = this.getPaidOrders()
      const buckets = [
        { label: '0-500', min: 0, max: 500 },
        { label: '500-1000', min: 500, max: 1000 },
        { label: '1000-2000', min: 1000, max: 2000 },
        { label: '2000-3000', min: 2000, max: 3000 },
        { label: '3000+', min: 3000, max: Infinity }
      ]

      const counts = buckets.map(() => 0)
      paidOrders.forEach(o => {
        const amount = Number(o.total_amount || 0)
        const idx = buckets.findIndex(b => amount >= b.min && amount < b.max)
        if (idx >= 0) counts[idx] += 1
      })

      chart.setOption({
        grid: { left: 44, right: 16, top: 26, bottom: 28 },
        tooltip: { trigger: 'axis' },
        xAxis: {
          type: 'category',
          data: buckets.map(b => b.label),
          axisLine: { lineStyle: { color: '#5d7aa8' } },
          axisLabel: { color: '#dbe9ff' }
        },
        yAxis: {
          type: 'value',
          axisLine: { lineStyle: { color: '#5d7aa8' } },
          splitLine: { lineStyle: { color: 'rgba(109, 147, 196, 0.2)' } },
          axisLabel: { color: '#dbe9ff' }
        },
        series: [
          {
            type: 'bar',
            data: counts,
            barWidth: 28,
            itemStyle: {
              borderRadius: [8, 8, 0, 0],
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: '#ffb74a' },
                { offset: 1, color: '#ff6f91' }
              ])
            }
          }
        ]
      })
    }
  }
}
</script>

<style scoped>
.big-screen {
  position: relative;
  min-height: calc(100vh - 108px);
  padding: 12px;
  border-radius: 12px;
  overflow: hidden;
  background:
    radial-gradient(circle at 20% 10%, rgba(36, 82, 162, 0.35), transparent 45%),
    radial-gradient(circle at 90% 90%, rgba(29, 155, 192, 0.2), transparent 42%),
    linear-gradient(160deg, #071526 0%, #0d2238 48%, #0a1930 100%);
}
.screen-overlay {
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(119, 160, 212, 0.12) 1px, transparent 1px), linear-gradient(90deg, rgba(119, 160, 212, 0.12) 1px, transparent 1px);
  background-size: 22px 22px;
  pointer-events: none;
}
.screen-content {
  position: relative;
  z-index: 1;
}
.screen-header {
  margin-bottom: 12px;
}
.title {
  font-size: 30px;
  letter-spacing: 2px;
  font-weight: 700;
  color: #dff0ff;
  text-shadow: 0 0 18px rgba(117, 209, 255, 0.35);
}
.subtitle {
  margin-top: 4px;
  color: #9ec4eb;
  font-size: 13px;
}
.kpi-row,
.chart-row,
.table-row {
  margin-bottom: 12px;
}
.kpi-card {
  min-height: 118px;
  padding: 16px 18px;
  border-radius: 12px;
  background: linear-gradient(145deg, rgba(13, 44, 74, 0.75), rgba(15, 64, 104, 0.55));
  border: 1px solid rgba(100, 176, 245, 0.35);
  box-shadow: inset 0 0 22px rgba(79, 168, 255, 0.18);
}
.kpi-label {
  color: #9ec4eb;
  font-size: 14px;
}
.kpi-value {
  margin-top: 8px;
  font-size: 38px;
  line-height: 1;
  color: #f4fbff;
  font-weight: 700;
}
.kpi-trend {
  margin-top: 10px;
  color: #64d4ff;
  font-size: 12px;
}
.panel {
  border-radius: 12px;
  padding: 12px 14px;
  background: rgba(11, 40, 68, 0.76);
  border: 1px solid rgba(97, 162, 220, 0.28);
}
.panel-title {
  color: #cfe8ff;
  font-size: 14px;
  margin-bottom: 8px;
  font-weight: 600;
}
.chart-box {
  width: 100%;
  height: 260px;
}
.screen-table {
  background: transparent;
}
::v-deep .screen-table th,
::v-deep .screen-table tr,
::v-deep .screen-table td,
::v-deep .screen-table .el-table__body-wrapper,
::v-deep .screen-table .el-table__header-wrapper,
::v-deep .screen-table::before {
  background: transparent !important;
}
::v-deep .screen-table th > .cell {
  color: #9ec4eb;
}
::v-deep .screen-table .cell {
  color: #e7f4ff;
}
</style>
