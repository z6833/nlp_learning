# coding = utf-8

# # TODO: 第一步： 从dic.txt中读取所有中文词。
# #  hint: 思考一下用什么数据结构来存储这个词典会比较好？ 要考虑我们每次查询一个单词的效率。
# dic_words =      # 保存词典库中读取的单词
#
# # 以下是每一个单词出现的概率。为了问题的简化，我们只列出了一小部分单词的概率。 在这里没有出现的的单词但是出现在词典里的，统一把概率设置成为0.00001
# # 比如 p("学院")=p("概率")=...0.00001
#
# word_prob = {"北京":0.03,"的":0.08,"天":0.005,"气":0.005,"天气":0.06,"真":0.04,"好":0.05,"真好":0.04,"啊":0.01,"真好啊":0.02,
#              "今":0.01,"今天":0.07,"课程":0.06,"内容":0.06,"有":0.05,"很":0.03,"很有":0.04,"意思":0.06,"有意思":0.005,"课":0.01,
#              "程":0.005,"经常":0.08,"意见":0.08,"意":0.01,"见":0.005,"有意见":0.02,"分歧":0.04,"分":0.02, "歧":0.005}
# print (sum(word_prob.values()))

import pandas as pd

# #  分数（10）
# ## TODO 请编写word_segment_naive函数来实现对输入字符串的分词
# def word_segment_naive(input_str):
#     """
#     1. 对于输入字符串做分词，并返回所有可行的分词之后的结果。
#     2. 针对于每一个返回结果，计算句子的概率
#     3. 返回概率最高的最作为最后结果
#
#     input_str: 输入字符串   输入格式：“今天天气好”
#     best_segment: 最好的分词结果  输出格式：["今天"，"天气"，"好"]
#     """
#
#     # TODO： 第一步： 计算所有可能的分词结果，要保证每个分完的词存在于词典里，这个结果有可能会非常多。
#     segments = []  # 存储所有分词的结果。如果次字符串不可能被完全切分，则返回空列表(list)
#     # 格式为：segments = [["今天"，“天气”，“好”],["今天"，“天“，”气”，“好”],["今“，”天"，“天气”，“好”],...]
#
#     for i in range(1, max_word_len + 1):
#
#     # TODO: 第二步：循环所有的分词结果，并计算出概率最高的分词结果，并返回
#     best_segment =
#     best_score =
#     for seg in segments:
#     # TODO ...
#
#     return best_segment

"""
based on max matching（最大匹配）
假设最大匹配为5
"""


def word_broke(input_str, word_dic):
    sent_list = []

    def sentence_seg(input_string):
        len_input_str = len(input_string)
        max_match = max({5, len_input_str})
        # print(max_match)
        start_index = 0
        for end_index in range(max_match):
            word = input_string[start_index:max_match - end_index]

            if word in word_dic:  # 在词表
                sents = word + ", " + input_str[max_match - end_index:]
                break
        return sents

    while len(input_str) > 0:
        sents = sentence_seg(input_str)
        result_split = sents.split(", ")

        sent_list.append(result_split[0])
        input_str = result_split[1]

    return sent_list


def word_segment_naive(input_str):
    vocab_path = r"./data/综合类中文词库.xlsx"
    word_dic_df = pd.read_excel(vocab_path, header=None)
    word_dic = [_ for _ in word_dic_df[0]]
    segments = word_broke(input_str, word_dic)

    return segments
    print(segments)


if __name__ == "__main__":
    word_segment_naive("北京的天气真好啊")
