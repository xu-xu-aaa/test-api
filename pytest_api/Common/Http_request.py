import requests
from Common.Log import Log
from Common.Reflection import get_data
from requests_toolbelt import MultipartEncoder
from Common.Read_config import Readconfig
import os

cookie = None


class Http_Request:
    def request_json(self, url=None, method=None, cookie=None, data=None, header=None, ):  # 封装json请求
        Log().info(
            "请求的入参url:{}...method:{}...cookie:{}...data:{}...header:{}".format(url, method, cookie, data, header))
        try:
            el = requests.request(method=method, url=url, json=data, cookies=cookie, headers=header, verify="False")
        except Exception as e:
            Log().error("{}请求方式有误：{}".format(method, e))
            raise e
        return el

    def request_data(self, url=None, method=None, cookie=None, data=None, header=None):  # 封装data请求
        Log().info(
            "请求的入参url:{}...method:{}...cookie:{}...data:{}...header:{}".format(url, method, cookie, data, header))
        try:
            el = requests.request(method=method, url=url, data=data, cookies=cookie, headers=header, verify="False")
        except Exception as e:
            Log().error("{}请求方式有误：{}".format(method, e))
            raise e
        return el

    def http_request(self, header=None, method=None):
        global cookie
        res = None
        if header == "form":
            res = self.request_data(url=getattr(get_data, "url"), method=method,
                                    cookie=cookie, data=getattr(get_data, "data"),
                                    header=getattr(get_data, "Header_form"))
        elif header == "json":
            res = self.request_json(url=getattr(get_data, "url"), method=method,
                                    cookie=cookie, data=getattr(get_data, "data"),
                                    header=getattr(get_data, "Header_json"))
        elif header == "text":
            res = self.request_data(url=getattr(get_data, "url"), method=method, cookie=cookie,
                                    data=getattr(get_data, "data"),
                                    header=getattr(get_data, "Header_text"))
        elif header == "file":
            data = getattr(get_data, "data")
            file_path = os.path.join(Readconfig().get_path('test_data', 'test_data', 0), data[1])
            if len(data) == 2:
                files = {data[0]: (data[1], open(file_path, 'rb'))}
                m = MultipartEncoder(files, boundary='------WebKitFormBoundaryPDylsMEaQhk1XpIh')
                res = self.request_data(url=getattr(get_data, "url"), method=method, cookie=cookie, data=m,
                                        header={'Content-Type': m.content_type})
            elif len(data) == 3:
                files = {data[0]: (data[1], open(file_path, 'rb'), data[2])}
                m = MultipartEncoder(files, boundary='------WebKitFormBoundaryPDylsMEaQhk1XpIh')
                res = self.request_data(url=getattr(get_data, "url"), method=method, cookie=cookie, data=m,
                                        header={'Content-Type': m.content_type})
            else:
                Log().error("入参数据不正确")
        else:
            Log().error("没有定义该请求方法")
        if res.cookies:  # 更新cookie
            cookie = res.cookies
        return res
