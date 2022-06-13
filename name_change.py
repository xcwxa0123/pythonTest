#coding=Shift_JIS
import os
import re
for file_name in os.listdir('./test/'):
    if re.search(r'\d+', file_name):
        start, end = re.search(r'\d+', file_name).span()
        new_name = file_name[start:end:]
        os.rename('./test/%s'%file_name, './test/%s'%new_name)