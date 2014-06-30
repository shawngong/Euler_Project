check_list = [11,13,14,16,17,18,19,20]

def evenly_divisible(step):
    for num in xrange(step, 999999999, step):
        if all (num % i == 0 for i in check_list):
            return num

print evenly_divisible(2520)

