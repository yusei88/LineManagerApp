import re,datetime
dt_now = datetime.datetime.now()
def speCheck1(rawText):
    lines = [
        [f"{dt_now.month}/{dt_now.day+1}", "1日後" "あした", "あす", "明日"],
        [f"{dt_now.month}/{dt_now.day+2}", "2日後", "明後日", "あさって",  "ふつかご"],
        ["2時", "にじ", "２じ", "２時"],
        ["3時", "さんじ", "３じ", "３時"],
        ["3日", "みっか"]
    ]
    for line in lines:
        for i in range(1, len(line)):
            rawText = rawText.replace(line[i], line[0])
    return rawText

def dateCheck(text):
    pattern1 = r"([0-9]{1,2}月[0-9]{1,2}日)|([0-9]{1,2}/[0-9]{1,2})|([0-9]{1,2}日)"
    pattern2 = r"[0-9]{1,2}時"
    date = re.findall(pattern1, text)
    time = re.findall(pattern2,text)
    print(f"date = {date}")
    print(f"time = {time}")

for i in range(1, 17):
    path = f"./datas/data-{i:0>2}.txt"
    with open(path, encoding="UTF-8") as f:
        print(f"\nfile : {path}")
        rawText = f.read()
        print(f"Text\n{rawText}\n")
        text = speCheck1(rawText)
        dateCheck(text)
        print("------------------------------")