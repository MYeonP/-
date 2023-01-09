import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#1. 데이터
path = './_data/ddarung/'
train_csv = pd.read_csv(path + 'train.csv', index_col=0)
# train_csv = pd.read_csv('./_data/ddarung/train.csv', index_col=0)
test_csv = pd.read_csv(path + 'test.csv', index_col=0)
submission = pd.read_csv(path + 'submission.csv', index_col=0)

##### 결측치 처리 1. 제거 #####
train_csv = train_csv.dropna()  #null, nan 등의 결측치 삭제 함수
x = train_csv.drop(['count'], axis=1)    #test에는 count가 없어서 맞추기 위해 삭제
y = train_csv['count']

x_train, x_test, y_train, y_test = train_test_split(x, y,
    train_size=0.7, shuffle=True, random_state=123)

#2. 모델구성
model = Sequential()
model.add(Dense(1, input_shape=(9,), activation = 'relu'))
model.add(Dense(50, activation ='relu'))
model.add(Dense(30, activation ='relu'))
model.add(Dense(30, activation ='relu'))
model.add(Dense(20, activation ='relu'))
model.add(Dense(10, activation ='relu'))
model.add(Dense(10, activation ='relu'))
model.add(Dense(1, activation = 'linear'))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')

from tensorflow.keras.callbacks import EarlyStopping
EarlyStopping = EarlyStopping(monitor='val_loss', mode='min',
                patience=10, restore_best_weights=True,
                verbose=1)
# loss, vai_ioss : mode='min'(최소) / accuracy : mode='max'(최대)

hist = model.fit(x_train, y_train, epochs=500, batch_size=32,
          validation_split=0.2, callbacks=[EarlyStopping], verbose=1)  # True = 1 / False = 0

#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

y_predict = model.predict(x_test)
print(y_predict)

from sklearn.metrics import mean_squared_error, r2_score
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
rmse = RMSE(y_test, y_predict)
print("RMSE : ", RMSE(y_test, y_predict))

r2 = r2_score(y_test, y_predict)
print("R2 : ", r2)

loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

print("=====================================")
print(hist)     #<keras.callbacks.History object at 0x00000203493BAAC0>
print("=====================================")
print(hist.history)     # loss와 val_loss의 변화값을 리스트 형태로 보여줌
print("=====================================")
print(hist.history['loss'])
print("=====================================")
print(hist.history['val_loss'])

import matplotlib.pyplot as plt

plt.figure(figsize=(9,6))
plt.plot(hist.history['loss'], c='red', 
         marker='.', label = 'loss')
plt.plot(hist.history['val_loss'], c='blue', 
         marker='.', label = 'val_loss')
plt.grid()
plt.xlabel('epochs')
plt.ylabel('loss')
plt.title('dacon_ddarung loss')
plt.legend()        # 그래프 없는 곳에 라벨 이름 표시
# plt.legend(loc='upper right')        # 위 쪽의 오른쪽에 표시
# plt.legend(loc='upper left')        # 위 쪽의 왼쪽에 표시
plt.show()

#5.제출
y_submit = model.predict(test_csv)
submission['count'] = y_submit

submission.to_csv(path + 'submission_01091622.csv')


"""
1. val_loss : 17490.298828125
2. val_loss : 2709.940673828125
3. val_loss : 15931.8154
4. val_loss : 2497.8748
5. val_loss : 2641.6697
"""