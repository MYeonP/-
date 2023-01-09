from sklearn.datasets import load_breast_cancer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from sklearn.model_selection import train_test_split

#1. 데이터
datasets = load_breast_cancer()
# print(datasets)
# print(datasets.DESCR)
# print(datasets.feature_names)

x = datasets['data']
y = datasets['target']
# print(x.shape, y.shape)     #(569, 30) (569,)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, shuffle=True, random_state=333, test_size=0.2)

#2. 모델 구성
model = Sequential()
model.add(Dense(50, activation='linear', input_shape=(30,)))
model.add(Dense(40, activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#3. 컴파일, 훈련
model.compile(loss='binary_crossentropy', optimizer='adam',
              metrics=['accuracy'])

from tensorflow.keras.callbacks import EarlyStopping
# EarlyStopping = EarlyStopping(monitor='val_loss', mode='min',
EarlyStopping = EarlyStopping(monitor='val_loss', mode='min',
                patience=20, restore_best_weights=True,
                verbose=1)
model.fit(x_train, y_train, epochs=10000, batch_size=16,
          validation_split=0.2, callbacks=[EarlyStopping],
          verbose=1)


#4. 평가, 예측
# loss = model.evaluate(x_test, y_test)
# print('loss, accuracy : ', loss)
loss, accuracy = model.evaluate(x_test, y_test)
print('loss : ', loss)
print('accuracy :', accuracy)
 
y_predict = model.predict(x_test)
print(y_predict)

y_predict_2 = np.where(y_predict >= 0.5, 1 , 0)
# np.where(condition, T, F) 값 변경
print(y_predict_2)

from sklearn.metrics import r2_score, accuracy_score
acc = accuracy_score(y_test, y_predict_2)
print("accuracy_score : ", acc)

"""
1. accuracy_score :  0.9473684210526315

"""


"""
# loss = model.evaluate(x_test, y_test)
# print('loss, accuracy : ', loss)

loss, accuracy = model.evaluate(x_test, y_test)
print('loss : ', loss)
print('accuracy : ', accuracy)

y_predict = model.predict(x_test)
intarr = list(map(int, y_predict))
print(intarr[:10])   # Q1. 정수형으로 바꿔라
print(y_test[:10])

from sklearn.metrics import r2_score, accuracy_score
acc = accuracy_score(y_test, intarr)
print("accuracy_score : ", acc)     # Q2. accuracy_score 확인
"""