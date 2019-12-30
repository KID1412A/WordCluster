# -*- coding: utf-8 -*-
import jieba
import jieba.analyse
import jieba.posseg as pseg
import re
from pyltp import NamedEntityRecognizer


# jieba.load_userdict('userdict.txt')
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist(r'D:\\pb\\test\\sources\\stopwords.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


# final
inputs = open('D:\\pb\\test\\sources\\text.txt', 'r', encoding='utf-8')
outputs = open('D:\\pb\\test\\mid_process\\cut_word.txt', 'w', encoding='utf-8')

# small_word
# inputs = open('D:\\pb\\test\\sources\\small.txt', 'r', encoding='utf-8')
# outputs = open('D:\\pb\\test\\mid_process\\small_cut_word.txt', 'w', encoding='utf-8')

# more_small_word
# inputs = open('D:\\pb\\test\\sources\\more_small.txt', 'r', encoding='utf-8')
# outputs = open('D:\\pb\\test\\mid_process\\more_small_cut_word.txt', 'w', encoding='utf-8')

for line in inputs:
    line_seg = seg_sentence(line)  # 这里的返回值是字符串
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()

