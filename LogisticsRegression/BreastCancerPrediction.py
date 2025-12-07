import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns


data = load_breast_cancer() # Load the dataset
df = pd.DataFrame(data.data, columns=data.feature_names) # Creating DataFrame

df['diagnosis'] = pd.Series(data.target).map({0: 'malignant', 1: 'benign'}) # Adding target variable

X = df.drop(columns=['diagnosis'])
y = df['diagnosis']

le = LabelEncoder() # Label Encoding
df['diagnosis'] = le.fit_transform(df['diagnosis'])

X = df.drop(columns=['diagnosis']) # Feature Selection
y = df['diagnosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler() # Feature Scaling
x_train_scaled = scaler.fit_transform(X_train)
x_test_scaled = scaler.transform(X_test)

model = LogisticRegression() # Model Training
model.fit(x_train_scaled, y_train)

y_pred = model.predict(x_test_scaled) # Model Evaluation
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
f1_score = f1_score(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix: {conf_matrix}')
print(f'F1 Score: {f1_score}')
print(classification_report(y_test, y_pred, target_names=['Benign', 'Malignant']))

# Visualization of Confusion Matrix
plt.figure(figsize=(8,6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='cubehelix',
            cbar=False,
            xticklabels=['Benign', 'Malignant'],
            yticklabels=['Benign', 'Malignant'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()

"""
Memo:
- This script performs breast cancer prediction using logistic regression. 
- It includes data loading, preprocessing, model training, evaluation, and visualization of results.
- The dataset used is the breast cancer dataset from sklearn.
- Key metrics such as accuracy, confusion matrix, and F1 score are calculated and displayed.
- A heatmap of the confusion matrix is generated for better visualization of model performance.
- The target variable is encoded to numerical values for model compatibility.
- Standard scaling is applied to the features to improve model performance.
- The script uses train-test split to evaluate the model on unseen data.
- The classification report provides detailed metrics for each class.
- Result summary:
-               Accuracy: 0.9736842105263158
-               Confusion Matrix: [[70  1]
                                    [ 2 41]]
-               F1 Score: 0.9647058823529412
"""