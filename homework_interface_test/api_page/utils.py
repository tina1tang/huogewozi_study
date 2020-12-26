#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/26 13:22
# @Site : 
# @File : utils.py
# @Software: PyCharm
from homework_interface_test.api_page.base_api import BaseApi


class Utils(BaseApi):

    def get_token(self, id, secret):
        data = {"method": "get",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                "params": {"corpid": id, "corpsecret": secret}
                }
        return self.send_api(data)["access_token"]