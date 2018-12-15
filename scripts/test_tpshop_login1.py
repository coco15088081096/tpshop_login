"""
目标：PO模式scripts脚本实现
    操作：
        1. 新建测试模块(test_页面对象.py)
        2. 类名(使用大驼峰去掉下划线)
        3. 不用过脑(def setup_class teardown_class test_login)编写三个方法
            setup_class
                1. 实例化 page页面对象
            teardown_class
                1. 关闭 driver对象
            test_login()
                1.根据操作步骤调用page对象内方法
"""
import sys
import os
sys.path.append(os.getcwd())
import pytest

from base.get_driver import get_driver

from base.read_tpshop_login_yaml import ReadTpshopLoginYaml



from page.page_tpshop_login import PageTpshopLogin


def get_data():
    datas = ReadTpshopLoginYaml("data_tpshop_login.yaml").read_tpshop_login_yaml().values()
    arrs = []
    for data in datas:
        arrs.append((data.get("username"), data.get("password"), data.get("code")))
    return arrs


class TestTpshopLogin():
    def setup(self):
        self.tpshop_login = PageTpshopLogin(get_driver())

    def teardown(self):
        self.tpshop_login.driver.quit()

    @pytest.mark.parametrize("username,password,code", get_data())
    def test_tpshop_login(self, username, password, code):
        # 1.点击登录
        self.tpshop_login.page_click_login_btn()
        # 2.清空输入框
        # 3.输入用户名
        self.tpshop_login.page_input_username(username)
        # 4.输入密码
        self.tpshop_login.page_input_password(password)
        # 5.输入验证码
        self.tpshop_login.page_input_code(code)
        # 6.点击登录
        self.tpshop_login.page_click_submit()

