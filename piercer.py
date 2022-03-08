#!/usr/bin/env python3

import random

trials = 1000000


for t in range(1, 8):

	normal = 0 
	pierce = 0

	for i in range(trials):
		r1 = random.randint(1, 8)
		normal += r1

		if r1 < 4:
			r2 = random.randint(1, 8)
			pierce += r2
		else:
			pierce += r1

	print(f'{t}\t{normal/trials:.4f}\t{pierce/trials:.4f}')
