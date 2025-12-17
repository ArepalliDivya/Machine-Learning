import random

# Create fake data (30 numbers between 1 and 10)
data = [random.randint(1, 10) for _ in range(30)]

print("Fake Data:", data)

# Manual mode calculation
frequency = {}

for num in data:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Find highest frequency
max_count = 0
mode = None

for key, value in frequency.items():
    if value > max_count:
        max_count = value
        mode = key

print("Frequency:", frequency)
print("Highest Frequently Repeated Element (Mode):", mode)
print("Frequency Count:", max_count)
print("Sorted Data:", sorted(data))