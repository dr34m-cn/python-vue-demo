<template>
	<div class="layout">
		<div class="lay-left">
			<el-menu :default-active="vuex_letfIndex" :router="true" :collapse="isCollapse" class="lay-left-menu">
				<el-menu-item :index="item.index" v-for="item in menuList">
					<i :class="`el-icon-${item.icon}`"></i>
					<span slot="title">{{item.title}}</span>
				</el-menu-item>
			</el-menu>
		</div>
		<div class="lay-right">
			<div class="lay-right-top">
				<div class="top-left">
					<div class="top-icon can-click" @click="isCollapse = !isCollapse">
						<i :class="isCollapse ? 'el-icon-s-unfold' : 'el-icon-s-fold'"></i>
					</div>
					<div style="margin-left: 10px;">{{ currentTime }}</div>
				</div>
				<div class="top-right">
					<div class="top-icon can-click" @click="fullScreen()">
						<i class="el-icon-full-screen"></i>
					</div>
					<div class="btn-item can-click" @click="toUser()">
						<div class="top-icon">
							<i class="el-icon-user"></i>
						</div>
						<span>{{vuex_userInfo ? vuex_userInfo.userName : '--'}}</span>
					</div>
					<div class="btn-item can-click" @click="logout()">
						<div class="top-icon">
							<i class="el-icon-switch-button"></i>
						</div>
						<span>退出登录</span>
					</div>
				</div>
			</div>
			<div class="lay-right-bottom" v-loading="vuex_loading"
				:style="`width: calc(100vw - ${isCollapse ? 64 : 140}px);`">
				<router-view />
			</div>
		</div>

	</div>
</template>
<script>
	import {
		logout
	} from "@/api/user";
	import {
		parseTime
	} from "@/utils/utils";
	export default {
		data() {
			return {
				isCollapse: false,
				menuList: [{
					index: 'home',
					title: '主页',
					icon: 'pie-chart'
				}, {
					index: 'user',
					title: '用户管理',
					icon: 'user'
				}],
				currentTime: '2023-10-10 00:00:00',
				timer: null
			};
		},
		created() {
			this.init();
		},
		beforeDestroy() {
			if (this.timer) {
				clearInterval(this.timer);
			}
		},
		methods: {
			init() {
				if (!this.vuex_userInfo) {
					this.logout();
				}
				this.getCurrentTime();
				this.timer = setInterval(() => {
					this.getCurrentTime();
				}, 1000);
			},
			getCurrentTime() {
				this.currentTime = parseTime(new Date());
			},
			fullScreen() {
				if (document.fullscreenElement) {
					document.exitFullscreen();
				} else {
					document.documentElement.requestFullscreen();
				}
			},
			toUser() {
				this.$router.push('/user');
			},
			logout() {
				logout().then(res => {
					this.$router.push('/login');
					this.$setVuex('vuex_userInfo', null);
				})
			},
			toIndex() {
				this.$router.push('/');
			}
		}
	}
</script>
<style lang="scss" scoped>
	.layout {
		position: fixed;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		display: flex;
		background-color: #191b2b;
		color: #FFFFFF;

		.lay-left {
			background-color: #001529;

			.lay-left-menu {
				height: 100%;
			}

			.lay-left-menu:not(.el-menu--collapse) {
				width: 140px;
			}
		}

		.lay-right {
			width: 100%;
			height: 100%;

			.lay-right-top {
				height: 50px;
				display: flex;
				justify-content: space-between;
				align-items: center;
				border-bottom: 1px solid #333333;
				font-size: 16px;

				.top-icon {
					height: 50px;
					width: 50px;
					display: flex;
					align-items: center;
					justify-content: center;
					font-size: 26px;
				}

				.can-click {
					cursor: pointer;
				}

				.can-click:hover {
					background-color: #393c4f;
				}

				.top-left {
					display: flex;
					align-items: center;
				}

				.top-right {
					display: flex;
					align-items: center;

					.btn-item {
						display: flex;
						align-items: center;
						padding-right: 20px;
						cursor: pointer;
					}
				}
			}

			.lay-right-bottom {
				height: calc(100% - 51px);
				overflow-y: auto;
				transition: width .3s ease-in-out;
			}
		}
	}
</style>