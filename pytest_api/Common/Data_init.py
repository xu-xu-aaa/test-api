from Common.Reflection import get_data
from Common.Log import Log


class Data_Init:  # 请求数据初始化
    def data_init(self, url=None, data=None, assertion=None, regular=None, sql=None, sql_assertion=None):
        try:
            variable_data = getattr(get_data, "variable_data")
            setattr(get_data, "sql", sql)
            setattr(get_data, "sql_assertion", sql_assertion)
            setattr(get_data, "assertion", assertion)
            setattr(get_data, "regular", regular)
            setattr(get_data, "url", url)
            setattr(get_data, "data", data)
            if getattr(get_data, "sql_assertion") is not None:  # 替换变量
                self.str_data(variable_data=variable_data, variable_name="sql_assertion")
            if getattr(get_data, "sql") is not None:  # 替换变量
                self.list_data(variable_data=variable_data, variable_name="sql")
            if getattr(get_data, "assertion") is not None:  # 替换变量
                self.str_data(variable_data=variable_data, variable_name="assertion")
            if getattr(get_data, "regular") is not None:  # 替换变量
                self.list_data(variable_data=variable_data, variable_name="regular")
            if getattr(get_data, "url") is not None:  # 替换变量
                self.str_data(variable_data=variable_data, variable_name="url")
            if getattr(get_data, "data") is not None:  # 替换变量
                self.str_data(variable_data=variable_data, variable_name="data")
                if (getattr(get_data, "data")[0] == "[" and getattr(get_data, "data")[
                    len(getattr(get_data, "data")) - 1] == "]") or (
                        getattr(get_data, "data")[0] == "{" and getattr(get_data, "data")[
                    len(getattr(get_data, "data")) - 1] == "}"):
                    setattr(get_data, "data", eval(getattr(get_data, "data")))
        except Exception as e:
            Log().error("数据初始化失败")
            raise e

    def list_data(self, variable_data=None, variable_name=None):
        for data_value in eval(getattr(get_data, variable_name)):
            if type(data_value) is dict:
                for key in data_value.keys():
                    if str(data_value[key]).find("${") != -1:
                        for variable_key in variable_data.keys():
                            if data_value[key].find(variable_key) != -1:
                                data = getattr(get_data, variable_name).replace(str(variable_key),
                                                                                str(variable_data[variable_key]))
                                setattr(get_data, variable_name, data)
            else:
                if data_value.find("${") != -1:
                    for variable_key in variable_data.keys():
                        if data_value.find(variable_key) != -1:
                            data = getattr(get_data, "sql").replace(str(variable_key), str(variable_data[variable_key]))
                            setattr(get_data, "sql", data)

    def str_data(self, variable_data=None, variable_name=None):
        if getattr(get_data, variable_name).find("${") != -1:
            for variable_key in variable_data.keys():
                if getattr(get_data, variable_name).find(variable_key) != -1:
                    data = getattr(get_data, variable_name).replace(str(variable_key), str(variable_data[variable_key]))
                    setattr(get_data, variable_name, data)
                    if variable_key.find("${int") != -1:
                        el = getattr(get_data, "variable_data")
                        el[variable_key] = str(int(variable_data[variable_key]) + 1)
                        setattr(get_data, "variable_data", el)
