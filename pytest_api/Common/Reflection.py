class get_data:
    Header_form = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36','Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    Header_json = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36','Content-Type': 'application/json;charset=UTF-8'}
    Header_text = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36','Content-Type': 'text/plain;charset=UTF-8'}
    data = None  # 请求入参替换
    url = None  # 请求url替换
    regular_value = None  # 正则提取出来的变量值
    assertion = None  # 断言数据替换
    variable_data = None  # 变量初始化化数据
    regular = None  # 正则数据替换
    sql = None  # SQL数据替换
    title_case = None
    sql_assertion = None  # SQL断言数据替换
    response = []  # 测试结果回写