# -*- coding:utf-8 -*-

from pd_access_unique import unique_ip_list
import re
import os


def w_file(file_name,date):
    out_file = open(file_name, 'a+')
    print >> out_file,date

def clean_access(filename):
    yun_ip_list =unique_ip_list(filename)
    print yun_ip_list
    for line in open(filename):
        # print line,#逗号不产生空格
        action_line =0
        try:
            client_ip = re.findall(r'(.*?) - - ',line)
            if client_ip[0] in yun_ip_list:
                action_line = 'drop'
        except:
            action_line = 'drop'
        try:
            request_url = re.findall(r'] "(.*?)"',line)
            pass_request_list = [".css", ".js", ".jpg", ".png", ".gif"]
            for pass_request in pass_request_list:
                pass_request_re =re.search(pass_request, str(request_url))
                if pass_request_re != None:
                    action_line = 'drop'
        except:
            action_line = 'drop'
        try:
            request_refer = line.split('"')[-4]
            if request_refer == '-':
                action_line = 'drop'
        except:
            action_line = 'drop'
        try:
            request_agent = line.split('"')[-2]
            # print request_agent
            if 'spider' in request_agent:
                action_line = 'drop'
        except:
            action_line = 'drop'
        if action_line != 'drop':
            w_file('result.txt',line.replace('\n',''))




























