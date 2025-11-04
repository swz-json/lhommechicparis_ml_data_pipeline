import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf


data = pd.read_excel("data/bd-vente.xlsx")

print("✅ Data loaded successfully!")
print(data.head())  


data = data.dropna()

X = data[["Quantity", "Price"]]      
y = data["Price"] * data["Quantity"]     

data["total amount"] = y
data.to_excel("data/clean_bd_vente.xlsx", index=False)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)


train_ds = tf.data.Dataset.from_tensor_slices((X_train, y_train)).batch(2)
test_ds = tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(2)

print("✅ Data ready for TensorFlow!")


model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.fit(train_ds, epochs=20)

loss, mae = model.evaluate(test_ds)
print(f"✅ Model trained! Mean Absolute Error: {mae:.2f}")


