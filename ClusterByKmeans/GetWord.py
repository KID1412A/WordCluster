# 将聚类好的TXT中非汉字的字符串过滤掉

import os


# 判断一个unicode是否是汉字
def is_chinese(uchar):
    if (uchar >= u'\u4e00') and (uchar <= u'\u9fa5'):
        return True
    else:
        return False


# 获取所有汉字
def real_word(content):
    # print("Get Word")
    content_str = ''
    cnt = 0
    for cur_str in content:
        if is_chinese(cur_str):
            content_str = content_str + cur_str
            if cnt < (len(content) - 1):
                content_str = content_str + ' '
    return content_str


def main():
    cur_path = r'D:/pb/test/result/word_cluster_by_kmeans/'
    cnt = 0  # 当前TXT的名字
    while cnt < len(os.listdir(cur_path)):
        """当前处理的TXT"""
        cur_name = str(cnt) + '.txt'
        cur_name = cur_path + cur_name

        """读取TXT中内容"""
        my_str1 = open(cur_name, 'r', encoding='utf-8')
        read_data = my_str1.read()
        my_str1.close()

        """将读出的内容按空格分割后存在list里"""
        out_str = read_data.split()

        """过滤汉字以外的信息"""
        out_str = real_word(out_str)

        """连续多个空格合并为一个空格"""
        out_str = ' '.join(out_str.split())

        """处理完的字符串写入原TXT"""
        useful_f = open(cur_name, 'w', encoding='utf-8')
        useful_f.write(out_str)
        useful_f.close()

        cnt = cnt + 1


if __name__ == '__main__':
    main()
    print("Get Word")