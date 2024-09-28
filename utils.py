from datetime import datetime
from random import choice
import platform
import string
import shutil
import json
import os

os_type = platform.system() # Windows, Darwin
# print(os_type)
date_format = '%Y-%m-%d'
time_format = '%Y-%m-%d %H:%M'

version = '1.2.0'

settings_file = os.path.join('.', 'settings.json')

data_file = os.path.join('.', 'data.json') # 弃用
data_file_dir = os.path.join('.', 'data')

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(choice(characters) for _ in range(length))

def copy_file(src, dst):
    shutil.copyfile(src, dst)
    # with open(src, 'rb') as f_src:
    #     with open(dst, 'wb') as f_dst:
    #         f_dst.write(f_src.read())

def time_it(func): # 测试用
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f"'{func.__name__}()' runtime: {end_time - start_time}")
        return result
    return wrapper

def get_date():
    return datetime.now().strftime(date_format)

def get_time():
    return datetime.now().strftime(time_format)

def get_data_path(date = datetime.now().strftime(date_format)):
    return os.path.join(data_file_dir, f'{date}.json')

def load_settings(settings, settings_file):
    if os.path.exists(settings_file):
        with open(settings_file, 'r', encoding='utf-8') as f:
            if f.read() == '':
                settings = {}
            else:
                f.seek(0)
                settings = json.load(f)
    else:
        settings = {'track_keyboard': True, 'track_mouse': True}
    return settings

def save_settings(settings, settings_file):
    with open(settings_file, 'w', encoding='utf-8') as f:
        json.dump(settings, f)

def load_data(data_file):
    if os.path.exists(data_file):
        with open(data_file, 'r', encoding='utf-8') as f:
            if f.read() == '':
                data = {}
            else:
                f.seek(0)
                data = json.load(f)
    else:
        data = {}
    return data

# @time_it
def save_data(data, data_file):
    if os.path.exists(data_file):
        tmp_data_file = f'{data_file}.{generate_random_string(8)}.tmp' # 避免程序中断，data文件未写完
        copy_file(data_file, tmp_data_file)
        with open(tmp_data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f)
        copy_file(tmp_data_file, data_file)
        try:
            os.remove(tmp_data_file)
        except Exception as e:
            print('Error: ', e)
    else:
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f)
