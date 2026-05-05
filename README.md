# Car-Price-Prediction

# Project OverView
This project uses a Random Forest Regressor model to estimate car prices. It provides a simple and interactive user interface where users can enter car details and get instant predictions.

# Features
Predict car resale price in real-time
User-friendly Streamlit interface
Handles categorical and numerical data
Accurate predictions using ML model
Fast and lightweight application

# Tech Stack
Python
Pandas & NumPy
Scikit-learn
Streamlit
Pickle

# Dataset
The dataset contains the following features:
Year
Present Price
Kms Driven
Fuel Type
Seller Type
Transmission
Owner
Target variable:
Selling Price

# Installation & Setup
-Train the model
python train_model.py
-Run the app
streamlit run app.py

# Project Structure
car-price-prediction/
│
├── app.py
├── train_model.py
├── model.pkl
├── car_data.csv
├── requirements.txt
└── README.md

# Screenshots
App Interface


Prediction Output


# Future Improvements
Add more data for better accuracy
Improve UI design
Deploy on cloud (Streamlit Cloud / Heroku)
Add user authentication

# Conclusion
This project demonstrates how Machine Learning and Streamlit can be combined to build a practical and user-friendly application for real-world problems like car price estimation.
# Author
Maitry Patel
