<template>
  <div class="app-shell">
    <el-header v-if="!isLoginPage" class="topbar">
      <div class="brand">汽车租赁服务用户需求与车型推荐关联系统</div>
      <el-menu v-if="user" :default-active="$route.path" mode="horizontal" router class="top-menu">
        <template v-if="currentRole === 'user'">
          <el-menu-item index="/rental">租赁车型</el-menu-item>
          <el-menu-item index="/bookings">我的预约</el-menu-item>
          <el-menu-item index="/requirements">用车需求</el-menu-item>
          <el-menu-item index="/recommend">智能推荐</el-menu-item>
        </template>
        <template v-else>
          <el-menu-item index="/dashboard">可视化大屏</el-menu-item>
          <el-menu-item index="/admin">管理中心</el-menu-item>
        </template>
      </el-menu>
      <div class="right-zone">
        <el-radio-group
          v-if="canSwitchRole"
          v-model="roleSwitch"
          class="role-switch"
          size="mini"
          @change="onRoleSwitch"
          style="margin-right: 10px"
        >
          <el-radio-button label="user">用户系统</el-radio-button>
          <el-radio-button label="admin">管理系统</el-radio-button>
        </el-radio-group>
        <el-button v-if="user" type="text" @click="logout">退出登录</el-button>
      </div>
    </el-header>
    <el-main :class="isLoginPage ? 'main-panel login-main' : 'main-panel'">
      <router-view />
    </el-main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      roleSwitch: localStorage.getItem('app_role_switch') || ''
    }
  },
  computed: {
    user() {
      const userText = localStorage.getItem('app_user')
      return userText ? JSON.parse(userText) : null
    },
    normalizedRole() {
      const role = ((this.user && this.user.role) || '').toString().trim().toLowerCase()
      if (role === 'admin' || role === 'administrator' || role === '管理员') {
        return 'admin'
      }
      return 'user'
    },
    canSwitchRole() {
      const username = ((this.user && this.user.username) || '').toString().trim().toLowerCase()
      return !!this.user && (this.normalizedRole === 'admin' || username === 'admin')
    },
    currentRole() {
      if (!this.user) {
        return 'guest'
      }
      if (this.canSwitchRole) {
        const role = this.roleSwitch || 'admin'
        return role === 'user' ? 'user' : 'admin'
      }
      return this.normalizedRole
    },
    isLoginPage() {
      return this.$route.path === '/login'
    }
  },
  methods: {
    onRoleSwitch(nextRole) {
      localStorage.setItem('app_role_switch', nextRole)
      const userPaths = ['/rental', '/bookings', '/requirements', '/recommend']
      const adminPaths = ['/dashboard', '/admin', '/data']
      const allowed = nextRole === 'admin' ? adminPaths : userPaths
      if (!allowed.includes(this.$route.path)) {
        this.$router.push(nextRole === 'admin' ? '/dashboard' : '/rental')
      }
    },
    logout() {
      localStorage.removeItem('app_user')
      localStorage.removeItem('app_role_switch')
      this.$router.push('/login')
    }
  },
  mounted() {
    if (this.canSwitchRole && !this.roleSwitch) {
      this.roleSwitch = 'admin'
      localStorage.setItem('app_role_switch', 'admin')
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
}
body {
  margin: 0;
  font-family: "Microsoft YaHei", sans-serif;
  background: linear-gradient(180deg, #eef5ff 0%, #f7faff 100%);
}
.app-shell {
  min-height: 100vh;
}
.topbar {
  background: linear-gradient(90deg, #d7e8fc 0%, #c5ddfb 45%, #b7d6ff 100%);
  color: #244466;
  height: 64px !important;
  display: flex;
  align-items: center;
  padding: 0 22px;
  box-shadow: 0 8px 24px rgba(64, 114, 178, 0.16);
  border-bottom: 1px solid #d3e5fb;
}
.brand {
  font-size: 19px;
  font-weight: 600;
  min-width: 360px;
  color: #1f3f63;
}
.top-menu {
  flex: 1;
  margin-left: 20px;
  background: transparent;
  border-bottom: 0;
}
.top-menu .el-menu-item {
  color: #355c87 !important;
  height: 64px !important;
  line-height: 64px !important;
  border-bottom: 2px solid transparent !important;
}
.top-menu .el-menu-item.is-active {
  color: #1c4f86 !important;
  border-bottom-color: #4a90e2 !important;
  background: rgba(255, 255, 255, 0.35) !important;
}
.right-zone {
  min-width: 230px;
  text-align: right;
  color: #345a84;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
.right-zone .el-button--text {
  color: #2d6db3;
}
.role-switch {
  border: 1px solid #aecdff;
  border-radius: 999px;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.55);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.6);
}
.role-switch .el-radio-button__inner {
  border: none !important;
  background: transparent !important;
  color: #3b6290 !important;
  padding: 8px 14px !important;
}
.role-switch .el-radio-button__orig-radio:checked + .el-radio-button__inner {
  color: #fff !important;
  background: linear-gradient(90deg, #5b9df5 0%, #3a84e6 100%) !important;
  box-shadow: none !important;
}
.main-panel {
  padding: 22px;
}
.login-main {
  padding: 0;
}

/* global visual polish */
.el-card {
  border-radius: 12px !important;
  border: 1px solid #e3eefb !important;
  box-shadow: 0 6px 20px rgba(49, 99, 165, 0.08) !important;
}
.el-card__header {
  background: linear-gradient(180deg, #f6faff 0%, #eff6ff 100%);
}
.el-button--primary {
  background: linear-gradient(90deg, #5b9df5 0%, #3a84e6 100%) !important;
  border-color: #3a84e6 !important;
}
.el-table th {
  background: #f1f7ff !important;
  color: #365a82 !important;
}
</style>
