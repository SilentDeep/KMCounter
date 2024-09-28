from pynput import keyboard, mouse
import pyautogui
import webbrowser

from utils import *
from display import run_frontend

settings = {}
data = {}

def k_on_press(key):
    date = get_date()
    time = get_time()
    if date not in data:
        data[date] = {}
    if time not in data[date]:
        data[date][time] = {}
    key = str(key).strip("'")
    if key in data[date][time]:
        data[date][time][key] += 1
    else:
        data[date][time][key] = 1
    save_data(data[date], get_data_path(date))

def m_on_click(x, y, button, pressed):
    if pressed:
        date = get_date()
        time = get_time()
        if date not in data:
            data[date] = {}
        if time not in data[date]:
            data[date][time] = {}
            
        name_button = str(button)
        screen_width, screen_height = pyautogui.size()
        name_position = f'{name_button}_position_{int(x / screen_width * 100)}_{int(y / screen_height * 100)}'
        
        if name_button in data[date][time]:
            data[date][time][name_button] += 1
        else:
            data[date][time][name_button] = 1
        if name_position in data[date][time]:
            data[date][time][name_position] += 1
        else:
            data[date][time][name_position] = 1
            
        save_data(data[date], get_data_path(date))

if __name__ == '__main__':
    date = get_date()
    if os.path.exists(data_file) and not os.path.exists(data_file_dir): # v1.0->v1.1 迁移数据
        copy_file(data_file, data_file + '.bak') # 备份数据
        os.mkdir(data_file_dir)
        data = load_data(os.path.join('.', 'data.json'))
        new_data = {}
        for key in data.keys():
            date = key[0:10]
            if date not in new_data:
                new_data[date] = {}
            new_data[date][key] = data[key]
        for date in new_data:
            save_data(new_data[date], get_data_path(date))
    data[date] = load_data(get_data_path(date))
    if os.path.exists(get_data_path(date)):
        copy_file(get_data_path(date), get_data_path(date) + '.bak') # 备份数据
    else:
        if not os.path.exists(data_file_dir):
            os.mkdir(data_file_dir)
        data[date] = {}
    for file_name in os.listdir(data_file_dir):
        if file_name.endswith('.tmp'):
            # print(os.path.join(data_file_dir, file_name))
            os.remove(os.path.join(data_file_dir, file_name))
    # print('\n\n\ntest\n\n\n')
    # settings = load_settings(settings, settings_file)
    listener_k = keyboard.Listener(on_press=k_on_press)
    listener_k.start()
    listener_m = mouse.Listener(on_click=m_on_click)
    listener_m.start()
    webbrowser.open('http://127.0.0.1:5000')
    run_frontend()