import numpy as np   #numpy를 np라고 부를거야
import tensorflow as tf   #tensorflow를 tf라고 부를거야
print(tf.__version__)    #버전 보여줘 : 2.7.4 

#1. (정제된) 데이터
x = np.array([1,2,3,4,5])  #약간 틀어보기 : x는 1,2,3,4,5 / y는 1,2,3,5,4
y = np.array([1,2,3,5,4])  #내가 원하는 값 : x=6일 때 y=6

#2. 모델 구성(y=Wx+b)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(1, input_dim=1))

#3. 컴파일, 훈련
model.compile(loss='mae', optimizer='adam')
model.fit(x, y, epochs=290)

#4. 평가, 예측
results = model.predict([6])
print('6의 예측값 :', results)   #290번 돌렸을 때 : 6의 예측값 : [[5.9999456]]
