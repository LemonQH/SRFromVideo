import uuid
import requests
import hashlib
import json
import time

YOUDAO_URL = 'https://openapi.youdao.com/asrapi'
APP_KEY = ''
APP_SECRET = ''

def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size-10:size]

def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()

def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)

def connect(audio_base64):
    data = {}
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(audio_base64) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = audio_base64
    data['salt'] = salt
    data['sign'] = sign
    data['signType'] = "v2"
    data['langType'] = 'zh-CHS'
    data['rate'] = 16000
    data['format'] = 'mp3'
    data['channel'] = 1
    data['type'] = 1

    response = do_request(data)

    return json.loads(str(response.content,'utf-8'))

