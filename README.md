# Smart Customer Segmentation and Recommendation System

## Project Overview

The Smart Customer Segmentation and Recommendation System is a data-driven project designed to analyze customer behavior and group customers into different segments based on purchasing patterns, income, spending habits, and other important features.

This system helps businesses understand their customers better and provide personalized product recommendations, targeted marketing strategies, and improved customer engagement.

The project uses Machine Learning algorithms such as K-Means Clustering and DBSCAN for customer segmentation and data visualization techniques for better business insights.

---

## Features

- Customer data analysis
- Data preprocessing and cleaning
- Customer segmentation using clustering algorithms
- K-Means Clustering implementation
- DBSCAN Clustering implementation
- Interactive dashboard using Streamlit
- Data visualization with Plotly
- Customer behavior insights
- Personalized recommendation support

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Matplotlib

---

## Project Structure

smart-customer-segmentation/
│
├── app.py
├── customer_data.csv
├── requirements.txt
├── README.md
│
├── models/
│   └── clustering_model.py
│
├── utils/
│   └── preprocessing.py
│
└── visualizations/
    └── charts.py

---

## Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/smart-customer-segmentation.git
```
### Step 2: Move to Project Folder

```bash
cd smart-customer-segmentation
```
## Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### step 4: Activate Virtual Environment
```bash
venv\scripts\activate
```
### step 5: Install Required Libraries
```bash
pip install -r requirements.txt
```
## Running the Project
### Run the Streamlit Dashboard
```bash
streamlit run app.py
```
## How It Works
### Data Collection
Customer data is collected from CSV files containing features like:
* Age
* Gender
* Annual Income
* Spending Score
* Purchase Frequency
* Product Preferences
* 
### Data Preprocessing
The data is cleaned by:
* Removing missing values
* Handling duplicate records
* Standardizing numerical values
* Preparing data for clustering

### Customer Segmentation
Machine Learning algorithms divide customers into groups such as:
* High-value customers
* Budget-conscious customers
* Frequent buyers
* Occasional buyers
* Premium product customers
  
### Recommendation System
Based on the customer segment, the system helps recommend:
* Suitable products
* Marketing campaigns
* Discount offers
* Loyalty programs
  
### Business Benefits
* Better customer understanding
* Improved customer retention
* Increased sales opportunities
* Personalized recommendations
* Effective marketing strategies
* Higher customer satisfaction
  
### Future Improvements
* Real-time recommendation engine
* Integration with E-commerce platforms
* AI-based advanced recommendation models
* Customer lifetime value prediction
* Sales forecasting system

  ### Dashboard Overview
 <img width="1230" height="594" alt="Image" src="https://github.com/user-attachments/assets/60712cff-8982-431a-936f-e6009be6aa41" />
 
 
 <img width="1311" height="582" alt="Image" src="https://github.com/user-attachments/assets/3bbe4d85-4b9f-4a0f-bab2-fde3aba09a46" />
 

<img width="1324" height="603" alt="Image" src="https://github.com/user-attachments/assets/649a5a31-0b57-4cd3-b662-3483e633c220" />


<img width="1353" height="507" alt="Image" src="https://github.com/user-attachments/assets/9d2544df-b08e-4f1d-906c-b09c96a1f373" />


<img width="1345" height="576" alt="Image" src="https://github.com/user-attachments/assets/5a5f8005-0eea-4093-8756-db52817abe9d" />


<img width="1343" height="603" alt="Image" src="https://github.com/user-attachments/assets/25551d77-d2de-4372-9c83-b3e4c3375e6b" />

  

  ## Author

Developed by Palak Rathore for Machine Learning and Data Analytics learning purposes.
  
