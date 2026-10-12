#ifndef TRANSIT_HPP
#define TRANSIT_HPP

struct transitParameters {
    double duration;
    double depth;
    double epoch;
    double period;
};

double calculateFlux(
    double time,
    const transitParameters& params
);

#endif