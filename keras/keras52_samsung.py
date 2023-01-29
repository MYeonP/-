import numpy as np
import pandas as pd
import tensorflow as tf
import time
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.layers import Dense, Flatten, Input, Conv1D, Dropout, MaxPooling1D
from tensorflow.python.keras.callbacks import EarlyStopping, ModelCheckpoint


# 1. 데이터

path = './_data/samsung/'
samjun_csv = pd.read_csv(path + 'samjun.csv', index_col=0, 
                         encoding='cp949', header=0, nrows= 1166, usecols=[0,1,2,3,4,8])
amore_csv = pd.read_csv(path + 'amore.csv', index_col=0, encoding='cp949', 
                        nrows= 1166, usecols=[0,1,2,3,4,8], header=0)
# print(samjun_csv)   # [1980 rows x 17 columns]
# print(amore_csv)   # [2220 rows x 17 columns]

# print(samjun_csv.info())    #결측치 있음
# print(amore_csv.info())    #결측치 있음

# samjun_csv = samjun_csv.dropna()
# amore_csv = amore_csv.dropna()  # samjun_csv, amore_csv의 결측치 모두 삭제

# print(samjun_csv.info())   
# print(amore_csv.info())    # 결측치 삭제 확인

# 1-2. 데이터 타입 변환

samjun_csv['시가'] = samjun_csv['시가'].str.replace(',', '').astype('float')
samjun_csv['고가'] = samjun_csv['고가'].str.replace(',', '').astype('float')
samjun_csv['저가'] = samjun_csv['저가'].str.replace(',', '').astype('float')
samjun_csv['종가'] = samjun_csv['종가'].str.replace(',', '').astype('float')
samjun_csv['거래량'] = samjun_csv['거래량'].str.replace(',', '').astype('float')

amore_csv['시가'] = amore_csv['시가'].str.replace(',', '').astype('float')
amore_csv['고가'] = amore_csv['고가'].str.replace(',', '').astype('float')
amore_csv['저가'] = amore_csv['저가'].str.replace(',', '').astype('float')
amore_csv['종가'] = amore_csv['종가'].str.replace(',', '').astype('float')
amore_csv['거래량'] = amore_csv['거래량'].str.replace(',', '').astype('float')

samjun_csv = samjun_csv.sort_values(['일자'], ascending=[True])
amore_csv = amore_csv.sort_values(['일자'], ascending=[True])

print(samjun_csv)   # [1166 rows x 5 columns]
print(amore_csv)    # [1166 rows x 5 columns]

sj_open = samjun_csv['시가'][1:]

x1_train, x1_test, y_train, y_test = train_test_split(
    samjun_csv[:1165], sj_open, train_size=0.7, shuffle=True, random_state=1234)

x1_train = x1_train.to_numpy()
x1_test = x1_test.to_numpy()

x2_train, x2_test = train_test_split(
   amore_csv[:1165], train_size=0.7, shuffle=True, random_state=123
)

x2_train = x2_train.to_numpy()
x2_test = x2_test.to_numpy()

print(x1_train.shape, x1_test.shape)#(815, 5) (350, 5)
print(x2_train.shape, x2_test.shape)#(815, 5) (350, 5)

x1_train = x1_train.reshape(815, 5, 1)
x1_test = x1_test.reshape(350, 5, 1)
x2_train = x2_train.reshape(815, 5, 1)
x2_test = x2_test.reshape(350, 5, 1)


#2. 모델구성

#2-1. 삼성전자 모델 구성
input1= Input(shape=(5, 1))
dense1= Conv1D(64, 2, padding='same', activation='relu', name='ds11')(input1)
dense2= Conv1D(128, 2, padding='same', activation='relu', name='ds12')(dense1)
dense3= Conv1D(128, 2, padding='same', activation='relu', name='ds13')(dense2)
dense4= Conv1D(256, 2, padding='same', activation='relu', name='ds14')(dense3)
dense5= Conv1D(256, 2, padding='same', activation='relu', name='ds16')(dense4)
dense6= Conv1D(256, 2, padding='same', activation='relu', name='ds17')(dense5)
dense7= Conv1D(512, 2, padding='same', activation='relu', name='ds18')(dense6)
dense8= Conv1D(512, 2, padding='same', activation='relu', name='ds20')(dense7)
dense9= Conv1D(128, 2, padding='same', activation='relu', name='ds24')(dense8)
dense10= Conv1D(128, 2, padding='same', activation='relu', name='ds25')(dense9)
dense11= Conv1D(64, 2, padding='same', activation='relu', name='ds26')(dense10)
dense12= Flatten(name='ds28')(dense11)
output1= Dense(32, activation='relu', name='ds29')(dense12) 

#2-2. 아모레 모델 구성
input2= Input(shape=(5, 1))
dense21= Conv1D(64, 2, padding='same', activation='relu', name='ds31')(input2)
dense22= Conv1D(128, 2, padding='same', activation='relu', name='ds32')(dense21)
dense23= Conv1D(128, 2, padding='same', activation='relu', name='ds34')(dense22)
dense24= Conv1D(256, 2, padding='same', activation='relu', name='ds35')(dense23)
dense25= Conv1D(256, 2, padding='same', activation='relu', name='ds37')(dense24)
dense26= Conv1D(256, 2, padding='same', activation='relu', name='ds38')(dense25)
dense27= Conv1D(512, 2, padding='same', activation='relu', name='ds39')(dense26)
dense28= Conv1D(512, 2, padding='same', activation='relu', name='ds41')(dense27)
dense29= Conv1D(512, 2, padding='same', activation='relu', name='ds42')(dense28)
dense30= Conv1D(256, 2, padding='same', activation='relu', name='ds43')(dense29)
dense31= Conv1D(256, 2, padding='same', activation='relu', name='ds45')(dense30)
dense32= Conv1D(128, 2, padding='same', activation='relu', name='ds46')(dense31)
dense33= Conv1D(128, 2, padding='same', activation='relu', name='ds47')(dense32)
dense34= Flatten(name='ds49')(dense33)
output2= Dense(32, activation='relu', name='ds50')(dense34)


#2-3. 모델병합
from tensorflow.keras.layers import concatenate 
merge1 = concatenate([output1, output2], name='mg1')
merge2 = Dense(128, activation='relu', name='mg2')(merge1)
merge3 = Dense(256, activation='relu', name='mg3')(merge2)
merge4 = Dense(128, activation='relu', name='mg4')(merge3)
merge5 = Dense(64, activation='relu', name='mg5')(merge4)
merge6 = Dense(32, activation='relu', name='mg6')(merge5)
merge7 = Dense(16, activation='relu', name='mg7')(merge6)
merge8 = Dense(8, activation='relu', name='mg8')(merge7)
last_output = Dense(1, name='last')(merge8)

model = Model(inputs=[input1, input2], outputs=last_output)  # 모델이 두개라서 input1, input2

model.summary()


#3. 컴파일, 훈련

model.compile(loss='mse', optimizer='adam', metrics=['acc'])

import datetime 
date = datetime.datetime.now()
date = date.strftime('%M%D_%H%M')

filepath = './_save/MCP/'
filename = '{epoch:04d}-{val_loss:.4f}.hdf5'

es = EarlyStopping(monitor='val_loss', mode='min', restore_best_weights=True, patience=20, verbose=1)

mcp = ModelCheckpoint(monitor='val_loss', mode='min', save_best_only=True, verbose=1, 
                      filepath= filepath + 'k52_1_' + date + '_' + filename)


# y_train = y_train.astype(float)
# y_test = y_test.astype(float)

model.fit([x1_train, x2_train], y_train, epochs=300, batch_size=32, validation_split=0.2, callbacks=[es, mcp])

model.save_weights(path + 'stock_weight.h5')

#4. 평가, 예측
loss = model.evaluate([x1_test, x2_test], y_test)
print('loss:', loss)

result = model.predict([samjun_csv[1165:].to_numpy(), amore_csv[1165:]])
print('1/30 삼전 시가:', result)

