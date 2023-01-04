import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. 데이터
x = np.array([range(10), range(21, 31), range(201, 211)])   #모든 개발은 0부터 시작. 0~9까지가 range(10)
# print(range(10))  'ctrl + /' 누르면 주석 처리로 교체. 0부터 10-1 까지

# print(x.shape)  #(3, 10)

y = np.array([[1,2,3,4,5,6,7,8,9,10],
              [1,1,1,1,2,1.3,1.4,1.5,1.6,1.4]])

# print(y.shape)  (2, 10)

x = x.T
y = y.T

print(x.shape)  #(10, 3)
print(y.shape)  #(10, 2)

#2. 모델 구성
model = Sequential()
model.add(Dense(5, input_dim=3))    # input_dim = 열의 개수
model.add(Dense(4))
model.add(Dense(3))
model.add(Dense(3))
model.add(Dense(2))

#3. 컴파일, 훈련
model.compile(loss='mae', optimizer='adam')
model.fit(x, y, epochs=1000, batch_size=1)

#4. 평가, 예측
loss = model.evaluate(x, y)
print('loss : ', loss)

result = model.predict([[9, 30, 210]])
print('[9, 30, 210]의 예측값 : ', result)

"""
1. loss :  0.14392229914665222 / [9, 30, 210]의 예측값 :  [[9.909229  1.5023099]]

"""