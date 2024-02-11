import pandas as pd
from sklearn.model_selection import train_test_split
from datetime import datetime

# Load the dataset
sample_df = pd.read_csv('C:/Users/Misha/Desktop/GitHub/ML_pipeline/sample.csv')

# Specify the date format and convert 'DATE OCC' to datetime
# Adjust the format according to your dataset's date format
sample_df['DATE OCC'] = pd.to_datetime(sample_df['DATE OCC'], format='%m/%d/%Y %H:%M')

# Feature Engineering
# Extract day of the week and month from 'DATE OCC'
sample_df['Day of Week'] = sample_df['DATE OCC'].dt.dayofweek
sample_df['Month'] = sample_df['DATE OCC'].dt.month

# Assuming 'TIME OCC' is in HHMM format and converting to hour for simplicity
sample_df['Hour'] = sample_df['TIME OCC'] // 100

# Define time of day categories: Morning (5-12), Afternoon (12-17), Evening (17-24), Night (0-5)
time_of_day_bins = [0, 5, 12, 17, 24]
time_of_day_labels = ['Night', 'Morning', 'Afternoon', 'Evening']
sample_df['Time of Day'] = pd.cut(sample_df['Hour'], bins=time_of_day_bins, labels=time_of_day_labels, right=False, ordered=True)

# Dropping the temporary 'Hour' column
sample_df.drop(columns=['Hour'], inplace=True)

# Preparing data for model training
# Ensure 'Time of Day' is correctly generated in the sample_df DataFrame
# Then, when selecting features for X, include 'Time of Day' if it's not already there

# Assuming 'Day of Week', 'Month', 'LAT', 'LON', and 'Time of Day' are your intended features
X = sample_df[['Day of Week', 'Month', 'LAT', 'LON', 'Time of Day']]

# Before one-hot encoding, ensure 'Time of Day' exists in X
# This line is just for demonstration and should be adjusted to match your actual data and features
X['Time of Day'] = sample_df['Time of Day']  # Adjust this as necessary

# Now, apply one-hot encoding, specifying the correct columns, including 'Time of Day'
X = pd.get_dummies(X, columns=['Day of Week', 'Month', 'Time of Day'], drop_first=True)

# Continue with your data split and model training as before

y = sample_df['Crm Cd']  # Assuming 'Crm Cd' as the target variable

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f'Training features shape: {X_train.shape}')
print(f'Testing features shape: {X_test.shape}')
print(f'Training labels shape: {y_train.shape}')
print(f'Testing labels shape: {y_test.shape}')
