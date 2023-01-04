# [실습]
# R2 0.55~0.6 이상

from sklearn.datasets import fetch_california_housing
import sklearn as sk
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

#1. 데이터
datasets = fetch_california_housing()
x = datasets.data
y = datasets.target

"""
print(x)
print(x.shape)  #(20640, 8)
print(y)
print(y.shape)  #(20640,)
"""

print(datasets.feature_names)
print(datasets.DESCR)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y,
    train_size=0.9, shuffle=True, random_state=65)

#2. 모델구성
model = Sequential()
model.add(Dense(5, input_dim=8))
model.add(Dense(50))
model.add(Dense(30))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam', metrics=['mae']) 
model.fit(x_train, y_train, epochs=600, batch_size=200)

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
1. R2 :  0.5430312595296418
2. R2 :  0.5195147824443711
3. R2 :  0.5256790471852559
4. R2 :  0.5308637038368442
5. R2 :  0.5453362142711884
6. R2 :  0.5778417890480458     train_size=0.9, random_state=65


"""