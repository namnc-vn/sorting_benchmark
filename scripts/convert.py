import numpy as np
import os

INPUT_FOLDER = "data"
OUTPUT_FOLDER = "data_bin"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".npy"):
        input_path = os.path.join(INPUT_FOLDER, filename)
        
        # Load numpy array
        arr = np.load(input_path)
        
        # Tạo tên file .bin
        bin_name = filename.replace(".npy", ".bin")
        output_path = os.path.join(OUTPUT_FOLDER, bin_name)
        
        # Xuất raw binary
        arr.tofile(output_path)

        print(f"Converted: {filename} -> {bin_name}")

print("Hoàn thành chuyển đổi!")