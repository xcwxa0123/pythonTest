import os
from bs4 import BeautifulSoup
from trans_params import KAKUYOMU_PARAMS as PARAMS_DATA

# HTML文件转为txt
# path=要读的文件的全路径; name=文件名; write_path=写入路径
def trans_text(path, name, write_path, params_data):
    temp_file = open(path, encoding='utf-8', errors='ignore')
    content = temp_file.read()
    soup = BeautifulSoup(content, 'html.parser')
    js_episode_body = soup.find_all('div', class_=params_data.get('TARGET_DOM_CLASS'))
    temp_all_text = js_episode_body[0].strings
    temp_file.close()

    transe_file = open('{0}/{1}.txt'.format(write_path, name), mode='w', encoding='utf-8')
    transe_file.write(''.join(list(temp_all_text)))
    transe_file.close()

# 找一下文件夹在不在目标目录下，不在就创建
def find_dir(name, params_data, path='./'):
    def _mk_target_dir():
        os.mkdir(params_data.get('WRITE_DIR_NAME'))
    temp_dir_list = os.listdir(path)
    if name not in temp_dir_list:
        return _mk_target_dir

def transe_start(params_data):
    # 创建目标目录
    target = find_dir(params_data.get('WRITE_DIR_NAME'), params_data, params_data.get('TARGET_CREATE_PATH'))
    target() if target else None
    # 开始转写
    file_list = os.listdir(params_data.get('TEXTFILE_PATH'))
    for file_name in file_list:
        trans_text('{0}/{1}'.format(params_data.get('TEXTFILE_PATH'), file_name), file_name, '{0}/{1}'.format(params_data.get('TARGET_CREATE_PATH'), params_data.get('WRITE_DIR_NAME')), params_data)

transe_start(PARAMS_DATA)
