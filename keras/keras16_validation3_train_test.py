import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#1. 데이터
x = np.array(range(1,17))
y = np.array(range(1,17))
#[실습] 잘라봐!
# train_test_split
# 10:3:3 으로 잘라라

x_train = x[:10] 
x_val = x[7:]
x_test = x[7:]
y_train = y[:7]
y_test = y[7:] 

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size=0.7, random_state=12)

# x_train = np.array(range(1,11))
# y_train = np.array(range(1,11))
# x_test = np.array([11,12,13])
# y_test = np.array([11,12,13])
# x_validation = np.array([14,15,16])
# y_validation = np.array([14,15,16])


#2. 모델
model = Sequential()
model.add(Dense(5, input_dim=1))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train, epochs=100, batch_size=1,
          validation_split=0.25)

#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

result = model.predict([17])
print("17의 예측값 : ", result)

"""
1. loss :  0.163548544049263 / 17의 예측값 :  [[16.218893]]
2. loss :  0.00013962025695946068 / 17의 예측값 :  [[16.976988]]

"""