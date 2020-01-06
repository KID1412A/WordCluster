# 从训练好的词向量模型中读取词及其对应词向量
import os
import gensim
from gensim.models import word2vec

bisDir = r'D:/pb/test/mid_process/'
model_path = bisDir + 'word2vec.vector'
word_from_model_write_path = bisDir + 'RealWord.txt'
vector_from_model_write_path = bisDir + 'RealWordVec.txt'


def load_word2vec_object(source_data_path):
    with open(source_data_path, 'r', encoding='utf-8') as word_vector_file:
        words = []
        vectors = []
        line = word_vector_file.readline()  # 按行读取词向量模型中的词及其对应向量
        while line:
            tmp = line.split()  # 将读出的词和词向量分割
            words.append(tmp[0])  # 存词
            vectors.append(tmp[1:])  # 存词对应向量
            line = word_vector_file.readline()  # 继续读，直至读完
    return words, vectors


def main():
    word_from_model, vector_from_model = load_word2vec_object(model_path)
    # 将从词向量模型中读出的词写入TXT方便后续处理
    f_write = open(word_from_model_write_path, 'w', encoding='utf-8')
    for index in range(1, len(word_from_model)):
        f_write.write(word_from_model[index] + ' ')

    # 将从词向量模型中读出的词向量的各个维度写入TXT方便后续处理
    fv_write = open(vector_from_model_write_path, 'w', encoding='utf-8')
    for index in range(1, len(vector_from_model)):
        for i in range(0, len(vector_from_model[index])):
            fv_write.write(vector_from_model[index][i] + ' ')
        fv_write.write('\n')


if __name__ == '__main__':
    main()
