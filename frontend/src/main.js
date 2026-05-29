import Vue from 'vue'// 导入 Vue 框架的核心库，这是整个前端应用的基础
import ElementUI from 'element-ui'// 导入 ElementUI 组件库，按钮、表单、弹窗、表格这些UI组件
import 'element-ui/lib/theme-chalk/index.css'// 导入 ElementUI 的CSS样式文件，UI组件必须要有样式才能正常显示
import App from './App.vue'//导入根组件 App.vue，这是整个前端应用的根容器，所有的页面都会渲染到这个根组件里
import router from './router'// 导入我们刚要学的 router 路由配置

Vue.use(ElementUI)// 把 ElementUI 注册到 Vue 应用
Vue.config.productionTip = false
// 创建 Vue 应用实例，启动整个应用
new Vue({
  router,// 把路由配置注入到整个应用，这样所有页面都能使用路由功能了
  render: h => h(App)// 把根组件 App.vue 渲染出来
}).$mount('#app')// 把整个应用，挂载到HTML页面上的 id="app" 的div元素。浏览器加载完HTML后，Vue会把我们写的所有页面，渲染到这个div里，页面就显示出来了
