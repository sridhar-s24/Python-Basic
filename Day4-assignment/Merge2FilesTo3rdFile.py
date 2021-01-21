f1 = open('C:\\Users\\srid_\\OneDrive\\Desktop\\python\\Python-Basic\\file1.txt','r')
f1r = f1.read()
f1.close()

f2 = open('C:\\Users\\srid_\\OneDrive\\Desktop\\python\\Python-Basic\\file2.txt','r')
f2r = f2.read()
f2.close()

f3 = open('C:\\Users\\srid_\\OneDrive\\Desktop\\python\\Python-Basic\\file3.txt','w')
f3.write(f1r + '\n' + f2r)
f3.close()
f3 = open('C:\\Users\\srid_\\OneDrive\\Desktop\\python\\Python-Basic\\file3.txt','r')
print(f3.read())
f3.close()
