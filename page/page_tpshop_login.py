"""
    目标：PO模式page页面封装
    提示：
        1. 类名 为大驼峰模块名(去掉下划线)
        2. 每一步操作，为单独的方法
    核心：page页面对象要集成Base
"""
import page
from base.base import Base


class PageTpshopLogin(Base):
    # 1.点击登录
    def page_click_login_btn(self):
        self.base_click(page.loc_login_btn)
    # 2.清空输入框
    # 3.输入用户名
    def page_input_username(self,username):
        self.base_input_text(page.loc_username,username)
    # 4.输入密码
    def page_input_password(self,password):
        self.base_input_text(page.loc_password,password)
    # 5.输入验证码
    def page_input_code(self,code):
        self.base_input_text(page.loc_code,code)
    # 6.点击登录
    def page_click_submit(self):
        self.base_click(page.loc_submit)
