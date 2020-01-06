# 简单处理分词结果，过滤汉字以外信息，过滤单个汉字
import os
import random
import time
import gensim
from gensim.models import word2vec
from collections import OrderedDict

import sys
sys.path.append('../')
from ClusterByKmeans.GetWord import real_word
from ClusterByKmeans.UsefulWord import format_str

bisDir = r'D:/pb/test/'


# 写文件
def write_file(write_file_path, write_str):
    f = open(write_file_path, 'w', encoding='utf-8')
    f.write(write_str)
    f.close()


# 读文件
def read_file(read_file_path):
    f = open(read_file_path, 'r', encoding='utf-8')
    read_str = f.read()
    file_str = read_str.split()  # 按空格分割存入list
    return file_str


# cut_word_filePath = bisDir + 'mid_process/cut_word.txt'
# new_cut_word_filePath = bisDir + 'mid_process/new_cut_word.txt'
cut_word_filePath = bisDir + 'mid_process/RealWord.txt'
new_cut_word_filePath = bisDir + 'mid_process/NewRealWord.txt'


# 过滤汉字以外信息
def chinese_word():
    chinese_character = read_file(cut_word_filePath)
    chinese_character = real_word(chinese_character)
    write_file(new_cut_word_filePath, chinese_character)


# 过滤单个汉字
def useful_word():
    useful_chinese_word = read_file(new_cut_word_filePath)
    useful_chinese_word = format_str(useful_chinese_word)
    write_file(new_cut_word_filePath, useful_chinese_word)


# 简单统计上述处理后字符串的个数
def simple_count():
    original_word = read_file(cut_word_filePath)
    i = len(original_word)
    print("原始单词共" + str(i) + "个")
    # print(original_word)

    chinese_word()
    china_word = read_file(new_cut_word_filePath)
    j = len(china_word)
    print("汉字共" + str(j) + "个")
    # print(china_word)

    useful_word()
    useful_china_word = read_file(new_cut_word_filePath)
    k = len(useful_china_word)
    print("有效汉字共" + str(k) + "个")
    # print(useful_china_word)

    useful_china_word = ' '.join(OrderedDict.fromkeys(useful_china_word))
    write_file(new_cut_word_filePath, useful_china_word)

    no_repeat_useful_china_word = read_file(new_cut_word_filePath)
    n = len(no_repeat_useful_china_word)
    print("无重复有效汉字共" + str(n) + "个")


def main():
    simple_count()


if __name__ == '__main__':
    main()
