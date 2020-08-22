#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/22 16:02
# @Site : 
# @File : wechat.py
# @Software: PyCharm
import shelve

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
# browser = webdriver.Chrome()
# options = Options()
# options.debugger_address = 'localhost:9222'
# drver = webdriver.Chrome(options=options)
# drver.get('https://work.weixin.qq.com/wework_admin/frame#index')
# print(drver.get_cookies())
# cookies= [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '3R_c-__9SjVLnog0UmnEMpYShAQS-gtBksnVqEtpB6FjRmSI932DmCWpYC2BqDpnSP1szMcFOvA269IDZLdb8vyBcjkoGqi-1uxVGkGeYFp5Yr82MD-LDyf-WAwDuSXjuDSi8mlU5vWskLlV7Ht0DE1ujEOmb5ufwU2SA7MFs3Ss7lvGZ2FPL5wIdTjhVR-trMpRTdCAj7VLCpZDVE1HzQMqHZwSAF0BLj1GxEz_WrSme-r6CGo76oKd2lGNn8MkDfpoRGionDB-VMsInAp44A'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850821773807'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850821773807'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325046156636'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'MxPomJ3DKtQqnSdU52z3nJ7SOgRUWH6PtT1P0TsX1fzMn3sIf0n2N7nPRBzGSMbw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a4014944'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '40139326591261134'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598117038, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': 'l8bk51'}, {'domain': '.qq.com', 'expiry': 1598178462, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.289082346.1598085504'}, {'domain': '.qq.com', 'expiry': 1661164062, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1988940030.1597756792'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629292790, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '2b4fd3cb4f0885f3c06076fd4e072410b5b3fa408bdab1439caa96d2438a5f4e'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629623115, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597756791,1598086843'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'sYK87M+CaC'}, {'domain': '.qq.com', 'expiry': 1599748557, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '547073717'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600684065, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.qq.com', 'expiry': 1598092122, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '3563646976'}]
db = shelve.open('./db/data.db')
# db['cookie'] = cookies
print(db['cookie'])
db.close()