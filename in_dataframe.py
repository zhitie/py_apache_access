# -*- coding: utf-8 -*-
import re
import datetime
import pandas as pd
from ip_mess import get_mess2
'''
222.77.241.144 - - [31/May/2018:00:19:09 +0800] "GET / HTTP/1.0" 200 431831 "http://ym.yuzhua.com/" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)"
114.47.119.111 - - [31/May/2018:00:33:22 +0800] "GET / HTTP/1.1" 200 43301 "https://www.google.com.tw/" "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
'''
def get_list(data):
    try:
        data2=data[0].replace(' HTTP','')
    except:
        data2=''
    return data2
def in_dataframe(filename):
    # print '导入---------------------------------------------'
    reader = pd.read_table(filename, sep=' ', names=[i for i in range(10)], iterator=True, low_memory=False)
    loop = True
    chunkSize = 10000000
    chunks = []
    while loop:
     try:
         chunk = reader.get_chunk(chunkSize)
         chunks.append(chunk)
     except StopIteration:
         loop = False
    df = pd.concat(chunks, ignore_index=True)
    states = ['ip','a','b','date_time','c','request','status_code','data_size','referer','agent']
    df.columns =states
    for i in ['a','b','c']:
        del df[i]
    # print df.columns
    # print '列数据---------------------------------------------'
    referer_list = df['referer']
    referer_list2=[]
    referer_list3=[]
    utm_list=[]

    date_time_list=df['date_time']

    request_list = df['request']
    request_list2 = []

    time_format_list = []

    ip_list = df['ip']
    region_list = []
    city_list = []
    # print '处理---------------------------------------------'
    # datasize_list = df['data_size']
    drop_i_list =[]
    for i in range(len(df)):
        referer = referer_list[i]
        try:
            referer2 = re.findall(r'//(.*?)\.com', referer)
        except:
            referer2=''
            # continue
        referer_list2.append(get_list(referer2))
        try:
            referer3 = re.findall(r'com/(.*?)/', referer)
        except:
            referer3=''
            # continue
        referer_list3.append(get_list(referer3))
        # print i,referer2,referer3
        try:
            utm = re.findall(r'utm_source=(.*?)&', referer)
        except:
            utm=''
            # continue
        utm_list.append(get_list(utm))

        date_time = date_time_list[i].replace('[', '')
        time_format = datetime.datetime.strptime(date_time, '%d/%b/%Y:%H:%M:%S').strftime("%Y/%m/%d/%H")
        # print time_format.strftime("%d/%m/%Y/%H")
        time_format_list.append(time_format)
        #
        request = request_list[i]
        request2 = re.findall(r' /(.*?)/', request)
        request_list2.append(get_list(request2))
        #
        region =get_mess2(ip_list[i],2)
        region_list.append(region)
        city = get_mess2(ip_list[i],3)
        city_list.append(city)
        # print region,city
    # print len(referer_list2)
    # print len(referer_list3)
    # print len(time_format_list)
    # print len(request_list2)
    # print len(region_list)
    # print len(city_list)
    df['utm'] = utm_list
    df['referer2'] = referer_list2
    df['referer3'] = referer_list3
    df['time_format'] = time_format_list
    df['request2']=request_list2
    df['region']=region_list
    df['city'] = city_list

    del df['date_time']
    # print df.columns
    # print df['utm']
    return df
def in_dataframe2(filename):
    # print '导入---------------------------------------------'
    reader = pd.read_table(filename, sep=' ', names=[i for i in range(10)], iterator=True, low_memory=False)
    loop = True
    chunkSize = 10000000
    chunks = []
    while loop:
     try:
         chunk = reader.get_chunk(chunkSize)
         chunks.append(chunk)
     except StopIteration:
         loop = False
    df = pd.concat(chunks, ignore_index=True)
    states = ['ip','a','b','date_time','c','request','status_code','data_size','referer','agent']
    df.columns =states
    return df
if __name__ == "__main__":
    in_dataframe('result.txt')
    # in_dataframe('access2.log')
    # in_dataframe('access_20180528.log')


