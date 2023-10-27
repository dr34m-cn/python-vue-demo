<template>
	<div class="login">
		<div class="loginArea">
			<div class="title">登录</div>
			<el-form :model="loginForm" :rules="rules" ref="loginForm" label-width="0">
				<el-form-item prop="userName">
					<el-input class="input" placeholder="请输入用户名" prefix-icon="el-icon-user" v-model="loginForm.userName"></el-input>
				</el-form-item>
				<el-form-item prop="passwd">
					<el-input placeholder="请输入密码" prefix-icon="el-icon-lock" v-model="loginForm.passwd" show-password
						@keyup.enter.native="login"></el-input>
				</el-form-item>
			</el-form>
			<el-button style="width: 100%;" type="primary" :loading="loading" @click="login">登录</el-button>
		</div>
	</div>
</template>

<script>
	import {
		login
	} from "@/api/user";
	export default {
		name: 'Login',
		data() {
			return {
				loginForm: {
					userName: null,
					passwd: null
				},
				loading: false,
				rules: {
					userName: [{
						required: true,
						message: '请输入用户名',
						trigger: 'blur'
					}],
					passwd: [{
						required: true,
						message: '请输入密码',
						trigger: 'blur'
					}]
				}
			};
		},
		created() {},
		methods: {
			login() {
				this.$refs.loginForm.validate((valid) => {
					if (valid) {
						this.loading = true;
						login(this.loginForm).then(res => {
							this.$setVuex('vuex_userInfo', res.data);
							this.$router.replace('/home');
							this.loading = false;
						}).catch(err => {
							this.loading = false;

						})
					} else {
						return false;
					}
				});
			}
		}
	}
</script>
<style lang="scss" scoped>
	.login {
		display: flex;
		justify-content: center;
		align-items: center;
		position: fixed;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		background-color: #191b2b;
		color: #FFFFFF;

		.loginArea {
			background-color: #001529;
			width: 360px;
			padding: 40px 30px;
			border-radius: 4px;

			.title {
				font-size: 18px;
				font-weight: 700;
				text-align: center;
				margin-bottom: 30px;
			}
		}
	}
</style>