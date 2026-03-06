# DATA  PIPELINE

COMPANY NAME : CODTECH IT SOLUTION

NAME : KOLANKAR RAHUL MADAN

INTERN ID :CTIS5094

DOMAIN NAME : DATA SCIENCE

BATCH DURATION : 6 WEEKS

MENTOR : NEELA SANTOSH

# ETL Pipeline using Pandas and Scikit-Learn

## 📌 Project Overview

This project demonstrates how to build an **ETL (Extract, Transform, Load) pipeline** using Python libraries such as **Pandas** and **Scikit-learn**.
The pipeline automatically reads raw data, preprocesses it, transforms it into a machine-learning-ready format, and saves the cleaned data.

ETL pipelines are widely used in **data engineering, data science, and machine learning workflows**.

---

## 🎯 Objective

The goal of this project is to automate data preprocessing by:

* Extracting raw data from a CSV file
* Handling missing values
* Scaling numeric features
* Encoding categorical variables
* Saving the processed data for further analysis or machine learning models

---

## 🛠 Tools and Technologies Used

* **Python**
* **Pandas**
* **Scikit-Learn**
* **VS Code**
* **Git & GitHub**

---

## 📂 Project Structure

```
ETL-Pipeline-Project
│
├── input_data.csv        # Raw dataset
├── processed_data.csv    # Output after ETL process
├── etl_pipeline.py       # Main ETL pipeline script
├── test.py               # Library testing script
└── README.md             # Project documentation
```

---

## ⚙️ ETL Process

### 1️⃣ Extract

Data is loaded from a CSV file using Pandas.

```python
df = pd.read_csv("input_data.csv")
```

---

### 2️⃣ Transform

The transformation stage includes:

**Handling Missing Values**

* Numeric columns → Mean Imputation
* Categorical columns → Most Frequent Value

**Feature Scaling**

Numeric columns are scaled using **StandardScaler** to normalize the data.

**Categorical Encoding**

Categorical values such as gender are converted to numeric format using **OneHotEncoder**.

Example:

| Gender | Encoded |
| ------ | ------- |
| Male   | 0 1     |
| Female | 1 0     |

---

### 3️⃣ Load

The transformed dataset is saved as:

```
processed_data.csv
```

This dataset is ready for machine learning models or data analysis.

---

## ▶️ How to Run the Project

### Step 1 – Install Required Libraries

```bash
pip install pandas scikit-learn
```

### Step 2 – Run the Pipeline

```bash
python etl_pipeline.py
```

### Step 3 – Check Output

The processed dataset will be generated as:

```
processed_data.csv
```

---

## 📊 Example Output Columns

The final processed dataset contains:

* `age_scaled`
* `salary_scaled`
* `gender_Female`
* `gender_Male`
* `target`

---

## 🌍 Real-World Applications

ETL pipelines like this are used in:

* Banking and finance (credit scoring)
* Healthcare data processing
* E-commerce recommendation systems
* Machine learning data preparation
* Business intelligence dashboards

---

## 👨‍💻 Author

**Rahul Kolankar**

Python Developer | Data Science Student
