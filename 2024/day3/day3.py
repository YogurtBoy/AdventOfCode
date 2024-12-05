import re


f = open("day3/memory.txt", "r")

line = f.read()

big_sum = 0
matches = re.findall(r'mul[(]\d*,\d*[)]|do\(\)|don.t\(\)', line)
print(matches)
do_it = True
for match in matches:
    print(match)
    if 'do()' in match:
        print(do_it)
        do_it = True
    elif 'don' in match:
        print(do_it)
        do_it = False
    elif 'mul' in match and do_it:
        print(do_it)
        spit = match.split(',')
        n1 = int(spit[0].split('(')[1])
        n2 = int(spit[1].split(')')[0])
        product = n1 * n2

        big_sum += product
        
    


print(big_sum)


f.close()