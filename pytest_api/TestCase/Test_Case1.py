from Common.Reflection import get_data
from Common.Read_case import Case
from Common.Common_testcase import Common_Testcase
from Common.Read_config import Readconfig
from Common.Write_back import Write_Back
import pytest


el = eval(Readconfig().get_config('sheet_name', 'sheet_name'))  # 获取excel的表单
test_path = Readconfig().get_path('case_path', 'case_path', 1)  # 获取excel的路径
setattr(get_data, "variable_data", Case().get_variable(test_path, el[0]))


class Test_case1:

    def teardown_class(self):
        Write_Back().set_data(test_path, el[0])
    @pytest.mark.parametrize('item', Case().get_case(test_path, el[1]))
    def test_api1(self, item):
        Common_Testcase().Testcase(sheet_name=el[1], url=item["url"], data=item["data"],
                                   assertion=item["assertion"],
                                   regular=item["regular"], sql=item["sql"], sql_assertion=item["sql_assertion"],
                                   case_id=item["case_id"], header=item["header"], method=item["method"], case_list=[])

    @pytest.mark.parametrize('item', Case().get_case(test_path, el[2]))
    def test_api2(self, item):
        Common_Testcase().Testcase(sheet_name=el[2], url=item["url"], data=item["data"],
                                   assertion=item["assertion"],
                                   regular=item["regular"], sql=item["sql"], sql_assertion=item["sql_assertion"],
                                   case_id=item["case_id"], header=item["header"], method=item["method"], case_list=[])
