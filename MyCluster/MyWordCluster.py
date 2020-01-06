# MyClusterWord（簇中心查找改进）

# data：2019.12.12
# 李腾飞

import os
import random
import time
import gensim
from gensim.models import word2vec


# 写文件
def write_file(write_file_path, write_str):
    f = open(write_file_path, 'a', encoding='utf-8')
    f.write(write_str + ' ')
    f.close()


# 读文件
def read_file(read_file_path):
    f = open(read_file_path, 'r', encoding='utf-8')
    read_str = f.read()
    file_str = read_str.split()  # 按空格分割存入list
    return file_str


def swap(a, b):
    return b, a


# 按当前词和簇心词相似度排序（低->高）,对应索引也随着相似度值一起排序
def bubble_sort_by_similarity(arr_similarity, correspond_index):
    end_index = len(arr_similarity) - 1
    cnt = end_index
    while cnt:
        for j in range(0, end_index):
            if arr_similarity[j] > arr_similarity[j+1]:
                arr_similarity[j], arr_similarity[j+1] = swap(arr_similarity[j], arr_similarity[j+1])
                correspond_index[j], correspond_index[j+1] = swap(correspond_index[j], correspond_index[j+1])
        end_index = end_index - 1
        cnt = cnt - 1
    return arr_similarity, correspond_index


bisDir = r'D:/pb/test/'

"""存放真实有效的词"""
# real_word_filePath = bisDir + 'mid_process/new_cut_word.txt'
real_word_filePath = bisDir + 'mid_process/NewRealWord.txt'

"""存放簇心词"""
cluster_center_file_name = bisDir + 'result/my_word_cluster1/0.txt'

"""自增长寻找簇心聚类"""
cluster_result_file_path = bisDir + 'result/my_word_cluster1/'  # 聚类结果存放文件夹地址

model = word2vec.Word2Vec.load(bisDir + 'mid_process/word2vec.model')


def get_cluster_center():
    center_word = []
    # 获取第一个簇的簇心
    txt_read = read_file(real_word_filePath)
    word_sum_cnt = len(txt_read)
    first_cluster_center = random.randint(0, word_sum_cnt - 1)
    center_word.append(txt_read[first_cluster_center])
    # 获取其他k-1个簇心
    for cur_word in txt_read:
        cluster_center_index = 0
        while cluster_center_index < len(center_word):
            # 当前词和簇心词相似度计算
            cur_word_similar_with_other_center = model.wv.similarity(cur_word, center_word[cluster_center_index])
            if cur_word_similar_with_other_center > 0.25:  # 当前词和已确定簇心词相似度大于0.25则为当前词不可能为簇心词
                break
            else:
                cluster_center_index = cluster_center_index + 1
        if cluster_center_index == len(center_word):
            center_word.append(cur_word)
        if len(center_word) == 20:  # 聚类个数
            break
    # print(center_word)
    f_write_cluster_center = open(cluster_center_file_name, 'a', encoding='utf8')
    for i in center_word:
        f_write_cluster_center.write(i + ' ')
    return center_word


def cluster_by_center_word(center_word):
    original_data = read_file(real_word_filePath)
    # 遍历待聚类的词，和簇心词一一计算相似度，放入最相似的簇心词对应的TXT
    for current_word in original_data:
        similar_value = []
        correspond_index = []
        cnt = 1  # 每个簇心词对应存放的TXT，从1开始是因为0.txt存的是所有簇心
        for cur_center_word in center_word:
            similar = model.wv.similarity(current_word, cur_center_word)
            similar_value.append(float(similar))
            correspond_index.append(int(cnt))
            cnt = cnt + 1
        # 将当前待处理词和所有簇心词计算相似度后按相似度排序（低->高）
        similar_value, correspond_index = bubble_sort_by_similarity(similar_value, correspond_index)
        index = len(correspond_index) - 1
        nxt_cluster = True  # 相似度最高的类已饱和，查看下一个类
        while nxt_cluster and index > -1:
            cur_max_similar_center_index = correspond_index[index]
            cur_cluster_txt_name = cluster_result_file_path + str(cur_max_similar_center_index) + '.txt'
            read_data = read_file(cur_cluster_txt_name)
            max_n = len(original_data) / len(os.listdir(cluster_result_file_path))
            # print(max_n)
            # 相似度最高的类未饱和，将当前词聚入此类
            if len(read_data) < (max_n + 1):
                write_file(cur_cluster_txt_name, current_word)
                nxt_cluster = False
            else:
                index = index - 1  # 相似度最高的类饱和，查看相似度次高者
    # 将当前词聚类到最相似的簇中
    # original_data = read_file(real_word_filePath)
    # for current_word in original_data:
        # cur_max_similar = 0
        # cur_max_similar_center_index = 0
        # cur_center_index = 0
        # for cur_center_word in center_word:
            # similar = model.wv.similarity(current_word, cur_center_word)
            # if similar > cur_max_similar:
            #     cur_max_similar = similar
            #     cur_max_similar_center_index = cur_center_index + 1  # 加1是因为0.TXT中存的是簇心
            # cur_center_index = cur_center_index + 1
        # cur_cluster_txt_name = cluster_result_file_path + str(cur_max_similar_center_index) + '.txt'
        # write_file(cur_cluster_txt_name, current_word)


def cluster_txt(center_word):
    cnt = 0
    while cnt < len(center_word):
        cur_cluster_txt_name = cluster_result_file_path + str(cnt + 1) + '.txt'
        write_file(cur_cluster_txt_name, center_word[cnt])
        cnt = cnt + 1


def main():
    center_word = get_cluster_center()
    cluster_txt(center_word)
    cluster_by_center_word(center_word)
    

# 开始计时
start_time = time.time()

if __name__ == '__main__':
    main()

end_time = time.time()  # 结束计时
# 计算聚类耗时
print(('cluster word time cost', end_time-start_time, 's'))
