import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('video_game_success.csv')

encoder = LabelEncoder()
df['Genre'] = encoder.fit_transform(df['Genre'])
df['Platform'] = encoder.fit_transform(df['Platform'])
df['Graphics'] = encoder.fit_transform(df['Graphics'])
df['Multiplayer'] = encoder.fit_transform(df['Multiplayer'])
df['Price_Range'] = encoder.fit_transform(df['Price_Range'])

X = df.drop('Success', axis=1)
y = df['Success']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

dt_classifier = DecisionTreeClassifier(max_depth=3)
dt_classifier.fit(X_train, y_train)
y_pred_dt = dt_classifier.predict(X_test)

dt_accuracy = accuracy_score(y_test, y_pred_dt)
dt_report = classification_report(y_test, y_pred_dt)

print(f"Decision Tree Accuracy: {dt_accuracy}")
print("Decision Tree Classification Report:")
print(dt_report)

arr = np.array([[0, 1, 3, 1, 2]])

print(dt_classifier.predict(arr))

"""
Memo:
- Imported necessary libraries: pandas, numpy, LabelEncoder, train_test_split, DecisionTreeClassifier, accuracy_score, classification_report.
- Loaded dataset from 'video_game_success.csv'.
- Encoded categorical features: 'Genre', 'Platform', 'Graphics', 'Multiplayer', 'Price_Range'.
- Defined features (X) and target variable (y).
- Split data into training (75%) and testing (25%) sets.
- Initialized and trained a Decision Tree Classifier with max depth of 3.
- Made predictions on the test set.
- Calculated and printed accuracy and classification report.
- Results: 80%
"""
