🏦 CrediGuard AI:
AI-Powered Credit Risk & Loan Default Prediction System

Project Type: Machine Learning | Data Science | Artificial Intelligence

Developed By: Hetang Patel

Technology Stack: Python, Scikit-learn, Streamlit, SHAP, Pandas, NumPy, Plotly

## 📑 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [Project Overview](#-project-overview)
3. [Problem Statement](#-problem-statement)
4. [Project Objectives](#-project-objectives)
5. [Key Features](#-key-features)
6. [Machine Learning Workflow](#-machine-learning-workflow)
7. [Project Architecture](#-project-architecture)
8. [Project Structure](#-project-structure)
9. [Dataset Information](#-dataset-information)
10. [Data Preprocessing](#-data-preprocessing)
11. [Feature Engineering](#-feature-engineering)
12. [Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)
13. [Machine Learning Models](#-machine-learning-models)
14. [Model Evaluation](#-model-evaluation)
15. [Explainable AI (SHAP)](#-explainable-ai-shap)
16. [Business Impact Analysis](#-business-impact-analysis)
17. [Streamlit Web Application](#-streamlit-web-application)
18. [Technology Stack](#-technology-stack)
19. [Installation Guide](#-installation-guide)
20. [Deployment](#-deployment)
21. [Future Improvements](#-future-improvements)
22. [Conclusion](#-conclusion)
23. [Author](#-author)

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**1. Executive Summary**

CrediGuard AI is an end-to-end Machine Learning application designed to predict loan default risk and assist financial institutions in making smarter lending decisions.

The project combines predictive analytics, explainable AI, and business impact analysis into an interactive Streamlit dashboard.

Instead of only predicting whether a customer will default, the application also estimates financial risk and explains why the prediction was made.

This makes the system more transparent and practical for real-world banking applications.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**2. Project Overview**

Loan default prediction is one of the most important problems in the banking and financial industry.

Approving loans for risky customers can result in significant financial losses.

Rejecting low-risk customers can reduce business opportunities.

CrediGuard AI helps solve this problem by predicting the probability of default before approving a loan application.

The application provides:

Loan default prediction
Default probability
Risk classification
Business impact estimation
Explainable AI using SHAP
Interactive dashboard
Automated prediction report

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**3. Problem Statement**

Banks receive thousands of loan applications every day.

Traditional loan approval methods rely heavily on manual analysis and predefined rules.

These approaches may:

Approve risky borrowers
Reject good customers
Increase financial losses
Reduce operational efficiency

The objective is to build an intelligent machine learning system capable of identifying risky loan applicants before loan approval.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**4. Project Objectives**

The primary objectives of this project are:

Build a machine learning model for credit risk prediction.
Compare multiple classification algorithms.
Improve prediction performance using feature engineering.
Explain model predictions using Explainable AI.
Estimate business losses due to defaults.
Deploy the model as a professional Streamlit web application.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**5. Key Features**
Interactive Dashboard

**The dashboard provides:**

Credit risk overview
Loan prediction interface
Business impact visualization
Model insights
Professional UI
Loan Default Prediction

**Users can enter borrower information such as:**

Loan Amount
Interest Rate
Annual Income
Employment Length
Credit History
Home Ownership
Debt-to-Income Ratio
Loan Purpose

**The system predicts:**

Default Probability
Loan Status
Risk Category
Lending Recommendation
Explainable AI (SHAP)

The application explains every prediction using SHAP values.

**Benefits include:**

Increased transparency
Better decision making
Regulatory compliance
Trustworthy AI
Business Impact Analysis

**The application estimates:**

Expected financial loss
Loan exposure
Risk-adjusted recommendation

This helps financial institutions understand the business impact of approving risky loans.

Automated Risk Report

**The application generates a downloadable report containing:**

Applicant Information
Loan Details
Prediction Result
Default Probability
Business Impact
Recommendation

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**6. Machine Learning Workflow**

Loan Dataset

↓

Exploratory Data Analysis (EDA)

↓

Data Cleaning

↓

Missing Value Treatment

↓

Feature Engineering

↓

Feature Encoding

↓

Data Scaling

↓

Train-Test Split

↓

Model Training

↓

Model Evaluation

↓

Explainable AI (SHAP)

↓

Streamlit Deployment

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**7. Project Architecture**

User Input

↓

Data Preprocessing

↓

Feature Engineering

↓

Machine Learning Model

↓

Probability Prediction

↓

SHAP Explainability

↓

Business Impact Calculation

↓

Prediction Report

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**8. Project Structure**

CrediGuard-AI/

│

├── app.py

├── report_generator.py

├── requirements.txt

├── README.md

│

├── models/

│   ├── model.pkl

│   ├── logistic_model.pkl

│   └── preprocessor.pkl

│

├── notebooks/

│   ├── 01_EDA.ipynb

│   ├── 02_Preprocessing.ipynb

│   └── 03_Model_Training.ipynb

│

├── assets/

│   └── style.css

│

└── .gitignore

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**9. Dataset Information**

The project uses a Lending Club loan dataset.

**The dataset contains borrower information including:**

Loan Amount
Interest Rate
Annual Income
Employment Length
Loan Purpose
Home Ownership
Revolving Balance
Revolving Utilization
Public Records
Mortgage Accounts
Credit History
Loan Status

Due to GitHub repository size limitations, the original dataset is not included.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**10. Data Preprocessing**

**The preprocessing pipeline includes:**

Missing value handling
Feature encoding
Feature scaling
Categorical transformation
Numerical normalization

Scikit-learn's Pipeline and ColumnTransformer are used to automate preprocessing.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**11. Feature Engineering**

Several new features were created to improve prediction performance.

**Examples include:**

Loan Income Ratio
Installment Income Ratio
Bankruptcy Indicator
Public Record Risk
High Credit Utilization Flag

These engineered features improved model learning and predictive capability.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**12. Exploratory Data Analysis (EDA)**

EDA was performed to understand the dataset.

**Analysis included:**

Missing values
Target distribution
Correlation analysis
Income distribution
Loan amount analysis
Default trends
Class imbalance analysis

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**13. Machine Learning Models**

The following algorithms were evaluated:

**Logistic Regression**

Advantages:

Fast
Interpretable
Suitable baseline model

**XGBoost**

Advantages:

High predictive performance
Efficient boosting algorithm
Excellent handling of structured data

**LightGBM**

Advantages:

Fast training
Low memory usage
High scalability

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**14. Model Evaluation**

**Evaluation metrics included:**

Accuracy
Precision
Recall
F1 Score
ROC-AUC Score
Confusion Matrix

Threshold optimisation was performed to balance business risk and approval rates.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**15. Explainable AI (SHAP)**

SHAP (SHapley Additive Explanations) was integrated to explain predictions.

**The dashboard displays:**

Positive contributing factors
Negative contributing factors
Feature importance
Individual prediction explanation

This improves transparency and interpretability.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**16. Business Impact Analysis**

The application estimates:

Default Probability
Expected Loss
Financial Exposure
Lending Recommendation

This helps banks understand the financial consequences of each lending decision.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**17. Streamlit Web Application**

The application includes:

Professional dashboard
Responsive layout
Interactive prediction form
Business analytics
SHAP explainability
PDF report generation

The interface is designed to simulate a real banking credit risk dashboard.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**18. Technology Stack**

Programming Language
Python
Machine Learning
Scikit-learn
XGBoost
LightGBM
Data Processing
Pandas
NumPy
Visualization
Matplotlib
Plotly
Explainable AI
SHAP
Deployment
Streamlit
Version Control
Git
GitHub

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**19. Installation Guide**

**Clone the repository:**

git clone https://github.com/HP2356/CrediGuard-AI.git

Navigate to the project:

cd CrediGuard-AI

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**20. Deployment**

The application is deployed on Streamlit Cloud.

**Live Application:**

https://creditguard-ai.streamlit.app

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**21. Future Improvements**

Potential future enhancements include:

Real-time credit bureau integration
Deep Learning models
Automated model retraining
Customer segmentation
Fraud detection module
MLOps pipeline
Docker containerisation
Cloud deployment on AWS/Azure/GCP
REST API integration

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**22. Conclusion**

CrediGuard AI demonstrates how Machine Learning can improve credit risk assessment through accurate prediction, explainable AI, and business impact analysis.

The project integrates data preprocessing, feature engineering, multiple machine learning algorithms, model evaluation, SHAP explainability, and Streamlit deployment into a single end-to-end solution.

It reflects practical skills in Machine Learning, Data Science, Python development, model deployment, and AI interpretability.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**23. Author**
**Hetang Patel**

Computer Science & Design Student

Machine Learning | Data Science | Artificial Intelligence

GitHub: https://github.com/HP2356

⭐ If you found this project useful, please consider giving the repository a star on GitHub.
