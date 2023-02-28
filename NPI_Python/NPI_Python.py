#21.02.2023
# 1. Ответ: Аллигатор
# 2. Ответ: КЛСАБОА  101 001 011 10 111 00 10
# 3. Ответ: 69
# 4. Ответ: 9
# 5. 
# 6. Ответ: 2 раза
# 7. http://biblio.com/books.xls
# 8.
# 9.
# 10. 56 59 54
#-----------------------------------------------------------------

list = []
work = 0
a = int(input())
for _ in range(a):
    x = int(input())
    if x % 10 < 10:
        list.append(x)
        work = 1
    if work == 1:
        print("YES")
    if work == 0:
        print("NO")
#b = sum(list)
