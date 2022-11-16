#!/usr/bin/env python3
from common.config import getconfig
from apis.login_api import login


def getToken():
	# 读取配置
	config = getconfig()
	# 全局token
	cookie = f'auth_key=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzcyOTMyNjAsIm5iZiI6MTYzNzIwNjg0MCwiaWF0IjoxNjM3MjA2ODUwLCJpc3MiOiJhdXRoOiBzcyIsInN1YiI6Im15IHRva2VuIiwiaWQiOiIxNTYxODcxODA2MCIsImRhdGEiOnsidXNlcl9pZCI6IjQ1IiwidXNlcm5hbWUiOiJ6ayIsIm5pY2tuYW1lIjoiXHU4ZDc1XHU1MWVmIiwiZW1haWwiOiJ6a0BxbWFpLmNuIiwiaXNfc3VwZXJ1c2VyIjpmYWxzZX19.3uH5zBj1ftxVvLdnE5QU7wRMlAskB4ZW_CBdM-CFd8A;'
	# 登录账号
	username = config['login']['username']
	# 登录密码
	password = config['login']['password']
	# 主逻辑
	auth_key = login(username, password)
	# 替换全局token
	cookie = f'auth_key={auth_key}'
	return cookie