#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/26 11:52
# @Site : 
# @File : mem_manage.py
# @Software: PyCharm
import requests

from interface_po_test.api_page.base_api import BaseApi
from interface_po_test.api_page.utils import Utils


class MemManage(BaseApi):
    def __init__(self):
        _corpsecret = "K3sTAAdCZK7N7UJChT6KILEbUTe889UOmy7lpcxfeLY"
        utils = Utils()
        self.token = utils.get_token(_corpsecret)
    def create_mem(self):
        data = {"url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
                "method": "post",
                "params": {"access_token": self.token},
                "json": {"userid": "112", "name": "张三","department": [1], "mobile": "+86 13800000000"}}
        return self.send_api(data)

    def get_mem(self):
        data = {"url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
                "method": "get",
                "params": {"access_token": self.token, "userid": 112}}
        return self.send_api(data)
