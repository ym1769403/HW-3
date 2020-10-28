#Yasir Mushtaque
#1769403

word_list = input()

word_freq = word_list.split()

for word in word_freq:
    freq = word_freq.count(word)
    print(word,freq)