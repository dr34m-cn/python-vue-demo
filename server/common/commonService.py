import datetime
import json
import logging
import os


# 日志规定
def get_logger(level_int):
    level_list = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
    level = level_list[level_int]
    logger = logging.getLogger()
    logger.setLevel(level)
    if not os.path.exists('log'):
        os.mkdir('log')

    # 创建一个handler，用于写入日志文件
    log_file = 'log/sys_%s.log' % datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
    fh = logging.FileHandler(log_file, encoding='utf-8')
    fh.setLevel(level)

    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    fh.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    return logger


def get_post_data(self):
    post_data = self.request.arguments
    post_data = {x: post_data.get(x)[0].decode("utf-8") for x in post_data.keys()}
    if not post_data:
        post_data = self.request.body.decode('utf-8')
        if post_data and post_data != '':
            post_data = json.loads(post_data)
        else:
            post_data = {}
    return post_data


def result_map(*dt):
    # code：200-成功，500-失败
    # 成功 ResultMap() or ResultMap(data) or ResultMap(msg, 200)
    # 失败 ResultMap(msg, 500)
    result = {"data": dt[0] if len(dt) == 1 else None, "code": 200 if len(dt) <= 1 else dt[1],
              "msg": "操作成功" if len(dt) <= 1 else dt[0]}
    return json.dumps(result, ensure_ascii=False)
