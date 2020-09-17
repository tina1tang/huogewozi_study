#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/16 16:57
# @Site : 
# @File : base_page.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BasePage:
    def __init__(self):
        options = Options()
        options.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
