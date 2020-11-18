# -*- coding:utf-8 -*-
from Ja_Extractor import Ext

#datasの中のデータで確認する
for i in range(17):
    print("------------------------------")

    path = f"./datas/data-{i+1:0>2}.txt"
    print(f"file : {path}")
    with open(path, encoding="UTF-8") as f:
        rawText = f.read()
        JaExt = Ext(rawText)
        dates, times, places = JaExt.Extract()
        print(f"元の文\n{rawText}\n")
        print(f"分析結果\ndates={dates},times={times},places={places}")
    print("------------------------------")