import numpy as np
from sklearn.datasets import fetch_covtype
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler


#1. 데이터
datasets = fetch_covtype()
x = datasets.data
y = datasets['target']

print(x.shape, y.shape)     # (581012, 54) (581012,)
print(np.unique(y, return_counts=True))
# (array([1, 2, 3, 4, 5, 6, 7]), 
# array([211840, 283301,  35754,   2747,   9493,  17367,  20510], dtype=int64))


########## 1. keras categorical ##########
# from tensorflow.keras.utils import to_categorical
# y = to_categorical(y)      # 원핫 인코딩
# print(y.shape)      # (581012, 8)
# print(type(y))      # <class 'numpy.ndarray'>
# print(y[:10])
# print(np.unique(y[:,0], return_counts=True))    # [:,0] -> 모든 행의 0번째
# # (array([0.], dtype=float32), array([581012], dtype=int64))
# print(np.unique(y[:,1], return_counts=True))

# print("======================================")
# y = np.delete(y, 0, axis=1)
# print(y.shape)
# print(y[:10])
# print(np.unique(y[:,0], return_counts=True))


########## 2. pandas get_dummies ##########
# import pandas as pd
# y = pd.get_dummies(y)
# print(y[:10])
# print(type(y))  # <class 'pandas.core.frame.DataFrame'>
# # y = y.values
# # print(type(y))  # <class 'numpy.ndarray'>

# y = y.to_numpy()
# print(type(y))  # <class 'numpy.ndarray'>
# print(y.shape)  # (581012, 7)


# 데이터의 형태는 pandas의 데이터 프레임 형태.
# np.argmax(넘파이 자료형)이 판다스를 바로 못 받아들임 -> 평가(훈련 결과) 에서 오류 발생!
# y_test = np.argmax(y_test, axis=1) -> y_test는 계속 판다스 상태


########## 3. sklearn One-Hot encordinng ##########
print(y.shape)  # (581012,) -> 1D(1차원 형태)
y = y.reshape(581012, 1)   # (581012,) -> (581012, 1)로 2D(2차원 형태)로 바꾼다(reshape)
print(y.shape)  # (581012, 1)

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder()
ohe.fit(y)   # fit : 실행시키다 / y를 OneHotEncoder 시키겠다.
# y = ohe.transform(y)
y = ohe.fit_transform(y)    # # y = ohe.transform(y)과 동일
# TypeError: A sparse matrix was passed, but dense data is required. 
# Use X.toarray() to convert to a dense numpy array.
y = y.toarray()
# 그래서 .toarray() 함수로 numpy array 형태로 전환!

print(y[:15])
print(type(y))  # <class 'scipy.sparse._csr.csr_matrix'>
print(y.shape)  # (581012, 7)



x_train, x_test, y_train, y_test = train_test_split(
    x, y, shuffle=True,
    test_size=0.2, stratify=y)  # stratify=y / 균형을 맞춰준다(yes)

scaler = MinMaxScaler()
# scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.fit_transform(x_train)
x_tset = scaler.transform(x_test)
# x_train = scaler.transform(x_train)
# x_tset = scaler.transform(x_test)

# import matplotlib.pyplot as plt
# plt.gray()
# plt.matshow(datasets.images[5])
# plt.show()

#2. 모델구성
model= Sequential()
model.add(Dense(50, activation='relu', input_shape=(54,)))
model.add(Dense(40, activation='sigmoid'))
model.add(Dense(30, activation='relu'))
model.add(Dense(20, activation='linear'))
model.add(Dense(7, activation='softmax'))
# 다중 분류일 경우 마지막 레이어는 무조건 softmax. / 마지막 노드의 개수는 클래스의 개수와 동일


#3. 컴파일, 훈련
from tensorflow.keras.callbacks import EarlyStopping
EarlyStopping = EarlyStopping(monitor='val_loss', mode='min',
                patience=5, restore_best_weights=True,
                verbose=1)

model.compile(loss='categorical_crossentropy', optimizer='adam',
              metrics=['accuracy'])
# model.fit(x_train, y_train, epochs=100, batch_size=64,
#           validation_split=0.2, verbose=1)

hist = model.fit(x_train, y_train, epochs=50, batch_size=64,
          validation_split=0.2, callbacks=[EarlyStopping], verbose=1)

#4. 평가, 예측
loss, accuracy = model.evaluate(x_test, y_test)
print('loss : ', loss)
print('accuracy : ', accuracy)

print(y_test[:5])
y_predict = model.predict(x_test[:10])
# print(y_predict)

from sklearn.metrics import accuracy_score
import numpy as np
y_predict = model.predict(x_test)
y_predict = np.argmax(y_predict, axis=1)
print("y_pred(예측값) : ", y_predict[:20])   #예측값

y_test = np.argmax(y_test, axis=1)
print("y_test(원래값) : ", y_test[:20])  #원래값

acc = accuracy_score(y_test, y_predict)
print(acc)

