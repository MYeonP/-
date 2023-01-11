#[과제, 실습]
#R2 0.62 이상

from sklearn.datasets import load_diabetes
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

#1. 데이터
datasets = load_diabetes()
x = datasets.data
y = datasets.target

"""
print(x)
print(x.shape)  #(442, 10)
print(y)
print(y.shape)  #(442,)
"""

print(datasets.feature_names)
print(datasets.DESCR)

x_train, x_test, y_train, y_test = train_test_split(x, y,
    train_size=0.8, shuffle=True, random_state=1234)

scaler = MinMaxScaler()
# scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.fit_transform(x_train)
x_tset = scaler.transform(x_test)
# x_train = scaler.transform(x_train)
# x_tset = scaler.transform(x_test)



#2. 모델구성
model = Sequential()
model.add(Dense(100, input_dim=10, activation = 'relu'))
model.add(Dense(90, activation='relu'))
model.add(Dense(60,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(1, activation = 'linear'))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam', metrics=['mae']) 
model.fit(x_train, y_train, epochs=500, batch_size=32, validation_split=0.3)

#4.평가, 예측 
y_predict = model.predict(x_test)

loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

from sklearn.metrics import mean_squared_error, r2_score
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE : ", RMSE(y_test, y_predict))

r2 = r2_score(y_test, y_predict)
print("R2 : ", r2)

"""

1. MinMaxScaler
loss :  [12284.3271484375, 88.80355834960938]
RMSE :  110.83468603253759
R2 :  -1.2185595697875402

2. StandardScaler
loss :  [8561.361328125, 66.74658966064453]
RMSE :  92.52762295201114
R2 :  -0.5461887677163335

"""