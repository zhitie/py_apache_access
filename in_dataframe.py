# -*- coding: utf-8 -*-
'''
家南，3023787540@qq.com
'''
import pandas as pd


# 将日志读入DataFrame
def in_dataframe(filename):
    reader = pd.read_table(filename, sep=' ', names=[i for i in range(10)], iterator=True)
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
    states = ['ip','a','b','date_time','c','request','status_code','d','referer','agent']
    df.columns =states
    return df




