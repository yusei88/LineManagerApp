import csv

for i in range(1, 17):
    path = f"./datas/data-{i:0>2}.txt"
    with open(path, encoding="UTF-8") as f:
        print(f"\nfile : {path}")
        rawText = f.read()
        words = nagisa.tagging(rawText)
        print(f"Text\n{text}\n")
        print("------------------------------")

with open("dict/NotationVariability.csv",encoding="UTF-8") as f:
    for row in csv.reader(f):
        print(row)
        for i in range(1,len(row)):
            print(f"{row[i]}=>{row[0]}")