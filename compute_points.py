import math

G = 6.67e-11
m1 = 1.989e30
m2 = 5.9722e24
R = 1.52e11

v_m2 = math.sqrt(G * m1 / R)
w_m2 = v_m2 / R

F1_by_m = lambda l1: G * m1 / (R-l1)**2
F2_by_m = lambda l1: G * m2 / (l1)**2
F_cent_by_m = lambda l1: w_m2**2 * (R - l1)

l1 = 1e4
delta = 1e8
upper_bound = R/2
num_increments = 0

for i in range(20):
	print(f'Iteration {i}: start={l1}, end={upper_bound}, delta={delta}')
	while l1 < upper_bound:
		if F2_by_m(l1) + F_cent_by_m(l1) < F1_by_m(l1):
			#print(f'Iteration {i}: {num_increments}')
			num_increments = 0
			break
		else:
			l1 += delta
			num_increments += 1
	upper_bound = l1
	l1 -= delta
	delta /= 2
print(f'Numerical estimates show that L1 is between {l1} and {l1 + delta}')

