# -*- coding: utf-8 -*-
import pytest
import yaml

def get_data(method):
    with open('./caldata.yml') as f:
        caldata = yaml.safe_load(f)
        datas = caldata[method]
        data = datas['datas']
        id = datas['ids']
    return data, id
class TestCal:
    def setup_class(self):
        print('开始计算')
    def teardown_class(self):
        print('计算结束')
    # def setup(self):
    #     print('开始计算')
    # def teardown(self):
    #     print('计算结束')
    @pytest.mark.parametrize("a, b, expect", get_data('add')[0],ids=get_data('add')[1])
    def test_add(self, a, b, expect):
        print('this is an add method')
        result = a + b
        result = round(result,2)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", get_data('sub')[0], ids=get_data('sub')[1])
    def test_sub(self, a, b, expect):
        print('this is an sub method')
        result = a - b
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", get_data('mul')[0], ids=get_data('mul')[1])
    def test_mul(self, a, b, expect):
        print('this is an mul method')
        result = a * b
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", get_data('div')[0], ids=get_data('div')[1])
    def test_div(self, a, b, expect):
        print('this is an div method')
        result = a / b
        assert result == expect