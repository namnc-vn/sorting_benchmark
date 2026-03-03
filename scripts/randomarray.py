import numpy as np
import os

os.makedirs("data", exist_ok=True)

SIZE = 1_000_000

# ===== 5 dãy số thực =====
float_arrays = []

# 1. tăng dần
float_arrays.append(np.sort(np.random.rand(SIZE)))

# 2. giảm dần
float_arrays.append(np.sort(np.random.rand(SIZE))[::-1])

# 3–5 random
for _ in range(3):
    float_arrays.append(np.random.rand(SIZE))

# ===== 5 dãy số nguyên =====
int_arrays = []

# 6. tăng dần
int_arrays.append(np.sort(np.random.randint(0, 10_000_000, SIZE)))

# 7. giảm dần
int_arrays.append(np.sort(np.random.randint(0, 10_000_000, SIZE))[::-1])

# 8–10 random
for _ in range(3):
    int_arrays.append(np.random.randint(0, 10_000_000, SIZE))

# ===== Lưu file =====
for i, arr in enumerate(float_arrays):
    np.save(f"data/float_{i+1}.npy", arr)

for i, arr in enumerate(int_arrays):
    np.save(f"data/int_{i+1}.npy", arr)

print("Tạo dữ liệu xong!")