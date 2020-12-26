#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/26 16:59
# @Site : 
# @File : utils.py
# @Software: PyCharm
import requests

from interface_po_test.api_page.base_api import BaseApi


class Utils(BaseApi):
    def get_token(self, corpsecret, copid="ww66d86f7dfe585c54"):
        data = {"url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                "params": {"corpid": copid, "corpsecret": corpsecret}}
        return requests.get(**data).json()["access_token"]
