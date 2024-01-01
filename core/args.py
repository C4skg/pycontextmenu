import argparse

class ServiceHelper:
    def __init__(self,descripton:str='') -> None:
        
        self.arg = argparse.ArgumentParser(allow_abbrev=True,add_help=False,description=descripton)

    def showArgs(self):
            self.arg.add_argument("-h","--help",dest="help",default=False,action="store_true",help="显示帮助信息")
            self.arg.add_argument(
                 '--change',
                 default=False,
                 choices=['install','uninstall'],
                 help='''
                        修改命令，使用 `install` 进行安装，使用 `uninstall` 进行卸载,
                        但只会解除注册表的占用，并不会删除本地的数据
                      '''
            )

            self.arg.add_argument('-c','--create',default=False,help='创建一个模板文件')
            self.arg.add_argument('-l','--list',default=False,help='输出所有已存在的插件')
            self.arg.add_argument('-add',default=False,help='添加插件至右键中')
            self.arg.add_argument('-name',default=False,help='需要操作或添加的对象的名称',required=False)


    def print_help(self):
        self.arg.print_help();

    
    def parse_args(self):
        return self.arg.parse_args();