#%%
                #Exercice 1
def fib(n):
    a, b = 1, 1
    while b <= n:
        a, b = b, a + b
    return b
# Tests
print("Fibonacci de 75 est:", fib(75))
print("Fibonacci de 50 est:", fib(50))
print("Fibonacci de 100 est:", fib(100))
# %%
                 #Exercice 2
import numpy as np

BOS = [2.67, 1.00, 1.21, 3.09, 3.43, 4.71, 3.88, 3.08, 4.10, 2.62, 1.01, 5.93]
MER = [6.83, 3.63, 7.20, 2.68, 2.05, 2.96, 1.04, 0.00, 0.03, 6.71, 8.28, 6.85]

# Calcul des précipitations totales et moyennes
total_BOS = sum(BOS)
Moyenne_BOS = np.mean(BOS)
total_MER = sum(MER)
Moyenne_MER = np.mean(MER)

# Mois où les précipitations sont supérieures à la moyenne
Mois_superieur_moyenne_BOS = [i + 1 for i, val in enumerate(BOS) if val > Moyenne_BOS]
Mois_superieur_moyenne_MER = [i + 1 for i, val in enumerate(MER) if val > Moyenne_MER]

# Mois où les précipitations de Boston sont inférieures à celles de Seattle
Mois_BOS_inferieur_MER = [i + 1 for i, (b, m) in enumerate(zip(BOS, MER)) if b < m]

print(f"Total BOS: {total_BOS}, Moyenne BOS: {Moyenne_BOS}")
print(f"Total MER: {total_MER}, Moyenne MER: {Moyenne_MER}")
print(f"Mois > Moyenne BOS: {Mois_superieur_moyenne_BOS}")
print(f"Mois > Moyenne MER: {Mois_superieur_moyenne_MER}")
print(f"Mois BOS < MER: {Mois_BOS_inferieur_MER}")
# %%
                     #Exercice 3
import numpy as np
from scipy.stats import norm

def correlation_test(X, Y, r0):
    n = len(X)
    r = np.corrcoef(X, Y)[0, 1]
    Z = 0.5 * np.log((1 + r) / (1 - r))
    Z0 = 0.5 * np.log((1 + r0) / (1 - r0))
    T = (Z - Z0) * np.sqrt(n - 3)
    p_value = 2 * (1 - norm.cdf(abs(T)))
    return r, p_value

# Exemple de données
X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]

# Tests
r, p0 = correlation_test(X, Y, 0)
print(f"Corrélation: {r}, p-valeur pour r0=0: {p0}")
r, p6 = correlation_test(X, Y, 0.6)
print(f"Corrélation: {r}, p-valeur pour r0=0.6: {p6}")

#%%
                         #Exercice 4
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
r = 2
a = 0.05
beta = 1
generations = 30
host_pop = [20]
parasitoid_pop = [2]

# Modèle
for t in range(generations):
    H_next = host_pop[-1] * np.exp(-a * parasitoid_pop[-1]) * r
    P_next = host_pop[-1] * (1 - np.exp(-a * parasitoid_pop[-1])) * beta
    host_pop.append(H_next)
    parasitoid_pop.append(P_next)

# Graphique
time = range(generations + 1)
plt.plot(time, host_pop, label="Hôtes")
plt.plot(time, parasitoid_pop, label="Parasitoïdes")
plt.xlabel("Temps (générations)")
plt.ylabel("Population")
plt.legend()
plt.title("Modèle de Nicholson-Bailey")
plt.show()
# %%
# %%
class mere:
     nom_mere=""
def mere(self):
    print(self.nom_mere)
# %%
