# -*- coding: utf-8 -*-
'''
家南，3023787540@qq.com
'''
import os
from py_clean_access import clean_access
from pd_show import pd_show

path = 'access_20180517.log'
if os.path.isdir(path):
    for filenames in os.walk(path):
        filenames_list = filenames[-1]
        for filename in filenames_list:
            print path+filename
            clean_access(path+filename)
            os.rename(path+filename,path+filename+'_pass.log')

else:
    print path
    clean_access(path)
    os.rename(path, path +'_pass.log')


pd_show('result.txt')










