import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, LSTM
from sklearn.model_selection import train_test_split

# 1. 데이터
a = np.array(range(1, 101))
x_predict = np.array(range(96, 106))
# 예상 y = 100 ~ 107


timesteps = 5  # x는 4개, y는 1개

# 선생님 방식!
# timesteps1 = 5  
# timesteps2 = 4  


def split_x(dataset, timesteps):
    aaa = []
    for i in range(len(dataset) - timesteps +1 ):
        subset = dataset[i : (i + timesteps)]
        aaa.append(subset)
    return np.array(aaa)

bbb = split_x(a, timesteps)
print(bbb)
print(bbb.shape)    # (96, 5)

x = bbb[:, :-1]
y = bbb[:, -1]
print(x, y)
print(x.shape, y.shape)     # (96, 4) (96,)

# 선생님 방식
x_predict = split_x(x_predict, timesteps=4)
print(x_predict)
print(x_predict.shape)    # (7, 4)

# 기존에 지현님 도움 받아 만든 방식 (결과는 동일함)
# x_predict = ccc
# x_predict = x_predict.reshape(7, 4, 1)
# x = x.reshape(96, 4, 1)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, shuffle=True, random_state=1234
)

print(x_train.shape, y_train.shape)     # (72, 4) (72,)
print(x_test.shape, y_test.shape)       # (24, 4) (24,)


x_train = x_train.reshape(72, 4, 1)
x_test = x_test.reshape(24, 4, 1)
x_predict = x_predict.reshape(7, 4, 1)

print(x_train.shape, y_train.shape)        # (72, 4, 1) (72,)
print(x_train.shape, y_train.shape)        # (72, 4, 1) (72,)
print(x_predict.shape)      # (7, 4, 1)



#2. 모델구성
model = Sequential()
model.add(LSTM(64, input_shape=(4, 1), activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(40, activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))

model.summary()

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train, epochs=300, batch_size=1)

#4. 평가, 예측 
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)
result = model.predict(x_predict)

print('결과 : ', result)

"""

loss :  1.0608298907754943e-05
결과 :  
[[100.00714 ]
 [101.00832 ]
 [102.009605]
 [103.01098 ]
 [104.01245 ]
 [105.01404 ]
 [106.01569 ]]

loss :  0.00036492792423814535
결과 :  [[ 99.98666]
 [100.98354]
 [101.98023]
 [102.97675]
 [103.97305]
 [104.96917]
 [105.96507]
 
 loss :  0.004789977800101042
결과 :  [[100.175385]
 [101.19184 ]
 [102.209595]
 [103.22758 ]
 [104.24588 ]
 [105.26446 ]
 [106.283295]]

"""

