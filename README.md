# Kepler-553 Light Curve Analysis

## Overview

This project analyzes real photometric observations of the **Kepler-553 exoplanet system** using computational methods. The main objective is to process multi-quarter Kepler observations, identify periodic transit signals, estimate the orbital period and transit epoch, construct a phase-folded light curve, and investigate the transit signal associated with **Kepler-553 c**.

The analysis uses the **Box-fitting Least Squares (BLS)** method to search for periodic transit signals in the observed light curve.

---

## Target System

**Target:** Kepler-553 c
**KIC:** 10937029

The Kepler-553 system contains at least two confirmed planets:

| Planet       | Period (days) | Transit Depth | Transit Duration |
| ------------ | ------------: | ------------: | ---------------: |
| Kepler-553 b |         4.030 |        ~0.30% |      ~2.80 hours |
| Kepler-553 c |       328.240 |        ~1.43% |     ~12.13 hours |

The main focus of this project is **Kepler-553 c**. It is particularly interesting because its orbital period is significantly longer than that of Kepler-553 b, making its transit signal more challenging to detect from the available Kepler observations.

---

## Installation

### Requirements

The project requires:

1. Python 3
2. The Python packages listed in `requirements.txt`
3. The required data files included in the repository
4. A compatible C++ compiler for the computational simulation

Install the required dependencies with:

```bash
pip install -r requirements.txt
```

The repository also provides an installation script:

```bash
bash install.sh
```

---

## Usage

After installing the required dependencies, the main analysis can be executed with:

```bash
python3 main.py
```

The project also contains supporting scripts for data preparation and analysis.

---

## Objectives

The main objectives of this project are:

* Download and process photometric observations of the Kepler-553 system.
* Combine observations from multiple Kepler quarters.
* Inspect and organize the observational data.
* Remove missing (`NaN`) values.
* Remove statistical outliers.
* Normalize the observed flux.
* Detrend the stellar light curve.
* Search for periodic transit signals using the **Box-fitting Least Squares (BLS)** method.
* Estimate the orbital period of the detected signal.
* Determine the transit epoch (`t0`).
* Estimate the transit duration and transit depth.
* Fold the light curve according to the estimated orbital period.
* Investigate the transit signal associated with Kepler-553 c.
* Compare the derived parameters with published values.
* Use the derived parameters as input for a computational simulation.

---

## Data

The observational data are obtained from the **NASA Kepler Mission**. The project uses Kepler photometric observations associated with the Kepler-553 system.

The data can be obtained from the **NASA Exoplanet Archive** and the relevant Kepler data archives.

### Parameters

The main transit parameters analyzed in this project are:

* **Orbital Period (`P`)**
* **Transit Epoch (`t0`)**
* **Transit Duration**
* **Transit Depth**
* **BLS Power**

---

## Data Processing

The data-processing workflow is:

```text
Multiple Kepler Quarter Files
            ↓
      Combine Data
            ↓
       Sort by Time
            ↓
       Data Inspection
            ↓
        Remove NaN
            ↓
      Remove Outliers
            ↓
      Normalize Flux
            ↓
         Detrending
            ↓
   Processed Light Curve
            ↓
       BLS Analysis
            ↓
      Transit Detection
            ↓
      Phase Folding
```

### Transit Search

The transit times are represented by:

$$
t_n = t_0 + nP
$$

where:

* $t_n$ is the time of the $n$-th transit,
* $t_0$ is the reference transit epoch,
* $P$ is the orbital period,
* $n$ is an integer representing the transit number.

The phase-folded light curve is calculated using:

$$
\phi =
\left(
\frac{t-t_0}{P}
\right)
\bmod 1
$$

where:

* $\phi$ is the orbital phase,
* $t$ is the observation time,
* $t_0$ is the reference transit epoch,
* $P$ is the orbital period.

### Parameter Comparison

To compare the parameters obtained from the analysis with published values, the absolute difference is defined as:

$$
\Delta X = X_{\mathrm{analysis}} - X_{\mathrm{published}}
$$

The relative percentage difference is calculated as:

$$
\Delta X_{\%}
=
\frac{
\left|X_{\mathrm{analysis}}-X_{\mathrm{published}}\right|
}{
\left|X_{\mathrm{published}}\right|
}
\times 100\%
$$

---

## Results

The following table summarizes the transit parameters obtained from the analysis and their comparison with published values.

| Parameter            |   Derived Value |    Published Uncertainty | Published Value |  Difference |
| -------------------- | --------------: | -----------------------: | --------------: | ----------: |
| Orbital Period (`P`) | 328.234706 days | +0.00039 / −0.00040 days | 328.240170 days |   0.001665% |
| Transit Epoch (`t0`) | 199.221670 BKJD |            0.000858 days | 199.203375 BKJD |   0.009184% |
| Transit Duration     |       0.42 days |       0.00279583333 days | 0.51135833 days |  17.865815% |
| Transit Depth        |     0.67194886% |                 0.00148% |       0.290830% | 131.045236% |

### Interpretation

The derived orbital period is very close to the published value, with a relative difference of approximately **0.001665%**. The estimated transit epoch also shows a small difference of approximately **0.009184%**.

However, the derived transit duration and transit depth show substantially larger differences from the published values. These differences may be influenced by the BLS model, detrending procedure, transit sampling, and the treatment of the observed light curve.

Therefore, the derived parameters should be interpreted as **results of the computational analysis**, rather than as replacements for the published planetary parameters.

---

## Computational Simulation

The derived transit parameters are subsequently used as input for a computational simulation implemented in **C++**.

The simulation is intended to provide a visual representation of the detected transit signal and its relationship to the derived orbital parameters.

The main simulation parameters are:

```text
Orbital Period     : 328.234706 days
Transit Epoch      : 199.221670 BKJD
Transit Duration   : 0.42 days
Transit Depth      : 0.67194886%
```

The simulation is not intended to replace the observational analysis. Instead, it provides a computational visualization of the transit model derived from the BLS analysis.

---

## Output Files

The analysis produces several output files containing the processed light curve, transit-search results, and derived parameters.

### Generated Files

| File                           | Description                                                                                                                         |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| `processed_light_curve.csv`    | Cleaned, normalized, and detrended light-curve data used for the transit analysis.                                                  |
| `bls_results.csv`              | Results from the Box-fitting Least Squares (BLS) period search, including the tested periods and corresponding BLS power.           |
| `phase_folded_light_curve.csv` | Light-curve data folded using the derived orbital period and transit epoch.                                                         |
| `transit_parameters.txt`       | Summary of the derived transit parameters, including orbital period, transit epoch, transit duration, transit depth, and BLS power. |
| `light_curve.png`              | Plot of the processed photometric light curve.                                                                                      |
| `bls_periodogram.png`          | BLS periodogram showing the detected periodic transit signal.                                                                       |
| `phase_folded_light_curve.png` | Phase-folded light curve showing the detected transit signal.                                                                       |

### C++ Simulation Output

The C++ simulation provides a graphical representation of the detected transit model using the parameters obtained from the BLS analysis.

The simulation uses:

```text
Orbital Period     : 328.234706 days
Transit Epoch      : 199.221670 BKJD
Transit Duration   : 0.42 days
Transit Depth      : 0.67194886%
```

The simulation displays:

* The host star and planetary orbit.
* The position of the planet during its orbit.
* The transit event.
* The simulated light curve.
* The derived BLS parameters.

The C++ simulation is intended as a visualization of the computational results and does not replace the observational light-curve analysis.

### Output Directory

The generated analysis results are stored in the project's output directory:

```text
output/
├── processed_light_curve.csv
├── bls_results.csv
├── phase_folded_light_curve.csv
├── transit_parameters.txt
├── light_curve.png
├── bls_periodogram.png
└── phase_folded_light_curve.png
```

The exact files generated may depend on the analysis configuration and scripts used.

---

## References
[^1] Agol, E., Luger, R. and Foreman-Mackey, D. (2020) 'Analytic Planetary Transit Light Curves and Derivatives for Stars with Polynomial Limb Darkening'. *The Astronomical Journal*. doi:10.3847/1538-3881/ab4fee.

[^2] Aigrain, S., Parviainen, H. and Pope, B. (2016) 'K2SC: Flexible systematics correction and detrending of K2 light curves using Gaussian Process regression'. *Monthly Notices of the Royal Astronomical Society*. doi:10.1093/mnras/stw706.

[^3] Aigrain, S. *et al.* (2016) 'Robust, open-source removal of systematics in Kepler data'. *Monthly Notices of the Royal Astronomical Society*, 000, pp. 1–12.

[^4] Berger, T. A. *et al.* (2020) 'The Gaia-Kepler Stellar Properties Catalog. I. Homogeneous Fundamental Properties for 186,301 Kepler Stars'. *The Astronomical Journal*, 159(6), 280. doi:10.3847/1538-3881/ab4fee.

[^5] Christiansen, J. L. *et al.* (2020) 'Measuring Transit Signal Recovery in the Kepler Pipeline. IV. Completeness of the DR25 Planet Candidate Catalog'. *The Astrophysical Journal*, 908, 86. doi:10.3847/1538-3881/abab0b.
