# -*- coding: utf-8 -*-
'''
家南，3023787540@qq.com
'''
from list_in_excel import in_excel
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from in_dataframe import in_dataframe

def pd_show(filename):
    yun_ip_list = []
    yun_ip_dict = {}
    refer_unique_dict={}
    request_unique_dict={}
    ip_unique_dict={}
    utm_unique_dict={}
    df = in_dataframe(filename)
    top_ip = df['ip'].value_counts()
    top_referer = df['referer'].value_counts()      #TOP Referer
    top_agent  = df['agent'].value_counts()      #TOP User-Agent
    top_request  = df['request'].value_counts()     #TOP URL
    # referer------------------------
    referer_list = top_referer.index
    for i in range(len(referer_list)):
        referer = re.findall(r'://(.*?)/', referer_list[i])
        if len(referer) == 0:
            refer_unique4 = referer_list[i]
        else:
            refer_unique4 = referer[0]
        try:
            refer_unique_dict[refer_unique4]=top_referer[referer_list[i]]+refer_unique_dict[refer_unique4]
        except:
            refer_unique_dict[refer_unique4] = top_referer[referer_list[i]]
    # request------------------------
    request_list = top_request.index
    for i in range(len(request_list)):
        request = re.findall(r'GET /(.*?)/', request_list[i])
        if len(request) == 0:
            try:
                request_unique4 = request_list[i].split(' ')[1]
            except:
                request_unique4 = request_list[i]
        else:
            request_unique4 = request[0]
        try:
            request_unique_dict[request_unique4] = top_request[request_list[i]]+request_unique_dict[request_unique4]
        except:
            request_unique_dict[request_unique4] = top_request[request_list[i]]
    # ip------------------------
    ip_list = top_ip.index
    for i in range(len(ip_list)):
        ip = ip_list[i]
        ip_unique_dict[ip] = top_ip[i]


    # 推广-----------------------
    referer_list = top_referer.index
    for i in range(len(referer_list)):
        utm_source = re.findall(r"utm_source=(.*?)&", referer_list[i])
        if len(utm_source) != 0:
            utm_source= utm_source[0]
            try:
                utm_unique_dict[utm_source]=top_referer[referer_list[i]]+utm_unique_dict[utm_source]
            except:
                utm_unique_dict[utm_source] = top_referer[referer_list[i]]

    # '--------输出------------------------------------------------------------------------------------------------'
    refer_unique_list = sorted(refer_unique_dict.items(), key=lambda v: v[1],reverse =True)
    ip_unique_listt = sorted(ip_unique_dict.items(), key=lambda v: v[1],reverse =True)
    request_unique_list = sorted(request_unique_dict.items(), key=lambda v: v[1],reverse =True)
    utm_unique_list = sorted(utm_unique_dict.items(), key=lambda v: v[1],reverse =True)
    in_excel(refer_unique_list,'refer')
    in_excel(ip_unique_listt,'ip')
    in_excel(request_unique_list,'request')
    in_excel(utm_unique_list,'utm')







