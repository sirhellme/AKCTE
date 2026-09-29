import os
import glob 
import numpy as np
from astropy.io import fits

def read_one_quarter(path):
    with fits.open(path) as hdul:
        print(hdul)
        table = hdul[1].data

        time = np.asarray(table["TIME"], dtype=float)
        flux = np.asarray(table["PDCSAP_FLUX"], dtype=float)

    mask = (
        np.isfinite(time)
        & np.isfinite(flux)
    )
    time = time[mask]
    flux = flux[mask]

    return time, flux

def normalized_quarter(time, flux):
    median_flux = np.median(flux)

    if not np.isfinite(median_flux) or median_flux == 0:
        raise ValueError("Median flux is not valid!")

    flux_normalized = flux / median_flux

    return time, flux_normalized

def combined_quarter(folder):
    file_lists = sorted(
        glob.glob(os.path.join(folder, "*.fits"))
    )

    if len(file_lists) == 0:
        raise FileNotFoundError(
            f"The .fits is not exist in '{folder}'"
        )

    all_time = []
    all_flux = []

    print("Reading the Kepler files:")

    for path in file_lists:
        name = os.path.basename(path)

        try:
            time, flux = read_one_quarter(path)

            time, flux = normalized_quarter(time, flux)

            all_time.append(time)
            all_flux.append(flux)

            print(
                f"OK    {name:<45} "
                f"{len(time):>6} titik"
            )
        except Exception as e:

            print(
                f"SKIP  {name:<45}"
                f"{e}"
            )

    if len(all_time) == 0:
        raise RuntimeError(
            "Nothing .fits file that can read!"
        )
    
    time = np.concatenate(all_time)
    flux = np.concatenate(all_flux)

    sort_time = np.argsort(time)

    time = time[sort_time]
    flux = flux[sort_time]

    return time, flux

def clean_outliers(time, flux, n_sigma=5):
    mask = np.isfinite(time) & np.isfinite(flux)

    time = time[mask]
    flux = flux[mask]

    for _ in range(3):

        median_flux = np.median(flux)
        # Standard Deviation
        std_flux = np.std(flux)

        if not np.isfinite(std_flux) or std_flux == 0:
            break 

        mask = np.abs(flux - median_flux) < n_sigma * std_flux

        time = time[mask]
        flux = flux[mask]
    return time, flux