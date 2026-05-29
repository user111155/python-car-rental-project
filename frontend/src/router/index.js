import Vue from 'vue'
import Router from 'vue-router'// 导入 Vue Router 路由插件，用来管理页面的跳转。就像后端的 Blueprint 蓝图工具，用来组织所有的页面
import LoginView from '../views/LoginView.vue'// 导入所有的业务页面组件
import RequirementView from '../views/RequirementView.vue'
import RecommendView from '../views/RecommendView.vue'
import DataManageView from '../views/DataManageView.vue'
import RentalView from '../views/RentalView.vue'
import AdminView from '../views/AdminView.vue'
import MyBookingsView from '../views/MyBookingsView.vue'
import BigScreenView from '../views/BigScreenView.vue'

Vue.use(Router)// 把 Router 插件注册到 Vue 应用，这样整个应用都能使用路由功能了
// 获取当前登录的用户信息，从浏览器的 localStorage 里读。localStorage 是浏览器的本地存储，用来保存用户的登录状态，这样刷新页面用户不会退出登录
const getCurrentUser = () => {
  const user = localStorage.getItem('app_user')
  return user ? JSON.parse(user) : null
}
const normalizeRole = user => {// 标准化用户的角色，把各种不同写法的管理员角色，统一转成 'admin'
  if (!user) return 'guest'
  const role = (user.role || '').toString().trim().toLowerCase()
  const username = (user.username || '').toString().trim().toLowerCase()
  if (role === 'admin' || role === 'administrator' || role === '管理员' || username === 'admin') {
    return 'admin'
  }
  return 'user'
}
const getCurrentRole = () => {// 获取当前用户的实际角色，支持管理员切换角色
  const user = getCurrentUser()
  if (!user) {
    return 'guest'
  }
  const normalizedRole = normalizeRole(user)
  if (normalizedRole === 'admin') {
    const roleSwitch = localStorage.getItem('app_role_switch')
    if (roleSwitch === 'user' || roleSwitch === 'admin') {
      return roleSwitch
    }
  }
  return normalizedRole
}
const getDefaultPathByRole = role => (role === 'admin' ? '/dashboard' : '/rental')// 根据用户的角色，返回默认的首页

const router = new Router({
  mode: 'hash',
  routes: [
    { path: '/', redirect: () => (getCurrentUser() ? getDefaultPathByRole(getCurrentRole()) : '/login') },
    { path: '/login', component: LoginView, meta: { guestOnly: true } },// 登录页面，只有游客（没登录的用户）才能访问
    { path: '/rental', component: RentalView, meta: { roles: ['user'] } },// 普通用户的页面，只有普通用户才能访问
    { path: '/bookings', component: MyBookingsView, meta: { roles: ['user'] } },
    { path: '/requirements', component: RequirementView, meta: { roles: ['user'] } },
    { path: '/recommend', component: RecommendView, meta: { roles: ['user'] } },
    { path: '/data', component: DataManageView, meta: { roles: ['admin'] } }, // 管理员的页面，只有管理员才能访问
    { path: '/admin', component: AdminView, meta: { roles: ['admin'] } },
    { path: '/dashboard', component: BigScreenView, meta: { roles: ['admin'] } }
  ]
})
// 路由守卫，每次用户跳转页面前，都会先执行这个函数，用来做权限校验
// 就像后端的接口权限校验，保证用户只能访问自己有权限的页面
router.beforeEach((to, from, next) => {
  const user = getCurrentUser()
  if (!user && to.path !== '/login') {
    next('/login')
    return
  }

  if (user && to.meta.guestOnly) {
    next(getDefaultPathByRole(user.role))
    return
  }

  const role = getCurrentRole()
  const allowRoles = to.meta.roles

  if (!allowRoles || allowRoles.includes(role)) {
    next()
    return
  }

  next(getDefaultPathByRole(role))
})

export default router
