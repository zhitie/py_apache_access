# -*- coding: utf-8 -*-
'''
家南，3023787540@qq.com
'''
import redis
import urllib
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# '--------ip查询------------------------------------------------'
pool = redis.ConnectionPool(host='172.17.6.140', port=6379,password='123', decode_responses=True)
r = redis.Redis(connection_pool=pool)
def in_redis(ip,mess):
    r.set(ip,mess)
def out_redis(ip):
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