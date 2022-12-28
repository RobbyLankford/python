# Question 1

## Import Data
with open("day-11.txt", "r") as file:
    monkey_notes = file.read().split('\n\n')

### Lists to store notes on monkeys
monkeys = []
items = []
operations = []
tests = []
result_true = []
result_false = []

### Iterate and parse through notes on each monkey
for notes in monkey_notes:
    monkey_info = notes.split('\n')
    
    monkey_ids = int(monkey_info[0].split(' ')[-1].strip(':'))
    starting_items = [int(i) for i in monkey_info[1].split(':')[-1].split(',')]
    lambda_funcs = eval(f"lambda old: {monkey_info[2].split('=')[-1]}")
    
    monkeys.append(monkey_ids)
    items.append(starting_items)
    operations.append(lambda_funcs)
    tests.append(int(monkey_info[3].split(' ')[-1]))
    result_true.append(int(monkey_info[4].split(' ')[-1]))
    result_false.append(int(monkey_info[5].split(' ')[-1]))

## For each round, iterate through each monkey's item(s)
num_rounds = 20
num_items = [0] * len(monkeys)

for _ in range(num_rounds):
    for i in range(len(monkeys)):
        for item in items[i]:
            num_items[i] += 1
            worry = operations[i](item) // 3
            
            if worry % tests[i] == 0:
                items[result_true[i]].append(worry)
            else:
                items[result_false[i]].append(worry)
            
        items[i] = []

## Need the top 2 largest values
num_items.sort(reverse=True)

## Print Answer
print(f"Answer 1: {num_items[0] * num_items[1]}")


# Question 2

## Import Data
with open("day-11.txt", "r") as file:
    monkey_notes = file.read().split('\n\n')

### Lists to store notes on monkeys
monkeys = []
items = []
operations = []
tests = []
result_true = []
result_false = []

### Iterate and parse through notes on each monkey
for notes in monkey_notes:
    monkey_info = notes.split('\n')
    
    monkey_ids = int(monkey_info[0].split(' ')[-1].strip(':'))
    starting_items = [int(i) for i in monkey_info[1].split(':')[-1].split(',')]
    lambda_funcs = eval(f"lambda old: {monkey_info[2].split('=')[-1]}")
    
    monkeys.append(monkey_ids)
    items.append(starting_items)
    operations.append(lambda_funcs)
    tests.append(int(monkey_info[3].split(' ')[-1]))
    result_true.append(int(monkey_info[4].split(' ')[-1]))
    result_false.append(int(monkey_info[5].split(' ')[-1]))

## For each round, iterate through each monkey's item(s)
num_rounds = 10000
num_items = [0] * len(monkeys)

### Calculate LCM of all tests to keep worry level low
modulo = 1
for test in tests:
    modulo *= test

for _ in range(num_rounds):
    for i in range(len(monkeys)):
        for item in items[i]:
            num_items[i] += 1
            
            ### Dividing by the LCM keeps the size of the numbers reasonable and does NOT change the outcome of the tests
            worry = operations[i](item) % modulo
            
            if worry % tests[i] == 0:
                items[result_true[i]].append(worry)
            else:
                items[result_false[i]].append(worry)
            
        items[i] = []

## Need the top 2 largest values
num_items.sort(reverse=True)

## Print Answer
print(f"Answer 2: {num_items[0] * num_items[1]}")