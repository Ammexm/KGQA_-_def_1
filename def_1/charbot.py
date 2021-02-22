# coding: utf-8
# File: AmmeRevision
# Update: 2021/2/21

from def_1.search import *

'''问答部分'''
class chat:
    def __init__(self):
        # print("定义 Searcher 类型的成员变量 searcher ")
        self.searcher = searcher()

    def chat_main(self, Qstring):
        # def_1 单一字符串直接查询:
        # 输入单一字符串，返回类型为 1对多 或者 多对1
        answer = '抱歉，小助手暂时无法回答您的问题，请咨询医生。'
        final_answers = self.searcher.def1_main_search(Qstring)
        # 如果检索不到答案，输入模板信息
        if not final_answers:
            print(answer)

if __name__ == '__main__':
    print("您好，欢迎进入医疗问答系统. 我是医疗问答小助手，希望可以帮到您！")
    handler = chat()
    while 1:
        # print("请输入问题")
        question = input("用户:");
        data = handler.chat_main(question);


