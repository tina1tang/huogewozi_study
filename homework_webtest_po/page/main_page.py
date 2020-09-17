#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/16 16:47
# @Site : 
# @File : main_page.py
# @Software: PyCharm
from homework_webtest_po.page.add_mem_page import AddMemPage
from homework_webtest_po.page.contact_page import ContactPage
from homework_webtest_po.page.import_contact_page import ImportContactPage


class MainPage:
    def go_to_add_mem(self):
        return AddMemPage()
    def go_to_import_contact(self):
        return ImportContactPage()
    def go_to_contact(self):
        return ContactPage()