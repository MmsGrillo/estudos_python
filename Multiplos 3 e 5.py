z = set()

for i in range (3,1000,3):
	z.add(i)
for i in range (5,1000,5):
	z.add(i)

print(sum(z))


print(sum(set(list(range(0, 1000, 3)) + list(range(0, 1000, 5)))))

print(sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0))