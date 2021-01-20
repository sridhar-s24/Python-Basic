stri = input('Enter string: ')
char = input('Enter the char: ')
cnt = stri.count(char)
u = 0


for i in range(cnt):
    u = stri.find(char,u)
    print (u, end = ' ')
    u += 1
if u != 0:
    print('are the index points where the character appears')
else:
    print('No such character in the sequence')
    
