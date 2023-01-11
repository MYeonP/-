
from tensorflow.keras.models import Sequential, Model 
from tensorflow.keras.layers import Dense, Input  # (Model, Input : 함수형)
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler

#1. 데이터
datasets = fetch_california_housing()
x = datasets.data
y = datasets.target

print(x.shape, y.shape)     #(20640, 8) (20640,)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, shuffle=True, random_state=333, test_size=0.2)

scaler = MinMaxScaler()
# scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.fit_transform(x_train)
x_tset = scaler.transform(x_test)
# x_train = scaler.transform(x_train)
# x_tset = scaler.transform(x_test)


#2. 모델구성
# model = Sequential()
# # model.add(Dense(5, input_dim=8))       # 다차원일 경우 input_shape를 쓴다
# model.add(Dense(5, input_shape=(8,)))    # (ex: (100,10,3) -> input_shape=(10, 3) / 행 무시)
# model.add(Dense(4))
# model.add(Dense(3))
# model.add(Dense(2))
# model.add(Dense(1))

#2. 모델구성(함수형)
input1 = Input(shape=(8,))
dense1 = Dense(50, activation = 'relu')(input1)
dense2 = Dense(40, activation = 'sigmoid')(dense1)
dense3 = Dense(30, activation = 'relu')(dense2)
dense4 = Dense(20, activation = 'linear')(dense3)
output1 = Dense(1, activation = 'linear')(dense4)
model = Model(inputs=input1, outputs=output1)
# model.summary()
# Total params: 4,611

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')

from tensorflow.keras.callbacks import EarlyStopping
EarlyStopping = EarlyStopping(monitor='val_loss', mode='min',
                patience=10, restore_best_weights=True,
                verbose=1)
# loss, vai_ioss : mode='min'(최소) / accuracy : mode='max'(최대)

hist = model.fit(x_train, y_train, epochs=300, batch_size=32,
          validation_split=0.2, callbacks=[EarlyStopping], verbose=1)  # True = 1 / False = 0

#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

y_predict = model.predict(x_test)

def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))

print("RMSE : ", RMSE(y_test, y_predict))

r2 = r2_score(y_test, y_predict)
print("R2 : ", r2)

"""

1. MinMaxScaler
loss :  35.66520309448242
RMSE :  5.972034184749349
R2 :  -26.992941421124556

2. StandardScaler
loss :  15.29551887512207
RMSE :  3.9109485322398165
R2 :  -11.005165920335914

"""