import os

import yaml

class ReadTpshopLoginYaml():
# 以下为动态方法:
    def __init__(self,filename):
        self.filename=os.getcwd()+os.sep+"data"+os.sep+filename
        # self.filename=filename
    def read_tpshop_login_yaml(self):
        with open(self.filename,"r",encoding="utf-8")as f:
            return yaml.load(f)
# if __name__ == '__main__':
#     ReadTpshopLoginYaml("../data/data_tpshop_login.yaml").read_tpshop_login_yaml()
#以下为静态方法:
#     def read_tpshop_login_yaml_degug(self):
#         with open("../data/data_tpshop_login.yaml","r",encoding="utf-8") as f:
#             return yaml.load(f)
#
# if __name__ == '__main__':
#     datas=ReadTpshopLoginYaml().read_tpshop_login_yaml_debug().values()
#     arrs=[]
#     for data in datas:
#         arrs.append((data.get("username"),data.get("password"),data.get("code")))
#     print(arrs)
