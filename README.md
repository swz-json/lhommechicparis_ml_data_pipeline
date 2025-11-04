# lhommechicparis_ml_data_pipeline
End-to-end data pipeline project for L’Homme Chic Paris: loading, cleaning, and delivering sales data into a TensorFlow machine learning model. Inspired by the tfdsio framework for dataset automation.

## 📖 Project Overview  
This project demonstrates an **end-to-end data pipeline** built for **L’Homme Chic Paris**, an e-commerce brand specialized in men’s accessories.  
The goal is to **automate data preparation** (loading, cleaning, transforming) and deliver clean datasets to a **TensorFlow machine-learning model** for analytics and forecasting.

> 🧩 Inspired by the open-source framework [tfdsio](https://github.com/trisongz/tfdsio), which dynamically builds TensorFlow / PyTorch datasets.  
> Here, I reproduced the same logic manually for my brand’s sales data using `pandas`, `scikit-learn`, and `TensorFlow`.

---

## ⚙️ Features  
✅ Load sales data from Excel (`bd-vente.xlsx`)  
✅ Clean & normalize data  
✅ Compute total sales per transaction  
✅ Split data into train/test sets  
✅ Train a simple TensorFlow model to learn sales patterns  
✅ Export cleaned dataset (`clean_bd_vente.xlsx`)  
✅ Ready for future automation with Airflow or Power BI integration  

---
