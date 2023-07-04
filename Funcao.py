
def primo (num):
	for n in range(2,num):
		if num % n == 0:
			print ("não é primo")
			break
	else:
		print("primo")


print(primo(31))