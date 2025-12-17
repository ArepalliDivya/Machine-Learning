import random
data = [random.randint(1, 50) for _ in range(100)]

print("Fake Data:", data)

total = 0
for num in data:
    total += num
mean_manual = total / len(data)

sorted_data = sorted(data)
n = len(sorted_data)

if n % 2 == 1:
    median_manual = sorted_data[n // 2]
else:
    median_manual = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

frequency = {}

for num in data:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_count = 0
mode_manual = None

for key, value in frequency.items():
    if value > max_count:
        max_count = value
        mode_manual = key

variance_sum = 0
for num in data:
    variance_sum += (num - mean_manual) ** 2

variance_manual = variance_sum / (len(data) - 1)

print("Mean (Manual):", mean_manual)
print("Median (Manual):", median_manual)
print("Mode (Manual):", mode_manual)
print("Variance (Manual):", variance_manual)
print("Sorted Data:", sorted_data)
