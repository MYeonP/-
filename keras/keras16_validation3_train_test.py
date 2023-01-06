import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

#1. 데이터
x = np.array(range(1,17))
y = np.array(range(1,17))
#[실습] 잘라봐!
# train_test_split
# 10:3:3 으로 잘라라

x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle = True, random_state=126, test_size=0.375)
x_test, x_val, y_test, y_val = train_test_split(x_test, y_test, shuffle = True, random_state=126, test_size=0.5)
print(x_train)  #[ 1  2  3  4  5  6  7  8  9 10]
print(x_test)   #[11 12 13]
print(y_train)  #[ 1  2  3  4  5  6  7  8  9 10]
print(y_test)   #[11 12 13]
print(x_val)    #[14 15 16]
print(y_val)    #[14 15 16]

# test_size=0.375로 맞춰주면 x_train은 10
# 남은 test_size를 validation으로 0.5로 나눠주면 10:3:3 완성!


#2. 모델
model = Sequential()
model.add(Dense(5, input_dim=1))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train, epochs=100, batch_size=1,
          validation_data=(x_val, y_val))    #validation_split=0.25

#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

result = model.predict([17])
print("17의 예측값 : ", result)

"""
1. loss :  0.163548544049263 / 17의 예측값 :  [[16.218893]]
2. loss :  0.00013962025695946068 / 17의 예측값 :  [[16.976988]]

"""