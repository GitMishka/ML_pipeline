import pandas as pd
from sklearn.model_selection import train_test_split
from datetime import datetime

sample_df = pd.read_csv('C:/Users/Misha/Desktop/GitHub/ML_pipeline/sample.csv')


sample_df['DATE OCC'] = pd.to_datetime(sample_df['DATE OCC'], format='%m/%d/%Y %H:%M')

k
sample_df['Month'] = sample_df['DATE OCC'].dt.month

sample_df['Hour'] = sample_df['TIME OCC'] // 100


time_of_day_bins = [0, 5, 12, 17, 24]
time_of_day_labels = ['Night', 'Morning', 'Afternoon', 'Evening']
sample_df['Time of Day'] = pd.cut(sample_df['Hour'], bins=time_of_day_bins, labels=time_of_day_labels, right=False, ordered=True)

sample_df.drop(columns=['Hour'], inplace=True)


X = sample_df[['Day of Week', 'Month', 'LAT', 'LON', 'Time of Day']]


X['Time of Day'] = sample_df['Time of Day']  

X = pd.get_dummies(X, columns=['Day of Week', 'Month', 'Time of Day'], drop_first=True)


y = sample_df['Crm Cd']  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f'Training features shape: {X_train.shape}')
print(f'Testing features shape: {X_test.shape}')
print(f'Training labels shape: {y_train.shape}')
print(f'Testing labels shape: {y_test.shape}')

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

clf = RandomForestClassifier(random_state=42)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
