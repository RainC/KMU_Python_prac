def getPrime(num):
	for x in range(num -1, 2, -1):
		if (num % x == 0):
			return "false"

	return "true"


def __main__():
	print(getPrime(11))

__main__()