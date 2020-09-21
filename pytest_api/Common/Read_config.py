import configparser
import os
import datetime

nowTime = datetime.datetime.now().strftime('%Y-%m-%d')  # 获取当前时间戳
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]  # 指定文件顶级目录
html_path = os.path.join(project_path, 'Result', "html", "report{}.html".format(str(nowTime)))  # 指定文件目录
log_path = os.path.join(project_path, 'Result', "log", "log{}.txt".format(str(nowTime)))  # 指定文件目录
case_path = os.path.join(project_path, 'TestCase')  # 指定文件目录


class Readconfig:
    def __init__(self):
        self.project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
        self.case_config_path = os.path.join(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0],
                                             "Configure", "configure.ini")  # 指定Config目录

    def get_config(self, section, option):
        cf = configparser.ConfigParser()  # 创建配置分析器
        cf.read(self.case_config_path)  # 打开配置文件
        return cf[section][option]  # 返回对应的section中的option的值

    def get_path(self, section, option,index):
        el = eval(self.get_config(section, option))
        path = os.path.join(self.project_path, el[index])
        return path


if __name__ == '__main__':
    aa = Readconfig().get_path("case_path", "case_path")
    print(aa)
