import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler

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
    train_size=0.9, shuffle=True, random_state=479)

scaler = MinMaxScaler()
# scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.fit_transform(x_train)
x_tset = scaler.transform(x_test)
# x_train = scaler.transform(x_train)
# x_tset = scaler.transform(x_test)

print(x_train.shape, x_test.shape)  #(7620, 8) (3266, 8)
print(y_train.shape, y_test.shape)  #(7620,) (3266,)

#2. 모델구성
model = Sequential()
model.add(Dense(5, input_dim=8, activation='relu'))
model.add(Dense(30, activation ='relu'))
model.add(Dense(20, activation ='relu'))
model.add(Dense(15, activation = 'relu'))
model.add(Dense(14, activation = 'relu'))
model.add(Dense(13, activation = 'relu'))
model.add(Dense(12, activation = 'relu'))
model.add(Dense(11, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(1, activation='linear'))

#3. 컴파일, 훈련
import time
model.compile(loss='mse', optimizer='adam',
                metrics=['mae'])
start = time.time()
model.fit(x_train, y_train, epochs=200, batch_size=32)
end = time.time()

#4.평가, 예측 
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

y_predict = model.predict(x_test)
print(y_predict)


def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
rmse = RMSE(y_test, y_predict)
print("RMSE : ", rmse)


#5.제출
y_submit = model.predict(test_csv)
# print(y_submit)
# print(y_submit.shape) #(715, 1)


# .to_csv()를 사용해서
# submission_0105.csv를 완성하시오!
# print(submission)
submission['count'] = y_submit
# print(submission)

# submission.to_csv(path + 'submission_01061908.csv')

"""
model.add(Dense(32, input_dim=8, activation='relu'))   # default
model.add(Dense(64, activation = 'sigmoid'))

0330 : RMSE :  52.771361535456684 / R2 :  0.5780160553878502
0331 : RMSE :  51.5345030616858 / R2 :  0.5975652137536669
0332 : RMSE :  51.231540961068056 / R2 :  0.6022829892539703
0335 : RMSE :  147.71284336723625
1908 : RMSE :  150.74173693655038

"""


"""
1. MinMaxScaler
loss :  [58771.265625, 170.61756896972656]
RMSE :  RMSE :  242.42787349044082

2. StandardScaler
loss :  [21361.658203125, 108.5748062133789]
RMSE :  146.15628821791444

"""