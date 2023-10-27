<template>
	<div class="user">
		<template v-if="vuex_userInfo">
			<div class="item">
				<div class="label">用户名</div>
				<div class="value">{{vuex_userInfo.userName}}</div>
			</div>
			<div class="item">
				<div class="label">角色</div>
				<div class="value">{{vuex_userInfo.role}}</div>
			</div>
			<div class="item">
				<div class="label">创建时间</div>
				<div class="value">{{vuex_userInfo.createTime | timeStampFilter}}</div>
			</div>
			<el-form :model="resetForm" :rules="rules" ref="resetForm" label-width="0">
				<el-form-item prop="oldPasswd">
					<el-input style="width: 200px;" class="input" placeholder="请输入旧密码" show-password
						v-model="resetForm.oldPasswd"></el-input>
				</el-form-item>
				<el-form-item prop="passwd">
					<el-input style="width: 200px;" placeholder="请输入新密码" show-password v-model="resetForm.passwd"
						show-password></el-input>
				</el-form-item>
				<el-form-item prop="passwd2">
					<el-input style="width: 200px;" placeholder="确认新密码" show-password v-model="resetForm.passwd2"
						show-password @keyup.enter.native="resetPasswd"></el-input>
				</el-form-item>
			</el-form>
			<el-button type="primary" style="width: 200px;" :loading="loading" @click="resetPasswd">修改密码</el-button>
		</template>
	</div>
</template>

<script>
	import {
		resetPwd
	} from "@/api/user";
	export default {
		name: 'User',
		data() {
			var validatePass2 = (rule, value, callback) => {
				if (value == '' || value == null) {
					callback(new Error('请再次输入密码'));
				} else if (value !== this.resetForm.passwd) {
					callback(new Error('两次输入密码不一致!'));
				} else {
					callback();
				}
			};
			return {
				resetForm: {
					oldPasswd: null,
					passwd: null,
					passwd2: null
				},
				loading: false,
				rules: {
					oldPasswd: [{
						required: true,
						message: '请输入旧密码',
						trigger: 'blur'
					}],
					passwd: [{
						required: true,
						message: '请输入新密码',
						trigger: 'blur'
					}],
					passwd2: [{
						validator: validatePass2,
						trigger: 'blur'
					}]
				}
			};
		},
		created() {},
		methods: {
			resetPasswd() {
				this.$refs.resetForm.validate((valid) => {
					if (valid) {
						this.loading = true;
						resetPwd(this.resetForm).then(res => {
							this.$message({
								message: res.msg,
								type: 'success'
							});
							this.$refs.resetForm.resetFields();
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
	.user {
		padding: 40px 80px;
		font-size: 16px;

		.item {
			display: flex;
			margin-bottom: 12px;

			.label {
				width: 70px;
				text-align: justify;
				margin-right: 40px;
			}

			.label::after {
				display: inline-block;
				width: 100%;
				content: "";
			}
		}
	}
</style>