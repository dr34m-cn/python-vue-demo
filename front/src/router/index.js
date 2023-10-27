import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from '@/views/layout.vue'

const originalPush = VueRouter.prototype.push

VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

Vue.use(VueRouter)

const routes = [{
		path: '/',
		name: '缓冲页',
		meta: {
			letfIndex: ''
		},
		component: () => import('@/views/index')
	},
	{
		path: '/login',
		name: '登录',
		meta: {
			letfIndex: ''
		},
		component: () => import('@/views/Login')
	},
	{
		path: '/home',
		component: Layout,
		children: [{
			path: '',
			component: () => import('@/views/page/home/index'),
			name: '主页',
			meta: {
				letfIndex: 'home'
			}
		}]
	},
	{
		path: '/user',
		component: Layout,
		children: [{
			path: '',
			component: () => import('@/views/page/user/index'),
			name: '用户管理',
			meta: {
				letfIndex: 'user'
			}
		}]
	}
]

const router = new VueRouter({
	mode: 'history',
	routes
})

export default router