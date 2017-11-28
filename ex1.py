n = int(input())
a = 0
x = 0
y = 0
for i in range (n):
	a = input().split(' ')
	x = x + int(a[0])
	y = y + int(a[1])
d = x
g = y
print((d/n),(g/n))
