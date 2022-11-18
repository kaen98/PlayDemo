#!/usr/bin/env python3
import time
import requests
from common.config import getconfig

# 登录token
config = getconfig()
authorization = config['login']['authorization']

def savePlay(course_id, cid, play_timestamp, play_duration, type):
  url = "https://skills-api.kjcxchina.com/api/v1/saveStudy"

  # payload = f'course_id=3275&cid=27529&play_duration=7940&type=0&play_timestamp={play_timestamp}'
  payload = f'course_id={course_id}&cid={cid}&play_timestamp={play_timestamp}&play_duration={play_duration}&type={type}'
  headers = {
    'authority': 'skills-api.kjcxchina.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': f'{authorization}',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://skills.kjcxchina.com',
    'referer': 'https://skills.kjcxchina.com/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  return response

def studyOne(cid):
  url = f'https://skills-api.kjcxchina.com/api/v1/studyOne?cid={cid}'
  payload = {}
  headers = {
    'authority': 'skills-api.kjcxchina.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': f'{authorization}',
    'origin': 'https://skills.kjcxchina.com',
    'referer': 'https://skills.kjcxchina.com/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  return response

def trainingPlan():
  url = "http://skills-api.kjcxchina.com/api/v1/trainingPlan"
  payload = {}
  headers = {
    'authority': 'skills-api.kjcxchina.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': f'{authorization}',
    'origin': 'https://skills.kjcxchina.com',
    'referer': 'https://skills.kjcxchina.com/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  return response

def coursesDetail(id, chapter_id):
  url = f'http://skills-api.kjcxchina.com/api/v1/coursesDetail?id={id}&key=&chapter_id={chapter_id}'
  payload = {}
  headers = {
    'authority': 'skills-api.kjcxchina.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': f'{authorization}',
    'origin': 'https://skills.kjcxchina.com',
    'referer': 'https://skills.kjcxchina.com/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  return response

def classCourseFinish(course_id):
  url = "https://skills-api.kjcxchina.com/api/v1/classCourseFinish"
  payload = f'course_id={course_id}'
  headers = {
    'authority': 'skills-api.kjcxchina.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9za2lsbHMtYXBpLmtqY3hjaGluYS5jb21cL2FwaVwvdjFcL2F1dGhvcml6YXRpb25zIiwiaWF0IjoxNjY4NzU0MDE4LCJleHAiOjE2NzEzNDYwMTgsIm5iZiI6MTY2ODc1NDAxOCwianRpIjoiWDQxMTlRTzRCZGNib1pEUyIsInN1YiI6MTAxOTcwMywicHJ2IjoiZjY0ZDQ4YTZjZWM3YmRmYTdmYmY4OTk0NTRiNDg4YjNlNDYyNTIwYSJ9.1cEblLJCssvoFxmZR9OBv0T-D76-DbWJ-yT39G8vYTk',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://skills.kjcxchina.com',
    'referer': 'https://skills.kjcxchina.com/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  return response


def getKey(prefix, k1, k2):
  return prefix + '-' + str(k1) + '-' + str(k2)

def toPlay(course_id, cid, play_timestamp, play_duration, type):
  while play_timestamp < play_duration:
    response = savePlay(course_id, cid, play_timestamp, play_duration, type)
    print(response.json())
    if 'data' not in response.json():
      print("savePlay返回数据: data 不存在")
      break
    if 'finish' not in response.json()['data']:
      print("savePlay返回数据: finish 不存在")
      break
    finish = response.json()['data']['finish']
    print("播放进度:" + finish + "%")
    if finish == '100':
      print("播放")
      break
    time.sleep(10)
    play_timestamp = play_timestamp + 10

def toPlayV2(course_id, cid, play_timestamp, play_duration, type):
  while 1:
    response = savePlay(course_id, cid, play_timestamp, play_duration, type)
    print(response.json())
    if 'data' not in response.json():
      print("savePlay返回数据: data 不存在")
      break
    if 'finish' not in response.json()['data']:
      print("savePlay返回数据: finish 不存在")
      break
    finish = response.json()['data']['finish']
    print("播放进度:" + finish + "%")
    if finish == '100':
      print("播放结束")
      break
    time.sleep(10)

def speedPlay():
  # 扫描未完成数据, 加入任务队列
  trainingPlanJson = trainingPlan().json()
  chapters = trainingPlanJson[0]['chapter']
  for chapter in chapters:
    print(chapter)
    course_id = chapter['course_id']
    chapter_id = chapter['chapter_id']
    # 已完成的课, 不继续播放
    if (chapter['finish'] == '已完成'):
      continue
    # 拉取视频信息
    coursesDetailJson = coursesDetail(course_id, chapter_id).json()
    videoParame = coursesDetailJson['data']['videoParame']
    play_duration = round(videoParame['VideoMeta']['Duration'] / 10)
    if play_duration > 300:
      play_duration = 300
    play_title = videoParame['VideoMeta']['Title']
    print("课程名:" + play_title)
    print("课程时长:" + str(videoParame['VideoMeta']['Duration']) + "秒")
    print("压缩至:" + str(play_duration) + "秒")
    print(".")
    print(".")
    print(".")
    # studyOne 拉取断点
    studyOneJson = studyOne(chapter_id).json()
    playTimestamp = studyOneJson['data']['play_timestamp']
    if playTimestamp >= play_duration:
      play_duration = playTimestamp + 100
    # savePlay 开始保存播放点
    print(play_title + " - 播放开始")
    toPlay(course_id, chapter_id, playTimestamp + 1, play_duration, 0)
    print(play_title + " - 播放完毕")
    print()
    print()
    print()


# 时长检查
def checkClassCourseFinish():
  print("时长检查 - 开始 ...")
  # 扫描未完成数据
  trainingPlanJson = trainingPlan().json()
  chapters = trainingPlanJson[0]['chapter']
  for chapter in chapters:
    print(chapter)
    course_id = chapter['course_id']
    chapter_id = chapter['chapter_id']
    # 只检查 3275课
    if course_id != 3275:
      continue
    # 拉取视频信息
    coursesDetailJson = coursesDetail(course_id, chapter_id).json()
    videoParame = coursesDetailJson['data']['videoParame']
    play_duration = round(videoParame['VideoMeta']['Duration'])
    play_title = videoParame['VideoMeta']['Title']
    print("课程名:" + play_title)
    print("课程时长:" + str(play_duration) + "秒")
    print(".")
    print(".")
    print(".")
    # studyOne 拉取断点
    studyOneJson = studyOne(chapter_id).json()
    playTimestamp = studyOneJson['data']['play_timestamp']
    if playTimestamp < play_duration:
      print(playTimestamp)
      print(play_duration)
      toPlayV2(course_id, chapter_id, play_duration, play_duration, 1)
    # 检查总时长
    classCourseFinishJson = classCourseFinish(course_id).json()
    # print(classCourseFinishJson)
    # exit()
    if classCourseFinishJson['is_finish'] != 0:
      print("总时长已达标")
    print("总时长统计: " + classCourseFinishJson['msg'])
    print("时长未达标, 继续下一个视频播放")
    time.sleep(1)
  print("时长检查 - 结束 ...")

checkClassCourseFinish()