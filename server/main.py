import asyncio
import json

from tornado.web import RequestHandler, Application

from common import commonService as CS, sqlInit
from common.config import CONFIG
from service import userService

# 初始化日志
logger = CS.get_logger(1)
# 后端配置
server = CONFIG['server']


class BaseHandler(RequestHandler):
    def get_current_user(self):
        return json.loads(self.get_signed_cookie("user"))


def handle_request(func):
    def wrapper(self):
        uri = self.request.uri
        user = self.get_signed_cookie("user")
        if not uri.startswith('/svr/noAuth') and user is None:
            self.clear_cookie("user")
            msg = CS.result_map("请登录", 401)
        else:
            try:
                req = CS.get_post_data(self)
                if user:
                    req['__user'] = userService.getUser(json.loads(user)['id'], None)
                msg = CS.result_map(func(self, req))
            except Exception as e:
                msg = CS.result_map(str(e), 500)
                logger.exception(e)
        self.write(msg)

    return wrapper


class Login(BaseHandler):
    @handle_request
    def post(self, req):
        user = userService.checkPwd(None, req['passwd'], req['userName'])
        del user['passwd']
        self.set_signed_cookie("user", json.dumps(user, ensure_ascii=False), expires_days=int(server['cookieExpiresDays']))
        return user

    @handle_request
    def delete(self, req):
        self.clear_cookie("user")


class User(BaseHandler):
    @handle_request
    def get(self, req):
        return req['__user']

    @handle_request
    def put(self, req):
        user = json.loads(self.get_signed_cookie("user"))
        userService.resetPasswd(user['id'], req['passwd'], req['oldPasswd'])


def make_app():
    # 初始化数据库，没有则创建
    sqlInit.init_sql()
    # 以/svr/noAuth开头的请求无需鉴权，例如登录等
    return Application([
        (r"/svr/noAuth/login", Login),
        (r"/svr/user", User)
    ], cookie_secret=server['passwdStr'])


async def main():
    app = make_app()
    app.listen(server['port'])
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
