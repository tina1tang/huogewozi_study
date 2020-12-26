#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/26 16:56
# @Site : 
# @File : test_mem_manage.py
# @Software: PyCharm
from interface_po_test.api_page.mem_manage import MemManage


class TestMemManagement:
    def setup_class(self):
        self.mem_manage = MemManage()

    def test_create_mem(self):
        response = self.mem_manage.create_mem()
        assert response["errcode"] == 0

    def test_get_mem(self):
        response = self.mem_manage.get_mem()
        assert response["errcode"] == 0