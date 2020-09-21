import unittest
from Common.Log import Log
from Common.Reflection import get_data


class Response_Assertion:
    def assertion(self, response_data=None, case_id=None, sheet_name=None, case_list=None):
        result = None
        case_dict = {}
        case_response = {}
        assertion = getattr(get_data, "assertion")
        try:
            unittest.TestCase().assertIn(str(assertion), response_data)
            result = "pass"
            Log().info("断言正确")
        except AssertionError as e:
            result = "fail"
            Log().error("断言错误{}".format(e))
            raise e
        finally:
            case_list.extend([result, response_data])
            case_dict[str(int(case_id) + 2)] = case_list
            case_response[sheet_name] = case_dict
            get_data.response.append(case_response)
