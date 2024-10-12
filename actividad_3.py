import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# data = {
#     'distancia': [5, 10, 20, 15, 25],
#     'pasajeros': [100, 150, 80, 60, 120],
#     'frecuencia': [10, 5, 15, 7, 6],
#     'demanda_alta': [1, 0, 1, 0, 1]  
# }

data = {
    'distancia': [5, 10, 20, 15, 25, 12, 8, 7, 19, 22, 30, 4],
    'pasajeros': [100, 150, 80, 60, 120, 95, 110, 70, 85, 200, 250, 50],
    'frecuencia': [10, 5, 15, 7, 6, 8, 9, 11, 4, 3, 6, 12],
    'demanda_alta': [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0] 
}

df = pd.DataFrame(data)


X = df[['distancia', 'pasajeros', 'frecuencia']]
y = df['demanda_alta']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


modelo = DecisionTreeClassifier()


modelo.fit(X_train, y_train)


predicciones = modelo.predict(X_test)


accuracy = accuracy_score(y_test, predicciones)
print(f'Precisión del modelo: {accuracy * 100:.2f}%')