import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Training data
data = {
    "Voltage": [230, 228, 235, 220, 180, 100, 240, 225, 190, 110],
    "Current": [5, 4, 6, 8, 15, 25, 5, 9, 18, 30],
    "Temperature": [30, 32, 31, 35, 50, 70, 29, 40, 55, 75],
    "Fault": [
        "Normal", "Normal", "Normal", "Overload", "Overload",
        "Short Circuit", "Normal", "Overload", "Overload",
        "Short Circuit"
    ]
}

df = pd.DataFrame(data)

# Input features
X = df[["Voltage", "Current", "Temperature"]]

# Output
y = df["Fault"]

# Create AI model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

print("AI Fault Detection System")
print("-------------------------")

# Get values from user
voltage = float(input("Enter Voltage (V): "))
current = float(input("Enter Current (A): "))
temperature = float(input("Enter Temperature (°C): "))

# Predict fault
prediction = model.predict([[voltage, current, temperature]])

print("\nDetected Condition:", prediction[0])

if prediction[0] == "Normal":
    print("System is operating normally.")
elif prediction[0] == "Overload":
    print("Warning: Overload detected!")
else:
    print("Warning: Possible short circuit detected!")
