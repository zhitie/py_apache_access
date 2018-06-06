# -*- coding: utf-8 -*-

import xlsxwriter
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_list(data):
    try:
        data2=data[0]
    except:
        data2=''
    return data2

def in_excel(data,sheet):
    if len(data) > 15:
        Sheet_num = 15
    else:
        Sheet_num = len(data) + 1
    workbook = xlsxwriter.Workbook(sheet+'.xlsx')
    worksheet = workbook.add_worksheet(sheet)
    headings = ["地址", "计数"]
    head_style = workbook.add_format({"bold": True, "bg_color": "yellow", "align": "center", "font": 13})
    worksheet.write_row("A1", headings, head_style)
    for i in range(0, len(data)):
        worksheet.write_row("A{}".format(i + 2), data[i])
    chart1 = workbook.add_chart({"type": "column"})
    chart1.add_series({
        "name": "=%s!$B$1" % sheet,  # 图例项
        "categories": "=%s!$A$2:$A$%d" % (sheet, Sheet_num),  # X轴 Item名称
        "values": "=%s!$B$2:$B$%d" % (sheet, Sheet_num)  # X轴Item值
    })
    chart1.set_title({"name": "柱状图"})
    chart1.set_y_axis({"name": "计数"})
    # chart1.set_x_axis({"name": "地址"})
    chart1.set_style(11)
    worksheet.insert_chart("B7", chart1)
    workbook.close()
def in_excel2(data,sheet):
    new_data = []
    for i in range(len(data)):
        data_url = data[i][0]
        data_url_1 = re.findall(r'http://(.*?)\.com', data_url)
        data_url_2 = re.findall(r'com/(.*?)/', data_url)
        data_unit = ('http://' + get_list(data_url_1) + '.com', get_list(data_url_2), data[i][1])
        new_data.append(data_unit)

    if len(data) > 15:
        Sheet_num = 15
    else:
        Sheet_num = len(data) + 1
    workbook = xlsxwriter.Workbook('test.xlsx')
    worksheet = workbook.add_worksheet(sheet)
    headings = ["地址",'分类', "计数"]
    head_style = workbook.add_format({"bold": True, "bg_color": "yellow", "align": "center", "font": 13})
    worksheet.write_row("A1", headings, head_style)
    for i in range(0, len(data)):
        worksheet.write_row("A{}".format(i + 2), new_data[i])
    chart1 = workbook.add_chart({"type": "column"})
    chart1.add_series({
        "name": "=%s!$B$1" % sheet,  # 图例项
        "categories": "=%s!$A$2:$A$%d" % (sheet, Sheet_num),  # X轴 Item名称
        "values": "=%s!$C$2:$C$%d" % (sheet, Sheet_num)  # X轴Item值
    })
    chart1.set_title({"name": "柱状图"})
    chart1.set_y_axis({"name": "计数"})
    # chart1.set_x_axis({"name": "地址"})
    chart1.set_style(11)
    worksheet.insert_chart("D7", chart1)
    workbook.close()


if __name__ == "__main__":
    data = [('http://ipr.yuzhua.com/', 88), ('http://gz.yuzhua.com/', 55), ('http://www.yuzhua.com/', 36), ('http://cd.yuzhua.com/', 22), ('http://sc.yuzhua.com/', 10), ('http://ym.yuzhua.com/', 9), ('http://ipr.yuzhua.com/case/49.html', 8), ('http://r.yuzhua.com/registerQuick?utm_source=baidu&utm_medium=DS&utm_campaign=R-ZC&utm_content=r-zc', 8), ('http://ym.yuzhua.com/search/1--0--0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0--0.html', 8), ('http://ipr.yuzhua.com/case/48.html', 6), ('http://cp.yuzhua.com/', 3), ('http://www.baidu.com/s?wd=WWBH', 3), ('http://www.yuzhua.com/user/login.html', 3), ('http://help.yuzhua.com/index/kefu.html', 2), ('http://qy.yuzhua.com/?utm_source=baidu&utm_medium=DS&utm_campaign=QY-ZR&utm_content=QY-yyzz-gm&utm_term=gm-Cchenshu', 2), ('http://r.yuzhua.com/registerQuick?utm_source=baidu&utm_medium=DS&utm_campaign=R-ST&utm_content=r-st04', 2), ('http://ipr.yuzhua.com/adviser.html', 2), ('blank', 2), ('6DAD513C8080D343AF171.221.29.60', 2), ('http://mt.yuzhua.com/operation.html?utm_source=baidu&utm_medium=DS&utm_campaign=DYY&utm_content=TG&utm_term=q', 2), ('http://mt.yuzhua.com/weixin/1079810881.html', 2), ('http://mj.yuzhua.com/', 2), ('http://yz.51liuliuqiu.cn/index.php/admin/order/index/type/4/order_type/4', 2), ('http://r.yuzhua.com/goods/9287241921.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-1091.html', 1), ('http://bj.yuzhua.com/goods/6975734435.html', 1), ('http://bj.yuzhua.com/news/2-19-293', 1), ('http://ipr.yuzhua.com/consulte/2-19-1601', 1), ('http://bj.yuzhua.com/goods/8591443794.html', 1), ('http://ipr.yuzhua.com/consulte/2-21-1123.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-2717.html', 1), ('http://ipr.yuzhua.com/consulte/1-19-110.html', 1), ('http://ipr.yuzhua.com/goods/9821738398', 1), ('http://www.baidu.com/s?wd=N7BO', 1), ('http://p.yuzhua.com/search.html', 1), ('http://ipr.yuzhua.com/consulte/1-20-6.html', 1), ('http://bj.yuzhua.com/goods/6733967829.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-1831.html', 1), ('http://bj.yuzhua.com/goods/8266887866.html', 1), ('http://bj.yuzhua.com/goods/1470838013.html', 1), ('http://ipr.yuzhua.com/consulte/2-20-2252.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-1458.html', 1), ('http://bj.yuzhua.com/goods/8496260993.html', 1), ('http://ipr.yuzhua.com/consulte/2-23-1815', 1), ('http://mt.yuzhua.com/packageDetail/77', 1), ('http://bj.yuzhua.com/goods/9383640857.html', 1), ('http://m.sogou.com/web/searchList.jsp?pid=sogou-mobb-d2dc6368837861b4-0007&keyword=nb%E4%BA%A4%E6%98%93%E5%B9%B3%E5%8F%B0%E9%9F%A9%E9%9B%81%E5%87%8C', 1), ('http://mt.yuzhua.com/weixin/s-----------------%E4%BD%9B-1-2.html', 1), ('http://bj.yuzhua.com/goods/9733511939.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-1052', 1), ('http://ipr.yuzhua.com/consulte/2-19-2528', 1), ('http://bj.yuzhua.com/goods/4837307276.html', 1), ('http://bj.yuzhua.com/goods/8735262920.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-1846.html', 1), ('http://bj.yuzhua.com/goods/8077324898.html', 1), ('http://bj.yuzhua.com/buy/1------8---------------23.html', 1), ('http://bj.yuzhua.com/buy/1-----------7-2---------249.html', 1), ('http://ipr.yuzhua.com/consulte/2-20-1378.html', 1), ('http://bj.yuzhua.com/buy/1-----------11-2---------53.html', 1), ('http://www.baidu.com/s?wd=4TG0', 1), ('http://ipr.yuzhua.com/consulte/1-22-43.html', 1), ('http://bj.yuzhua.com/goods/8752368896.html', 1), ('http://p.yuzhua.com/PatentApplication.html?utm_source=360&utm_medium=DS&utm_campaign=ZC&utm_content=ZL&utm_term=zlzc', 1), ('http://ipr.yuzhua.com/consulte/1-22-86.html', 1), ('http://ipr.yuzhua.com/consulte/2-21-1826', 1), ('http://bj.yuzhua.com/goods/6489419514.html', 1), ('http://bj.yuzhua.com/precious/5-----------27-4---------5.html', 1), ('http://ipr.yuzhua.com/consulte/2-21-1755.html', 1), ('http://www.baidu.com/s?wd=8VD8', 1), ('http://bj.yuzhua.com/news/1-20-23.html', 1), ('http://bj.yuzhua.com/goods/5205356364.html', 1), ('http://ipr.yuzhua.com/consulte/2-21-1270.html', 1), ('http://ipr.yuzhua.com/consulte/1-23-23.html', 1), ('http://www.baidu.com/s?wd=LHXS', 1), ('http://ipr.yuzhua.com/consulte/2-21-1076.html', 1), ('http://bj.yuzhua.com/buy/1-----------35-5---------1.html', 1), ('http://ipr.yuzhua.com/consulte/2-23-1925', 1), ('http://ipr.yuzhua.com/consulte/2-20-1039', 1), ('http://wd.yuzhua.com/new.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-2435', 1), ('http://ipr.yuzhua.com/consulte/2-19-2579.html', 1), ('http://bj.yuzhua.com/goods/2500159703.html', 1), ('http://gz.yuzhua.com/goods/3391830225.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-1112.html', 1), ('http://bj.yuzhua.com/goods/1951997220.html', 1), ('http://ipr.yuzhua.com/consulte/2-23-1753.html', 1), ('http://bj.yuzhua.com/buy/1--------4-------------1295.html', 1), ('http://bj.yuzhua.com/news/2-19-335', 1), ('http://ipr.yuzhua.com/consulte/2-22-1634.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-2479.html', 1), ('http://www.baidu.com/s?wd=0J4U', 1), ('http://bj.yuzhua.com/goods/8551780918.html', 1), ('http://r.yuzhua.com/registerQuick?utm_source=baidu&utm_medium=DS&utm_campaign=R-ST&utm_content=r-st01', 1), ('http://www.r.yuzhua.com/', 1), ('http://bj.yuzhua.com/goods/2153806317.html', 1), ('http://zz.yuzhua.com/', 1), ('http://ipr.yuzhua.com/consulte/2-19-1379.html', 1), ('http://ipr.yuzhua.com/consulte/2-23-1888.html', 1), ('http://bj.yuzhua.com/goods/2862057244.html', 1), ('http://www.yuzhua.com/user/order/index/type/4/ahm/0/staff_style/4.html', 1), ('http://bj.yuzhua.com/precious/5------1-----35-5---------94.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-2635', 1), ('http://bj.yuzhua.com/goods/3418584791.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-2270.html', 1), ('http://r.yuzhua.com/registerQuick?utm_source=baidu&utm_medium=DS&utm_campaign=R-CX&utm_content=r-cx', 1), ('http://ipr.yuzhua.com/consulte/2-22-1218.html', 1), ('https://www.baidu.com/link?url=hKZJshNnkd_QO3zM0sq2VF6QsNL-dPAGpk00GClqhXS&wd=&eqid=9b8985080000e4d4000000055b100720', 1), ('http://bj.yuzhua.com/news/2-20-669.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-2684.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-2698.html', 1), ('http://bj.yuzhua.com/goods/8706295905.html', 1), ('http://ipr.yuzhua.com/consulte/1-20-9.html', 1), ('http://wz.yuzhua.com/goods/4577248865.html', 1), ('http://bj.yuzhua.com/goods/7731284911.html', 1), ('http://bj.yuzhua.com/buy/1------1-----3-1---------2.html', 1), ('http://www.baidu.com/s?wd=WVLW', 1), ('http://bj.yuzhua.com/goods/1818221145.html', 1), ('http://www.baidu.com/s?wd=FBEE', 1), ('http://ipr.yuzhua.com/consulte/2-19-1832.html', 1), ('http://help.yuzhua.com/search/%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B3%E9%94%AE%E5%AD%97-0-1.html', 1), ('http://www.yuzhua.com/info.html', 1), ('http://www.yuzhua.com/user.html', 1), ('http://ipr.yuzhua.com/consulte/1-19-117.html', 1), ('http://bj.yuzhua.com/goods/1250411813.html', 1), ('http://bj.yuzhua.com/goods/7720660451.html', 1), ('http://ipr.yuzhua.com/consulte/2-23-2087', 1), ('http://r.yuzhua.com/search/05--\\xe8\\x86\\x8f\\xe5\\x89\\x82--1--.html', 1), ('http://bj.yuzhua.com/goods/9732383274.html', 1), ('http://bj.yuzhua.com/goods/6258057956.html', 1), ('http://ipr.yuzhua.com/consulte/2-20-595.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-2596.html', 1), ('http://bj.yuzhua.com/cover/170801.html', 1), ('http://qy.yuzhua.com/logout.html', 1), ('http://www.yuzhua.com/yzabout', 1), ('http://gz.yuzhua.com/goods/6017343950.html', 1), ('http://bj.yuzhua.com/goods/1796640552.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-2450.html', 1), ('http://bj.yuzhua.com/goods/2053770746.html', 1), ('http://bj.yuzhua.com/goods/1799549035.html', 1), ('http://www.baidu.com/s?wd=65OI', 1), ('https://www.google.com/', 1), ('http://ipr.yuzhua.com/consulte/2-22-2132.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-1697', 1), ('http://ipr.yuzhua.com/consulte/2-19-2512', 1), ('http://ipr.yuzhua.com/consulte/2-20-996', 1), ('http://www2.yuzhua.com/', 1), ('http://ipr.yuzhua.com/consulte/2-22-1810', 1), ('http://bj.yuzhua.com/', 1), ('http://ipr.yuzhua.com/consulte/2-19-2203', 1), ('http://bj.yuzhua.com/goods/2527778451.html', 1), ('http://bj.yuzhua.com/goods/7981660163.html', 1), ('http://www.dizhi.xin/', 1), ('http://bj.yuzhua.com/buy/1-----------9-2---------3.html', 1), ('http://bj.yuzhua.com/news/2-20-3869.html', 1), ('http://wd.yuzhua.com/tmall/212503.html', 1), ('http://bj.yuzhua.com/goods/3877773903.html', 1), ('http://bj.yuzhua.com/goods/9260517141.html', 1), ('http://bj.yuzhua.com/goods/7813320584.html', 1), ('http://ipr.yuzhua.com/consulte/2-21-1874', 1), ('http://p.yuzhua.com/search/--23-3-1--1--1-500-1-1.html', 1), ('http://ipr.yuzhua.com/goods/9001296086', 1), ('http://bj.yuzhua.com/goods/7087217946.html', 1), ('http://r.yuzhua.com/goods/1319228964.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-2551.html', 1), ('http://www.baidu.com/s?wd=O2Z3', 1), ('https://www.baidu.com/link?url=T2JEA1ShIkFY0kAPbk3mmULre2JLAkhw8RQ2-muqQwC&wd=&eqid=8fb9225700020e56000000055b101aab', 1), ('http://bj.yuzhua.com/goods/1497607829.html', 1), ('http://ipr.yuzhua.com/goods/3239027937', 1), ('http://bj.yuzhua.com/news/1-20-1.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-2256.html', 1), ('http://ipr.yuzhua.com/consulte/1-19-94.html', 1), ('http://bj.yuzhua.com/goods/1358069187.html', 1), ('http://ipr.yuzhua.com/consulte/2-23-1291.html', 1), ('http://ipr.yuzhua.com/goods/9467111725', 1), ('http://bj.yuzhua.com/goods/4908464693.html', 1), ('http://bj.yuzhua.com/pack/3------1-----11-2---------100.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-2563', 1), ('http://ipr.yuzhua.com/consulte/2-22-2070', 1), ('http://ipr.yuzhua.com/goods/4360344816', 1), ('http://ipr.yuzhua.com/consulte/2-20-1258', 1), ('http://www.baidu.com/s?wd=EIYP', 1), ('http://ipr.yuzhua.com/consulte/2-19-2760.html', 1), ('http://qy.yuzhua.com/goods/1068801490.html', 1), ('https://www.baidu.com/link?url=isdK6SiqPMfIaScCstc9c33hwtkTWh2jDwiMPznSkeK&wd=&eqid=a0bbb1f40000bae7000000025b0fa97c', 1), ('http://ipr.yuzhua.com/consulte/2-19-1654', 1), ('http://bj.yuzhua.com/goods/9459747222.html', 1), ('http://bj.yuzhua.com/goods/3383804414.html', 1), ('http://bj.yuzhua.com/news/2-20-4251.html', 1), ('http://bj.yuzhua.com/goods/4343716968.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-655', 1), ('http://bj.yuzhua.com/goods/4947572612.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-1341.html', 1), ('http://ipr.yuzhua.com/consulte/2-23-1762.html', 1), ('http://cd.yuzhua.com/goods/4252842520.html', 1), ('http://ipr.yuzhua.com/consulte/1-19-87.html', 1), ('http://bj.yuzhua.com/goods/1558503986.html', 1), ('http://ipr.yuzhua.com/case/50.html', 1), ('http://ipr.yuzhua.com/consulte/1-23-33.html', 1), ('http://bj.yuzhua.com/goods/6680550371.html', 1), ('http://ipr.yuzhua.com/consulte/1-23-16.html', 1), ('http://bj.yuzhua.com/goods/5511480013.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-1557', 1), ('http://ipr.yuzhua.com/consulte/2-19-1189.html', 1), ('http://bj.yuzhua.com/goods/1529025805.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-1255', 1), ('http://ipr.yuzhua.com/consulte/2-21-1820.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-853', 1), ('http://bj.yuzhua.com/buy/1------1-----4-1---------93.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-2706', 1), ('http://bj.yuzhua.com/buy/5---------------------3229.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-2214.html', 1), ('http://wd.yuzhua.com/?utm_source=baidu&utm_medium=DS&utm_campaign=WD&utm_content=A&utm_term=zrpt', 1), ('http://bj.yuzhua.com/news/2-19-4009.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-2362.html', 1), ('http://ipr.yuzhua.com/consulte/2-21-639.html', 1), ('http://p.yuzhua.com/case/27.html', 1), ('http://bj.yuzhua.com/goods/1961180698.html', 1), ('http://wd.yuzhua.com/taobao/143299.html', 1), ('http://r.yuzhua.com/case/7.html', 1), ('http://ipr.yuzhua.com/goods/7263868249', 1), ('http://ipr.yuzhua.com/consulte/2-22-1561', 1), ('https://www.google.com.tw/', 1), ('http://ipr.yuzhua.com/consulte/2-22-2125', 1), ('http://ipr.yuzhua.com/consulte/2-21-1847.html', 1), ('http://ipr.yuzhua.com/consulte/2-19-1304', 1), ('http://ipr.yuzhua.com/consulte/2-22-1385.html', 1), ('http://bj.yuzhua.com/goods/7079738103.html', 1), ('http://mt.yuzhua.com/packageDetail/70', 1), ('http://ipr.yuzhua.com/consulte/2-21-1094.html', 1), ('http://www.baidu.com/s?wd=BE75', 1), ('http://mj.yuzhua.com/search/2------------%E5%85%AD%E5%85%AD---1.html', 1), ('http://bj.yuzhua.com/goods/7576522235.html', 1), ('http://ipr.yuzhua.com/consulte/2-20-1407.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-1708.html', 1), ('http://bj.yuzhua.com/goods/5754112519.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-1764', 1), ('http://bj.yuzhua.com/goods/1041766051.html', 1), ('http://bj.yuzhua.com/goods/4329301914.html', 1), ('http://ipr.yuzhua.com/consulte/2-20-666.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-2740', 1), ('http://ipr.yuzhua.com/goods/7749182307', 1), ('http://ipr.yuzhua.com/consulte/2-23-1164', 1), ('http://bj.yuzhua.com/news/2-23-617.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-1497', 1), ('http://ipr.yuzhua.com/consulte/1-22-93.html', 1), ('http://bj.yuzhua.com/goods/4957727263.html', 1), ('http://ipr.yuzhua.com/goods/5214903565', 1), ('http://ipr.yuzhua.com/consulte/2-19-1166', 1), ('http://bj.yuzhua.com/goods/3045691881.html', 1), ('http://bj.yuzhua.com/goods/3983130314.html', 1), ('http://bj.yuzhua.com/goods/2160145487.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-2218', 1), ('http://help.yuzhua.com/', 1), ('http://ipr.yuzhua.com/consulte/2-22-572', 1), ('http://ipr.yuzhua.com/consulte/2-22-2370.html', 1), ('http://bj.yuzhua.com/goods/2010047956.html', 1), ('http://r.yuzhua.com/', 1), ('http://bj.yuzhua.com/buy/1-----------20-3---------89.html', 1), ('http://ipr.yuzhua.com/consulte/2-21-2736.html', 1), ('http://www.netcraft.com/survey/', 1), ('http://bj.yuzhua.com/goods/4414602288.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-1408.html', 1), ('http://bj.yuzhua.com/goods/7715164864.html', 1), ('http://ipr.yuzhua.com/consulte/1-21-9.html', 1), ('http://bj.yuzhua.com/buy/1-----------3-1---------10.html', 1), ('http://bj.yuzhua.com/goods/8738811470.html', 1), ('http://ipr.yuzhua.com/consulte/2-22-2289.html', 1), ('http://bj.yuzhua.com/goods/2434375287.html', 1), ('http://r.yuzhua.com/search.html', 1), ('http://wd.yuzhua.com/tmall/188755.html', 1), ('http://www.yuzhua.com/index.php/api/order/check/order/100136980531790407180207', 1), ('http://bj.yuzhua.com/buy/1-----------35-5---------3.html', 1), ('http://bj.yuzhua.com/buy/1------8---------------99.html', 1)]
    new_data =[]
    for i in range(len(data)):
        data_url = data[i][0]
        data_url_1 = re.findall(r'http://(.*?)\.com',data_url)
        data_url_2 = re.findall(r'com/(.*?)/', data_url)
        data_unit = ('http://'+get_list(data_url_1)+'.com',get_list(data_url_2),data[i][1])
        new_data.append(data_unit)
    print new_data
    sheet ='test'
    in_excel2(new_data,sheet)











