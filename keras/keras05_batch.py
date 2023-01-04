import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#1. 데이터
x = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,5,4,6])

#2. 모델구성
model = Sequential()
model.add(Dense(3, input_dim=1))
model.add(Dense(50))
model.add(Dense(40))
model.add(Dense(10))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mae', optimizer='adam')
model.fit(x, y, epochs=10, batch_size=7)  # batch size default = 32

#4. 평가, 예측
result = model.predict([6])
print('6의 결과 : ', result)

"""
안녕하세용
주석과 마찬가지인
쌍따옴표 세개에용
"""    #쌍따옴표 3개 후 쓴 글들은 #(주석)과 마찬가지로 BLOCK처리