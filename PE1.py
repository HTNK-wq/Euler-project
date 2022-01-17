a = [i for i in range(1, 1000) if i % 3 == 0]   #Set of multiples of 3

b = [i for i in range(1, 1000) if i % 5 == 0]   #Set of multiples of 5

c = [i for i in range(1, 1001) if i % 15 == 0]  #Set of multiples of 15

g = sum(a) + sum(b) - sum(c)             #Set a + Set b - Set c, to find the total sum of multiple of 3 and 5
print(g)
