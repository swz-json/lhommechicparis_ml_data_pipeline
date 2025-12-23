# lhommechicparis_ml_data_pipeline
Pipeline de données de bout en bout pour L'Homme Chic Paris : chargement, nettoyage et livraison des données de vente à un modèle d'apprentissage automatique TensorFlow. Inspiré par le framework tfdsio pour l'automatisation des ensembles de données.

## 📖 Project Overview  
Ce projet présente un pipeline de données de bout en bout (end-to-end) conçu pour L'Homme Chic Paris, une marque e-commerce spécialisée dans les accessoires pour hommes.

L'objectif est d'automatiser la préparation des données (chargement, nettoyage, transformation) et de livrer des ensembles de données propres à un modèle d'apprentissage automatique TensorFlow pour l'analyse et la prévision.

---

## ⚙️ Fonctionnalités  
- Chargement des données de vente depuis Excel (bd-vente.xlsx)

- Nettoyage et normalisation des données

- Calcul des ventes totales par transaction

- Division des données en ensembles d'entraînement/test (train/test sets)

- Entraînement d'un modèle TensorFlow simple pour identifier les schémas de vente

- Exportation de l'ensemble de données nettoyé (clean_bd_vente.xlsx)

- Prêt pour l'automatisation future avec Airflow ou l'intégration Power BI 

---

## 📊 Project Results (Power BI Dashboard)
Here is the final output of the data pipeline, visualizing sales performance and customer insights:


<img width="1341" height="753" alt="dashboard" src="https://github.com/user-attachments/assets/db114ae3-af33-46b9-914a-cbcbfd0b076b" />

## 🧰 Stack Technique
| Category | Tools |
|-----------|-------|
| Data Handling | Python, Pandas |
| Machine Learning | TensorFlow, Scikit-learn |
| Automation | (planned) Apache Airflow |
| Visualization | Power BI (planned) |
| Version Control | Git & GitHub |

---
## 📈 Sortie du Terminal :
Après 20 époques d'entraînement, le modèle a atteint une erreur absolue moyenne (Mean Absolute Error) d'environ 445 €, ce qui signifie qu'en moyenne, la prédiction se situe dans une fourchette de $\pm 445 €$ de la valeur réelle des ventes.

```bash
Epoch 20/20
loss: 284832.5938 - mae: 405.3340
✅ Model trained! Mean Absolute Error: 445.95
```

