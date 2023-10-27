from common import sqlBase


def getUserByName(name):
    return sqlBase.fetchall_to_table("select * from user_list where userName = ?", (name,))


def getUserById(userId):
    return sqlBase.fetchall_to_table("select * from user_list where id = ?", (userId,))


def resetPasswd(userId, passwd):
    sqlBase.execute_update("update user_list set passwd = ? where id = ?", (passwd, userId))
