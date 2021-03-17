def run(self, N, M):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		x = ""
		for i in range(N, M+1):
			if (i % 3 == 0 and i % 5 == 0):
				x = x + "FizzBuzz,"
			else:
				if (i % 3 == 0):
					x = x + "Fizz," 
				else:
					if (i % 5 == 0):
						x = x + "Buzz" + ","
					else:
						x = x + str(i)+","
                    # print(str(i))
		#sequence = None
		return x[:-1]
