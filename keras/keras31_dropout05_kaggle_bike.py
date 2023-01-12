
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
path = './_data/bike/'
train_csv = pd.read_csv(path + 'train.csv', index_col=0)
# train_csv = pd.read_csv('./_data/ddarung/train.csv', index_col=0)
test_csv = pd.read_csv(path + 'test.csv', index_col=0)
submission = pd.read_csv(path + 'sampleSubmission.csv', index_col=0)

print(train_csv.shape)  #(10886, 11)
print(submission.shape) #(6493, 1)

print(train_csv.columns)
# Index(['season', 'holiday', 'workingday', 'weather', 'temp', 'atemp',
#       'humidity', 'windspeed', 'casual', 'registered', 'count'],
#      dtype='object')

print(train_csv.info())
print(test_csv.info())
print(train_csv.describe())

##### 결측치 처리 1. 제거 #####
print(train_csv.isnull().sum())
train_csv = train_csv.dropna()  #null, nan 등의 결측치 삭제 함수
print(train_csv.isnull().sum())
print(train_csv.shape)

x = train_csv.drop(['casual', 'registered', 'count'], axis=1)    #test에는 count가 없어서 맞추기 위해 삭제
print(x)        #[10886 rows x 8 columns]

y = train_csv['count']
# print(y)        
# print(y.shape)  #(10886,)


x_train, x_test, y_train, y_test = train_test_split(x, y,
    train_size=0.8, shuffle=True, random_state=123)

# scaler = MinMaxScaler()
scaler = StandardScaler()
scaler.fit(x_train)
# x_train = scaler.fit_transform(x_train)
# x_tset = scaler.transform(x_test)
x_train = scaler.transform(x_train)
x_tset = scaler.transform(x_test)

print(x_train.shape, x_test.shape)  #(7620, 8) (3266, 8)
print(y_train.shape, y_test.shape)  #(7620,) (3266,)


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
input1 = Input(shape=(8,))
dense1 = Dense(50, activation = 'relu')(input1)
drop1 = Dropout(0.5)(dense1)
dense2 = Dense(40, activation = 'sigmoid')(drop1)
drop2 = Dropout(0.3)(dense2)
dense3 = Dense(30, activation = 'relu')(drop2)
drop3 = Dropout(0.2)(dense3)
dense4 = Dense(20, activation = 'linear')(drop3)
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
                              patience=20, 
                              # restore_best_weights=False,
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
                     filepath = filepath + 'k31_05_' + date + '_' + filename)



model.fit(x_train, y_train, epochs=5000, batch_size=32,     
        validation_split=0.2, callbacks=[es, mcp], #   EarlyStopping 치명적 단점 == 끊은시점에 weight로 저장된다.
        verbose=1)        #   verbose = 0 일때 속도가 더 빠르다. // verbose = 2 간략하게 보임(progress bar X) // verbose >=3 훈련 횟수만 보임

model.save(path + "keras31_dropout05_save_model.h5")

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
model2 = load_model(path + 'keras31_dropout05_save_model.h5')
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
 
submission.to_csv(path + 'submission_01121848.csv')

# print("========================= 3. ModelCheckPoint 츨력 =========================")
# model3 = load_model(path + 'MCP/keras30_ModelCheckPoint3.hdf5')
# mse, mae = model3.evaluate(x_test, y_test)
# print('mse : ', mse)


# y_predict = model3.predict(x_test)
# r2 = r2_score(y_test, y_predict)
# print("R2 스코어 : ", r2)


