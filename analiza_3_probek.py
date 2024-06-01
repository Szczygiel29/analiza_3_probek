import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Próbka': ['Próbka 1', 'Próbka 2', 'Próbka 3'],
    'O2 (%)': [0.32, 1.55, 0.30],
    'O2 Odchylenie (%)': [0.06, 0.29, 0.06],
    'CO2 (%)': [36.05, 33.11, 33.62],
    'CO2 Odchylenie (%)': [2.02, 1.85, 1.88],
    'CO (%)': [0.0002, 0.0002, 0.0002],
    'CH4 (%)': [63.08, 58.60, 65.99],
    'CH4 Odchylenie (%)': [3.78, 3.52, 3.96],
    'H2 (%)': [0.005, 0.005, 0.005],
    'C2H4 (%)': [0.005, 0.005, 0.005],
    'C2H6 (%)': [0.005, 0.005, 0.005],
    'N2 (%)': [0.56, 0.56, 0.09],
    'N2 Odchylenie (%)': [4.29, 6.74, 4.38],
    'Wartość opałowa (MJ/m3)': [22.67, 21.05, 23.71],
    'Wartość opałowa Odchylenie (MJ/m3)': [1.37, 1.27, 1.43]
}

df = pd.DataFrame(data)

# Obliczanie przedziałów wartości opałowej
df['Wartość opałowa min (MJ/m3)'] = df['Wartość opałowa (MJ/m3)'] - df['Wartość opałowa Odchylenie (MJ/m3)']
df['Wartość opałowa max (MJ/m3)'] = df['Wartość opałowa (MJ/m3)'] + df['Wartość opałowa Odchylenie (MJ/m3)']

# Analiza wpływu poszczególnych składników na wartość opałową
# Założenie: Ciepło spalania CH4 = 35.8 MJ/m3, CO2, O2, H2, C2H4, C2H6, N2 mają pomijalny wpływ na wartość opałową

# Procentowy udział CH4 w wartości opałowej
df['Udział CH4 w wartości opałowej (MJ/m3)'] = df['CH4 (%)'] * 35.8 / 100

# Podsumowanie statystyczne danych
summary_stats = df.describe()

# Wykresy
plt.figure(figsize=(14, 10))

# Wykres zawartości O2
plt.subplot(3, 2, 1)
plt.errorbar(df['Próbka'], df['O2 (%)'], yerr=df['O2 Odchylenie (%)'], fmt='o', capsize=5)
plt.title('Zawartość O2 w próbkach biogazu')
plt.xlabel('Próbka')
plt.ylabel('O2 (%)')

# Wykres zawartości CO2
plt.subplot(3, 2, 2)
plt.errorbar(df['Próbka'], df['CO2 (%)'], yerr=df['CO2 Odchylenie (%)'], fmt='o', capsize=5)
plt.title('Zawartość CO2 w próbkach biogazu')
plt.xlabel('Próbka')
plt.ylabel('CO2 (%)')

# Wykres zawartości CH4
plt.subplot(3, 2, 3)
plt.errorbar(df['Próbka'], df['CH4 (%)'], yerr=df['CH4 Odchylenie (%)'], fmt='o', capsize=5)
plt.title('Zawartość CH4 w próbkach biogazu')
plt.xlabel('Próbka')
plt.ylabel('CH4 (%)')

# Wykres wartości opałowej
plt.subplot(3, 2, 4)
plt.errorbar(df['Próbka'], df['Wartość opałowa (MJ/m3)'], yerr=df['Wartość opałowa Odchylenie (MJ/m3)'], fmt='o', capsize=5)
plt.title('Wartość opałowa biogazu')
plt.xlabel('Próbka')
plt.ylabel('Wartość opałowa (MJ/m3)')

# Wykres udziału CH4 w wartości opałowej
plt.subplot(3, 2, 5)
plt.bar(df['Próbka'], df['Udział CH4 w wartości opałowej (MJ/m3)'], color='orange')
plt.title('Udział CH4 w wartości opałowej')
plt.xlabel('Próbka')
plt.ylabel('Udział CH4 (MJ/m3)')

plt.tight_layout()
plt.show()

# Wyświetlanie podsumowania statystycznego
print("Podsumowanie statystyczne danych:")
print(summary_stats)
