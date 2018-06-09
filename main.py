# -*- coding: utf-8 -*-
from clean_access import clean_access
from ip_user_follow import region_follow,city_follow,visit_time_follow
from in_excel_openpyxl import in_excel,in_excel2,in_excel3
from refer_user_follow import user_follow1,user_follow2,user_follow3,user_follow4

clean_access('access_20180528.log')
# clean_access('access2.log')

index = ('referer', 'referer_num')
result_file = "user_analysis.xlsx"
sheet_name1 = 'region'
region_list = region_follow('result.txt')
in_excel(region_list, result_file, sheet_name1,2,'A','B',1)
sheet_name2 = 'city'
city_list = city_follow('result.txt')
in_excel(city_list, result_file, sheet_name2,2,'A','B',1)
sheet_name3 = 'visit_time'
visit_time_list = visit_time_follow('result.txt')
in_excel(visit_time_list, result_file, sheet_name3,2,'A','B',1)

result_file = "user_analysis.xlsx"
index = ('referer', 'referer_num')
sheet_tite = 'request'
data_list = user_follow3('result.txt', index)
# print data_list
in_excel3(['referer'], result_file, sheet_tite)
in_excel2(data_list, result_file, sheet_tite)

index1 = ('referer', 'referer_num')
sheet_tite1 = 'referer'
data_list1 = user_follow1('result.txt', index1)
in_excel(data_list1, result_file,sheet_tite1,2,'A','B',1)

index2 = ('referer', 'request_next', 'request_num')
sheet_tite2 = 'request'
data_list2 = user_follow2('result.txt',index2)
in_excel(data_list2, result_file, sheet_tite2,3,'B','C',2)

index3 = ('utm', 'utm_num')
sheet_tite3 = 'utm'
data_list3 = user_follow4('result.txt', index3)
in_excel(data_list3, result_file, sheet_tite3, 2, 'A', 'B', 1)