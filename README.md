# 🏭 Smart Manufacturing Platform

An integrated manufacturing monitoring system for machine health, predictive maintenance, and product quality inspection.

## 📌 Project Overview

The Smart Manufacturing Platform is an academic MCA project developed to demonstrate how technology can help monitor manufacturing operations.

It provides a dashboard to monitor machine status, check sensor readings, track maintenance schedules, inspect product defects, and view machine performance.

## ✨ Features

- **Factory Dashboard:** Displays machine statistics and temperature reports.
- **Machine Fault Detection:** Checks temperature, vibration, and pressure readings using predefined thresholds.
- **Predictive Maintenance:** Shows maintenance alerts based on machine working hours.
- **Product Defect Detection:** Allows users to upload product images and manually mark defects such as scratches, cracks, shape defects, and color defects.
- **Machine Performance:** Displays machine efficiency and performance status.

## 🛠️ Technologies Used

- Python
- Streamlit
- NumPy
- Matplotlib
- Pillow
- Joblib

## 📂 Project Structure

```text
Smart-Manufacturing-Platform/
│
├── app.py
├── fault_detector.py
├── train_model.py
├── test_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ssdp9598-source/Smart-Manufacturing-Platform.git
```

### 2. Open the project folder

```bash
cd Smart-Manufacturing-Platform
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment (Windows)

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal.

## 🧪 Testing

The application can be tested using:

- High temperature and vibration readings for machine fault alerts.
- Working hours above the maintenance interval.
- Uploaded product images with manually selected defect checkboxes.
- Different machine efficiency values.

## ⚠️ Project Limitations

This is an academic demonstration project. Machine fault detection uses predefined thresholds, maintenance alerts use a predefined interval, and product inspection uses manual defect selection. It does not currently perform automated AI-based image inspection or use a trained predictive model in the running application.

## 🚀 Future Scope

- Real-time IoT sensor integration.
- Automated image-based defect detection using computer vision.
- Machine learning-based fault prediction.
- Database integration for storing machine history.
- Cloud deployment and live monitoring.

## 👨‍🎓 Project Information

**Project:** Smart Manufacturing Platform  
**Group:** 8  
**Course:** MCA  
**Developer:** Dipendra Yadav

---

*Developed using Python and Streamlit.*