# Sorting Algorithm Benchmark

## Description
Benchmark comparison of QuickSort, HeapSort, MergeSort,
NumPy sort and C++ std::sort on 1,000,000 elements datasets.

## Structure
- src/: source code
- scripts/: dataset generation
- results/: benchmark results
- report/: final PDF report

## Create data
py randomarray.py
py convert.py

## Compile C++
g++ -O3 -march=native -std=c++17 benchmark_cpp.cpp -o benchmark_cpp

## Run Python
python benchmark.py