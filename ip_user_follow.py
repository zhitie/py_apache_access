# -*- coding: utf-8 -*-

from in_excel_openpyxl import in_excel
import datetime
# from ip_mess import get_mess2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from in_dataframe import in_dataframe
import pandas as pd

def get_list(data):
    try:
        data2=data[0].replace(' HTTP','')
    except:
        data2=''
    return data2
def region_follow(df):
    region_follow_list=[('region','num')]

    # df = in_dataframe(filename)

    # top_ip = df['ip'].value_counts()
    # ip_list = top_ip.index

    top_region = df['region'].value_counts()
    region_list = top_region.index

    # top_city = df['city'].value_counts()
    # cit_list = top_city.index

    for i in range(len(region_list)):
        region = region_list[i]
        region_follow_list.append((region,top_region[region]))
    return region_follow_list
def city_follow(df):
    city_follow_list=[('city','num')]

    # df = in_dataframe(filename)

    # top_ip = df['ip'].value_counts()
    # ip_list = top_ip.index

    # top_region = df['region'].value_counts()
    # region_list = top_region.index

    top_city = df['city'].value_counts()
    cit_list = top_city.index

    for i in range(len(cit_list)):
        region = cit_list[i]
        city_follow_list.append((region,top_city[region]))
    return city_follow_list
def visit_time_follow(df):
    visit_time_follow_list=[('time','num')]
    # df = in_dataframe(filename)
    top_visit_time = df['time_format'].value_counts()
    visit_time_list = top_visit_time.index
    for i in range(len(visit_time_list)):
        region = visit_time_list[i]
        visit_time_follow_list.append((region,top_visit_time[region]))
    return visit_time_follow_list


if __name__ == "__main__":
    index = ('referer', 'referer_num')
    result_file = "user_analysis.xlsx"
    filename = 'result.txt'
    df = in_dataframe(filename)

    sheet_name1 = 'region'
    region_list = region_follow(df)
    in_excel(region_list, result_file, sheet_name1,2,'A','B',1)
    sheet_name2 = 'city'
    city_list = city_follow(df)
    in_excel(city_list, result_file, sheet_name2,2,'A','B',1)
    sheet_name3 = 'visit_time'
    visit_time_list = visit_time_follow(df)
    in_excel(visit_time_list, result_file, sheet_name3,2,'A','B',1)






