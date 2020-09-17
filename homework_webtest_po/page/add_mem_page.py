#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/16 16:48
# @Site : 
# @File : add_mem_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from test_appium.page.basepage import BasePage


class AddMemPage(BasePage):
    def add_mem(self):
        self.driver.find_element(By.ID, "username").send_keys("李灵")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("1111")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("187111222333")
