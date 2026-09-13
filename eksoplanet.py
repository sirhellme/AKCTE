import numpy as np
import matplotlib.pyplot as plt

# Data pengamatan
t = np.array([
    0.0, 0.5, 1.0, 1.5, 2.0,
    2.5, 3.0, 3.5, 4.0, 4.5, 5.0
])

F = np.array([
    1.000, 1.001, 1.000, 0.998, 0.993,
    0.990, 0.993, 0.998, 1.000, 1.001, 1.000
])

# Fluks maksimum sebagai pendekatan
# fluks di luar transit
F_out = np.max(F)

# Fluks minimum
F_in = np.min(F)

# Kedalaman transit
delta = (F_out - F_in) / F_out

# Radius relatif planet
Rp_Rstar = np.sqrt(delta)

# Radius bintang (km)
Rstar = 696340

# Radius planet
Rp = Rp_Rstar * Rstar

print("Fluks luar transit =", F_out)
print("Fluks minimum      =", F_in)
print("Kedalaman transit  =", delta)
print("Rp/Rstar            =", Rp_Rstar)
print("Radius planet (km) =", Rp)

plt.figure(figsize=(8, 5))

plt.plot(t, F, 'o-')

plt.xlabel("Waktu (jam)")
plt.ylabel("Fluks ternormalisasi")
plt.title("Kurva Cahaya Transit Eksoplanet")

plt.grid()
plt.show()