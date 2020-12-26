#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/26 17:00
# @Site : 
# @File : base_api.py
# @Software: PyCharm
import requests


class BaseApi:
    def send_api(self, data):
        return requests.request(**data).json()