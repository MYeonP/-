import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN

#1. 데이터
dataset = np.array([1,2,3,4,5,6,7,8,9,10])  # (10, )
# y = ???

x = np.array([[1,2,3],
              [2,3,4], 
              [3,4,5], 
              [4,5,6], 
              [5,6,7],
              [6,7,8], 
              [7,8,9]])
y = np.array([4, 5, 6, 7, 8, 9, 10])
print(x.shape, y.shape) # (7, 3), (7, )

# x = x.reshape(7, 3, 1)      # -> [[[1],[2],[3]], 
#                             #    [[2],[3],[4]], ...]
# print(x.shape)              # (7, 3, 1) 


#2. 모델구성
model = Sequential()
# model.add(SimpleRNN(64, input_shape=(3, 1)))
model.add(Dense(64, input_shape=(3, )))
model.add(Dense(16, activation='relu'))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x, y, epochs=200)

#4. 평가, 예측 
loss = model.evaluate(x, y)
print('loss : ', loss)
y_pred = np.array([8, 9, 10]).reshape(1, 3, 1)
result = model.predict(y_pred)
print('[8, 9, 10]의 결과 : ', result)


# loss :  0.12367131561040878
# [8, 9, 10]의 결과 :  [[11.5371475]]

# loss :  0.10536845773458481
# [8, 9, 10]의 결과 :  [[11.494989]]



