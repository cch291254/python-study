text = "hello world python hello world hello"
text_list=text.split()
words={}
for word in text_list:
    words[word]=words.get(word,0)+1
print(words)
