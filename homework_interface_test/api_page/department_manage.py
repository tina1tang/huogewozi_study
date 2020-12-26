#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/26 12:28
# @Site : 
# @File : department_manage.py
# @Software: PyCharm
import requests

from homework_interface_test.api_page.base_api import BaseApi
from homework_interface_test.api_page.utils import Utils


class DepartManage(BaseApi):
    def __init__(self):
        _id = "ww66d86f7dfe585c54"
        _secret = "K3sTAAdCZK7N7UJChT6KILEbUTe889UOmy7lpcxfeLY"
        utils = Utils()
        self.token = utils.get_token(_id, _secret)

    def add_department(self):
        data = {"method": "post",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/create",
                "params": {"access_token": self.token},
                "json": {"name": "深圳研发中心", "name_en": "RDSZ", "parentid": 1}
               }
        return self.send_api(data)

    def update_department(self):
        data = {"method": "post",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/update",
                "params": {"access_token": self.token},
                "json": {"name": "南京研发中心", "id": 4}
                }
        return self.send_api(data)

    def delete_department(self):
        data = {"method": "get",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/delete",
                "params": {"access_token": self.token, "id": 4}
                }
        return self.send_api(data)

    def get_department(self):
        data = {"method": "get",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/list",
                "params": {"access_token": self.token, "id": 1}
               }
        return self.send_api(data)