freq = dict()
filename = "text.txt"
for piece in open(filename).read().lower().split():
    word = "".join(c for c in piece if c.isalpha())
    if word:
        freq[word] = 1 + freq.get(word,0)

max_word = ''
max_count = 0
for (w,c) in freq.items():
    if c > max_count:
        max_word = w
        max_count = c
print("the most frequent word is ",max_word)
print("its number of occurrence is ",max_count)




