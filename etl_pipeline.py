import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

print("STEP 1: Extracting Data...")
df = pd.read_csv("C:/Users/Rahul Kolankar/Downloads/Python/Task 1/input_data.csv")
print("\nOriginal Data:")
print(df)

# Separate features and target
X = df.drop("target", axis=1)
y = df["target"]

# Identify column types
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
categorical_features = X.select_dtypes(include=['object']).columns

print("\nNumeric Columns:", list(numeric_features))
print("Categorical Columns:", list(categorical_features))

# Numeric pipeline
numeric_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Categorical pipeline
categorical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder())
])

# Combine pipelines
preprocessor = ColumnTransformer([
    ('num', numeric_pipeline, numeric_features),
    ('cat', categorical_pipeline, categorical_features)
])

print("\nSTEP 2: Transforming Data...")
X_processed = preprocessor.fit_transform(X)

print("\nTransformed Data:")
print(X_processed)

# Convert to normal array
X_array = X_processed.toarray() if hasattr(X_processed, "toarray") else X_processed

# Create proper column names
column_names = ["age_scaled", "salary_scaled", "gender_Female", "gender_Male"]

processed_df = pd.DataFrame(X_array, columns=column_names)

# Add target column
processed_df["target"] = y.values
print("\nSTEP 3: Loading Data (Saving to file)...")
processed_df.to_csv("processed_data.csv", index=False)

print("\nETL Process Completed Successfully ✅")
print("\nFinal Processed Data:")
print(processed_df)