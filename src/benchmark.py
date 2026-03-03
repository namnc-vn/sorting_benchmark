import numpy as np
import time
from sorting_algorithms import quicksort, heapsort, mergesort
import pandas as pd
import os

results = []

data_folder = "data"

for file in os.listdir(data_folder):
    path = os.path.join(data_folder, file)
    arr = np.load(path)

    arr_list = arr.tolist()

    print(f"Đang test {file}")

    # QuickSort
    start = time.perf_counter()
    quicksort(arr_list.copy())
    quick_time = (time.perf_counter() - start) * 1000

    # HeapSort
    start = time.perf_counter()
    heapsort(arr_list.copy())
    heap_time = (time.perf_counter() - start) * 1000

    # MergeSort
    start = time.perf_counter()
    mergesort(arr_list.copy())
    merge_time = (time.perf_counter() - start) * 1000

    # numpy sort
    start = time.perf_counter()
    np.sort(arr.copy())
    numpy_time = (time.perf_counter() - start) * 1000

    results.append([file, quick_time, heap_time, merge_time, numpy_time])

df = pd.DataFrame(results, columns=[
    "Dataset", "QuickSort", "HeapSort", "MergeSort", "NumPy sort"
])

df.to_csv("results.csv", index=False)
print("Hoàn thành benchmark!")