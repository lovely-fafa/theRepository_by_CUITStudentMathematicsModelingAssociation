#!/usr/bin/python 3.10
# -*- coding: utf-8 -*- 
#
# @Time    : 2022-07-27 23:47
# @Author  : 发发
# @QQ      : 1315337973
# @File    : 航班管家爬虫.py
# @Software: PyCharm

import csv
from concurrent import futures
import requests
import pandas as pd
import time
import tqdm
import random


def get_data(start_time, end_time, air="CTU"):
    url_get_data = "https://data-api.133.cn/api/v1/airport/statistics"
    params = {
        "airport": air,
        "route_type": "all",
        "start_time": start_time,
        "end_time": end_time
    }
    headers = {
        "Authorization": 复制粘贴你的,
        "Origin": "https://dast.133.cn",
        "Referer": "https://dast.133.cn/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "client-id": 复制粘贴你的,
        "Content-Type": "application/x-www-form-urlencoded",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }
    resp = requests.get(url=url_get_data, params=params, headers=headers)
    resp_json = resp.json()
    arr_plan = resp_json["data"]["fluctuation"]["arr_plan"]  # 计划进港
    arr_real = resp_json["data"]["fluctuation"]["arr_real"]  # 实际进港
    dep_plan = resp_json["data"]["fluctuation"]["dep_plan"]  # 计划出港
    dep_real = resp_json["data"]["fluctuation"]["dep_real"]  # 实际出港

    data_list = arr_plan + arr_real + dep_plan + dep_real
    return data_list


def main(da):
    data = get_data(start_time=da, end_time=da)
    dataWriter.writerow([da] + data)


if __name__ == '__main__':
    with open("CTU_data_twoYears.csv", mode="a", encoding="utf-8", newline="") as f:
        dataWriter = csv.writer(f)

        for date in tqdm.tqdm(pd.date_range("2020-06-25", "2022-07-27")):
            date_str = str(date.date())
            main(date_str)
            time.sleep(random.random() + 2)  # 一定要 2 秒以上，不然大概率封号一阵子

        # tasks = []
        # with futures.ThreadPoolExecutor(20) as t:
        #     for date in pd.date_range("2020-01-01", "2022-07-27"):
        #         tasks.append(t.submit(main, date))
        #     print("爬")
        #     for task in tqdm.tqdm(futures.as_completed(tasks), total=len(tasks)):
        #         task.result()
