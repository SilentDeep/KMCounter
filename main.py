from pynput import keyboard, mouse
# import webbrowser

from utils import *
from display import run_frontend

settings_file = './settings.json'
data_file = './data.json'
settings = {}
data = {}

def k_on_press(key):
    if get_time() not in data:
        data[get_time()] = {}
    key = str(key).strip("'")
    if key in data[get_time()]:
        data[get_time()][key] += 1
    else:
        data[get_time()][key] = 1
    save_data(data, data_file)

def m_on_click(x, y, button, pressed):
    if pressed:
        if get_time() not in data:
            data[get_time()] = {}
        if str(button) in data[get_time()]:
            data[get_time()][str(button)] += 1
        else:
            data[get_time()][str(button)] = 1
        save_data(data, data_file)

if __name__ == '__main__':
    data = load_data(data, data_file)
    # settings = load_settings(settings, settings_file)
    listener_k = keyboard.Listener(on_press=k_on_press)
    listener_k.start()
    listener_m = mouse.Listener(on_click=m_on_click)
    listener_m.start()
    # webbrowser.open('http://127.0.0.1:5000')
    run_frontend()