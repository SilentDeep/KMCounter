# import platform

# platform = platform.system()

from flask import Flask, render_template, jsonify, request
import json
from datetime import datetime
import math

from utils import *

app = Flask(__name__)

def load_data(data_file):
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    data = load_data('./data.json')
    return render_template('index.html', data=data)

@app.route('/fetch_key_counts', methods=['POST'])
def fetch_key_counts():
    request_json = request.json
    start_time = datetime.strptime(str(request_json.get('start_time')), '%Y-%m-%dT%H:%M')
    end_time = datetime.strptime(str(request_json.get('end_time')), '%Y-%m-%dT%H:%M')
    
    data = load_data('./data.json')
    filtered_data = {time: counts for time, counts in data.items() if start_time <= datetime.strptime(time, time_format) <= end_time}
    merge_keys = {'~': '`', '!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7', '*': '8', '(': '9', ')': '0', '_': '-', '+': '=', 
                  'q': 'Q', 'w': 'W', 'e': 'E', 'r': 'R', 't': 'T', 'y': 'Y', 'u': 'U', 'i': 'I', 'o': 'O', 'p': 'P','{': '[', '}': ']', '|': '\\',
                  'a': 'A', 's': 'S', 'd': 'D', 'f': 'F', 'g': 'G', 'h': 'H', 'j': 'J', 'k': 'K', 'l': 'L', ':': ';', '"\'"': "'", '"': "'",
                  'z': 'Z', 'x': 'X', 'c': 'C', 'v': 'V', 'b': 'B', 'n': 'N', 'm': 'M', '<': ',', '>': '.', '?': '/'}
    key_counts = {}
    for counts in filtered_data.values():
        for key, count in counts.items():
            merged_key = merge_keys.get(key, key)
            if merged_key in key_counts:
                key_counts[merged_key] += count
            else:
                key_counts[merged_key] = count
    max_count_k = max(count for key, count in key_counts.items() if not key.startswith('Button.'))
    max_count_m = max(count for key, count in key_counts.items() if key.startswith('Button.'))
    key_counts_rate = {key: math.log(count, max_count_k) for key, count in key_counts.items() if not key.startswith('Button.')}
    key_counts_rate.update({key: math.log(count, max_count_m) for key, count in key_counts.items() if key.startswith('Button.')})
    # print(key_counts_rate)
    return jsonify(key_counts, key_counts_rate)

@app.route('/fetch_total_key_counts')
def fetch_total_key_counts():
    data = load_data('./data.json')
    total_key_counts = {time: sum(counts.values()) for time, counts in data.items()}
    return jsonify(total_key_counts)

@app.route('/end_program', methods=['POST'])
def end_program():
    os._exit(0)

def run_frontend():
    app.run(debug=True)