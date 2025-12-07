import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv('restaurant_rating.csv')

encoder = LabelEncoder()
df['Cuisine'] = encoder.fit_transform(df['Cuisine'])
df['Location'] = encoder.fit_transform(df['Location'])
df['Price_Level'] = encoder.fit_transform(df['Price_Level'])
df['Wait_Time'] = encoder.fit_transform(df['Wait_Time'])
df['Ambiance'] = encoder.fit_transform(df['Ambiance'])

X = df[['Cuisine', 'Location', 'Price_Level', 'Wait_Time', 'Ambiance']]
y = df['Rating']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)

accuracy = knn.score(X_test_scaled, y_test)
print(f'KNN Model Accuracy: {accuracy * 100:.2f}%')

"""
Memo:
- Imported necessary libraries: pandas, KNeighborsClassifier, LabelEncoder, StandardScaler, train_test_split.
- Loaded dataset from 'restaurant_rating.csv'.
- Encoded categorical features: 'Cuisine', 'Location', 'Price_Level', 'Wait_Time', 'Ambiance'.
- Defined features (X) and target variable (y).
- Split data into training (80%) and testing (20%) sets.
- Standardized the feature data using StandardScaler.
- Initialized and trained a K-Nearest Neighbors Classifier with 7 neighbors.
- Made predictions on the test set.
- Calculated and printed accuracy of the model.
- Results: 73%
"""