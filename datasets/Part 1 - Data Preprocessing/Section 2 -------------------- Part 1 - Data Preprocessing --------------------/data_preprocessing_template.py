#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20-10-2019

@author: joaJua
"""

# Plantilla de Pre Procesado

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Data.csv')


#variables independientes
# quiero todas las filas>> uso :
# quiero todas salvo la ultima columna>> uso el -1
X = dataset.iloc[:, :-1].values

#variable dependiente a predecir
y = dataset.iloc[:, 3].values


# Dividir el data set en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Escalado de variables
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""