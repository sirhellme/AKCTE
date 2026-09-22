import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = "/home/hell/Projects/AKCTE Komputasi/dataset.csv"

df =pd.read_csv(file)

print("DATASET EKSOPLANET")
print("=" * 60)

print(f"Jumlah data awal : {len(df)}")
print(f"Jumlah kolom : {len(df.columns)}")

print("\nNama kolom: ")
print(df.columns.tolist())

print("INFORMASI DATA")
print("=" * 30)
print(df.info())

print("\nJumlah NaN setiap kolom:")
print(df.isna().sum())

columns = [
    "Planet_Name",
    "Planet_Radius",
    "Planet_Mass",
    "Temp_equilibrium",
    "Period",
    "Temp_stellar_eff",
]

data = df[columns].copy()

numeric_columns = [
    "Planet_Radius",
    "Planet_Mass",
    "Temp_equilibrium",
    "Period",
    "Temp_stellar_eff",
]

for column in numeric_columns:
    data[column] = pd.to_numeric(
        data[column],
        errors="coerce"
    )

data = data.dropna(
    subset=[
        "Planet_Radius",
        "Planet_Mass",
        "Temp_equilibrium",
    ]
)

print("\nJumlah data setelah cleaning:", len(data))

earth_like = data[
    (data["Planet_Radius"].between(0.8, 1.25)) &
    (data["Planet_Mass"].between(0.5, 1.5)) &
    (data["Temp_equilibrium"].between(200, 320))
].copy()

print("\nHasil Seleksi Earth-Like")
print(f"Jumlah kandidat : {len(earth_like)}")

# Parameter Bumi
EARTH_RADIUS = 1.0
EARTH_MASS = 1.0
EARTH_TEQ = 255.0

# Skala toleransi
RADIUS_SCALE = 0.5
MASS_SCALE = 1.0
TEMP_SCALE = 100.0

# Radius Score
earth_like["score_radius"] = (
    1 - 
    abs(earth_like["Planet_Radius"] - EARTH_RADIUS)
    / RADIUS_SCALE
)

# Mass Score
earth_like["score_mass"] = (
    1 -
    abs(earth_like["Planet_Mass"] - EARTH_MASS)
    / MASS_SCALE
)

# Temperature Score

earth_like["score_temp"] = (
    1 - 
    abs(earth_like["Temp_equilibrium"] - EARTH_TEQ)
    / TEMP_SCALE
)

# Pastikan score tidak negatif!
earth_like["score_radius"] = (
    earth_like["score_radius"].clip(0, 1)
)

earth_like["score_mass"] = (
    earth_like["score_mass"].clip(0, 1)
)

earth_like["score_temp"] = (
    earth_like["score_temp"].clip(0, 1)
)

# Total kemiripan dengan bumi
earth_like["Earth_Similiarity"] = (
    0.4 * earth_like["score_radius"] +
    0.4 * earth_like["score_mass"] +
    0.2 * earth_like["score_temp"] 
)

# Sorting
earth_like = earth_like.sort_values(
    "Earth_Similiarity",
    ascending=False
)

# 20 Kandidat teratas

print("\n 20 Kandidat TERATAS JATUH KEPADA....")

result = earth_like[
    [
        "Planet_Name",
        "Planet_Radius",
        "Planet_Mass",
        "Temp_equilibrium",
        "Period",
        "Temp_stellar_eff",
    ]
].head(20)

print(result.to_string(index=False))

# Simpan Hasil
output_file = "earth_like_cand.csv"

earth_like.to_csv(
    output_file,
    index=False
)

print("\nHasil disimpan sebagai:")
print(output_file)

# Visualisasi Radius vs Mass
plt.figure(figsize=(8, 6))

plt.scatter(
    data["Planet_Radius"],
    data["Planet_Mass"], 
    alpha=0.3,
    label="All planets"
)

plt.scatter(
    EARTH_RADIUS,
    EARTH_MASS,
    marker="*",
    s=250,
    label="Earth"
)

plt.xlabel("Planet Radius (R$_\\oplus$)")
plt.ylabel("Planet Mass (M$_\\oplus$)")

plt.title("Planet Radius vs Planet Mass")
plt.legend()
plt.grid(alpha=0.2)
plt.tight_layout()
plt.show()

#  Radius vs Temperature
plt.figure(figsize=(8, 6))

plt.scatter(data["Planet_Radius"], 
    data["Temp_equilibrium"], 
    alpha=0.3, 
    label="All planets" 
) 
plt.scatter(earth_like["Planet_Radius"],
    earth_like["Temp_equilibrium"],
    alpha=0.8,
    label="Earth-like candidates"
) 
plt.scatter(EARTH_RADIUS,
    EARTH_TEQ,
    marker="*", 
    s=250, 
    label="Earth"
 )

plt.xlabel("Planet Radius (R$_\\oplus$)")
plt.ylabel("Equilibrium Temperature (K)")

plt.title("Planet Radius vs Equilibrium Temp")

plt.legend()
plt.grid(alpha=0.2)

plt.tight_layout()
plt.show()

# Distribusi Earth Similiarity
plt.figure(figsize=(8, 6))

plt.hist(
    earth_like["Earth_Similiarity"],
    bins=20
)

plt.xlabel("Earth Similiarity Score")
plt.ylabel("Number of Planets")

plt.title("Distribution of Earth Similiarity Score")

plt.grid(alpha=0.2)
plt.tight_layout()
plt.show()