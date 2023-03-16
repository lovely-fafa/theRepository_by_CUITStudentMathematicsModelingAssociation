#程序文件Pex2_48_1.py
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np
n, p=5, 0.4
x=np.arange(6); y=binom.pmf(x,n,p)
plt.subplot(121); plt.plot(x, y, 'ro')
plt.vlines(x, 0, y, 'k', lw=3, alpha=0.5)  #vlines(x, ymin, ymax)画竖线图
#lw设置线宽度，alpha设置图的透明度
plt.subplot(122); plt.stem(x, y, use_line_collection=True)
plt.savefig("figure2_48.png", dpi=500); plt.show()
