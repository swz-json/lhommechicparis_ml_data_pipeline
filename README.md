# lhommechicparis_ml_data_pipeline
End-to-end data pipeline project for L’Homme Chic Paris: loading, cleaning, and delivering sales data into a TensorFlow machine learning model. Inspired by the tfdsio framework for dataset automation.

## 📖 Project Overview  
This project demonstrates an **end-to-end data pipeline** built for **L’Homme Chic Paris**, an e-commerce brand specialized in men’s accessories.  
The goal is to **automate data preparation** (loading, cleaning, transforming) and deliver clean datasets to a **TensorFlow machine-learning model** for analytics and forecasting.

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

## 🧰 Tech Stack  
| Category | Tools |
|-----------|-------|
| Data Handling | Python, Pandas |
| Machine Learning | TensorFlow, Scikit-learn |
| Automation | (planned) Apache Airflow |
| Visualization | Power BI (planned) |
| Version Control | Git & GitHub |

---
## 📈 The terminal output 
After 20 epochs of training, the model achieved a Mean Absolute Error ≈ 445 €, meaning on average the prediction is within ± 445 € of the actual sales value.

```bash
Epoch 20/20
loss: 284832.5938 - mae: 405.3340
✅ Model trained! Mean Absolute Error: 445.95
```

