#include "transit.hpp"
#include <cmath>

double calculateFlux(double time, const transitParameters& params) {
    // Implementation for flux calculation
    double phase = std::fmod(time - params.epoch, params.period);

    if (phase < 0.0) {
        phase =+ params.period;
    }

    if (phase > params.period / 2.0) {
        phase -= params.period;
    }

    if (std::abs(phase) <= params.duration / 2.0) {
        return 1.0 - params.depth;
    }

    return 1.0;
}