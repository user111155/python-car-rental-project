<template>
  <el-row :gutter="16">
    <el-col :span="9">
      <el-card>
        <div slot="header">提交用车需求</div>
        <el-form :model="form" label-width="90px">
          <el-form-item label="用途">
            <el-input v-model="form.use_case" placeholder="如商务出行" />
          </el-form-item>
          <el-form-item label="时长(天)">
            <el-input-number v-model="form.duration_days" :min="1" />
          </el-form-item>
          <el-form-item label="预算下限">
            <el-input-number v-model="form.budget_min" :min="0" />
          </el-form-item>
          <el-form-item label="预算上限">
            <el-input-number v-model="form.budget_max" :min="0" />
          </el-form-item>
          <el-form-item label="座位数">
            <el-input-number v-model="form.seat_count" :min="2" :max="9" />
          </el-form-item>
          <el-form-item label="配置需求">
            <el-input v-model="form.config_need" placeholder="如新能源/SUV/商务" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submit">提交需求</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </el-col>
    <el-col :span="15">
      <el-card>
        <div slot="header">我提交的需求</div>
        <el-table :data="list" style="width: 100%">
          <el-table-column prop="use_case" label="用途" />
          <el-table-column prop="duration_days" label="时长(天)" width="90" />
          <el-table-column prop="budget_min" label="预算下限" />
          <el-table-column prop="budget_max" label="预算上限" />
          <el-table-column prop="seat_count" label="座位" width="70" />
          <el-table-column prop="config_need" label="配置需求" />
          <el-table-column prop="created_at" label="提交时间" />
        </el-table>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
import { createRequirement, getRequirements } from '../api'

export default {
  data() {
    return {
      form: {
        user_name: '',
        use_case: '',
        duration_days: 1,
        budget_min: 100,
        budget_max: 300,
        seat_count: 5,
        config_need: ''
      },
      list: []
    }
  },
  mounted() {
    const user = JSON.parse(localStorage.getItem('app_user') || '{}')
    this.form.user_name = user.username || ''
    this.loadData()
  },
  methods: {
    async loadData() {
      const user = JSON.parse(localStorage.getItem('app_user') || '{}')
      const res = await getRequirements({ user_name: user.username })
      this.list = res.data.data || []
    },
    async submit() {
      await createRequirement(this.form)
      this.$message.success('提交成功')
      this.loadData()
    }
  }
}
</script>
