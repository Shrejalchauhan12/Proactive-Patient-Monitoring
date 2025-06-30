#Importing the libraries

import pickle
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


#Loading the data
diabetes_data=pd.read_csv('Data and EDA/Cleaned_Diabetes.csv')
print(diabetes_data.head(5))

#Finding the correlation
correlation=diabetes_data.corr()
print(correlation)

#Train test split
X=diabetes_data.drop("Outcome",axis=1)
Y=diabetes_data['Outcome']

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
print(X_train)

#Training the model

model = RandomForestClassifier(
    n_estimators=100,     # number of trees
    max_depth=10,         # control tree depth
    min_samples_split=5,  # minimum samples to split
    random_state=42
)
model.fit(X_train, Y_train)

#Make pickle file of our file

# Ensure the directory exists
directory = 'C:/Users/Shivangi/OneDrive/Desktop/Shivangi Singh/MediMother'
os.makedirs(directory, exist_ok=True)

# Construct the absolute file path
file_path = os.path.join(directory, 'result.pkl')

# Example data to be pickled
data = {'example': 'data'}

try:
    # Open the file in write-binary mode
    with open(file_path, 'wb') as f:
        # Pickle the data and write it to the file
        pickle.dump(data, f)
    print("Pickle file created successfully.")
except Exception as e:
    print("Error:", e)

pickle.dump(model,open("diabetesresult.pkl","wb")) 