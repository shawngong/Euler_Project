#Project Euler Solution 4
#Shawn Gong

def palindromic(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

def three_digit_product():
    solution = []
    for x in xrange(999,99,-1) and for y in xrange(999,99,-1):
            product = x*y
            if palindromic(product) == True:
                solution.append(product)
    return max(solution)

print three_digit_product()



