import math
n = int(input())
max = -1
x = 0
y = 0
for i in range(n):
	a = list(map(int, input().split()))
	if max < math.sqrt(a[0]**2+a[1]**2):
		x = a[0]
		y = a[1]
		max = math.sqrt(a[0]**2+a[1]**2)
print(x,y)
