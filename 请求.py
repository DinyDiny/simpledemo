#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests,json
# 接口的url
url = ""
# 接口头部信息
headers = {
	"Accept": "*/*",
	"Accept-Encoding": "gzip, deflate, br",
	"Content-Type": "application/json"
}
# 接口的参数
params = {
    "index": "1"
}
# 发送接口
r = requests.request("get", url, headers=headers, params=params)
r = r.json()
js = json.dumps(r, indent=4, separators=(',', ': '), ensure_ascii=False)
# 打印返回结果
print(js)

