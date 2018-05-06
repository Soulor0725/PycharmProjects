def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def monisen2(n):
    if prime(n) == False:
        return False, 0
    result = 2**n-1
    if prime(result) == False:
        return False, 0
    return True, result

def monisen(n):
	count = 0
	flag = 0
	i = 2
	while 1:
	    if True == monisen2(i)[0]:
	        count += 1
	        if count == 4:
	            flag = i
	            break
	    i += 1
	return monisen2(flag)[1]     

print(monisen(int(input())))