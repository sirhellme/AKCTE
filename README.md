# Analysis Light Curve Kepler-553 (KIC 010937029)


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

My main focus of this project is with Kepler-553 c because it is particularly interesting because its orbital period is much longer than Kepler-553 b.

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

```
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
