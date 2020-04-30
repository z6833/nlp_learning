# coding = utf-8

import pandas as pd



def create_vocab():
    path = './data/综合类中文词库.xlsx'
    df_word_dic = pd.read_excel(path, header=None)
    word_dic = set(df_word_dic[0])
    word_prob = {"北京": 0.03, "的": 0.08, "天": 0.005, "气": 0.005, "天气": 0.06, "真": 0.04, "好": 0.05, "真好": 0.04, "啊": 0.01,
                 "真好啊": 0.02,
                 "今": 0.01, "今天": 0.07, "课程": 0.06, "内容": 0.06, "有": 0.05, "很": 0.03, "很有": 0.04, "意思": 0.06,
                 "有意思": 0.005, "课": 0.01,
                 "程": 0.005, "经常": 0.08, "意见": 0.08, "意": 0.01, "见": 0.005, "有意见": 0.02, "分歧": 0.04, "分": 0.02,
                 "歧": 0.005}
    return word_dic, word_prob

def word_lcut(input_str, word_dic):

    # segment = []
    inputstr_len = len(input_str)

    if inputstr_len == 0:
        return

    for index in range(1, inputstr_len+1):
        word = input_str[:index]
        if word in word_dic:
            # print(word)
            sub_str = input_str[index:]
            yield word
            # yield word
            # print(input_str, "--", word, "--", sub_str)
            word_lcut(sub_str, word_dic)
            # print(word + " " + sub_str)
        else:
            continue

    # print(segment)
    # yield segment

def word_segment_naive(input_str):

    word_dic, word_prob = create_vocab()

    # segments = word_lcut(input_str, word_dic)
    def word_cut(input_str, word_dic):
        for i in range(1, input_str+1):
            word = input_str[:i]
            if word in word_dic:

                yield word
    index = 0
    while True:
        input_str = word_cut(input_str, word_dic)
        # index += 1
    # print(next(segment) for segment in segments)

def main():
    # 2. 分词
    print(word_segment_naive("北京的天气真好啊"))
    # print(word_segment_naive("今天的课程内容很有意思"))
    # print(word_segment_naive("经常有意见分歧"))


if __name__ == "__main__":
    main()



