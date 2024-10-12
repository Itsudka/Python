import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


data = {
    'distancia': [5, 10, 20, 15, 25, 12, 8, 7, 19, 22, 30, 4],
    'duracion': [30, 45, 60, 50, 70, 40, 35, 33, 55, 75, 90, 25],
    'pasajeros': [100, 150, 80, 60, 120, 95, 110, 70, 85, 200, 250, 50]
}

df = pd.DataFrame(data)


kmeans = KMeans(n_clusters=3, random_state=42)


kmeans.fit(df)


df['cluster'] = kmeans.labels_


print(df)


plt.scatter(df['distancia'], df['duracion'], c=df['cluster'], cmap='viridis')
plt.xlabel('Distancia (km)')
plt.ylabel('Duración (min)')
plt.title('Agrupamiento de Viajes por Distancia y Duración')
plt.show()
print(f'Inercia del modelo: {kmeans.inertia_}')