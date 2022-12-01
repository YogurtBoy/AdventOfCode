
# f = open('2022/Practice/2019_day2_input_small.txt', 'r')
f = open('2022/Practice/2019_day2_input.txt', 'r')

# C:\Users\jpar1\Desktop\Prog\AdventOfCode\2022\Practice\2019_day2_input_small.txt

if f:
    print("Successfully opened data...")

for line in f:
    intcode = line.split(',')
for ii in range(len(intcode)):
    intcode[ii] = int(intcode[ii])

intcode_orig = intcode.copy()
num_instructions = len(intcode)

# The problem says to do this step...
noun = 0
verb = 0

# # Find the last code that writes over position 0
# final_writer = 0
# find_position = 3
# while find_position < num_instructions:
#     if intcode(find_position) == 0:
#         final_write = find_position
#     else: 
#         find_position = find_position + 4

desired_output = 19690720    



for ii in range(100):
    noun = ii
    for jj in range(100):
        verb = jj
        for every_damn_int in range(len(intcode)):
            intcode[every_damn_int] = intcode_orig[every_damn_int]
        intcode[1] = noun
        intcode[2] = verb 

        line_count = 0
        code_position = 0
        product = 0
        
        while code_position <= num_instructions:
            if intcode[code_position] == 1:
                product = intcode[intcode[code_position + 1]] + intcode[intcode[code_position + 2]]
                intcode[intcode[code_position + 3]] = product
            elif intcode[code_position] == 2:
                product = intcode[intcode[code_position + 1]] * intcode[intcode[code_position + 2]]
                intcode[intcode[code_position + 3]] = product
            elif intcode[code_position] == 99:
                break
            else:
                print('Got OP code ' + str(intcode[code_position]) + ' at position ' + str(code_position))
                print('You broke it...')
                break
            
            line_count = line_count + 1
            code_position = line_count * 4

        if intcode[0] == desired_output:
            goodnoun = noun
            goodverb = verb

print('ANSWER:')
print(print(100 * goodnoun + goodverb))