arr = []


NUMBER = 1000000
MIN = -1000000
MAX = 1000000

import random
for i in range(NUMBER):
	a = random.randint(MIN, MAX)
	b = random.randint(MIN, MAX)
	arr.append((a, b))



with open("testcases.txt", "a+") as wfile:
	wfile.writelines(f"{i}\n" for i in arr);



