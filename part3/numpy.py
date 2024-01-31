import numpy as np

random_floats = np.random.rand(10)

print("generated array:", random_floats)

mean_value = np.mean(random_floats)
median_value = np.median(random_floats)
std_deviation = np.std(random_floats)

print("mean:", mean_value)
print("median:", median_value)
print("mtandard Deviation:", std_deviation)