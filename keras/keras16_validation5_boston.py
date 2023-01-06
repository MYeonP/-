# [실습]
# 1. train 0.7 이상
# 2. R2 : 0.8 이상 / RMSE 사용

# import sklearn as sk
# print(sk.__version__)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#1. 데이터
dataset = load_boston()
x = dataset.data
y = dataset.target  #가격 데이터

# print(x)
# print(x.shape)  # (506, 13)
# print(y)
# print(y.shape)  # (506,)

# print(dataset.feature_names)
# # ['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT']
# print(dataset.DESCR)

x_train, x_test, y_train, y_test = train_test_split(x, y,
    train_size=0.8, shuffle=True, random_state=42)
  
#2. 모델구성
model = Sequential()
model.add(Dense(5, input_dim=13))
model.add(Dense(24, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train, epochs=100, batch_size=1,
          validation_split=0.25)

#4.평가, 예측 
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

y_predict = model.predict(x_test)

# print("==================")
# print(y_test)
# print(y_predict)
# print("==================")


def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE : ", RMSE(y_test, y_predict))

r2 = r2_score(y_test, y_predict)
print("R2 : ", r2)

"""
1. RMSE :  4.70221954124473 / R2 :  0.6984900047264051

"""