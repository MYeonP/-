import numpy as np
from sklearn.datasets import load_wine
from tensorflow.keras.models import Sequential, Model 
from tensorflow.keras.layers import Dense, Input  # (Model, Input : 함수형)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler


#1. 데이터
datasets = load_wine()
x = datasets.data
y = datasets.target

print(x.shape, y.shape)     #(178, 13) (178,)
print(y)
print(np.unique(y))     #[0 1 2]
print(np.unique(y, return_counts=True))  # return_counts : array 수를 세어줌
#(array([0, 1, 2]), array([59, 71, 48], dtype=int64)


# from tensorflow.keras.utils import to_categorical
# y = to_categorical(y)      # 원핫 인코딩
# print(y)
# print(y.shape)      # (178, 3)

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

#2. 모델구성
# model= Sequential()
# model.add(Dense(50, activation='relu', input_shape=(13,)))
# model.add(Dense(40, activation='sigmoid'))
# model.add(Dense(30, activation='relu'))
# model.add(Dense(20, activation='linear'))
# model.add(Dense(10, activation='linear'))
# model.add(Dense(3, activation='softmax'))
# 다중 분류일 경우 마지막 레이어는 무조건 softmax. / 마지막 노드의 개수는 클래스의 개수와 동일

#2. 모델구성(함수형)
input1 = Input(shape=(13,))
dense1 = Dense(50, activation = 'relu')(input1)
dense2 = Dense(40, activation = 'sigmoid')(dense1)
dense3 = Dense(30, activation = 'relu')(dense2)
dense4 = Dense(20, activation = 'linear')(dense3)
output1 = Dense(3, activation = 'softmax')(dense4)
model = Model(inputs=input1, outputs=output1)
model.summary()


#3. 컴파일, 훈련
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam',
              metrics=['accuracy'])
# model.fit(x_train, y_train, epochs=1000, batch_size=32,
#           validation_split=0.2, verbose=1)
from tensorflow.keras.callbacks import EarlyStopping
EarlyStopping = EarlyStopping(monitor='val_loss', mode='min',
                patience=30, restore_best_weights=True,
                verbose=1)

hist = model.fit(x_train, y_train, epochs=1000, batch_size=1,
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
print("y_pred(예측값) : ", y_predict)   #예측값

# y_test = np.argmax(y_test, axis=1)
print("y_test(원래값) : ", y_test)  #원래값

acc = accuracy_score(y_test, y_predict)
print(acc)

"""
1. MinMaxScaler
loss :  22.658496856689453
accuracy :  0.3333333432674408
accuracy_score :  0.3333333333333333

2. StandardScaler
loss :  0.0994223803281784
accuracy :  0.9722222089767456
accuracy_score :  0.9722222222222222

"""
