from datetime import datetime
import json
import os

time_format = '%Y-%m-%d %H:%M'

def get_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M')

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

def load_data(data, data_file):
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

def save_data(data, data_file):
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f)