how_much_value = int(input('How much speed value will you add ?: '))

speeds = []

for i in range(how_much_value):
    x = float(input('Enter the speed: '))
    speeds.append(x)

with open('speeds.txt', 'w') as file:
    for s in speeds:
        file.write(str(s) + '\n')

average = sum(speeds) / how_much_value
max_speed = max(speeds)
min_speed = min(speeds)

def sd():
    sum_of_square = 0
    for n in speeds:
        sum_of_square += (n - average) ** 2
    sd = (sum_of_square / (how_much_value - 1)) ** 0.5
    return sd

standard_deviation = sd()

print(f'Average: {average}')
print(f'Max value: {max_speed}')
print(f'Min value: {min_speed}')
print(f'Standard deviation: {standard_deviation}')
