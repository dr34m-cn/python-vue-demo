FROM python:3.11.6-alpine3.18 AS python-builder

WORKDIR /app

COPY ./server ./

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
    && apk add binutils \
    && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install -r requirements.txt \
    && pip install pyinstaller \
    && pyinstaller -F main.py

FROM node:16.20.2-alpine3.18 AS node-builder

WORKDIR /app

COPY ./front ./

RUN npm config set registry https://registry.npmmirror.com \
    && npm install \
    && npm run build

FROM nginx:1.25.3-alpine3.18

WORKDIR /app

COPY --from=python-builder /app/dist/main .
COPY --from=node-builder /app/dist/ ./front/
COPY ./server/config.ini .
COPY ./python-web.conf /etc/nginx/conf.d/

CMD nginx && ./main