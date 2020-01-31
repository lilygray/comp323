import sys

def gcd(a, b):
	# 1
	u = 1
	g = a
	x = 0
	y = b

	return gcd_helper(u, g, x, y, a, b)


def gcd_helper(u, g, x, y, a, b):
	# 2
	if y == 0:
		v = (g - a*u) / b
		return (g, u, v)
	
	# 3
	# Divide g by y with remainder, g = qy + t, with 0 <= t < y
	t = g % y
	q = (g - t) / y
	
	# 4
	# Set s = u - qx
	s = u - (q * x)
	
	# 5
	# Set u = x and g = y
	u = x
	g = y

	# 6
	# Set x = s and y = t
	x = s
	y = t

	# 7
	# Go to step 2

	return gcd_helper(u, g, x, y, a, b)

if __name__ == "__main__":
	if len(sys.argv) > 2:
		a = int(sys.argv[1])
		b = int(sys.argv[2])

		if (a == 0) and (b == 0):
			print("GCD undefined.")
		elif (a == 0):
			print("GCD:", b)
		elif b == 0:
			print("GCD:", a)
		else:
			g, u, v = gcd(a, b)
			print("GCD:", g)
			if u <= 0:
				print("Equal to", u + b/g, "*", a, "+", v - a/g, "*", b)
			else:
				print("Equal to", u, "*", a, "+", v, "*", b)


