
import numpy as np

def detect_fault(temperature, vibration, pressure):

    readings = np.array(
        [temperature, vibration, pressure],
        dtype=float
    )

    # Demo operating limits
    minimum = np.array([20, 0, 30])
    maximum = np.array([80, 7, 120])

    labels = [
        "Temperature",
        "Vibration",
        "Pressure"
    ]

    faults = []

    for i in range(3):
        if readings[i] < minimum[i] or readings[i] > maximum[i]:
            faults.append(labels[i])

    risk_score = (len(faults) / 3) * 100

    if len(faults) >= 2:
        status = "Critical"
    elif len(faults) == 1:
        status = "Warning"
    else:
        status = "Normal"

    return {
        "status": status,
        "faults": faults,
        "risk_score": round(risk_score, 2)
    }


# Test the detector
result = detect_fault(90, 8, 100)

print("Machine Status:", result["status"])
print("Detected Faults:", result["faults"])
print("Rule-based Risk Score:", result["risk_score"], "%")
