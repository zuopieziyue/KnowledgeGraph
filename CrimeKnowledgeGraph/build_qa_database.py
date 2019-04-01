# -*- coding: utf-8 -*-  
########################  
#author:gongyue  
#date:2019/04/02  
########################  
import os
import time

import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import pymongo

class ProcessIntoES:
    def __init__(self):
        self._index = "crime_data"
        self.es = Elasticsearch([{"host": "127.0.0.1", "port": 9200}])
        self.doc_type = "crime"
        cur = "/".join(os.path.abspath(__file__).split('/')[:-1])
        self.music_file = os.path.join(cur, 'qa_corpus.json')

    '''创建ES索引，确定分词类型'''
    def create_mapping(self):
        node_mapping = {
        
        }


if __name__ == "__main__":
    # 将数据库插入到elasticsearch当中
    # init_ES()
    # 按照标题进行查询
    question = '我老公要起诉离婚 我不想离婚怎么办'
    


