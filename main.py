import nagisa

text = "pythonで使える12月13日に学校で"
words = nagisa.tagging(text)
print(words)
print(words.words)
print(nagisa.wakati(text))