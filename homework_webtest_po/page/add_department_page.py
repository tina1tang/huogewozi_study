#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/16 16:48
# @Site : 
# @File : add_department_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from homework_webtest_po.page.base_page import BasePage
from homework_webtest_po.page.contact_page import ContactPage


class AddDepartmentPage(BasePage):
    def add_department(self, depat_name):
        self.find(By.CSS_SELECTOR, ".member_tag_dialog_inputDlg .ww_inputText").send_keys(depat_name)
        self.find(By.CSS_SELECTOR, ".member_tag_dialog_inputDlg .js_toggle_party_list").click()
        self.find(By.CSS_SELECTOR, ".member_tag_dialog_inputDlg [id='1688850821773912_anchor']").click()
        self.find(By.CSS_SELECTOR, ".ww_dialog_foot .ww_btn_Blue").click()
        return ContactPage(self.driver)