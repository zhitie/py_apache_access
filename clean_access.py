# -*- coding:utf-8 -*-

from ip_check import unique_ip_list
import re
import os
'''
日志格式示例：
111.231.176.99 - - [15/May/2018:00:01:09 +0800] "HEAD / HTTP/1.1" 301 - "-" "-"
61.158.148.36 - - [15/May/2018:00:01:09 +0800] "GET /servicecheck/user HTTP/1.1" 200 37 "http://www.yidian51.com/utm_source=306&jd/f12-g8" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
111.231.176.99 - - [15/May/2018:00:01:09 +0800] "HEAD / HTTP/1.1" 200 - "-" "-"
40.77.167.47 - - [15/May/2018:00:01:09 +0800] "GET /buylist/t11-g98-f2-p2 HTTP/1.1" 200 27784 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
123.126.113.84 - - [15/May/2018:00:01:10 +0800] "GET /jd/g14-f34-s4 HTTP/1.1" 200 23674 "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"
'''
def w_file(file_name,date):
    out_file = open(file_name, 'a+')
    print >> out_file,date
def clean_access(filename):
    yun_ip_list =unique_ip_list(filename)
    print yun_ip_list
    for line in open(filename):
        action_line =0
        try:
            client_ip = re.findall(r'(.*?) - - ',line)
            if client_ip[0] in yun_ip_list:
                # print client_ip[0]
                action_line = 'drop'
                w_file('drop_yun.txt', line.replace('\n', ''))
        except:
            action_line = 'drop_except'
        try:
            request_url = re.findall(r'] "(.*?)"',line)
            pass_request_list = [".css", ".js", ".jpg", ".png", ".gif"]
            for pass_request in pass_request_list:
                pass_request_re =re.search(pass_request, str(request_url))
                if pass_request_re != None:
                    action_line = 'drop'
                    w_file('drop_static.txt', line.replace('\n', ''))
        except:
            action_line = 'drop_except'
        try:
            request_refer = line.split('"')[-4]
            if request_refer == '-':
                action_line = 'drop'
                w_file('drop_none.txt', line.replace('\n', ''))
        except:
            action_line = 'drop_except'
        try:
            request_agent = line.split('"')[-2]
            # print request_agent
            if 'spider' in request_agent:
                action_line = 'drop'
                w_file('drop_spider.txt', line.replace('\n', ''))
        except:
            action_line = 'drop_except'
        if action_line == 'drop_except':
            w_file('drop_except.txt', line.replace('\n', ''))
        elif action_line != 'drop':
            w_file('result.txt', line.replace('\n', ''))


if __name__ == "__main__":
    clean_access('access_20180528.log')
    # clean_access('access2.log')

























