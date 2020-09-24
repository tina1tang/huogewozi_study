#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/23 17:47
# @Site : 
# @File : test_department_management.py
# @Software: PyCharm
import requests
def get_token():
    id = "ww66d86f7dfe585c54"
    secret = "K3sTAAdCZK7N7UJChT6KILEbUTe889UOmy7lpcxfeLY"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={id}&corpsecret={secret}"
    res = requests.get(url).json()
    return res["access_token"]

def test_add_department():
    token = get_token()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token}"
    data = {
        "name": "广州研发中心",
        "name_en": "RDGZ",
        "parentid": 1,
        "order": 1,
        "id": 2
    }
    res = requests.post(url, json=data).json()
    print(res)

def test_update_department():
    token = get_token()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={token}"
    data = {
        "id": 2,
        "name": "杭州研发中心",
        "name_en": "RDHZ"
    }
    res = requests.post(url, json=data).json()
    print(res)

def test_delete_department():
    token = get_token()
    id = "2"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={token}&id={id}"
    res = requests.get(url).json()
    print(res)

def test_get_department():
    token = get_token()
    id = "1"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}&id={id}"
    res = requests.get(url).json()
    print(res)