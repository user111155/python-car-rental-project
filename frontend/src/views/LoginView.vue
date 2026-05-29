<template>
  <div class="login-wrap">
    <div class="login-mask"></div>
    <div class="login-hero">
      <h1>智能汽车租赁服务平台</h1>
      <p>按用户需求推荐车型，便捷预约，快速取还车</p>
    </div>
    <el-card class="login-card">
      <div slot="header">{{ isRegister ? '用户注册' : '用户登录' }}</div>
      <el-form :model="form" label-width="70px">
        <el-form-item label="用户名">
          <el-input v-model="form.username" placeholder="请输入用户名" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.password" type="password" show-password placeholder="请输入密码" />
        </el-form-item>
        <el-form-item v-if="isRegister" label="手机号">
          <el-input v-model="form.phone" placeholder="请输入手机号" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submit">{{ isRegister ? '注册' : '登录' }}</el-button>
          <el-button type="text" @click="isRegister = !isRegister">
            {{ isRegister ? '已有账号，去登录' : '没有账号，去注册' }}
          </el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import { login, register } from '../api'// 从我们之前学的 ../api/index.js 里，导入 login 和 register 这两个接口函数，用来调用后端的登录和注册接口的

export default {
  data() {
    return {
      isRegister: false,
      form: {
        username: '',
        password: '',
        phone: ''
      }
    }
  },
  methods: {
    async submit() {
      if (this.isRegister) {
        await register(this.form)
        this.$message.success('注册成功，请登录')
        this.isRegister = false
        return
      }
      const res = await login(this.form)
      localStorage.setItem('app_user', JSON.stringify(res.data.data))
      this.$router.push(res.data.data.role === 'admin' ? '/admin' : '/rental')
    }
  }
}
</script>

<style scoped>
.login-wrap {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  background:
    linear-gradient(rgba(16, 41, 70, 0.45), rgba(16, 41, 70, 0.45)),
    url('https://images.unsplash.com/photo-1493238792000-8113da705763?auto=format&fit=crop&w=1800&q=80') center/cover no-repeat;
  overflow: hidden;
}
.login-wrap::before {
  content: "";
  position: absolute;
  left: -10%;
  right: -10%;
  bottom: 10%;
  height: 120px;
  background: repeating-linear-gradient(
    to right,
    rgba(255, 255, 255, 0.18) 0 40px,
    rgba(255, 255, 255, 0) 40px 80px
  );
  transform: perspective(600px) rotateX(65deg);
}
.login-mask {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 20% 20%, rgba(215, 232, 252, 0.35), transparent 40%);
}
.login-hero {
  position: absolute;
  top: 16%;
  left: 8%;
  color: #f3f8ff;
  text-shadow: 0 3px 10px rgba(0, 0, 0, 0.3);
}
.login-hero h1 {
  margin: 0 0 10px;
  font-size: 34px;
}
.login-hero p {
  margin: 0;
  font-size: 16px;
}
.login-card {
  width: 460px;
  z-index: 2;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(4px);
  border-radius: 14px;
}
</style>
