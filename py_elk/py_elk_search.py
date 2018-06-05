# -*- coding: utf-8 -*-
'''
家南，3023787540@qq.com
'''
from datetime import datetime
from elasticsearch import Elasticsearch
import redis
import urllib
import json
import re
import pygal
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

es = Elasticsearch("172.17.6.106")

def in_redis(ip,mess):
    # r = redis.Redis(host='192.168.94.133', port=6379, db=0, password='123')
    r.set(ip,mess)
def out_redis(ip):
    # r = redis.Redis(host='192.168.94.133', port=6379, db=0, password='123')
    mess = r.get(ip)
    return mess
url = "http://ip.taobao.com/service/getIpInfo.php?ip="
def ip_find(ip):
    print '网络查询'
    data = urllib.urlopen(url + ip).read()
    datadict = json.loads(data)
    for oneinfo in datadict:
        if "code" == oneinfo:
            if datadict[oneinfo] == 0:
                return datadict["data"]["country"] + datadict["data"]["region"] + datadict["data"]["city"] +datadict["data"]["isp"]
def w_file(file_name,date):
    out_file = open(file_name, 'a+')
    print >> out_file,date
def get_mess(ip):
    location=out_redis(ip)
    try:
        if location == None:
            location = ip_find(ip)
            in_redis(ip, location)
    except:
        w_file('error_ip.txt',ip)
    return location
def body_search(body,size):
    res = es.search(
        index='httpd-yz-0514_2018.05.25',
        size = size,
        body=body,
        request_timeout=30
    )
    return res



pool = redis.ConnectionPool(host='172.17.6.106', port=6379,password='123', decode_responses=True)
r = redis.Redis(connection_pool=pool)
body1= {
    "query":{
        "match_all":{}
    }
}
body2={
"query":{
        "bool":{
            "must_not":[
                {
                    "term":{
                        "request":"public"
                    }
                },
                {
                    "term":{
                        "request":"ajax"
                    }
                },
                {
                    "term":{
                        "agent":"spider"
                    }
                }
            ]
        }
    }
}
body3={
"query":{
        "bool":{
            "must":[
                {
                    "term":{
                        "request":"utm_source"
                    }
                }
            ],
            "must_not":[
                {
                    "term":{
                        "agent":"spider"
                    }
                }
            ]
        }
    }
}

#查询ip---------------------------------------------------------------------
# #
#获取size总计
result_file='result_0514.txt'
res0=body_search(body2,0)
totle_num = res0['hits']['total']
print '去除public、ajax、spider，点击量总计：'+str(totle_num)

res_totle=body_search(body2,totle_num)
resss_totle= res_totle['hits']['hits']
print '去除public、ajax、spider，点击量总计：'+str(len(resss_totle))
w_file(result_file,'去除public、ajax、spider，点击量总计：'+str(len(resss_totle)))
ip_list_all =[]
ip_list_all_dict={}
ip_list_real=[]
ip_list_real_dict={}
ip_list_yun=[]
request_list=[]
referer_list=[]
request_dict={}
referer_dict={}
ip_list_all_utm_dict={}

#client ip分析---------------------------------------------------------------------
#
for line in resss_totle:
    try:
        source = line['_source']
        clientip =source['clientip']
        # clientip = re.findall(r"clientip': u'(.*?)',", str(source))[0]
        ip_list_all.append(clientip)
        mess =get_mess(clientip)
        if '阿里' in mess or '腾讯' in mess:
            ip_list_yun.append(clientip)
        else:
            ip_list_real.append(clientip)
            # print len(ip_list_real)
    except Exception,ex:
        # print Exception, ":", ex
        continue
        w_file('error_ip.txt',line)

ip_list_all2 = list(set(ip_list_all))
print '独立ip:'+str(ip_list_all2)
print '独立ip数:'+str(len(ip_list_all2))
w_file(result_file,'独立ip数:'+str(len(ip_list_all2)))
for item_ip in ip_list_all2:
    ip_list_all_dict[item_ip]=ip_list_all.count(item_ip)
print ip_list_all_dict
# w_file(result_file,ip_list_all_dict)
    # print str(item_ip)+':'+str(ip_list_all.count(item_ip))
# print ip_list_all
#

ip_list_real2 = list(set(ip_list_real))
print '去除云平台独立ip:'+str(ip_list_real2)
print '去除云平台独立ip数:'+str(len(ip_list_real2))
w_file(result_file,'去除云平台独立ip数:'+str(len(ip_list_real2)))
for item_ip in ip_list_real2:
    ip_list_real_dict[item_ip]=ip_list_real.count(item_ip)
    # print str(item_ip)+':'+str(ip_list_real.count(item_ip))
print ip_list_real_dict
# w_file(result_file,ip_list_real_dict)
#
ip_list_yun2 = list(set(ip_list_yun))
print '云平台独立ip:'+str(ip_list_yun2)
print '云平台独立ip数:'+str(len(ip_list_yun2))
w_file(result_file,'云平台独立ip数:'+str(len(ip_list_yun2)))
#请求分析---------------------------------------------------------------------

for line in resss_totle:
    try:
        source = line['_source']
        request_m =source['request']
        #print request_m
        request_mess = re.findall(r'/(.*?)/',request_m)
        if len(request_mess)==0:
            request_mess =request_m
        elif len(request_mess)>0:
            request_mess = request_mess[0]
        #print request_mess
        request_list.append(request_mess)
    except Exception,ex:
        # print Exception, ":", ex
        continue
        w_file('error_request.txt',line)

request_list2 = list(set(request_list))
print '请求地址:'+str(request_list2)
print '请求地址数:'+str(len(request_list2))
w_file(result_file,'请求地址数:'+str(len(request_list2)))
for item in request_list2:
    request_dict[item]=request_list.count(item)
    # print str(item)+':'+str(request_list.count(item))
print request_dict
# w_file(result_file,request_dict)
line_chart = pygal.HorizontalBar()
line_chart.title = 'request(>300)'
for k,v in request_dict.items():
    # print k,v
    if v >300:
        w_file(result_file,str(k)+':'+str(v))
        line_chart.add(k, v)
        line_chart.render_to_file('request_0514.svg')
#来源分析---------------------------------------------------------------------

for line in resss_totle:
    try:
        source = line['_source']
        referer_m =source['Referer']
        # print referer_m
        referer_mess = re.findall(r'//(.*?)/',referer_m)
        if len(referer_mess)==0:
            referer_mess =referer_m
        elif len(referer_mess)>0:
            referer_mess = referer_mess[0]
        # print referer_mess
        referer_list.append(referer_mess)
    except Exception,ex:
        # print Exception, ":", ex
        continue
        w_file('error_request.txt',line)

referer_list2 = list(set(referer_list))
print '来源地址:'+str(referer_list2)
print '来源地址数:'+str(len(referer_list2))
w_file(result_file,'来源地址数:'+str(len(referer_list2)))
for item in referer_list2:
    referer_dict[item]=referer_list.count(item)
    # print str(item)+':'+str(referer_list.count(item))
print referer_dict
# w_file(result_file,referer_dict)
line_chart = pygal.HorizontalBar()
line_chart.title = 'referer(>500)'
for k,v in referer_dict.items():
    # print k,v
    if v >500:
        w_file(result_file, str(k) + ':' + str(v))
        line_chart.add(k, v)
        line_chart.render_to_file('referer_0514.svg')
#查询推广---------------------------------------------------------------------
res_utm=body_search(body3,5)
totle_utm = res_utm['hits']['total']
# print res_utm['hits']['hits']
# print res_utm
print '推广点击量总计：'+str(totle_utm)
w_file(result_file,'推广点击量总计：'+str(totle_utm))
res_totle_utm=body_search(body3,totle_utm)
resss_totle_utm= res_totle_utm['hits']['hits']
# print res_totle_utm
# print '去除public、ajax、spider，点击量总计：'+str(len(resss_totle_utm))
ip_list_all_utm =[]
ip_list_real_utm=[]
ip_list_yun_utm=[]
for line_utm in resss_totle_utm:
    # print type(line)
    # print line['_source']['clientip']
    # print 1
    try:
        source = line_utm['_source']
        # print source
        # print 2
        source2 =source['request']
        clientip = re.findall(r"utm_source=(.*?)&", str(source2))[0]
        ip_list_all_utm.append(clientip)
        mess =get_mess(clientip)
        if '阿里' in mess or '腾讯' in mess:
            ip_list_yun_utm.append(clientip)
        else:
            ip_list_real_utm.append(clientip)
    except Exception,ex:
        # print Exception, ":", ex
        # print 3
        continue
        w_file('error.txt',line_utm)
# print ip_list_all_utm
ip_list_all_utm2 = list(set(ip_list_all_utm))
print '推广渠道:'+str(ip_list_all_utm2)
print '推广渠道数:'+str(len(ip_list_all_utm2))
w_file(result_file,'推广渠道数:'+str(len(ip_list_all_utm2)))
for item in ip_list_all_utm2:
    ip_list_all_utm_dict[item]=ip_list_all_utm.count(item)
    # print str(item)+':'+str(referer_list.count(item))
print ip_list_all_utm_dict
w_file(result_file,ip_list_all_utm_dict)
# w_file(result_file,referer_dict)
line_chart = pygal.HorizontalBar()
line_chart.title = 'utm'
for k,v in ip_list_all_utm_dict.items():
    # print k,v
    # if v >50:
    line_chart.add(k, v)
    line_chart.render_to_file('utm_0514.svg')








