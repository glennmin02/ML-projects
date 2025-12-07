from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd

df = pd.read_csv('insurance.csv') # Load dataset

encoder = LabelEncoder() # Initialize label encoder
df['sex'] = encoder.fit_transform(df['sex']) # Encode categorical variables
df['smoker'] = encoder.fit_transform(df['smoker'])
df['region'] = encoder.fit_transform(df['region'])
X = df.drop('charges', axis=1)

X = df[['age','smoker','bmi','children']] # Feature selection
y = df['charges'] # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42) # Split data

model = LinearRegression() # Initialize model
model.fit(X_train, y_train) # Train  model
y_pred = model.predict(X_test) # Make predictions

r2 = r2_score(y_test, y_pred) # Evaluate model
print(f'R2: {r2}')

print(f'Intercept: {model.intercept_}')  # Intercept
print(f'Coefficient: {model.coef_}')     # Coefficients

# Example prediction
print(model.predict([[40, 1, 25.0, 2]])) # Predict charges for a 40-year-old smoker with BMI 25.0 and 2 children
print(model.predict([[21, 0, 23.0, 0]])) # Predict charges for a 21-year-old non-smoker with BMI 23.0 and 0 children
print(model.predict([[21, 1, 23.0, 0]])) # Predict charges for a 21-year-old smoker with BMI 23.0 and 0 children

"""
Memo:
- This script performs health insurance charge prediction using linear regression.
- It includes data loading, preprocessing, model training, evaluation, and example predictions.
- The dataset used is the insurance dataset from a CSV file.
- Features used are age, smoker status, BMI, and number of children.
- The target variable is the insurance charges.
- The model's performance is evaluated using R-squared metric.
- Example predictions are provided for different profiles.
- Categorical variables are encoded using LabelEncoder.
- The dataset is split into training and testing sets with a 75-25 ratio.
- The model's intercept and coefficients are printed for interpretation.
- Result:
-       R2: 0.7653688584061047
-       Intercept: -12268.326378050246
"""