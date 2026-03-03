#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <chrono>
#include <iomanip>

using namespace std;
using namespace chrono;

// ===== Load float64 (double) =====
vector<double> load_double(const string& filename) {
    ifstream file(filename, ios::binary);
    if (!file) {
        throw runtime_error("Cannot open file: " + filename);
    }

    file.seekg(0, ios::end);
    size_t size = file.tellg();
    file.seekg(0, ios::beg);

    if (size % sizeof(double) != 0) {
        throw runtime_error("File size mismatch for double");
    }

    size_t count = size / sizeof(double);
    vector<double> data(count);

    file.read(reinterpret_cast<char*>(data.data()), size);
    return data;
}

// ===== Load int32 =====
vector<int> load_int32(const string& filename) {
    ifstream file(filename, ios::binary);
    if (!file) {
        throw runtime_error("Cannot open file: " + filename);
    }

    file.seekg(0, ios::end);
    size_t size = file.tellg();
    file.seekg(0, ios::beg);

    if (size % sizeof(int) != 0) {
        throw runtime_error("File size mismatch for int32");
    }

    size_t count = size / sizeof(int);
    vector<int> data(count);

    file.read(reinterpret_cast<char*>(data.data()), size);
    return data;
}

int main() {

    cout << "===== FLOAT DATASETS =====\n";

    // 5 file float_1 → float_5
    for (int i = 1; i <= 5; i++) {
        string filename = "data_bin/float_" + to_string(i) + ".bin";
        cout << "Testing " << filename << endl;

        auto data = load_double(filename);

        auto start = high_resolution_clock::now();
        sort(data.begin(), data.end());
        auto end = high_resolution_clock::now();

        long double duration = duration_cast<nanoseconds>(end - start).count() / 1e6;
        cout << fixed << setprecision(4);
        cout << "Time: " << duration << " ms\n";
        cout << "------------------------\n";
    }

    cout << "\n===== INT DATASETS =====\n";

    // 5 file int_1 → int_5
    for (int i = 1; i <= 5; i++) {
        string filename = "data_bin/int_" + to_string(i) + ".bin";
        cout << "Testing " << filename << endl;

        auto data = load_int32(filename);

        auto start = high_resolution_clock::now();
        sort(data.begin(), data.end());
        auto end = high_resolution_clock::now();

        long double duration = duration_cast<nanoseconds>(end - start).count() / 1e6;
        cout << fixed << setprecision(4);
        cout << "Time: " << duration << " ms\n";
        cout << "------------------------\n";
    }

    return 0;
}