# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from ip_mess import get_mess
from in_dataframe import in_dataframe


def unique_ip_list(falname):
    df = in_dataframe(falname)
    unique_ip_list = []
    for client_ip in df['ip'].unique():
        mess =get_mess(client_ip)
        if '阿里' in mess or '腾讯' in mess:
        # if '美国' in mess:
            unique_ip_list.append(client_ip)
    return unique_ip_list



if __name__ == "__main__":
    print unique_ip_list()

















