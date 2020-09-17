#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/16 16:47
# @Site : 
# @File : contact_page.py
# @Software: PyCharm
from homework_webtest_po.page.add_department_page import AddDepartmentPage
from homework_webtest_po.page.add_mem_page import AddMemPage
from homework_webtest_po.page.import_contact_page import ImportContactPage


class ContactPage:
    def go_to_add_mem(self):
        return AddMemPage()
    def go_to_add_department(self):
        return AddDepartmentPage()
    def go_to_import_contact(self):
        return ImportContactPage()

