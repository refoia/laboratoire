




import numpy as np

# Constantes
G = 6.67408e-11  # Constante de gravitation universelle en m^3 kg^-1 s^-2
M_earth = 5.972e24  # Masse de la Terre en kg
M_moon = 7.34767309e22  # Masse de la Lune en kg

# Période de révolution de la Lune autour de la Terre en secondes
T = 29.530588853 * 86400  # Un mois lunaire

# Calcul de la distance moyenne entre la Terre et la Lune
r = ((G * M_earth * T**2) / (4 * np.pi**2))**(1/3)
print(f"Distance moyenne Terre-Lune : {r:.2f} m")

# Calcul de la distance Terre-Lune chaque année
num_years = 10
for i in range(num_years):
    r = ((G * M_earth * (T + i*365*86400)**2) / (4 * np.pi**2))**(1/3)
    print(f"Distance Terre-Lune en année {i+1}: {r:.2f} m")

# Ce code calcule d'abord la distance moyenne entre la Terre et la Lune en utilisant la période de révolution de la Lune autour de la Terre. Ensuite, il calcule la distance entre la Terre et la Lune chaque année en ajoutant la durée d'une année à la période de révolution et en effectuant à nouveau le calcul.

# Il est important de noter que cette approche ne tient pas compte des perturbations gravitationnelles causées par d'autres corps célestes, comme le Soleil, et ne donnera donc pas une précision absolue. Cependant, elle peut être utilisée comme une estimation grossière de la distance entre la Terre et la Lune au fil du temps. Si vous avez des questions sur son utilisation ou si vous souhaitez en savoir plus sur la loi de Kepler, n'hésitez pas à me poser d'autres questions.








