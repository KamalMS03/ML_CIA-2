import pandas as pd
import pickle

data = pd.read_csv(r"C:\Users\kamal\Downloads\Crop_recommendation.csv")

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

from sklearn.linear_model import LogisticRegression
reg = LogisticRegression()
reg.fit(x,y)

pickle.dump(reg,open("model.pkl",'wb'))
