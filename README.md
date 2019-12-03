# EasierSpider介绍
最近做了一些爬虫项目，发现有很多模块可以抽取出来的，
于是就把一些业务逻辑抽离掉，剩个骨架，
便有了这个简单（简陋）爬虫框架，希望这个项目能帮助到一些要做很小型爬虫的人。



# 技术选型
运行系统：Windows\Linux

开发语言：Pyhton 3.X

数据库：MySQL


# 功能介绍
- 日志记录
- 执行异常报警
    - 邮件
    - 短信
- 常用配置文件读写
    - MySQL
    - Token
    - 账户
- mysql连接函数封装
- 常用工具类封装
    - 获取项目根目录
    - 文件操作类
    - 字符编码类
    - 版本对比
    - json操作


# 使用流程
在根目录的app.py上编写你的爬虫程序，调用编写好的函数完成你的功能即可。


# 项目目录介绍
- config 项目配置
- download 下载到的文件，保存在这个目录
- logs 日志保存的地方，默认保存7日内的日志
- sonspider 编写子爬虫目录
- tools工具类
    - alert.py 报警、通信工具
    - common.py 常用工具
    - file_tool.py 文件操作工具
    - json_tool.py json操作工具
    - log.py 日志操作工具
    - mySQLdb.py mysql连接工具
    - transcoding_tool.py 字符转换工具
- app1.py 爬虫1
- app2.py 爬虫2
- getRootPath.py 获取根目录的工具函数


# crontab 定时规则记录
```linux
# 每天12:00点执行一次脚本
0 12 * * * /etc/anaconda3/bin/python3 /home/mysticbinary/code/EasierSpider/app1.py >>app1.py.log 2>&1 &
```



