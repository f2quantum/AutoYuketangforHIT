GitHub地址：[https://github.com/xrervip/AutoYuketangforHIT](https://github.com/xrervip/AutoYuketangforHIT)


代码基于 [https://github.com/lingyan12/yuketang](https://github.com/lingyan12/yuketang) 和[https://github.com/xrervip/HIT_auto_report/blob/master/HIT_auto_report.py](https://github.com/xrervip/HIT_auto_report/blob/master/HIT_auto_report.py) 进行修改

**使用方法：**
依赖于python运行环境+chorme+selenium chrome驱动

 1. 安装Chorme浏览器
 2. 下载安装python运行环境+chorme+selenium chrome驱动selenium chrome驱动 镜像地址: [http://npm.taobao.org/mirrors/selenium](http://npm.taobao.org/mirrors/selenium)
 3. 配置`config.json`  ：文件格式如下 在URL中替换为雨课堂（学堂在线）对应课程的`成绩单`页  `https://hit.yuketang.cn/pro/lms/******/*****/score`
 4. 启动python脚本 
 5. 备注：使用参数 CookieMode 可以在`cookie.json` 写入cookie并进行快捷登录

**下一步目标：**

1.增加多线程播放功能
2.提高稳定性和健壮性
3.倍速播放未完善

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200925164844953.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ZyYW5rbGluc19GYW4=,size_16,color_FFFFFF,t_70#pic_center)
  





**config.json**

```c
[{
	"URL":"https://hit.yuketang.cn/pro/lms/8692P78g7Lk/4412088/score"
}]
```


说明：启动使用参数 `CookieMode` 可以在cookie，json 写入cookie并进行快捷登录

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
