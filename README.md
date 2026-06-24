# 🌾 Crop Recommendation System
### Machine Learning + Django Web Application

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-Framework-green?style=flat&logo=django)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat&logo=scikit-learn)
![Accuracy](https://img.shields.io/badge/Accuracy-99.57%25-brightgreen?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat)

---

## 🧠 Problem Statement

Farmers often struggle to decide which crop to grow based on their soil and environmental conditions. Wrong crop selection leads to poor yield and financial loss. This project solves that by using Machine Learning to recommend the most suitable crop based on real soil and climate data — delivered through a browser-based web interface.

---

## 🎯 What This Project Does

A user enters soil nutrient values and environmental conditions into a web form. The ML model processes the inputs and instantly recommends the best crop to grow — all in real time through a Django-powered web interface.

---

## 📊 Model Performance

| Model | Accuracy |
|---|---|
| **Naive Bayes** ✅ Best | **99.57%** |
| Random Forest | ~98% |
| Decision Tree | ~97% |
| Support Vector Machine (SVM) | ~96% |

> **Naive Bayes achieved the highest accuracy of 99.57%** and was selected as the final deployed model.

---

## 🔧 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| ML Library | Scikit-learn |
| Web Framework | Django |
| Data Processing | Pandas, NumPy |
| Model Serialization | Pickle (.pkl) |
| Frontend | HTML, CSS |
| Notebook | Jupyter Notebook |

---

## 📥 Input Parameters

The model takes the following 7 inputs from the user:

| Parameter | Description |
|---|---|
| **N** | Nitrogen content in soil |
| **P** | Phosphorus content in soil |
| **K** | Potassium content in soil |
| **Temperature** | Ambient temperature (°C) |
| **Humidity** | Relative humidity (%) |
| **pH** | Soil pH value |
| **Rainfall** | Annual rainfall (mm) |

---

## 🚀 How It Works

```
User Input (NPK + Climate)
        ↓
Django Web Interface
        ↓
Data Preprocessing (StandardScaler)
        ↓
Naive Bayes ML Model (99.57% accuracy)
        ↓
Crop Recommendation Output
```

---

## 📸 Screenshots

### Input Page
![Input Page](crop%20input1.png)

### Prediction Output
![Output Page](crop%20output1.png)

---

## 🗂️ Project Structure

```
Crop-Recommendation-System/
│
├── croprecommendation/        # Django app
│   └── ...
├── crop_train.ipynb           # Model training notebook
├── Crop_recommendation.csv    # Dataset
├── best_model.pkl             # Saved Naive Bayes model
├── scaler.pkl                 # Saved StandardScaler
├── views.py                   # Django views (prediction logic)
├── urls.py                    # URL routing
├── index.html                 # Input form
├── result.html                # Output page
└── manage.py                  # Django entry point
```

---

## ⚙️ Setup & Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/shravanibhat07/Crop-Recommendation-System-Using-Machine-Learning-And-Django.git
cd Crop-Recommendation-System-Using-Machine-Learning-And-Django

# 2. Install dependencies
pip install django scikit-learn pandas numpy

# 3. Run the Django server
python manage.py runserver

# 4. Open in browser
http://127.0.0.1:8000/
```

---

## 🔬 ML Pipeline

1. **Data Collection** — Agricultural dataset with 2200 samples, 22 crop types
2. **Preprocessing** — StandardScaler normalization, null value handling
3. **Feature Engineering** — 7 input features selected based on domain relevance
4. **Model Training** — 4 models benchmarked (Decision Tree, Random Forest, SVM, Naive Bayes)
5. **Evaluation** — Accuracy, precision, recall, F1-score comparison
6. **Deployment** — Best model serialized with Pickle, served via Django

---

## 🌱 Future Improvements

- [ ] Integration with IoT soil sensors for real-time data
- [ ] Live weather API integration (OpenWeatherMap)
- [ ] Mobile application (Android/iOS)
- [ ] Deep Learning model for improved accuracy
- [ ] Multi-language support (Kannada, Hindi)
- [ ] REST API for third-party integration

---

## 👩‍💻 About the Developer

**Shravani Bhat**
B.E. in Electronics & Communication Engineering | CGPA: 8.82/10
Alva's Institute of Engineering and Technology, Udupi

- 📧 shravanibhat07@gmail.com
- 🔗 [LinkedIn](https://linkedin.com/in/shravanibhat07)
- 💻 [GitHub](https://github.com/shravanibhat07)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ **If you found this project useful, please give it a star!**
