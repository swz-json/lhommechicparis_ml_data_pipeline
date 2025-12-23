<div align="center">
  <img width="120" height="120" alt="symbol l homme chic paris" src="https://github.com/user-attachments/assets/e116d19b-401f-4825-822a-46b400fec4db" />
  <h1>L'Homme Chic Paris</h1>



# 👔 Pipeline Data & ML End-to-End : L'Homme Chic Paris

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-F2C811)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📖 Aperçu du Projet

Ce projet est un pipeline de données complet (**End-to-End**) conçu pour **L'Homme Chic Paris**, une marque e-commerce spécialisée dans la mode masculine.

L'objectif principal est de transformer des données brutes transactionnelles en *insights* actionnables. Le pipeline automatise l'ingestion, le nettoyage et la préparation des données pour alimenter à la fois :
1.  Un **Tableau de Bord Power BI** pour le suivi des KPIs business.
2.  Un **Modèle de Machine Learning (TensorFlow)** pour la prévision des ventes.

---

## 🏗️ Architecture & Flux de Données

Le projet suit un flux ETL (Extract, Transform, Load) strict :

1.  **Ingestion :** Chargement des données brutes depuis les exports transactionnels (`bd-vente.xlsx`).
2.  **Processing (Pandas) :**
    * Nettoyage des valeurs nulles et formatage des dates.
    * Normalisation des catégories produits.
    * Agrégation des ventes par transaction (Feature Engineering).
3.  **Machine Learning (TensorFlow) :** Entraînement d'un réseau de neurones pour identifier les corrélations prix/quantité.
4.  **Reporting :** Export des données propres (`clean_bd_vente.xlsx`) vers Power BI.

---

## 📊 Business Intelligence (Résultats)

Le pipeline alimente ce tableau de bord interactif, permettant aux équipes métier de suivre les performances en temps réel.

![Tableau de bord Power BI L'Homme Chic Paris](https://github.com/user-attachments/assets/db114ae3-af33-46b9-914a-cbcbfd0b076b)
*Vue d'ensemble : Chiffre d'affaires, Panier moyen, Analyse géographique et Top Produits.*

---

## ⚙️ Fonctionnalités Techniques

### 🔹 Data Engineering
- **ETL Automatisé :** Script Python modulaire pour le traitement des fichiers Excel.
- **Data Quality :** Validation des types de données et gestion des anomalies.
- **Export :** Génération automatique de datasets prêts pour l'analyse (`clean_bd_vente.xlsx`).

### 🔹 Machine Learning
- **Split Train/Test :** Séparation rigoureuse des données pour valider le modèle.
- **Modélisation :** Utilisation de `TensorFlow` (Keras) pour créer un modèle de régression.
- **Métriques :** Évaluation via MAE (Mean Absolute Error) pour quantifier la précision.

---

## 🧰 Stack Technique

| Domaine | Outils utilisés |
|-----------|-----------------|
| **Langage** | Python 3.10 |
| **Manipulation de Données** | Pandas, NumPy |
| **Machine Learning** | TensorFlow, Scikit-learn |
| **Visualisation** | Power BI, Matplotlib |
| **Contrôle de Version** | Git & GitHub |

---

## 🚀 Comment lancer le projet ?

```bash
# 1. Cloner le dépôt
git clone [https://github.com/swz-json/lhommechicparis_ml_data_pipeline.git](https://github.com/swz-json/lhommechicparis_ml_data_pipeline.git)

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer le pipeline ETL et l'entraînement
python main.py
