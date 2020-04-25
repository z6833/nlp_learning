# coding = utf-8
import pandas as pd

"""
based on max matching（最大匹配）
假设最大匹配为5
"""
def word_broke(input_str, word_dic):

    sent_list = []
    def sentence_seg(input_string):
        len_input_str = len(input_string)
        max_match = max({5, len_input_str})
        start_index = 0
        for end_index in range(max_match):
            word = input_string[start_index:max_match-end_index]

            if word in word_dic:  # 在词表
                sents = word + ", " + input_str[max_match-end_index:]
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

if __name__ == "__main__":
    # 测试
    print(word_segment_naive("北京的天气真好啊"))
    print(word_segment_naive("今天的课程内容很有意思"))
    print(word_segment_naive("经常有意见分歧"))
