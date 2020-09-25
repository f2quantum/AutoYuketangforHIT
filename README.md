GitHub地址：[https://github.com/xrervip/AutoYuketangforHIT](https://github.com/xrervip/AutoYuketangforHIT)


代码基于 [https://github.com/lingyan12/yuketang](https://github.com/lingyan12/yuketang) 和[https://github.com/xrervip/HIT_auto_report/blob/master/HIT_auto_report.py](https://github.com/xrervip/HIT_auto_report/blob/master/HIT_auto_report.py) 进行修改


**使用方法：**
依赖于python运行环境+chorme+selenium chromedriver驱动

 1. 安装Chorme浏览器
 2. 下载安装**python运行环境**+**selenium 包**+ **chromedriver驱动**    selenium可以直接可以用pip安装。`pip install selenium` 。chormedriver 镜像地址: [https://npm.taobao.org/mirrors/chromedriver/](https://npm.taobao.org/mirrors/chromedriver/) 寻找对应您的chrome浏览器的版本即可，解压后将`chromedriver.exe`文件放在chrome浏览器根目录，也就是`chrome.exe`同目录下，同时需要将该目录添加到`环境变量`里 [第二步教程](https://www.cnblogs.com/lfri/p/10542797.html)
 4. 配置`config.json`  ：文件格式如在**附录2** 在URL中替换为雨课堂（学堂在线）对应课程的`成绩单`页，例如： **附录1** `https://hit.yuketang.cn/pro/lms/******/*****/score`
 5. 启动python脚本 
 6. 备注：使用参数 CookieMode 可以在**附录3**`cookie.json` 写入cookie并进行快捷登录（非必须）

**下一步目标：**

1.增加多线程播放功能
2.提高稳定性和健壮性
3.倍速播放未完善

---
## 附录1：网页页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200925164844953.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ZyYW5rbGluc19GYW4=,size_16,color_FFFFFF,t_70#pic_center)
  



---
## 附录2：config.json
在URL中替换为雨课堂（学堂在线）对应课程的链接即可
**config.json**

```c
[{
	"URL":"https://hit.yuketang.cn/pro/lms/8692P78g7Lk/4412088/score"
}]
```


说明：启动使用参数 `CookieMode` 可以在cookie，json 写入cookie并进行快捷登录

---
## 附录3：cookie.json
以下内容非必须，一般用户通过扫码登录即可


**cookie.json:**

```json
[{
		"domain": "hit.yuketang.cn",
		"name": "sessionid",
		"path": "/",
		"value": "替换为数值"
	},
	{
		"domain": "hit.yuketang.cn",
		"name": "csrftoken",
		"path": "/",
		"value": "替换为数值"
	},
	{
		"domain": "hit.yuketang.cn",
		"name": "platform_id",
		"path": "/",
		"value": "替换为数值"
	},
	{
		"domain": "hit.yuketang.cn",
		"name": "university_id",
		"path": "/",
		"value": "替换为数值"
	},
	{
		"domain": "hit.yuketang.cn",
		"name": "user_role",
		"path": "/",
		"value": "替换为数值"
	}
]
```
---

## 附录4：如何获取Cookie?
这里谈一个比较简单但是繁琐的方法
 ### 1.首先在浏览器地址栏旁边点击这个按钮 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200925171529155.png#pic_center)
### 2.点击Cookie
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200925171658840.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ZyYW5rbGluc19GYW4=,size_16,color_FFFFFF,t_70#pic_center)
### 3.获取Cookie
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200925171727355.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ZyYW5rbGluc19GYW4=,size_16,color_FFFFFF,t_70#pic_center)
然后将域名下Cookie文件夹中的几个cookie获取下来，将`内容`中的数值（`fzbYQfMAyui8j0CQRRaPze0fFA1emawT`）填写到上面 `cookie.json` 中 的`"value": "替换为数值"`



