import csv, spacy, jaconv, re
nlp = spacy.load("ja_ginza")

def NotationVariability(text):
    table = str.maketrans({
    '、': '', #左が置換したい文字、右が新しい文字。
    '。': '', #左が置換したい文字、右が新しい文字。
    '・': '', #左が置換したい文字、右が新しい文字。
    '\n': '', #左が置換したい文字、右が新しい文字。
    '\t': '',  #左が置換したい文字、右が新しい文字。
    '?': '',  #左が置換したい文字、右が新しい文字。
    '!': '',  #左が置換したい文字、右が新しい文字。
    })
    text = jaconv.z2h(text, kana=False, digit=True, ascii=True)
    with open("dict/NotationVariability.csv",encoding="UTF-8") as f:
        for row in csv.reader(f):
            for i in range(1, len(row)):
                text = text.replace(row[i], row[0])
    text = text.translate(table)  #不要文字の削除
    text = re.sub("明日|あした|あす","1日後",text)
    text = re.sub("明後日|あさって|みょうごにち", "2日後", text)
    return text

for i in range(17):
    path = f"./datas/data-{i+1:0>2}.txt"
    print("------------------------------")
    with open(path, encoding="UTF-8") as f:
        print(f"file : {path}")
        text = NotationVariability(f.read()) #正規化
        print(text)
        print("\n")
        doc = nlp(text)
        for ent in doc.ents:
            print(ent.text, ent.label_)
        print("------------------------------")