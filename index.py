import jieba.analyse
#准备语料
corpus = "《知否知否应是绿肥红瘦》是由东阳正午阳光影视有限公司出品，侯鸿亮担任制片人，张开宙执导，曾璐、吴桐编剧，赵丽颖、冯绍峰领衔主演，朱一龙、施诗、张佳宁、曹翠芬、刘钧、刘琳、高露、王仁君、李依晓、王鹤润、张晓谦、李洪涛主演，王一楠、陈瑾特别出演的古代社会家庭题材电视剧"

#textrank
keywords_textrank = jieba.analyse.textrank(corpus)
print(keywords_textrank)