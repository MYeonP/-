import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#1. 데이터
x_train = np.array(range(1,11)) # 1,2,3,4,5,6,7,8,9,10
y_train = np.array(range(1,11))
x_test = np.array([11,12,13])
y_test = np.array([11,12,13])
x_validation = np.array([14,15,16])
y_validation = np.array([14,15,16])


#2. 모델
model = Sequential()
model.add(Dense(5, input_dim=1))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train, epochs=1000, batch_size=100,
          validation_data=(x_validation, y_validation))
# validation_data를 통해서 val_loss 추가
# 훈련 + 검증(Validation) + 평가 (fit+validation+ evaluate)

#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

result = model.predict([17])
print("17의 예측값 : ", result)

"""
1. loss :  0.163548544049263 / 17의 예측값 :  [[16.218893]]
2. loss :  0.00013962025695946068 / 17의 예측값 :  [[16.976988]]

"""


