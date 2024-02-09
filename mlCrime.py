# Handling Missing Values: Check for missing values in the dataset
import pandas as pd

# Load the sample dataset
sample_df = pd.read_csv('Crime_Data_from_2020_to_Present(1).csv')

# Display the first few rows of the dataset to understand its structure
sample_df.head()


missing_values = sample_df.isnull().sum()

# Feature Selection: Based on initial overview, let's initially select a broad set of features
# These might include 'Date Rptd', 'DATE OCC', 'TIME OCC', 'AREA', 'AREA NAME', 'Crm Cd', 'Crm Cd Desc', 'LAT', 'LON'
# We will refine this selection based on missing values and relevance to the crime prediction task

# For demonstration, we'll just check missing values and suggest features without actually dropping or imputing yet
selected_features = ['Date Rptd', 'DATE OCC', 'TIME OCC', 'AREA', 'AREA NAME', 'Crm Cd', 'Crm Cd Desc', 'LAT', 'LON']

missing_values[selected_features]
