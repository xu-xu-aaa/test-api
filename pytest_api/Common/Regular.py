from Common.Reflection import get_data
import re
import json
from Common.Log import Log


class Regular:
    def get_regular(self, regular, ddd):
        global null
        null = None
        if type(ddd) is list:
            el = str(ddd)
            if re.search(regular, el) != None:
                setattr(get_data, "regular_value", re.search(regular, el).group(1))
            for a in ddd:
                el = str(a)
                if re.search(regular, el) != None:
                    setattr(get_data, "regular_value", re.search(regular, el).group(1))
                if type(a) is list:
                    for b in a:
                        el = str(b)
                        if re.search(regular, el) != None:
                            setattr(get_data, "regular_value", re.search(regular, el).group(1))
                        if type(b) is list:
                            for c in b:
                                el = str(c)
                                if re.search(regular, el) != None:
                                    setattr(get_data, "regular_value", re.search(regular, el).group(1))
                        if type(b) is dict:
                            for c in b.keys():
                                d = b[c]
                                el = str(d)
                                if re.search(regular, el) != None:
                                    setattr(get_data, "regular_value", re.search(regular, el).group(1))
                if type(a) is dict:
                    for b in a.keys():
                        c = a[b]
                        el = str(c)
                        if re.search(regular, el) != None:
                            setattr(get_data, "regular_value", re.search(regular, el).group(1))
                        if type(c) is list:
                            for d in c:
                                el = str(d)
                                if re.search(regular, el) != None:
                                    setattr(get_data, "regular_value", re.search(regular, el).group(1))
                        if type(c) is dict:
                            for d in c.keys():
                                e = c[d]
                                el = str(e)
                                if re.search(regular, el) != None:
                                    setattr(get_data, "regular_value", re.search(regular, el).group(1))
        if type(ddd) is dict:
            el = str(ddd)
            if re.search(regular, el) != None:
                setattr(get_data, "regular_value", re.search(regular, el).group(1))
            for a in ddd.keys():
                b = ddd[a]
                el = str(b)
                if re.search(regular, el) != None:
                    res = re.search(regular, el).group(1)
                    setattr(get_data, "regular_value", res)
                if type(b) is list:
                    for c in b:
                        el = str(c)
                        if re.search(regular, el) != None:
                            res = re.search(regular, el).group(1)
                            setattr(get_data, "regular_value", res)
                        if type(c) is list:
                            for d in c:
                                el = str(d)
                                if re.search(regular, el) != None:
                                    res = re.search(regular, el).group(1)
                                    setattr(get_data, "regular_value", res)
                        if type(c) is dict:
                            for d in c.keys():
                                e = c[d]
                                el = str(e)
                                if re.search(regular, el) != None:
                                    res = re.search(regular, el).group(1)
                                    setattr(get_data, "regular_value", res)
                if type(b) is dict:
                    for c in b.keys():
                        d = b[c]
                        el = str(d)
                        if re.search(regular, el) != None:
                            res = re.search(regular, el).group(1)
                            setattr(get_data, "regular_value", res)
                        if type(d) is list:
                            for e in d:
                                el = str(e)
                                if re.search(regular, el) != None:
                                    res = re.search(regular, el).group(1)
                                    setattr(get_data, "regular_value", res)
                        if type(d) is dict:
                            for e in d.keys():
                                f = d[e]
                                el = str(f)
                                if re.search(regular, el) != None:
                                    res = re.search(regular, el).group(1)
                                    setattr(get_data, "regular_value", res)
        if type(ddd) is str:
            if re.search(regular, ddd) != None:
                setattr(get_data, "regular_value", re.search(regular, ddd).group(1))

    def get_key(self, regular, ddd, data_key=0):
        if type(ddd) is list:
            for b in ddd:
                if type(b) is dict:
                    for c in b.keys():
                        if regular == str(c):
                            setattr(get_data, "regular_value", b[c])
                            if type(b[c]) is list:
                                d = b[c]
                                setattr(get_data, "regular_value", d[data_key])
                        d = b[c]
                        if type(d) is dict:
                            for e in d.keys():
                                if regular == str(e):
                                    setattr(get_data, "regular_value", d[e])
                                    if type(b[c]) is list:
                                        f = d[e]
                                        setattr(get_data, "regular_value", f[data_key])
                        if type(d) is list:
                            for e in d:
                                if type(e) is dict:
                                    for f in e.keys():
                                        if regular == str(f):
                                            setattr(get_data, "regular_value", e[f])
                                            if type(e[f]) is list:
                                                g = e[f]
                                                setattr(get_data, "regular_value", g[data_key])
                if type(b) is list:
                    for c in b:
                        if type(c) is dict:
                            for d in c.keys():
                                if regular == str(d):
                                    setattr(get_data, "regular_value", b[c])
                                    if type(b[c]) is list:
                                        e = b[c]
                                        setattr(get_data, "regular_value", e[data_key])
                        if type(c) is list:
                            for d in c:
                                if type(d) is dict:
                                    for e in d.keys():
                                        if regular == str(e):
                                            setattr(get_data, "regular_value", b[c])
                                            if type(b[c]) is list:
                                                g = b[c]
                                                setattr(get_data, "regular_value", g[data_key])
        if type(ddd) is dict:
            for a in ddd.keys():
                b = ddd[a]
                if type(b) is dict:
                    for c in b.keys():
                        if regular == str(c):
                            setattr(get_data, "regular_value", b[c])
                            if type(b[c]) is list:
                                g = b[c]
                                setattr(get_data, "regular_value", g[data_key])
                        d = b[c]
                        if type(d) is dict:
                            for e in d.keys():
                                if regular == str(e):
                                    setattr(get_data, "regular_value", d[e])
                                    if type(d[e]) is list:
                                        g = d[e]
                                        setattr(get_data, "regular_value", g[data_key])
                        if type(d) is list:
                            for e in d:
                                if type(e) is dict:
                                    for f in e.keys():
                                        if regular == str(f):
                                            setattr(get_data, "regular_value", e[f])
                                            if type(e[f]) is list:
                                                g = e[f]
                                                setattr(get_data, "regular_value", g[data_key])
                if type(b) is list:
                    for c in b:
                        if type(c) is dict:
                            for d in c.keys():
                                if regular == str(d):
                                    setattr(get_data, "regular_value", c[d])
                                    if type(c[d]) is list:
                                        g = c[d]
                                        setattr(get_data, "regular_value", g[data_key])
                        if type(c) is list:
                            for d in c:
                                if type(d) is dict:
                                    for e in d.keys():
                                        if regular == str(e):
                                            setattr(get_data, "regular_value", d[e])
                                            if type(b[c]) is list:
                                                g = d[e]
                                                setattr(get_data, "regular_value", g[data_key])

    def regular(self, res_request):
        variable_data = getattr(get_data, 'variable_data')
        try:
            for regular_value in eval(getattr(get_data, "regular")):  # 遍历正则匹配数据
                for key in regular_value.keys():
                    if type(regular_value[key]) is str:
                        self.get_regular(regular_value[key], json.loads(res_request))  # 调用字典列表拆解获取唯一结果
                        variable_data[key] = str(getattr(get_data, "regular_value"))  # 将正则返回结果存入变量中
                        Log().info("正则获取到的变量{}".format(getattr(get_data, "regular_value")))
                        setattr(get_data, "variable_data", variable_data)  # 反射变量
                    elif type(regular_value[key]) is list:
                        data = regular_value[key]
                        self.get_key(data[0], json.loads(res_request), data[1])
                        variable_data[key] = str(getattr(get_data, "regular_value"))  # 将正则返回结果存入变量中
                        Log().info("正则获取到的变量{}".format(getattr(get_data, "regular_value")))
                        setattr(get_data, "variable_data", variable_data)  # 反射变量
                        if type(getattr(get_data, "regular_value")) is list:
                            list_data = getattr(get_data, "regular_value")
                            setattr(get_data, "variable_data", list_data[0])  # 反射变量
                            variable_data[key] = str(getattr(get_data, "regular_value"))
                        elif type(getattr(get_data, "regular_value")) is str:
                            if (getattr(get_data, "regular_value")[0] == "[" and getattr(get_data, "regular_value")[
                                len(getattr(get_data, "regular_value")) - 1] == "]"):
                                setattr(get_data, "regular_value", eval(getattr(get_data, "regular_value"))[0])
                                variable_data[key] = str(getattr(get_data, "regular_value"))
                        Log().info("正则获取到的变量{}".format(getattr(get_data, "regular_value")))
        except Exception as e:
            Log().error("正则执行失败{}".format(e))
            raise e

# if __name__ == '__main__':
#     ddd = {"files":[{"jsonData":"[{\"startMeterNum\":\"\",\"gasEnvironment\":\"\",\"line\":1,\"userNo\":\"\",\"meterRange\":\"\",\"useYears\":\"\",\"remark\":\"\",\"addrStatusDes\":\"待用\",\"installPosition\":\"\",\"fixedWay\":\"\",\"plugCardDirection\":\"\",\"installDate\":\"\",\"addrDes\":\"东城区批量开户开户01栋1单元01层101号\",\"meterType\":\"\",\"gasDirection\":\"\",\"meterCartonNo\":\"\",\"meterNo\":\"\",\"manufactureDate\":\"\",\"addrId\":\"202008281025046110102211782734\",\"meterModelDes\":\"\",\"manuId\":\"\",\"meterModelId\":\"\"},{\"startMeterNum\":\"\",\"gasEnvironment\":\"\",\"line\":2,\"userNo\":\"\",\"meterRange\":\"\",\"useYears\":\"\",\"remark\":\"\",\"addrStatusDes\":\"待用\",\"installPosition\":\"\",\"fixedWay\":\"\",\"plugCardDirection\":\"\",\"installDate\":\"\",\"addrDes\":\"东城区批量开户开户01栋1单元01层101号\",\"meterType\":\"\",\"gasDirection\":\"\",\"meterCartonNo\":\"\",\"meterNo\":\"\",\"manufactureDate\":\"\",\"addrId\":\"202008281025046110102211782734\",\"meterModelDes\":\"\",\"manuId\":\"\",\"meterModelId\":\"\"}]","size":9401,"name":"111222.xlsx","deleteType":"DELETE","deleteUrl":"http://gxcr.etbc-enesys.eslink.net.cn/enesys-web/meterBatInstall/deleteImport?fileName=111222.xlsx","type":"xlsx/xls","params":["line","addrId","userNo","addrDes","addrStatusDes","meterNo","meterModelId","meterModelDes","meterType","meterRange","manuId","useYears","gasDirection","installDate","manufactureDate","installPosition","meterCartonNo","fixedWay","plugCardDirection","gasEnvironment","startMeterNum","remark"],"url":"111222.xlsx","thumbnailUrl":"111222.xlsx"}]}
#     el = 'jsonData":"[(.+?)]","size'
#     Regular().regular(el, ddd)
#     print(getattr(get_data, "regular_value"))
