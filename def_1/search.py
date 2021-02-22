# coding: utf-8
# File: AmmeRevision
# Update: 2021/2/21

from py2neo import Graph
import pandas as pd

class searcher:
    def __init__(self):
        # 建立数据库连接
        self.g = Graph(
            host="127.0.0.1",
            http_port=7474,
            user="neo4j",
            password="amme")
        self.num_limit = 20
        # print('search 初始化完成')

    '''执行cypher查询，并返回相应结果'''
    def def1_main_search(self, Qstring):
        flag=0
        print("小助手：")
        # 结点和关系查询
        query1 = "MATCH (n) where n.name=$name return labels(n) as Type, n.name as Name"
        query2 = "MATCH (a)-[r]->(b) where b.name = $name return a.name as start_node, r.name as rel_type, b.name as end_node"
        nodes_data = self.g.run(query1,name=Qstring).data()
        links_data = self.g.run(query2, name=Qstring).data()
        if nodes_data:
            flag=1
            print("一、查询的医疗信息如下：")
            # print(pd.DataFrame(nodes_data))
            for node in nodes_data:
                print(node)
        if links_data:
            flag = 1
            print("二、查询医疗相关联信息如下：")
            # print(pd.DataFrame(links_data))
            for link in links_data:
                print(link)

        data=[]
        data = self.g.find_one(label='Disease',property_key='name', property_value=Qstring)
        if data:
            flag = 1
            print("三、关于疾病的具体信息如下：")
            print('（1）疾病名称：',dict(data)['name'])
            print('（2）疾病症状：',dict(data)['desc'])
            print('（3）疾病预防：',dict(data)['prevent'])
            print('（4）治疗方式：',dict(data)['cure_way'])
            print('（5）起因：',dict(data)['cause'])
            print('（6）治疗持续时长：',dict(data)['cure_lasttime'])
            print('（7）治愈可能性：',dict(data)['cured_prob'])
            print('（8）建议查看科室：',dict(data)['cure_department'])
            print('（9）易感人群：',dict(data)['easy_get'])
        if not flag:
            return 0
        else:
            return 1

if __name__ == '__main__':
    searcher = searcher()


