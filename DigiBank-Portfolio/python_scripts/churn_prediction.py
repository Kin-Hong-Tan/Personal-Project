import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('retention_dataset.csv')
X = df[['login_frequency', 'product_count', 'days_since_last_txn']]
y = df['churn_flag']

model = LogisticRegression()
model.fit(X, y)
print(f'Model Accuracy: {model.score(X, y):.2f}')