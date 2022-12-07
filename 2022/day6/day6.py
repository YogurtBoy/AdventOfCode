# f = open('2022/day6/signal_small.txt', 'r')
f = open('2022/day6/signal.txt', 'r')

if f:
    print("Successfully opened data...")

signal = f.readline()

required_unique = 14
check_list = []
unique_ind = 0
for ii in range(len(signal)):
    signal_char = signal[ii]
    if len(check_list) < required_unique:
        check_list.append('')
    elif len(set(check_list)) == required_unique:
        break
    check_list[ii % required_unique] = signal_char

print(ii)