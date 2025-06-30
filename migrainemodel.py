import os 
import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

migraine_dataset=pd.read_csv('Data and EDA/Cleaned_Migraine.csv')

#Loading the data
migraine_data=pd.read_csv('Data and EDA/Cleaned_Diabetes.csv')
print(migraine_data.head(5))

#Finding the correlation
correlation=migraine_data.corr()
print(correlation)

#Train test split
X=migraine_dataset.drop(columns='Type',axis=1)
Y=migraine_dataset['Type']

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2)
print(X.shape,X_train.shape,X_test.shape)

#Training the model

knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,Y_train)
#Make pickle file of our file

# Ensure the directory exists
directory = 'C:/Users/Shivangi/OneDrive/Desktop/Shivangi Singh/Nexora/HealthMate'
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

pickle.dump(knn,open("migraineresult.pkl","wb")) 