import warnings

warnings.filterwarnings(
    "ignore",
    message=".*tpfmodel submodule is not available.*"
)

import lightkurve as lk

search = lk.search_lightcurve(
    "Kepler-227 b",
    mission="Kepler"
)

lc = search.download()

print(lc.time)
print(lc.flux)
print(search)
