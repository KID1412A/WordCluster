# 过滤单个汉字

import os


def format_str(old_str):
    new_str = ''
    cnt = 0
    for cur_str in old_str:
        # j = len(cur_str)
        if len(cur_str) > 1:
            new_str = new_str + cur_str
            if cnt < (len(old_str) - 1):
                new_str = new_str + ' '
        cnt = cnt + 1
    return new_str


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

        """过滤单个汉字"""
        out_str = format_str(out_str)

        """连续多个空格合并为一个空格"""
        out_str = ' '.join(out_str.split())

        """处理完的字符串写入原TXT"""
        useful_f = open(cur_name, 'w', encoding='utf-8')
        useful_f.write(out_str)
        useful_f.close()

        cnt = cnt + 1


if __name__ == '__main__':
    main()
    print("Useful Word")