import pandas as pd
from konlpy.tag import Okt
from tqdm import tqdm 

complain = pd.read_pickle("/home/mglee/VSCODE/Duplicated/sample5data/sample5_df.pkl")
complain_body = complain['본문']


okt = Okt()
test = [
    "이것은 메켑 테스트 입니다.",
    "이것도 메켑 메켑 테스트 임",
    "그것은 메켑 테스트 테스트 입니까?"
]

def tf_count(lst):
    word_dict = {}
    for txt in tqdm(lst):
        txt = str(txt)
        if len(txt) < 1000:
            lst = okt.nouns(txt)
        else:
            lst = ['TOO', "LONG"]
        for word in lst:
            try:
                word_dict[word] = word_dict[word] + 1 
            except:
                word_dict[word] = 1
    return word_dict

tf_count(test)

complain_tf = tf_count(complain_body)
pd.to_pickle(complain_tf, "complain_tf_py.pkl")