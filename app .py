import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor

st.title('🏠House Price prediction using ML')
st.image('https://i.pinimg.com/originals/ec/d3/b6/ecd3b6b355ab6f67c9679c42f585d817.gif')

df = pd.read_csv('house_data.csv')
X = df.iloc[:,:-3]
y = df.iloc[:,-1]

st.sidebar.title('🏘️ Select House features')
st.sidebar.image('https://i.pinimg.com/originals/ec/d3/b6/ecd3b6b355ab6f67c9679c42f585d817.gif')
all_value = []
for i in X:
  min_value = int(X[i].min())
  max_value = int(X[i].max())
  ans = st.sidebar.slider(f'Select {i} value',min_value,max_value)
  all_value.append(ans)

#st.write(all_value)
scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)
final_value = scaler.transform([all_value])

model = RandomForestRegressor()
model.fit(X,y)
House_price = model.Predict(final_value)

with st.spinner('Predicting House Price'):
  time.sleep(3)
st.write(house_price)

