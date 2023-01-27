import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, LSTM

a = np.array(range(1, 11))
timesteps = 5

def split_x(dataset, timesteps):
    aaa = []
    for i in range(len(dataset) - timesteps +1 ):
        subset = dataset[i : (i + timesteps)]
        aaa.append(subset)
    return np.array(aaa)
    
bbb = split_x(a, timesteps)
print(bbb)
print(bbb.shape)

x = bbb[:, :-1]
y = bbb[:, -1]
print(x, y)
print(x.shape, y.shape)     # (6, 4) (6,)

# 실습
# LSTM 모델 구성

x_predict = np.array([7, 8, 9, 10])
x = x.reshape(6, 4, 1)

#2. 모델구성
model = Sequential()
model.add(LSTM(units = 128, input_shape=(4, 1), activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(40, activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))

model.summary()

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x, y, epochs=300)

#4. 평가, 예측 
loss = model.evaluate(x, y)
print('loss : ', loss)
y_pred = np.array([7, 8, 9, 10]).reshape(1, 4, 1)
result = model.predict(y_pred)
print('[7, 8, 9, 10]의 결과 : ', result)

