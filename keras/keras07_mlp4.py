import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. 데이터
x = np.array([range(10)])
x = x.T  #(10, ) (10, 1)

y = np.array([[1,2,3,4,5,6,7,8,9,10],
              [1,1,1,1,2,1.3,1.4,1.5,1.6,1.4],
              [9,8,7,6,5,4,3,2,1,0]])
y = y.T
# print(x.shape)    (10, )
# print(y.shape)    (10, 3)

#2. 모델 구성
model = Sequential()
model.add(Dense(5, input_dim=1))    # input_dim = 열의 개수
model.add(Dense(40))
model.add(Dense(3))
model.add(Dense(5))
model.add(Dense(3))

#3. 컴파일, 훈련
model.compile(loss='mae', optimizer='adam')
model.fit(x, y, epochs=200, batch_size=1)

#4. 평가, 예측
loss = model.evaluate(x, y)
print('loss : ', loss)

result = model.predict([[9]])
print('[9]의 예측값 : ', result)

"""
1. loss : 0.164252370595932 / [9]의 예측값 : [[9.883142 1.2916913 0.3477585]]
2. loss : 0.10310079902410507 / [9]의 예측값 : [[10.221615 1.6405311 -0.12180462]]

"""