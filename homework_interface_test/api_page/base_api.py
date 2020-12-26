#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/26 12:30
# @Site : 
# @File : base_api.py
# @Software: PyCharm
import requests




class BaseApi:
    def send_api(self, data: dict):
        return requests.request(**data).json()
