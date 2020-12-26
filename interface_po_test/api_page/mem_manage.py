#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/26 11:52
# @Site : 
# @File : mem_manage.py
# @Software: PyCharm
import requests


class MemManage:

    def create_mem(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN"
        data = {"userid":"112", "name":"张三"}
        requests.post(url, data)

    def get_mem(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID"
        data = {"userid": "112", "name": "张三"}
        requests.get(url, data)

    def update_mem(self):
        pass

    def delete_mem(self):
        pass