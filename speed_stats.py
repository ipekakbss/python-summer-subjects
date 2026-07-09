import statistics

speeds = []

for i in range(10):
    x = float(input('Enter the speed: '))
    speeds.append(x)

average = sum(speeds) / 10
max_speed = max(speeds)
min_speed = min(speeds)
sd = statistics.stdev(speeds)

print(f'Average: {average}')
print(f'Max value: {max_speed}')
print(f'Min value: {min_speed}')
print(f'Standard deviation: {sd}')
