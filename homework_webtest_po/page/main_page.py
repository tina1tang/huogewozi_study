#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/16 16:47
# @Site : 
# @File : main_page.py
# @Software: PyCharm
import time

from selenium.webdriver.common.by import By

from homework_webtest_po.page.add_mem_page import AddMemPage
from homework_webtest_po.page.base_page import BasePage
from homework_webtest_po.page.contact_page import ContactPage
from homework_webtest_po.page.import_contact_page import ImportContactPage


class MainPage(BasePage):
    _url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    def go_to_add_mem(self):
        self.driver.find_element(By.CSS_SELECTOR, '.js_service_list a:nth-child(1)').click()
        return AddMemPage(self.driver)
    def go_to_import_contact(self):
        return ImportContactPage()
    def go_to_contact(self):
        return ContactPage(self.driver)