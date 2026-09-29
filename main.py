import os 
import glob
import numpy as np
import matplotlib.pyplot as plt

from src.io import combined_quarter, clean_outliers
from src.transit import find_period, phase_fold

DATA = "../Exoplanet-Analysis/data/raw/Kepler553/"
OUTPUT = "../Exoplanet-Analysis/data/output"

TARGET = "Kepler-553 c"
KIC = "KIC 10937029"

TARGET_PERIOD = 328.24

def main():
    os.makedirs(OUTPUT, exist_ok=True)

    fits_files = glob.glob(os.path.join(DATA, "*.fits"))

    if len(fits_files) == 0:
        raise FileNotFoundError(
            f"No .fits file found in {DATA}"
        )
    else:
        print(f"Found {len(fits_files)} fits file, starting to combined...")
        time, flux = combined_quarter(DATA)
        clean_time, clean_flux = clean_outliers(time, flux)

    print(f"Target: {TARGET}")
    print(f"HOST: {KIC}")
    print(f"Expected Period: {TARGET_PERIOD} days")

    print(f"Numbers of points after cleaning: {len(clean_time)}")

    print("Finding the BLS...")
    result = find_period(clean_time, clean_flux)

    print(f"Best Period: {result['period']} days")
    print(f"Transit Time: {result['t0']}")
    print(f"Transit Durations: {result['duration']} days")
    print(f"Depth of Transit: {result['depth']*100} %")
    print(f"BLS Power: {result['power']}")

    phase, folded_flux = phase_fold(
        clean_time,
        clean_flux,
        result['period'],
        result['t0'])

    # save the summary
    with open(os.path.join(OUTPUT, "result of analysis.txt"), "w") as f:
        f.write(f"Number of Data Points: {len(clean_time)}\n")
        f.write(f"Best Period: {result['period']:.6f} days\n")
        f.write(f"Epoch   : {result['t0']:.6f}\n")
        f.write(f"Transit Duration    : {result['duration']:.6f} days\n")
        f.write(f"Depth of transit : {result['depth']*100:.6f} %\n")
        f.write(f"Power BLS         : {result['power']:.4f}\n")

    fig, ax = plt.subplots(2, 2, figsize=(12, 8))

    ax[0, 0].plot(time, flux, ".", ms=2, color="gray")
    ax[0, 0].set_title("Raw Light Curve")
    ax[0, 0].set_xlabel("Time (days)")
    ax[0, 0].set_ylabel("Flux")

    ax[0, 1].plot(clean_time, clean_flux, ".", ms=2, color="steelblue")
    ax[0, 1].set_title("After Cleaned & Normalized")
    ax[0, 1].set_xlabel("Time (days)")
    ax[0, 1].set_ylabel("Flux relative")

    ax[1, 0].plot(result["period_grid"], result["power_grid"], color="darkorange")
    ax[1, 0].axvline(result["period"], color="red", linestyle="--", linewidth=1)
    ax[1, 0].set_title("Periodogram BLS")
    ax[1, 0].set_xlabel("Period (days)")
    ax[1, 0].set_ylabel("Power")

    ax[1, 1].plot(phase, folded_flux, ".", ms=3, color="black")
    ax[1, 1].set_title(f"Folded Curve (P = {result['period']:.3f} days)")
    ax[1, 1].set_xlabel("Phase")
    ax[1, 1].set_ylabel("Flux relative")
    ax[1, 1].set_xlim(-0.5, 0.5)

    fig.tight_layout()
    path_gambar = os.path.join(OUTPUT, "light curve analysis.png")
    fig.savefig(path_gambar, dpi=200)
    plt.close(fig)

    print(f"\nThe Image saved in {path_gambar}")
    print(f"The Summary saved in {os.path.join(OUTPUT, 'result of analysis.txt')}")


if __name__ == "__main__":
    main()
