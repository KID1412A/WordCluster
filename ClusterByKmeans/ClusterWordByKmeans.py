import numpy as np
from sklearn import metrics
from sklearn.cluster import KMeans

baseDir = r'D:/pb/test/'

with open(baseDir + "mid_process/word2vec.vector", 'r', encoding='utf-8') as word_vector_file:
# with open(baseDir + "mid_process/small_word2vec.vector", 'r', encoding='utf-8') as word_vector_file:
# with open(baseDir + "mid_process/more_small_word2vec.vector", 'r', encoding='utf-8') as word_vector_file:
    words = []
    vectors = []
    word_vector_file.readline()
    line = word_vector_file.readline()
    while line:
        tmp = line.split()
        words.append(tmp[0])
        vectors.append(tmp[1:])
        line = word_vector_file.readline()

    # scores = []
    # for k in range (2, 10):
    #     labels = KMeans(n_clusters=k).fit(vectors).labels_
    #     score = metrics.silhouette_score(vectors, labels)
    #     scores.append(score)
    #     print('这个是k={}次时的轮廓系数：'.format(k), score)

    kmeans = KMeans(n_clusters=20, n_jobs=-1)
    kmeans.fit(vectors)
    for index, cluster_id in enumerate(kmeans.labels_):
        with open(baseDir + 'result/word_cluster_by_kmeans/' + str(cluster_id) + '.txt', mode='a', encoding='utf-8') as words_file:
            if words[index] != ' ':
                words_file.write(words[index] + ' ')