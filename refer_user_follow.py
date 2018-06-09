# -*- coding: utf-8 -*-

from in_excel_openpyxl import in_excel
from in_excel_openpyxl import in_excel2
from in_excel_openpyxl import in_excel3
import datetime
import re
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
def user_follow1(filename,index):
    user_follow_list = [index]
    df = in_dataframe(filename)
    top_referer = df['referer2'].value_counts()  # TOP Referer
    referer_list = top_referer.index
    for i in range(len(referer_list)):
        referer = referer_list[i]
        user_follow_list.append((referer + '.com', top_referer[referer]))
    return user_follow_list
def user_follow2(filename,index):
    user_follow_list = [index]
    df = in_dataframe(filename)
    top_referer = df['referer2'].value_counts()  # TOP Referer
    referer_list = top_referer.index
    for i in range(len(referer_list)):
        referer = referer_list[i]
        df_request_count = df.loc[(df['referer2'] == referer)]['request2'].value_counts()
        df_request_name_index= df_request_count.index
        for i in range(len(df_request_name_index)):
            df_request_name2= df_request_count[df_request_name_index[i]]
            user_follow_list.append((df_request_name_index[i],df_request_name2))
    return user_follow_list
def user_follow3(filename,index):
    user_follow_list = [index]
    df = in_dataframe(filename)
    top_referer = df['referer2'].value_counts()  # TOP Referer
    referer_list = top_referer.index
    for i in range(len(referer_list)):
        referer = referer_list[i]
        df_request_count = df.loc[(df['referer2'] == referer)]['request2'].value_counts()
        user_follow_list.append((referer+'.com',len(df_request_count.index)))
    return user_follow_list
def user_follow4(filename,index):
    user_follow_list = [index]
    df = in_dataframe(filename)
    top_utm = df['utm'].value_counts()  # TOP Referer
    utm_list = top_utm.index
    for i in range(len(utm_list)):
        utm = utm_list[i]
        if utm != '':
            df_utm_count = df.loc[(df['utm'] == utm)]['utm'].value_counts()
            user_follow_list.append((utm,df_utm_count[utm]))
    print user_follow_list
    return user_follow_list
if __name__ == "__main__":
    result_file = "user_analysis.xlsx"
#request
    index = ('referer', 'referer_num')
    sheet_tite = 'request'
    data_list = user_follow3('result.txt', index)
    # print data_list
    in_excel3(['referer'], result_file, sheet_tite)
    in_excel2(data_list, result_file, sheet_tite)

    index2 = ('referer', 'request_next', 'request_num')
    sheet_tite2 = 'request'
    data_list2 = user_follow2('result.txt', index2)
    in_excel(data_list2, result_file, sheet_tite2, 3, 'B', 'C', 2)
#referer
    index1 = ('referer', 'referer_num')
    sheet_tite1 = 'referer'
    data_list1 = user_follow1('result.txt', index1)
    in_excel(data_list1, result_file,sheet_tite1,2,'A','B',1)
# utm
    index3 = ('utm', 'utm_num')
    sheet_tite3 = 'utm'
    data_list3 = user_follow4('result.txt', index3)
    in_excel(data_list3, result_file, sheet_tite3, 2, 'A', 'B', 1)



