#!/usr/bin/env python3
import os
import yaml

def getconfig():
	# 获取脚本所在目录
	base_path = os.path.split(os.path.realpath(__file__))[0]
	# 读取配置
	yamlPath = base_path + '/../config.yaml'
	with open(yamlPath, "r") as stream:
		try:
		    config = yaml.safe_load(stream)
		except yaml.YAMLError as exc:
		    print(exc)
		    exit("读取配置失败")
	return config