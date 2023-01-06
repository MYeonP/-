import numpy as np
import pandas as pd
import time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


#1. 데이터
path = './_data/bike/'
train_csv = pd.read_csv(path+'train.csv', index_col=0)
# print(train_csv) # [10886 rows x 11 columns]
test_csv = pd.read_csv(path+'test.csv', index_col=0)
submission = pd.read_csv(path+'sampleSubmission.csv', index_col=0)

print(train_csv.isnull().sum())
train_csv = train_csv.dropna()
print(train_csv.shape) # (10886, 11)

x = train_csv.drop(['casual', 'registered', 'count'], axis=1) # axis=축, x값만 남기기


print(x)
# [10886 rows x 8 columns] -> dropna로 인한 변경

y = train_csv['count']
print(y) # Length: 10886


x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True,
    train_size=0.8,
    random_state=1234)

print(x_train.shape, x_test.shape) # (7620, 8), (3266, 8)
print(y_train.shape, y_test.shape) # (7620,), (3266,)


# 2. 모델구성
model = Sequential()
model.add(Dense(32, input_dim=8, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='relu')) # output_dim = 1


# 3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
start = time.time()
model.fit(x_train, y_train, epochs=100, batch_size=32)
end = time.time()


# 4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print("loss: ", loss)

y_predict = model.predict(x_test)
# print(y_predict)

def RMSE (y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))

rmse = RMSE(y_test, y_predict)
print("RMSE: ", rmse)

print("소요 시간: ", end - start)

# 제출
y_submit = model.predict(test_csv)
print(y_submit)
# print(y_submit.shape) 

submission['count'] = y_submit
# pandas(submission['count'])에 numpy(y_submit)를 직접 대입시키면 numpy가 pandas가 됨
print(submission)

submission.to_csv(path+'sampleSubmission_01061957.csv')