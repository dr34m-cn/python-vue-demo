import time

from common import commonUtils
from common import sqlBase
from common.config import CONFIG


@sqlBase.connect_sql
def init_sql(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE name='user_list'")
    if cursor.fetchone() is None:
        timeNow = int(time.time())
        cursor.execute("create table user_list("
                       "id integer primary key autoincrement,"
                       "userName text,"         # 用户名
                       "role text,"             # 角色(admin/guest)
                       "passwd text,"           # 密码
                       "createTime integer"     # 创建时间（秒级时间戳）
                       ")")
        cursor.execute("insert into user_list(userName, passwd, role, createTime) values (?, ?, ?, ?)",
                       (CONFIG['init']['user'], commonUtils.passwd2md5(CONFIG['init']['passwd']), 'admin', timeNow))
        cursor.execute("insert into user_list(userName, passwd, role, createTime) values (?, ?, ?, ?)",
                       (CONFIG['init']['guestUser'], commonUtils.passwd2md5(CONFIG['init']['guestPasswd']), 'guest', timeNow))
        conn.commit()
    cursor.close()
