# auto_12306  
第一步：可能需要安装的python包：requests，selenium  
第二步：安装selenium webdriver 驱动，这里以chrome浏览器为例
chromedriver下载地址：  
http://chromedriver.storage.googleapis.com/index.html  
http://npm.taobao.org/mirrors/chromedriver/  
下载对应版本的chromedriver，下载对应浏览器版本解压后，把exe文件复制到浏览器的安装目录下：C:\Program Files (x86)\Google\Chrome\Application（要根据自己实际安装目录）  
把exe文件复制到python的安装目录下，可以在自己的编辑器中查看python.exe位置，与之放在同一文件夹下  
配置环境变量:此电脑→右击属性→高级系统设置→环境变量→用户变量→Path→编辑→新建，将以下路径复制,然后不要忘记后续全部点击确定  
第三步：  
更新get_ticket.py中的账号和密码  
更新auto_12306.py中的12306对应查票网站Cookie  
运行auto_12306.py即可爬虫和购票
