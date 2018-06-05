# -*- coding: utf-8 -*-

import xlsxwriter

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














