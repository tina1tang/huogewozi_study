#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/16 16:48
# @Site : 
# @File : add_mem_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from homework_webtest_po.page.base_page import BasePage
from homework_webtest_po.page.contact_page import ContactPage


class AddMemPage(BasePage):

    def add_mem(self, name, id, phone):
        _username = (By.ID, "username")
        _userid = (By.ID, "memberAdd_acctid")
        _userphone = (By.ID, "memberAdd_phone")
        _save = (By.CSS_SELECTOR, ".js_btn_save")
        self.find(*_username).send_keys(name)
        self.find(*_userid).send_keys(id)
        self.find(*_userphone).send_keys(phone)
        self.find(*_save).click()
        return ContactPage(self.driver)

