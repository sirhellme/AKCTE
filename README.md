# Kepler-553 Exoplanet Transit Analysis

A computational astronomy project for analyzing the Kepler light curve of **KIC 10937029 (Kepler-553)** using Python and Lightkurve.

The main goal of this project is to process photometric data from the Kepler mission, detect periodic transit signals, and investigate the orbital properties of the planets in the Kepler-553 system.

## Overview

Exoplanet transit analysis is based on detecting small decreases in a star's observed brightness when a planet passes in front of its host star.

For a normalized light curve,

<img width="210" height="87" alt="image" src="https://github.com/user-attachments/assets/6da9d942-06a6-400c-bb6f-607fcaf5955e" />

where:

- <img width="115" height="67" alt="image" src="https://github.com/user-attachments/assets/38700791-eaf7-42da-90e6-057f8a5089f9" />
 is the stellar flux outside the transit.
- <img width="115" height="67" alt="image" src="https://github.com/user-attachments/assets/665c81fa-b811-4b56-ba75-6b6fa91105b1" />
 is the flux during the transit.
- <img width="51" height="39" alt="image" src="https://github.com/user-attachments/assets/25a224b8-01a0-4302-be44-b98d226e3194" />
 is the transit depth.

The orbital period can then be estimated from the time interval between repeated transit events.

---

## Target System

**Target:** Kepler-553  
**KIC:** 10937029

The system contains at least two confirmed planets:

| Planet | Approx. orbital period |
|--------|-------------------------|
| Kepler-553 b | ~4.03 days |
| Kepler-553 c | ~328.24 days |

Kepler-553 c is particularly interesting because its orbital period is much longer than that of Kepler-553 b, making its transit signal more difficult to detect with a short observation segment.

---

## Objectives

This project aims to:

- Download Kepler photometric observations.
- Combine observations from multiple Kepler quarters.
- Clean and normalize the light curve.
- Remove NaN values and statistical outliers.
- Detrend the stellar light curve.
- Search for periodic transit signals using the Box Least Squares (BLS) method.
- Estimate the orbital period of the detected signal.
- Determine transit epochs.
- Fold the light curve according to the estimated period.
- Investigate the transit signal of Kepler-553 c.
- Compare the derived parameters with published values.

---

## Data

The observations are obtained from the **NASA Kepler mission** through the Lightkurve Python package.

The target is identified using:

```python
"KIC 10937029"
