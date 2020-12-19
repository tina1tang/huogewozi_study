#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/16 16:57
# @Site : 
# @File : base_page.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _url = ""

    def __init__(self, driver_base=None):
        if driver_base == None:
            options = Options()
            options.debugger_address = 'localhost:9222'
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver:WebDriver = driver_base
        if self._url != "":
            self.driver.get(self._url)
        self.driver.implicitly_wait(3)

    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)

    def finds(self, by, value):
        return self.driver.find_elements(by=by, value=value)