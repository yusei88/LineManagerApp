from Ja_Extractor import Ext
import nagisa

#datasの中のデータで確認する
for i in range(1, 17):
    print("------------------------------")

    path = f"./datas/data-{i:0>2}.txt"
    print(f"file : {path}")
    with open(path, encoding="UTF-8") as f:
        rawText = f.read()
        JaExt = Ext(rawText)
        change = JaExt.NotationVariability()
        print(change)
        dates, times = JaExt.DateCheck(change)
        places  = JaExt.PlaceCheck(change)
        print(f"dates={dates},times={times},places={places}")

    print("------------------------------")

#print(f"date = {Datas["date"]} time = {Datas["time"]}")