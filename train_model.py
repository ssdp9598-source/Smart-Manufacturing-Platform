
# Smart Manufacturing - Machine Fault Prediction
# Group 8 MCA Project

import numpy as np
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Create sample sensor data
np.random.seed(42)

temperature = np.random.uniform(30, 120, 1000)
vibration = np.random.uniform(0, 10, 1000)
pressure = np.random.uniform(20, 100, 1000)

# Prepare input features
X = np.column_stack((
    temperature,
    vibration,
    pressure
))

# Create labels: 0 = Normal, 1 = Fault
y = (
    (temperature > 80) |
    (vibration > 7) |
    (pressure > 85)
).astype(int)

# Split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Training Successful!")
print("Model Accuracy:", round(accuracy * 100, 2), "%")
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Save model
Path("models").mkdir(exist_ok=True)

joblib.dump(
    model,
    "models/machine_fault_model.pkl"
)

print("Model saved successfully!")
