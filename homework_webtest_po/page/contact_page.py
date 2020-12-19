#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/16 16:47
# @Site : 
# @File : contact_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
from homework_webtest_po.page.base_page import BasePage
from homework_webtest_po.page.import_contact_page import ImportContactPage


class ContactPage(BasePage):
    _url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def go_to_add_mem(self):
        from homework_webtest_po.page.add_mem_page import AddMemPage
        return AddMemPage(self.driver)

    def get_mem_list(self):
        mem_list = []
        member = self.find(By.CSS_SELECTOR, '#member_list td:nth-child(2)').text
        mem_list.append(member)
        return mem_list

    def go_to_add_department(self):
        from homework_webtest_po.page.add_department_page import AddDepartmentPage
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        return AddDepartmentPage(self.driver)

    def go_to_import_contact(self):
        return ImportContactPage()

    def get_department_list(self):
        department_list = []
        # departments = self.driver.find_elements(By.CSS_SELECTOR, ".member_colLeft_bottom a")
        departments = self.finds(By.CSS_SELECTOR, ".member_colLeft_bottom a")
        for department in departments:
            print(department.text)
            department_list.append(department.text)
        return department_list


