import numpy as np
from sklearn.datasets import load_digits
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

#1. 데이터
datasets = load_digits()
x = datasets.data
y = datasets['target']
print(x.shape, y.shape)     # (1797, 64) (1797, ) / 64 = 8*8*1(흑백)
print(np.unique(y, return_counts=True))
# (array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 
# array([178, 182, 177, 183, 181, 182, 181, 179, 174, 180], dtype=int64))

import matplotlib.pyplot as plt
plt.gray()
plt.matshow(datasets.images[5])
plt.show()

from tensorflow.keras.utils import to_categorical
y = to_categorical(y)      # 원핫 인코딩
print(y)
print(y.shape)   # (1797, 10)


x_train, x_test, y_train, y_test = train_test_split(
    x, y, shuffle=True,
    test_size=0.2, stratify=y)  # stratify=y / 균형을 맞춰준다(yes)

#2. 모델구성
model= Sequential()
model.add(Dense(50, activation='relu', input_shape=(64,)))
model.add(Dense(40, activation='sigmoid'))
model.add(Dense(30, activation='relu'))
model.add(Dense(20, activation='linear'))
model.add(Dense(10, activation='softmax'))
# 다중 분류일 경우 마지막 레이어는 무조건 softmax. / 마지막 노드의 개수는 클래스의 개수와 동일


#3. 컴파일, 훈련
model.compile(loss='categorical_crossentropy', optimizer='adam',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=1000, batch_size=32,
          validation_split=0.2, verbose=1)

from tensorflow.keras.callbacks import EarlyStopping
EarlyStopping = EarlyStopping(monitor=['accuracy'], mode='max',
                patience=10, restore_best_weights=True,
                verbose=1)

hist = model.fit(x_train, y_train, epochs=300, batch_size=32,
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

y_test = np.argmax(y_test, axis=1)
print("y_test(원래값) : ", y_test)  #원래값

acc = accuracy_score(y_test, y_predict)
print(acc)



   
