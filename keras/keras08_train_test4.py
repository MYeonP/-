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

#[실습] train_test_split을 이용하여
#7:3으로 잘라서 모델 구현 / 소스 완성

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, 
    train_size=0.7, 
    #test_size=0.3,     #더 강한 숫자 위주 / 에러일 때 표시 X
    #shuffle=False,     #'True'가 기본값
    random_state=123    #다음에 돌려도 동일한 데이터로 출력
)

"""
print('x_train : ', x_train)
print('x_test : ', x_test)
print('y_train : ', y_train)
print('y_test : ', y_test)
"""

#2. 모델 구성
model = Sequential()
model.add(Dense(5, input_dim=3))
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
1. loss : 0.2915177047252655 / [9, 30, 210]의 예측값 : [[10.4054165  1.7011592]]
2. loss : 0.18258710205554962 / [9, 30, 210]의 예측값 : [[10.024476   1.3539234]]
3. loss : 0.18258710205554962 / [9, 30, 210]의 예측값 : [[10.024476   1.3539234]]

"""
