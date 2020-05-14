#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
from matplotlib.ticker import FuncFormatter
from matplotlib.font_manager import FontProperties  # 字体管理器

# 设置汉字格式
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)


def file_name(file_dir):
    File_Name=[]
    for files in os.listdir(file_dir):
        if os.path.splitext(files)[1] == '.txt': #只读txt文件
            File_Name.append(files)
    return File_Name

def to_percent(y):
        return '%1.1f'%(100*y) + '%'

def main():
    # P_PUNum文件夹
    path = r'C:\Users\45452\OneDrive\科研\HEVC_CNN_信息隐藏EMD pro\HM-16.15\bin\vc2010\Win32\Debug\批处理 Cover\QP=32\pu文件\P_PUNum'
    os.chdir(path)

    txt_file_name = file_name("./")
    for item in txt_file_name:
        plt.clf()  # clear figure
        data = np.loadtxt(item)

        # Normalization
        data = np.sum(data, axis=0)
        all_data = np.sum(data)
        data = data / all_data

        # axis setting
        x = range(len(data))
        # plt.xticks(x,["4*4","8*8","8*4","4*8","16*16","16*8",
        #               "8*16","16*4","4*16","16*12","12*16","32*32","32*16","16*32",
        #               "32*24","24*32","32*8","8*32","64*64","64*32","32*64","64*48",
        #               "48*64","64*16","16*64"],fontsize=5)
        plt.xticks(x)
        plt.yticks(np.arange(0, 0.3, 0.025))
        plt.title(txt_file_name[1].strip(".txt"))
        # plt.title('1080P视频25种大小的PU数量占比', fontproperties=font) 中文字体需要加个属性
        def to_percent(y, position):
            return '%1.1f' % (100 * y) + '%'

        plt.bar(x, data)
        formatter = FuncFormatter(to_percent)
        plt.gca().yaxis.set_major_formatter(formatter)
        # plt.show()
        plt.savefig(item + '.png', dpi=600)



if __name__ == '__main__':
    main()



