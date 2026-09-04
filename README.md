# 🧠 Mental Wellness Prediction

A Machine Learning project that predicts **students' mental health scores** using lifestyle, academic, stress-level, and social media usage data. The project includes data preprocessing, feature engineering, model training, evaluation, and deployment using **FastAPI**.

## 📌 Project Overview

The goal of this project is to build a Machine Learning regression model that can predict a student's **mental health score** based on factors such as:

* Social media usage
* Study hours
* Sleep hours
* Physical activity
* Stress level
* Academic level
* Country and demographic information

The trained model is deployed through a **FastAPI REST API** for real-time predictions.

## 🚀 Key Features

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Duplicate and outlier analysis
* Feature engineering
* Categorical feature encoding
* Feature scaling and log transformation
* Machine Learning model comparison
* Hyperparameter tuning
* Cross-validation
* Model persistence using Joblib
* FastAPI REST API deployment
* Pydantic input validation

## 🛠️ Technologies Used

**Programming Language**

* Python

**Data Analysis & Visualization**

* Pandas
* NumPy
* Matplotlib
* Seaborn

**Machine Learning**

* Scikit-learn
* Linear Regression
* Random Forest Regressor
* RandomizedSearchCV
* StandardScaler
* OneHotEncoder
* OrdinalEncoder

**Deployment**

* FastAPI
* Pydantic
* Joblib

## 📂 Project Structure

```text
Mental-Wellness-Prediction/
│
├── data/
│   └── dataset.csv
│
├── notebooks/
│   └── Mental_Wellness_Analysis.ipynb
│
├── model/
│   └── Mental_Wellness_Model.pkl
│
├── main.py
├── requirements.txt
└── README.md
```

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Data Preprocessing
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Hyperparameter Tuning
   ↓
Model Saving
   ↓
FastAPI Deployment
   ↓
Mental Health Score Prediction
```

## 📊 Data Preprocessing

The dataset was cleaned and prepared before model training.

Key preprocessing steps included:

1. Handling data quality issues
2. Removing duplicate records
3. Performing outlier analysis
4. Checking data distribution and skewness
5. Grouping high-cardinality country categories
6. Applying categorical encoding
7. Scaling numerical features
8. Applying log transformation where required

## 🧩 Feature Engineering

The dataset contained **111 country categories**. To reduce high-cardinality issues, countries were grouped into **10 major countries and an "Other" category**.

This helped simplify categorical data and make the model more efficient.

## 🤖 Machine Learning Models

Two regression algorithms were evaluated:

* **Linear Regression**
* **Random Forest Regressor**

The models were evaluated using:

* **R² Score**
* **Mean Absolute Error (MAE)**
* **Root Mean Squared Error (RMSE)**

## ⚙️ Model Optimization

**RandomizedSearchCV** was used to tune the Random Forest hyperparameters.

The optimization process used:

* Randomized hyperparameter search
* **5-Fold Cross-Validation**
* Model performance evaluation

The final trained preprocessing and Machine Learning pipeline was saved using **Joblib** for reusable predictions.

## 🌐 FastAPI Deployment

The trained model was integrated with a **FastAPI REST API**.

The API provides a `/predict` endpoint that accepts student information and returns the predicted mental health score.

Example request flow:

```text
Student Information
        ↓
Pydantic Validation
        ↓
Data Preprocessing
        ↓
Trained ML Model
        ↓
Predicted Mental Health Score
```

## 📥 Input Features

The prediction API accepts information such as:

* Age
* Gender
* Country
* Academic Level
* Most Used Platform
* Purpose of Use
* Daily Usage Hours
* Daily Unlocks
* Study Hours
* Physical Activity Hours
* Sleep Hours
* Stress Level

You can use the `/predict` endpoint to test the model.

Project Highlights

* Developed an end-to-end **Machine Learning regression pipeline**
* Performed **EDA, data cleaning, and feature engineering**
* Compared multiple regression models using standard evaluation metrics
* Optimized Random Forest using **RandomizedSearchCV and 5-Fold Cross-Validation**
* Saved the complete ML pipeline using **Joblib**
* Deployed the prediction model through a **FastAPI REST API**

Learning Outcomes

Through this project, I gained practical experience in:

* Machine Learning
* Regression Modeling
* Data Preprocessing
* Feature Engineering
* Model Evaluation
* Hyperparameter Tuning
* Cross-Validation
* REST API Development
* ML Model Deployment

## 👨‍💻 Author

**Zuheb Khan**

Aspiring **AI/ML Engineer | Data Analyst**

Thank you for taking the time to explore this project. I hope it provides a clear overview of my approach to building and deploying a Machine Learning solution.

If you find this project useful, please consider giving the repository a ⭐.
