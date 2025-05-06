// #include <iostream>
// #include <vector>
// #include<climits>
// #include <omp.h>
// using namespace std;

// // Sequential Bubble Sort
// void bubbleSortSequential(vector<int>& arr, int n) {
//     for (int i = 0; i < n - 1; i++) {
//         for (int j = 0; j < n - i - 1; j++) {
//             if (arr[j] > arr[j + 1]) {
//                 swap(arr[j], arr[j + 1]);
//             }
//         }
//     }
// }

// // Parallel Bubble Sort using OpenMP
// void bubbleSortParallel(vector<int>& arr, int n) {
//     for (int i = 0; i < n; i++) {
//         #pragma omp parallel for
//         for (int j = i%2 ; j < n - 1; j += 2) {
//             if (arr[j] > arr[j + 1]) {
//                 swap(arr[j], arr[j + 1]);
//             }
//         }
//     }
// }

// int main() {
//     vector<int> arr1 = {5, 2, 9, 1, 5, 6};  // Original array
//     int n = arr1.size();

//     vector<int> arr2 = arr1; // Copy for parallel sort

//     double start, end;

//     // Sequential timing
//     start = omp_get_wtime();
//     bubbleSortSequential(arr1, n);
//     end = omp_get_wtime();
//     cout << "Sequential Bubble Sort Time: " << end - start << " sec\n";

//     // Parallel timing
//     start = omp_get_wtime();
//     bubbleSortParallel(arr2, n);
//     end = omp_get_wtime();
//     cout << "Parallel Bubble Sort Time: " << end - start << " sec\n";

//     // Output result
//     cout << "Sorted Array (Parallel): ";
//     for (int i = 0; i < n; i++) cout << arr2[i] << " ";
//     cout << endl;

//     return 0;
// }

#include <iostream>
#include <vector>
#include <omp.h>
#include <cstdlib>
using namespace std;

// Merging two sorted halves
void merge(vector<int>& arr, int low, int mid, int high) {
    vector<int> temp;
    int i = low, j = mid + 1;

    // Merge two sorted parts
    while (i <= mid && j <= high) {
        if (arr[i] < arr[j])
            temp.push_back(arr[i++]);
        else
            temp.push_back(arr[j++]);
    }

    // Copy remaining elements
    while (i <= mid) temp.push_back(arr[i++]);
    while (j <= high) temp.push_back(arr[j++]);

    // Copy sorted temp back to original vector
    for (int k = 0; k < temp.size(); k++)
        arr[low + k] = temp[k];
}

// Sequential Merge Sort
void mergeSortSequential(vector<int>& arr, int low, int high) {
    if (low < high) {
        int mid = (low + high) / 2;
        mergeSortSequential(arr, low, mid);
        mergeSortSequential(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }
}

// Parallel Merge Sort using OpenMP
void mergeSortParallel(vector<int>& arr, int low, int high) {
    if (low < high) {
        int mid = (low + high) / 2;

        // Use OpenMP to split work in parallel
        #pragma omp parallel sections
        {
            #pragma omp section
            mergeSortParallel(arr, low, mid);

            #pragma omp section
            mergeSortParallel(arr, mid + 1, high);
        }

        merge(arr, low, mid, high);
    }
}

int main() {
    const int n = 1000;
    vector<int> original;  // Input array

    for (int i = 0; i < n; i++) {
        original.push_back(rand() % 10000);
    }

    // Create two copies: one for sequential, one for parallel
    vector<int> a = original;
    vector<int> b = original;

    double start, end;

    // Sequential merge sort
    start = omp_get_wtime();
    mergeSortSequential(a, 0, a.size() - 1);
    end = omp_get_wtime();
    cout << "\nSequential Merge Sort Time: " << end - start << " sec";

    // Parallel merge sort
    start = omp_get_wtime();
    #pragma omp parallel
    {
        #pragma omp single
        mergeSortParallel(b, 0, b.size() - 1);
    }
    end = omp_get_wtime();
    cout << "\nParallel Merge Sort Time: " << end - start << " sec\n";

    // Print sorted array
    cout << "Sorted Array (Parallel): ";
    for (int val : b)
        cout << val << " ";
    cout << endl;

    return 0;
}


