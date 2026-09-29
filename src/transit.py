import numpy as np
from astropy.timeseries import BoxLeastSquares

def find_period(time, flux, min_period=300, max_period=360, n_period=6000):
    model = BoxLeastSquares(time, flux)
    period_grid = np.linspace(min_period, max_period, n_period)
    duration_grid = np.linspace(0.20, 0.80, 25)
    result = model.power(period_grid, duration_grid)
    i = np.argmax(result.power)

    return {
        'period' : result.period[i],
        'duration' : result.duration[i],
        't0' : result.transit_time[i],
        'depth' : result.depth[i],
        'power' : result.power[i],
        'period_grid' : result.period,
        'power_grid' : result.power,
    }

def phase_fold(time, flux, period, t0):
    phase = ((time - t0 + 0.5 * period) % period - 0.5)
    sort = np.argsort(phase)
    phase= phase[sort]
    folded_flux = flux[sort]
    
    return phase, folded_flux[sort]