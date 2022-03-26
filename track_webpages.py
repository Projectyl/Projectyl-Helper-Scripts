#!/bin/python

from tqdm import tqdm
from multiprocessing import Pool
import csv
import requests
import os


def check(url_info):
    name, url = url_info
    bit = 0
    try:
        txt = requests.get(url).text
        if os.path.exists(data_folder + name + '-old'):
            open(data_folder + name + '-new', 'w').write(txt)
            if not open(data_folder + name + '-new', 'r').read() == open(data_folder + name + '-old', 'r').read():
                bit = 1
            else:
                os.replace(data_folder + name + '-new', data_folder + name + '-old')
        else:
            open(data_folder + name + '-old', 'w').write(txt)
    except:
        bit = 2
    return  bit, name, url


data_folder = "./url_data/"
if not os.path.exists(data_folder):
    os.mkdir(data_folder)

url_folder = "../projectyl.github.io/_data/summer/"
files = os.listdir(url_folder)
files = [file for file in files if ".csv" in file]
url_infos = [[dat[0], dat[-1]] for file in files for dat in list(csv.reader(open(url_folder+file, 'r'), delimiter=','))[2:]]
url_outputs = tqdm(Pool().imap(check, url_infos), total=len(url_infos))

for bit, name, url in sorted(url_outputs):
    sign = '✓' if bit == 0 else ('' if bit == 1 else '✗')
    print (sign, '\t', name, url)
