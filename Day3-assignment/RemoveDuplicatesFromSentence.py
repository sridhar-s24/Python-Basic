str = input('Enter a sentence: ')
words = str.split()
length = len(words)
dup = []
for i in range(0, length-1):
    for j in range(i+1, length):
        if words[i].lower() == words[j].lower():
            dup.append(j)
            if(dup.count(j) > 1):
                dup.remove(j)
dup.sort()
count = 0
for itr in dup:
    copyItr = itr
    words.pop(copyItr - count)
    count += 1
print(' '.join(words))
