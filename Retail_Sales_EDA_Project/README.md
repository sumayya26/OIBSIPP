🛍️ Retail Sales EDA Project
📘 Overview

This project performs Exploratory Data Analysis (EDA) on a retail sales dataset to uncover insights about product performance, customer behavior, and sales trends over time.
It is part of my Oasis Infobyte Data Science Internship (Project 2).

🎯 Objectives

Understand overall sales distribution and performance

Identify top-performing products and customers

Detect seasonal trends and correlations in sales data

Provide business-driven insights and recommendations

📂 Dataset Description

The dataset used for this analysis contains the following sample columns:

Column Name	Description
Date	Date of the transaction
Product	Product name or category
Quantity	Units sold
UnitPrice	Price per unit
CustomerID	Unique ID of each customer
Region	Sales region or store location
TotalSales	Calculated as Quantity × UnitPrice
🧰 Tools & Libraries Used

Python

Google Colab / Jupyter Notebook

Libraries:

pandas – Data manipulation

numpy – Numerical analysis

matplotlib, seaborn – Data visualization

⚙️ Steps Performed

Data Loading – Imported the raw CSV file and explored its structure.

Data Cleaning – Handled missing values, removed duplicates, corrected data types.

Feature Engineering – Added new columns like “Month”, “TotalSales”, etc.

Exploratory Data Analysis –

Analyzed overall sales distribution

Identified top 10 products and customers

Visualized monthly & regional sales trends

Examined correlations between key variables

Insights & Summary – Derived key findings and recommendations.

📊 Key Insights

🏆 Top Products: Certain items consistently drive majority of sales.

💰 Customer Trends: A few repeat customers contribute significantly to total revenue.

🗓️ Seasonal Behavior: Sales peak during specific months or holidays.

🌍 Regional Patterns: Some store locations outperform others.

💡 Recommendations

Increase stock and promotions for top-selling products.

Introduce loyalty programs for high-value customers.

Focus marketing during high-demand months.

Reassess inventory for underperforming products.

📁 Project Files
File Name	Description
Retail_Sales_EDA_Project.ipynb	Main Jupyter notebook for analysis
retail_sales_dataset.csv	Raw dataset used for analysis
load_and_clean.py	Script for loading and cleaning data
requirements.txt	Python dependencies
summary_report.txt	Brief text summary of insights
summary_report.pdf	(Optional) PDF version of report
🧩 How to Run This Project

Clone this repository or open it in Google Colab.

Install dependencies:

pip install -r requirements.txt


Open the notebook:

Retail_Sales_EDA_Project.ipynb


Run all cells to view the analysis and visualizations.

🧠 Author

Sumayya Harmain
Data Science Intern @ Oasis Infobyte
📧 23r01a05j4@cmrithyderabad.edu.in

📍 CMR Institute of Technology, Hyderabad

⭐ Acknowledgement

This project was developed as part of the Oasis Infobyte Internship Program.
Special thanks to the mentors and team for guidance and support.
