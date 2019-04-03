# -*- coding: utf-8 -*-  
import os
import time
import json
from elasticsearch import Elasticsearch
import numpy as np
import jieba.poseseg as pseg

class CrimeQA:
    def __init__(self):
        self._index = "crime_data"
        self.es = Elasticsearch([{"host": "127.0.0.1", "port": 9200}])
        self.doc_type = "crime"
        cur = "/".join(os.path.abspath(__file__).split('/')[:-1])
        self.embedding_path = os.path.join(cur, 'embedding/word_vec_300.bin')
        self.embedding_dict = self.load_embedding(self.embedding_path)
        self.embedding_size = 300
        self.min_score = 0.4
        self.min_sim = 0.8

    '''根据question进行事件的匹配查询'''
    def search_specific(self, value, key="question"):
        query_body = {
            "query": {
                "match": {
                    key: value
                }
            }
        }
        searched = self.es.search(index=self._index, doc_type=self.doc_type, body=query_body, size=20)
        #输出查询到的结果
        return searched['hits']['hits']

    '''基于ES的问题查询'''
    def search_es(self, question):
        answers = []
        res = self.search_specific(question)
        for hit in res:
            answer_dict = []
            answer_dict['score'] = hit['_score']
            answer_dict['sim_question'] = hit['_source']['question']



    def search_es(self, question):
        answers = []
        res = self.search_specific(question)
        for hit in res:
            answer_dict = {}
            answer_dict['score'] = hit['_score']
            answer_dict['sim_question'] = hit['_source']['question']
            answer_dict['answers'] = hit['_source']['answers'].split('\n')
            answers.append(answer_dict)
        return answers











if __name__ == "__main__":
    handler = CrimeQA()
    while(1):
        question = input('question:')
        final_answer = handler.search_main(question)
        print('answers:', final_answer)




