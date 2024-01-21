import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from sklearn.linear_model import LinearRegression 
 #Download and Prepare the Data 
data_root = "https://github.com/ageron/data/raw/main"
lifesat = pd.read_cvs(data_root + "lifesat/lifesat.cvs")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat [["Life Satisfaction"]].values

#Visualize the Data
lifesat.plot(kind = 'scatter', grid=True,
X="GDP per capita (USD)", y="Life Satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show
#Select a Linear Model now
model = LinearRegression()
#Train the Model 
model.fit(X, y)
#Make a Prediction for Cyprus
X_new = [[37_655.2]]  #Cyprus Capita per GPT in 2020
print(model.predict(X_new))