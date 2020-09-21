import pymysql
from Common.Reflection import get_data
from Common.Read_config import Readconfig
import unittest
from Common.Log import Log


class Read_Mysql:
    def get_data(self, sql_name):  # 获取变量读数据库
        cis_8 = eval(Readconfig().get_config("MYSQL", "cis_8"))
        cnn = pymysql.connect(**cis_8)
        cursor = cnn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql_name)
        res = cursor.fetchone()
        cursor.close()
        cnn.close()
        if type(res) is dict and len(res) == 1:
            for key in res:
                return res[key]
        else:
            return res

    def sql_assertion(self, case_list=None):  # 执行SQL获取数据并断言
        temporary_data = {}
        result = None
        try:
            sql_data = eval(getattr(get_data, "sql"))
            variable_data = getattr(get_data, 'variable_data')
            Log().info("SQL语句{}".format(sql_data))
            i = 0
            j = -1
            for sql_value in sql_data:  # 遍历SQL语句
                i = i + 1
                if type(sql_value) is dict:  # 判断是否为字典类型数据
                    for key in sql_value.keys():  # 遍历SQL语句
                        sql = self.get_data(sql_value[key])  # 执行SQL
                        variable_data[key] = str(sql)  # 将SQL语句返回结果存入变量池variable_data
                        temporary_data[str(i)] = str(sql)  # 将SQL语句返回结果存入sql_data
                        Log().info("SQL查询结果{}".format(sql))
                        setattr(get_data, "variable_data", variable_data)  # 反射变量池
                else:
                    sql_assertion = eval(getattr(get_data, "sql_assertion"))  # 获取断言
                    j = j + 1
                    sql = self.get_data(sql_value)  # 执行SQL
                    Log().info("SQL查询结果{}".format(sql))
                    if sql is not None:  # SQL断言
                        try:
                            unittest.TestCase().assertIn(sql_assertion[j], str(sql))
                            result = "pass"
                            Log().info("SQL断言正确")
                        except AssertionError as e:
                            result = "fail"
                            Log().error("SQL断言错误{}".format(e))
                            raise e
                        finally:
                            temporary_data[str(i)] = str(sql)  # 将SQL语句返回结果存入sql_data
                    else:
                        try:
                            unittest.TestCase().assertEqual(sql_assertion[j], 'None')
                            result = "pass"
                            Log().info("SQL断言正确")
                        except AssertionError as e:
                            result = "fail"
                            Log().error("SQL断言错误{}".format(e))
                            raise e
                        finally:
                            temporary_data[str(i)] = str(sql)  # 将SQL语句返回结果存入sql_data
            return temporary_data
        except Exception as e:
            Log().error("SQL执行错误")
            raise e
        finally:
            case_list.extend([temporary_data, result])
