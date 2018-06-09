# -*- coding: utf-8 -*-
import redis
import urllib
import json
from in_excel_openpyxl import in_excel3
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# '--------ip查询------------------------------------------------'
def new_user(ip,local_region,local_city):
    # new_user_list =[]
    result_file = "user_analysis.xlsx"
    sheet_tite = 'new_user'
    in_excel3([ip,local_region,local_city],result_file,sheet_tite)
def in_redis(ip,mess):
    r.set(ip,mess)
def out_redis(ip):
    mess = r.get(ip)
    return mess
url = "http://ip.taobao.com/service/getIpInfo.php?ip="
def ip_find(ip):
    print '网络查询1'
    data = urllib.urlopen(url + ip).read()
    datadict = json.loads(data)
    for oneinfo in datadict:
        if "code" == oneinfo:
            if datadict[oneinfo] == 0:
                new_user(ip, datadict["data"]["region"], datadict["data"]["city"])
                return datadict["data"]["country"] + datadict["data"]["region"] + datadict["data"]["city"] +datadict["data"]["isp"]
def ip_find2(ip):
    print '网络查询2'
    data = urllib.urlopen(url + ip).read()
    datadict = json.loads(data)
    for oneinfo in datadict:
        if "code" == oneinfo:
            if datadict[oneinfo] == 0:
                new_user(ip,datadict["data"]["region"],datadict["data"]["city"])
                return [datadict["data"]["country"],datadict["data"]["region"],datadict["data"]["city"],datadict["data"]["isp"]]

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
        w_file('error_get_mess.txt',ip)
    return location
def get_mess2(ip,num):
    try:
        if num ==0:
            location_num = out_redis(ip)
            if location_num == None:
                location_num_list = ip_find2(ip)
                # print type(location_num_list)
                location_num2=''
                for i in location_num_list:
                    # print i,type(i)
                    location_num2=location_num2+str(i)
                    # print location_num
                location_num = location_num2
                in_redis(ip, location_num2)
                in_redis(ip + '-3', location_num_list[2])
                in_redis(ip + '-2', location_num_list[1])
        else:
            location_num=out_redis(ip+'-'+str(num))
            if location_num == None:
                location_num_list = ip_find2(ip)
                # print type(location_num_list)
                location_num2 = ''
                for i in location_num_list:
                    # print i,type(i)
                    location_num2 = location_num2 + str(i)
                    # print location_num
                location_num =location_num_list[num]
                in_redis(ip, location_num2)
                in_redis(ip + '-3', location_num_list[2])
                in_redis(ip + '-2', location_num_list[1])
    except:
        w_file('error_get_mess2.txt',ip)
    return location_num
pool = redis.ConnectionPool(host='172.17.6.140', port=6379,password='123', decode_responses=True,db=5)
r = redis.Redis(connection_pool=pool)
if __name__ == "__main__":
    # local_region= get_mess2('42.236.48.52',2)
    # local_city = get_mess2('42.236.48.52',3)
    # print local_region,local_city
    print get_mess2('1.186.41.175',0)
    # print get_mess2('1.186.41.175', 2)
    # print get_mess2('1.186.41.175', 3)




