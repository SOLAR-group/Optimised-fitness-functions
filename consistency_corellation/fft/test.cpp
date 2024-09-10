#include <fftw3.h>
#include <iostream>
#include <cmath>
#include <chrono>

int main() {
    int N = 1048576; // Large size, e.g., 2^20
    fftw_complex *in, *out;
    fftw_plan p;

    // Allocate input and output arrays
    in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);

    // Create a "plan"
    p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);

    // Initialize input data with random values
    for (int i = 0; i < N; i++) {
        in[i][0] = (double)rand() / RAND_MAX; // Real part
        in[i][1] = (double)rand() / RAND_MAX; // Imaginary part
    }

    // Benchmarking
    auto start = std::chrono::high_resolution_clock::now();
    
    // Run FFT multiple times
    for (int j = 0; j < 10; j++) {
        fftw_execute(p); // Execute the plan on the input data
    }

    auto finish = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = finish - start;
    std::cout << "Elapsed time: " << elapsed.count() << " s\n";

    // Cleanup
    fftw_destroy_plan(p);
    fftw_free(in);
    fftw_free(out);

    return 0;
}
