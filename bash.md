
打开环境
```angular2html
source activate learn;
```

关闭gunicorn
```
pstree -ap|grep gunicorn
kill -9 pid
```

部署服务器
```
 gunicorn -w 3 -b 0.0.0.0:5000 app:app
```