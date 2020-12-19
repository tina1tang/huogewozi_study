#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/19 0:13
# @Site : 
# @File : test_add_member.py
# @Software: PyCharm
from homework_webtest_po.page.main_page import MainPage


class TestAddMem:
    def setup_class(self):
        self.main = MainPage()

    def test_add_mem(self):
        mem_list = self.main.go_to_add_mem().add_mem("李灵", "111", "18711111111").get_mem_list()
        assert "李灵" in mem_list

    def test_add_department(self):
        department_list = self.main.go_to_contact().go_to_add_department().add_department("杭州研发中心").get_department_list()
        assert "杭州研发中心" in department_list

    def teardown_class(self):
        self.main.driver.quit()