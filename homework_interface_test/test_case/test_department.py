#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/26 13:43
# @Site : 
# @File : test_department.py
# @Software: PyCharm
from homework_interface_test.api_page.department_manage import DepartManage


class TestDepartment:
    def setup_class(self):
        self.department_management = DepartManage()

    def test_get_department(self):
        response = self.department_management.get_department()
        assert response["errcode"] == 0

    def test_add_department(self):
        response = self.department_management.add_department()
        assert response["errcode"] == 0

    def test_update_department(self):
        response = self.department_management.update_department()
        assert response["errcode"] == 0

    def test_delete_department(self):
        response = self.department_management.delete_department()
        assert response["errcode"] == 0