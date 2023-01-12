
from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.layers import Dense, Input, Dropout
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler

path = './_save/'
# path = '../_save/'        # path = 'c:/study/_save/'


#1. 데이터

path = './_data/ddarung/'
train_csv = pd.read_csv(path + 'train.csv', index_col=0)
# train_csv = pd.read_csv('./_data/ddarung/train.csv', index_col=0)    # 원래 해야하는거, index_col=0 == 0번째는 데이터 아니다.
test_csv = pd.read_csv(path + 'test.csv', index_col=0)
submission = pd.read_csv(path + 'submission.csv', index_col=0)

# print(train_csv)    #(1459, 10) , count는 y값이므로 제외해야한다. input_dim=9
# print(submission.shape)
# print(train_csv.columns)
# # Index(['hour', 'hour_bef_temperature', 'hour_bef_precipitation',
# #        'hour_bef_windspeed', 'hour_bef_humidity', 'hour_bef_visibility',
# #        'hour_bef_ozone', 'hour_bef_pm10', 'hour_bef_pm2.5', 'count'],
# #       dtype='object')
# print(train_csv.info())     #Non-Null Count 결측치(1459- 1457 =2), (1459-1457 = 2), (1459-1450=9) ...
#                             # 결측치가 있는 데이터는 삭제해버린다.
# print(test_csv.info())
# print(train_csv.describe()) #std = 표준편차, 50% = 중간값

###### 결측치 처리  1. 제거#####
print(train_csv.isnull().sum())         # null값 모두 더하기
train_csv = train_csv.dropna()          # 결측치 제거
print(train_csv.isnull().sum())         # null값 모두 더하기
print(train_csv.shape)                  # (1328, 10)

x = train_csv.drop(['count'], axis=1)   # axis=축
# print(x)    #   [1459 rows x 9 columns]
y = train_csv['count']
# print(y)
# print(y.shape)  # (1459, )

x_train, x_test, y_train, y_test = train_test_split(x, y,
                        train_size=0.8, shuffle=True, random_state=2134)
print(x_train.shape, x_test.shape)  #   (929, 9) (399, 9)
print(y_train.shape, y_test.shape)  #   (929,) (399,)

scaler = MinMaxScaler()
# scaler =StandardScaler()
# scaler.fit(x_train)
# x_train = scaler.transform(x_train)
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
test_csv = scaler.transform(test_csv)

# print(x)
# print(type(x))  # <class 'numpy.ndarray'>


#2. 모델구성(순차형)     # Drop out은 훈련 시에만 적용 된다
# model = Sequential()
# model.add(Dense(50, activation ='relu', input_shape=(8,)))
# model.add(Dropout(0.5))
# model.add(Dense(40, activation = 'sigmoid'))
# model.add(Dropout(0.3))
# model.add(Dense(30, activation = 'relu'))
# model.add(Dropout(0.2))
# model.add(Dense(20, activation = 'linear'))
# model.add(Dense(1, activation = 'linear'))
# model.summary()


#2. 모델구성(함수형)
input1 = Input(shape=(9,))
dense1 = Dense(50, activation = 'relu')(input1)
drop1 = Dropout(0.5)(dense1)
dense2 = Dense(40, activation = 'relu')(drop1)
drop2 = Dropout(0.3)(dense2)
dense3 = Dense(30, activation = 'relu')(drop2)
drop3 = Dropout(0.2)(dense3)
dense4 = Dense(20, activation = 'relu')(drop3)
output1 = Dense(1, activation = 'linear')(dense4)
model = Model(inputs=input1, outputs=output1)
model.summary()

# Total params: 4,611

# model.save(path + 'keras29_1_save_model.h5')
# model.save('./_save/keras29_1_save_model.h5')


#3. 컴파일, 훈련

model.compile(loss='mse', optimizer = 'adam', metrics = ['mae'])

from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

es = EarlyStopping(monitor='val_loss', mode='min',
                              patience=50, 
                              restore_best_weights=True,
                              verbose=1)       # loss = mode ='min' / accuracy = mode ='auto'  //restore_best_weights의 defalut값은 False

import datetime
date = datetime.datetime.now()
print(date)     # 2023-01-12 14:57:50.997693
print(type(date))    #<class 'datetime.datetime'>
date = date.strftime("%m%d_%H%M")   
print(date)    # 0112_1502
print(type(date))    #<class 'str'>

filepath = './_save/MCP/'
filename = '{epoch:04d}-{val_loss:.4f}.hdf5'    #0037-0.0048.bdf5


mcp = ModelCheckpoint(monitor='val_loss', mode='auto', verbose=1, 
                      save_best_only=True, 
                      #filepath=path + 'MCP/keras30_ModelCheckPoint3.hdf5')
                     filepath = filepath + 'k31_04_' + date + '_' + filename)



model.fit(x_train, y_train, epochs=5000, batch_size=32,     
        validation_split=0.2, callbacks=[es, mcp], #   EarlyStopping 치명적 단점 == 끊은시점에 weight로 저장된다.
        verbose=1)        #   verbose = 0 일때 속도가 더 빠르다. // verbose = 2 간략하게 보임(progress bar X) // verbose >=3 훈련 횟수만 보임

model.save(path + "keras31_dropout04_save_model.h5")

# model = load_model(path + 'MCP/keras30_ModelCheckPoint1.hdf5')


#4. 평가, 예측
print("========================= 1. 기본 출력 =========================")

mse, mae = model.evaluate(x_test, y_test)
print('mse : ', mse)

y_predict = model.predict(x_test)

def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))

r2 = r2_score(y_test, y_predict)
print("R2 스코어 : ", r2)


print("========================= 2. load_model 츨력 =========================")
model2 = load_model(path + 'keras31_dropout04_save_model.h5')
mse, mae = model2.evaluate(x_test, y_test)
print('mse : ', mse)


y_predict = model2.predict(x_test)
r2 = r2_score(y_test, y_predict)
print("R2 스코어 : ", r2)

# 제출
y_submit = model.predict(test_csv)   #예측한 카운트가 y_submit 
# print(y_submit)
#print(y_submit.shape) #(715, 1) 

#.to_csv()를 사용해서
#submission.0105.csv를 완성하시오 

# print(submission)
submission['count'] = y_submit
# print(submission)
 
submission.to_csv(path + 'submission_01121905.csv')

# print("========================= 3. ModelCheckPoint 츨력 =========================")
# model3 = load_model(path + 'MCP/keras30_ModelCheckPoint3.hdf5')
# mse, mae = model3.evaluate(x_test, y_test)
# print('mse : ', mse)


# y_predict = model3.predict(x_test)
# r2 = r2_score(y_test, y_predict)
# print("R2 스코어 : ", r2)


