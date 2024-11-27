from time import sleep

import requests
import datetime
import threading

API_URL = "https://blockchain.info/ticker"

values_list = []


def get_curr_value():
    while True:
        resp = requests.get(API_URL).json()
        values_list.append(resp["USD"]['last'])
        sleep(1)


def print_current_value():
    while True:
        if values_list and len(values_list)<20:
            print(f"latest value: {values_list[-1]} USD, Average: N/A,  date: {datetime.datetime.now()}")
        elif values_list:
            print(f"latest value: {values_list[-1]} USD, Average: {sum(values_list[-20:]) / 20}, date: {datetime.datetime.now()}")
        sleep(4)



task_1 = threading.Thread(target=get_curr_value)
task_2 = threading.Thread(target=print_current_value)

task_1.start()
task_2.start()

task_1.join()
task_2.join()

