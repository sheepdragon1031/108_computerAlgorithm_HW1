URL = '測試資料.txt'
total = 0
f = open(URL)
text = []
for line in f:
    text.append(line)
    
for texts in text:    
    arrText = texts.split( )
    for num in arrText:
        total += int(num) 
    # print(num)
print(total)
f.close()

f = open(URL,mode='w')
for line in text:
    f.writelines(line)
f.write('\n')
f.write(str(total))
f.close()