#!/usr/bin/env python

import psutil
import json
import time
from datetime import datetime
import argparse


parser = argparse.ArgumentParser(description='My example explanation')
parser.add_argument(
    '--time',
    type=int,
    default=300,
    help='time'
)
parser.add_argument(
    '--type',
    type=str,
    default='text',
    help='text or json'
)
my_namespace = parser.parse_args()


def system_info():
    cpu_overall = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    memory = psutil.virtual_memory()[0]
    virtual_memory = psutil.virtual_memory()[3]
    io = psutil.disk_io_counters()[0:2]
    network = psutil.net_io_counters()
    snapshot = {'cpu_overall': cpu_overall,
                'total memory': memory,
                'virtual memory': virtual_memory,
                'IO': io,
                'network': network,
                }
    return snapshot


def display(info, n):
    snapshot = info
    result = (f"SNAPSHOT {n} : {datetime.now()}\n"
              f"CPU overall load     | {snapshot['cpu_overall']}\n"
              f"Memory usage         | {snapshot['total memory']}\n"
              f"Virtual memory usage | {snapshot['virtual memory']}\n"
              f"IO                   | {snapshot['IO']}\n"
              f"Network              | {snapshot['network']}\n")
    return result


def display_json(info, n):
    snapshot = info
    result = f"SNAPSHOT {n} : {datetime.now()}\n" \
             f"{json.dumps(snapshot)}\n"
    return result


def output():
    interval = my_namespace.time
    file_type = my_namespace.type
    info = system_info()
    counter = 1
    while True:
        if file_type == 'text':
            with open('result', 'a') as file:
                file.writelines(display(info=info, n=counter) + '\n')
        elif file_type == 'json':
            with open('result', 'a') as file:
                file.writelines(display_json(info=info, n=counter) + '\n')
        time.sleep(interval)
        counter += 1


if __name__ == "__main__":
    output()
