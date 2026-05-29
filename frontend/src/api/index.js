import axios from 'axios'// 导入 axios 库，这是前端用来发送 HTTP 请求的工具，负责帮我们把请求发给后端，处理响应

const request = axios.create({// 创建 axios 的请求实例，统一配置所有的请求
  baseURL: '/api',// 所有请求的基础前缀，也就是说，所有接口的路径，都会自动加上 /api 前缀
  timeout: 8000 // 请求超时时间，如果8秒内后端没响应，就自动报错
})

export const login = data => request.post('/auth/login', data)// 登录接口，对应后端 auth.py 里的 /auth/login 接口
export const register = data => request.post('/auth/register', data)

export const getRequirements = params => request.get('/requirements/', { params })
export const createRequirement = data => request.post('/requirements/', data)
export const updateRequirement = (id, data) => request.put(`/requirements/${id}`, data)

export const getCars = () => request.get('/data/cars')
export const getUsers = () => request.get('/data/users')
export const getOrders = () => request.get('/data/orders')

export const getRecommend = data => request.post('/recommend/', data)

export const getRentalCars = () => request.get('/rental/cars')
export const createBooking = data => request.post('/rental/book', data)
export const previewRentalPayment = data => request.post('/rental/payment/preview', data)
export const payRentalBooking = data => request.post('/rental/payment/pay', data)
export const getRentalOrders = params => request.get('/rental/orders', { params })
export const pickupOrder = id => request.put(`/rental/pickup/${id}`)
export const returnOrder = id => request.put(`/rental/return/${id}`)

export const getAdminOrders = () => request.get('/admin/orders')
export const getAdminInventory = () => request.get('/admin/inventory')
export const getAdminStats = () => request.get('/admin/stats')
export const getAdminUsers = () => request.get('/admin/users')
export const createAdminUser = data => request.post('/admin/users', data)
export const updateAdminUser = (id, data) => request.put(`/admin/users/${id}`, data)
export const deleteAdminUser = id => request.delete(`/admin/users/${id}`)
export const getAdminCars = () => request.get('/admin/cars')
export const deleteAdminCar = id => request.delete(`/admin/cars/${id}`)
export const getAdminOrderList = () => request.get('/admin/orders/all')
export const updateAdminOrderStatus = (id, data) => request.put(`/admin/orders/${id}/status`, data)
export const updateAdminCarStatus = (id, data) => request.put(`/admin/cars/${id}/status`, data)
export const getAdminRequirementStats = () => request.get('/admin/requirements/stats')
