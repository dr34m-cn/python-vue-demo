from common import commonUtils
from mapper import userMapper


def getUser(userId, userName=None):
    """
    通过用户名获取用户信息
    :param userId: 用户id
    :param userName: 用户名
    :return: 用户信息
    """
    users = userMapper.getUserByName(userName) if not userId else userMapper.getUserById(userId)
    if users:
        return users[0]
    else:
        raise Exception("用户不存在")


def checkPwd(userId, passwd, userName=None):
    """
    检查密码是否正确
    :param userId: 用户id
    :param passwd: 密码
    :param userName: 用户名
    :return: 用户信息
    """
    user = getUser(userId, userName)
    if commonUtils.passwd2md5(passwd) == user['passwd']:
        return user
    else:
        raise Exception("密码错误")


def resetPasswd(userId, passwd, oldPasswd):
    """
    重置密码
    :param userId: 用户id
    :param passwd: 新密码
    :param oldPasswd: 旧密码
    """
    checkPwd(userId, oldPasswd)
    userMapper.resetPasswd(userId, commonUtils.passwd2md5(passwd))
