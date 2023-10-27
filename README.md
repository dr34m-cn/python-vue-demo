# python-vue-demo
这是一个后端基于python的tornado，前端基于vue使用element-ui框架，简单易用基本框架项目；
内置了用户登录注销修改密码、接口统一处理与拦截等功能，以下介绍本项目的docker启动方式，如需单独启动前后端，可以查看这里[前端文档](./front/README.md)与[后端文档](./server/README.md)。

## 1.前置准备

按需修改`server/config.ini`中的配置;

## 2.构建镜像

`cd`到本项目根目录，然后执行

```shell
docker build -t pv:v1 .
```

## 3. 通过镜像启动容器

```shell
docker run --restart=always -p 9001:9001 -d --name pv pv:v1
```

执行后，会自动启动并运行在`9001`端口，并开机自启

## 4. 启动停止的方式

```shell
docker stop pv # 停止
docker start pv # 启动
docker restart pv # 重启
```