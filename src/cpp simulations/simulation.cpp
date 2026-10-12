#include "simulation.hpp"

std::vector<dataPoint> simulateTransit(
    double start_time,
    double end_time,
    double cadence,
    const transitParameters& params
) {
    std::vector<dataPoint> data;

    for (double time = start_time;
        time <= end_time;
        time += cadence) {
            double flux = calculateFlux(time, params);
            data.push_back({time, 
                flux}
            );
        }
    return data;
}