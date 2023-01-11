
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler

#1. 데이터
datasets = fetch_california_housing()
x = datasets.data
y = datasets.target

print(x.shape, y.shape)     #(506, 13) (506,)

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
model = Sequential()
# model.add(Dense(5, input_dim=13))       # 다차원일 경우 input_shape를 쓴다
model.add(Dense(5, input_shape=(8,)))    # (ex: (100,10,3) -> input_shape=(10, 3) / 행 무시)
model.add(Dense(4))
model.add(Dense(3))
model.add(Dense(2))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')

from tensorflow.keras.callbacks import EarlyStopping
EarlyStopping = EarlyStopping(monitor='val_loss', mode='min',
                patience=10, restore_best_weights=True,
                verbose=1)
# loss, vai_loss : mode='min'(최소) / accuracy : mode='max'(최대)

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
loss :  2360896.0
RMSE :  1536.5206328503307
R2 :  -1853021.779569484

2. StandardScaler
loss :  0.6379747986793518
RMSE :  0.7987330427118031
R2 :  0.499265785158874

"""