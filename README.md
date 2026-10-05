# Analysis Light Curve Kepler-553


## Overview

This project analyzes real photometric observations of the exoplanet system Kepler-553 using computational methods. The main objective is to process multi-quarter Kepler observations, identify periodic transit signals, estimate the orbital period and transit epochs, construct a phase-folded light curve, and investigate the transit signal associated with Kepler-553 c.

--- 

## Target system

**Target**: Kepler-553 c

**KIC**: 10937029

The system must be contains at least one of these two confirmed planets:

| Planet        | Period (days) | Depth of Transit | Transit Duration |
|---------------|----------------|--------------------|-----------------|
| Kepler-553 b  | 4.030          | ~0.30 %            | ~2.80 hour       |
| Kepler-553 c  | 328.240        | ~1.43 %            | ~12.13 hour      |

My main focus of this project is to find the light curve of Kepler-553 c, it is particularly interesting because its orbital period is much longer than Kepler-553 b.

--- 

## Installation

### What do we need?
1. Download tables of Exoplanet (included inside in my repo)
2. Search for earth-like candidate with Earth_like_Candidate.py

### How to use it?

```bash 
pip install -r requirements.txt
bash install.sh
```

and after that you can use the:
```bash 
python3 main.py 
```


### Objectives

- Download the exoplanet photometric observations (for example: Kepler-553).
- Combine observations from multiple Kepler quarters.
- Clean and normalize the light curve.
- Remove NaN values and statistical outliers.
- Detrend the stellar light curve.
- Search for periodic transit signals using the Box Least Squares (BLS) method.
- Estimate the orbital period of the detected signal.
- Determine transit epochs (t0).
- Fold the light curve according to the estimated period.
- Investigate the transit signal of Kepler-553 c.
- Compare the derived parameters with published values.

## Data 
The observations are obtained from the **NASA Kepler Mission** and you can download the exact mission date you want from **NASA Archive Exoplanet**.

### Parameters 
- Orbital Period 
- Transit Epoch 
- Transit Duration 
- Depth of Transit 
- Power BLS  

### Data Processing 

The data-processing workflow is:
> Multiple Kepler Quarter Files -> Combine Data -> Sort by Time -> Data Inspection -> Remove NaN -> Remove Outliers -> Normalize the Flux -> Detrending -> Processed Light Curve

#### Transit Search
The estimated transit times are represented by:

> [t_n = t0 + nP]
_Where (P) is the orbital period and (t0) is the reference transit epoch._

The phase-folded light curve is calculated using:

> [\phi = \left \frac{t-t_0}{P}\right\bmod 1.]

To define the difference using:

> [ΔX = X_analysis − X_published] 



---

| Parameters | Derived Value |Published Uncertainty | Published Value | Difference |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| Orbital Period (P) | 328.238.234706 days | +0.00039 / −0.00040 | 328.240170 | 0.001665% |
| Transit Epoch (t0) | 199.221670 | 0.000858 | 19.203375 | 0.009184% |
| Transit Duration | 0.42 days | 0.00279583333 | 0.51135833 | 17.865815% |
| Depth of Transit | 0.67194886% | 0.00148 | 0.29083 | 131.045236% |

--- 

## Reference 
[^1] Agol, E., Luger, R. and Foreman-Mackey, D. (2020) 'Analytic Planetary Transit Light Curves and Derivatives for Stars with Polynomial Limb Darkening', doi:10.3847/1538-3881/ab4fee.
[^2] Aigrain, S., Parviainen, H. and Pope, B. (2016) 'K2SC: Flexible systematics correction and detrending of K2 light curves using Gaussian Process regression', doi:10.1093/mnras/stw706.
[^3] Aigrain, S. et al. (2016) 'Robust, open-source removal of systematics in Kepler data', Mon. Not. R. Astron. Soc, 000, pp. 1–12.
[^4] Berger, T.A. et al. (2020) 'The Gaia-Kepler Stellar Properties Catalog. I. Homogeneous Fundamental Properties for 186,301 Kepler Stars', doi:10.3847/1538-3881/159/6/280.
[^5] Christiansen, J.L. et al. (2020) 'Measuring Transit Signal Recovery in the Kepler Pipeline. IV. Completeness of the DR25 Planet Candidate Catalog', doi:10.3847/1538-3881/abab0b.
