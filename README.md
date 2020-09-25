使用方法：
代码基于 [https://github.com/lingyan12/yuketang](https://github.com/lingyan12/yuketang) 和[https://github.com/xrervip/HIT_auto_report/blob/master/HIT_auto_report.py](https://github.com/xrervip/HIT_auto_report/blob/master/HIT_auto_report.py) 进行修改
依赖于python运行环境+chorme+selenium chrome驱动
selenium chrome驱动 镜像地址: [http://npm.taobao.org/mirrors/selenium](http://npm.taobao.org/mirrors/selenium)

说明：使用参数 CookieMode 可以在cookie，json 写入cookie并进行快捷登录

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
