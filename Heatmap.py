import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytaj dane z pliku Excel (zmień 'nazwa_pliku.xlsx' na nazwę swojego pliku)
df = pd.read_excel('C:/Users/damia/Desktop/heatmap.xlsx')

# Tworzenie heatmapy
plt.figure(figsize=(12, 8))

# Definicja heatmap_data przed użyciem
heatmap_data = df.pivot('Data', 'Temperatura', 'IloscSzkodnikow')

# Zaktualizuj brakujące wartości na najniższą możliwą wartość
heatmap_data = heatmap_data.fillna(heatmap_data)

# Usuń zera
heatmap_data[heatmap_data == 0] = np.nan

# Dodanie koloru dla pustych przestrzeni (NaN)
cmap = sns.color_palette("YlOrBr", as_cmap=True)

# Zwiększenie odstępów osi y (pionowej)
sns.heatmap(heatmap_data, annot=True, cmap=cmap, fmt=".0f", cbar_kws={'label': 'Ilość szkodników'},
            annot_kws={'size': 8})

# Zwiększenie odstępów między wartościami osi y (pionowej)
plt.yticks(rotation=0, ha='right', fontsize=11)

# Zwiększenie czcionki dla etykiet osi y (dat)
plt.xticks(fontsize=10)

plt.title('Częstotliwość pojawiania się owadów')
plt.xlabel('Temperatura powietrza (°C)')
plt.ylabel('Data')
plt.show()
