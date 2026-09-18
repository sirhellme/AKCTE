import warnings
import lightkurve as lk
import matplotlib.pyplot as py

warnings.filterwarnings(
    "ignore",
    message=".*tpfmodel submodule is not available.*"
)

search = lk.search_lightcurve(
    "Kepler-227 b",
    mission="Kepler"
)

lc = search.download()

print(lc.time)
print(lc.flux)
print(search)
