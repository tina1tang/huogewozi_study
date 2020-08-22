#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/22 18:21
# @Site : 
# @File : TestWechat.py
# @Software: PyCharm
import shelve

from selenium import webdriver
import time
class TestWechat:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    def test_connect(self):
        file = "D:\huogewozi_study\homework_business_wechat\connect.xlsx"
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # time.sleep(3)
        db = shelve.open('./db/data.db')
        cookies = db['cookie']
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element_by_xpath("//div[@class='index_service_cnt js_service_list']/a[2]").click()
        self.driver.find_element_by_id("js_upload_file_input").send_keys(file)
        assert "connect.xlsx" == self.driver.find_element_by_id("upload_file_name").text