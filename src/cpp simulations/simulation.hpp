#ifndef SIMULATION_HPP
#define SIMULATION_HPP

#include <vector>
#include "transit.hpp"

struct dataPoint {
    double time;
    double flux;
};

std::vector<dataPoint> simulateTransit(
    double start_time,
    double end_time,
    double cadence,
    const transitParameters& params
);

#endif