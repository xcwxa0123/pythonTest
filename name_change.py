#coding=Shift_JIS
import os
import re

def transe_name(data_params):
    for file_name in os.listdir(data_params.get('TEXTFILE_PATH')):
        if re.search(r'\d+', file_name):
            start, end = re.search(r'\d+', file_name).span()
            new_name = file_name[start:end:]
            os.rename('{0}/{1}'.format(data_params.get('TEXTFILE_PATH'), file_name), '{0}/{1}'.format(data_params.get('TEXTFILE_PATH'), new_name))