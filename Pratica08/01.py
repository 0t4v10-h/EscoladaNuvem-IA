""""
Comparação de Métricas de Classificação em IA
Calcular e comparar diferentes métricas de classificação (Precisão, Recall, F1-Score, AUC-ROC) usando um modelo de aprendizado de máquina em Python.

Sugestão
Usar o conjundo de dados (dataset) load_breast_cancer disponível na biblioteca scikit-learn;
Utilize o algoritmo Random Forest;
Dividir o conjunto de dados em 70% para treino e 30% para teste, garantindo a reprodutibilidade dos dados com 'random_state=42';
Variável target (vetor) composta de 0 (maligno) ou 1 (benigno)

Objetivo
Analisar o desempenho do modelo de classificação por meio das métricas selecionadas, discutindo os resultados obtidos para essa situação médica.

Sugestão de dependências
scikit-learn==1.4.0
pandas==2.2.0
numpy==1.26.3
matplotlib==3.8.2
seaborn==0.13.1
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score
import matplotlib.pyplot as plt
import numpy as np  
import pandas as pd

# Carregar o conjunto de dados
data = load_breast_cancer()
X = data.data
y = data.target

# Dividir o conjunto de dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Criar o modelo de Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Treinar o modelo
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Probabilidades para AUC-ROC
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Avaliar o desempenho do modelo
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc_roc = roc_auc_score(y_test, y_pred_proba)

print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)
print("AUC-ROC:", auc_roc)
