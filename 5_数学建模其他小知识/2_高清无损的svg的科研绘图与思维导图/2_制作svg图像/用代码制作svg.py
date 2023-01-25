#!/usr/bin/python 3.10
# -*- coding: utf-8 -*- 
#
# @Time    : 2023-01-25 16:34
# @Author  : 发发
# @QQ      : 1315337973
# @GitHub  : https://github.com/lovely-fafa
# @File    : 用代码制作svg.py
# @Software: PyCharm

import matplotlib.pyplot as plt

plt.style.use("seaborn-pastel")

plt.figure(figsize=(10, 10), dpi=300)

plt.bar([0, 1, 2, 3], [10, 23, 20, 7])
plt.savefig(r'./pic/pic.jpg')
plt.savefig(r'./pic/pic.png')
plt.savefig(r'./pic/pic.svg')  # 保存的格式是 svg
plt.show()
