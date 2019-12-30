# import gensim
from gensim.models import word2vec
import logging

baseDir = r'D:/pb/test/mid_process/'
# 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u"D:\\pb\\test\\mid_process\\cut_word.txt")  # 加载语料
# sentences = word2vec.Text8Corpus(u"D:\\pb\\test\\mid_process\\small_cut_word.txt")
# sentences = word2vec.Text8Corpus(u"D:\\pb\\test\\mid_process\\more_small_cut_word.txt")

model = word2vec.Word2Vec(sentences, min_count=1, size=50)  # 默认window=5

# final
model.save(baseDir + u'word2vec.model')
model.wv.save_word2vec_format(baseDir + u'word2vec.vector')

# small
# model.save(baseDir + u'small_word2vec.model')
# model.wv.save_word2vec_format(baseDir + u'small_word2vec.vector')

# more_small
# model.save(baseDir + u'more_small_word2vec.model')
# model.wv.save_word2vec_format(baseDir + u'more_small_word2vec.vector')
