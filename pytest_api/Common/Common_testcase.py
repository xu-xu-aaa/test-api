from Common.Http_request import Http_Request
from Common.Log import Log
from Common.Read_mysql import Read_Mysql
from Common.Regular import Regular
from Common.Data_init import Data_Init
from Common.Response_assertion import Response_Assertion


class Common_Testcase:
    def Testcase(self, url=None, data=None, assertion=None, regular=None, sql=None, sql_assertion=None,
                 case_id=None, header=None, method=None, sheet_name=None, case_list=None):
        Log().info("执行的用例{}".format(case_id))
        # s数据初始化
        Data_Init().data_init(url=url, data=data, assertion=assertion, regular=regular, sql=sql,
                              sql_assertion=sql_assertion)
        # 发送HTTP请求
        res = Http_Request().http_request(header=header, method=method)
        response_data = res.text
        # 断言
        if assertion is not None:
            Response_Assertion().assertion(response_data=response_data, case_id=case_id, case_list=case_list,
                                           sheet_name=sheet_name)
        # 正则匹配
        if regular is not None:
            Regular().regular(response_data)
        # 执行sql
        if sql is not None:
            Read_Mysql().sql_assertion(case_list=case_list)
