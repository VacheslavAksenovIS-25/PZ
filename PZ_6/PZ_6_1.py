# Сформировать и вывести целочисленный список размера 10,содержащий 10
# первых положительных нечетных чисел: 1,3,5,...
a = []
i = 0
for i in range(10):
    i += 1*i+1
    a.append(i)
print(a)
