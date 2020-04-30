# coding = utf-8
"""
1.枚举法列出前向最大匹配，后项最大匹配的所有分词可能
    1.0 调用两种分词方法
    1.1 前向最大匹配  假定：max_match = 5
    1.2 后向醉打匹配  假定：max_match = 5
2.计算所有分词可能中概率最大的，作为最后分词结果
"""
import pandas as pd

def create_vocab(vocab_path):
    # # TODO: 第一步： 从dic.txt中读取所有中文词。
    # #  hint: 思考一下用什么数据结构来存储这个词典会比较好？ 要考虑我们每次查询一个单词的效率。
    # dic_words =  # 保存词典库中读取的单词
    #
    # # 以下是每一个单词出现的概率。为了问题的简化，我们只列出了一小部分单词的概率。 在这里没有出现的的单词但是出现在词典里的，统一把概率设置成为0.00001
    # # 比如 p("学院")=p("概率")=...0.00001

    word_prob = {"北京": 0.03, "的": 0.08, "天": 0.005, "气": 0.005, "天气": 0.06, "真": 0.04, "好": 0.05, "真好": 0.04, "啊": 0.01,
                 "真好啊": 0.02,
                 "今": 0.01, "今天": 0.07, "课程": 0.06, "内容": 0.06, "有": 0.05, "很": 0.03, "很有": 0.04, "意思": 0.06,
                 "有意思": 0.005, "课": 0.01,
                 "程": 0.005, "经常": 0.08, "意见": 0.08, "意": 0.01, "见": 0.005, "有意见": 0.02, "分歧": 0.04, "分": 0.02,
                 "歧": 0.005}
    word_dic_df_tolist = pd.read_excel(vocab_path, header=None)[0].tolist()

    word_dic = dict()
    max_word_len = 0
    for word in word_dic_df_tolist:
        if len(word) > max_word_len:  # 最大词长度
            max_word_len = len(word)

        if word in word_prob.keys():  # 字典存储词典中词及其概率大小
            word_dic[word] = word_prob[word]
        else:
            word_dic[word] = 0.00001

    return max_word_len, word_dic



def word_segment(max_match, max_word_len, word_dic):
    # 定义参数
    max_match = max_match
    max_word_len = max_word_len
    word_dic = word_dic

    segments = []
    index = 0  # 只想input_str的角标

def word_segment_naive(input_str):

    # 构造词典
    vocab_path = "./data/综合类中文词库.xlsx"
    max_word_len, word_dic = create_vocab(vocab_path=vocab_path)

    # 分词部分
    max_match = 5  # 设置最大匹配词长度
    input_str = input_str  # 输入字符串

    segments = word_segment(max_match, max_word_len, word_dic)

    # TODO： 第一步： 计算所有可能的分词结果，要保证每个分完的词存在于词典里，这个结果有可能会非常多。
    segments = []  # 存储所有分词的结果。如果次字符串不可能被完全切分，则返回空列表(list)
    # 格式为：segments = [["今天"，“天气”，“好”],["今天"，“天“，”气”，“好”],["今“，”天"，“天气”，“好”],...]

    # TODO: 第二步：循环所有的分词结果，并计算出概率最高的分词结果，并返回
    best_segment = ""
    best_score = ""
    # for seg in segments:
    # TODO ...

    # return best_segment


if __name__ == "__main__":
    # 测试
    print(word_segment_naive("北京的天气真好啊"))
    print(word_segment_naive("今天的课程内容很有意思"))
    print(word_segment_naive("经常有意见分歧"))