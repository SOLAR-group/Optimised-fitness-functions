#include <fftw3.h>
#include <vector>
#include <fstream>
#include <iostream>
#include <sndfile.h> // Libsndfile library for reading audio files

// using namespace std;

int main() {
    // Open the audio file
    SF_INFO sfinfo;
    SNDFILE *infile = sf_open("sound2.wav", SFM_READ, &sfinfo);

    // Prepare buffer for audio data
    std::vector<double> buffer(sfinfo.frames);
    sf_read_double(infile, buffer.data(), sfinfo.frames);
    sf_close(infile);

    // Prepare FFTW input and output arrays
    fftw_complex *in = fftw_alloc_complex(buffer.size());
    fftw_complex *out = fftw_alloc_complex(buffer.size());
    for (size_t i = 0; i < buffer.size(); ++i) {
        in[i][0] = buffer[i]; // Real part
        in[i][1] = 0.0;       // Imaginary part
    }

    // Create and execute the FFT plan
    fftw_plan p = fftw_plan_dft_1d(buffer.size(), in, out, FFTW_FORWARD, FFTW_ESTIMATE);
    fftw_execute(p);

    // Cleanup
    fftw_destroy_plan(p);
    fftw_free(in);
    fftw_free(out);
    //print that the fourier was done successfully
    // cout << "Fourier finished ";
    return 0;
}
