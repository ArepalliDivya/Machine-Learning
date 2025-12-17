import random

# create fake data (100 numbers between 1 and 50)
data = [random.randint(1, 50) for _ in range(100)]

print("Fake Data:", data)
import statistics

mean_value = statistics.mean(data)
median_value = statistics.median(data)
mode_value = statistics.mode(data)
variance_value = statistics.variance(data)

print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
print("Variance:", variance_value)
print("Sorted Data:", sorted(data))