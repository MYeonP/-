from sklearn.datasets import load_iris   
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split


#1. 데이터
datasets = load_iris()
# print(datasets.DESCR)      # pandas 에서는 .describe() 혹은 .info()
# print(datasets.feature_names)   #pandas .columns 으로 씀 괄호가 

x = datasets.data
y = datasets['target']
# print(x) 
# print(y)
# print(x.shape, y.shape)   #(150, 4),  (150, ) / y의 값의 개수 만큼 열의 개수가 늘어남

# from tensorflow.keras.utils import to_categorical
# y = to_categorical(y)      # 원핫 인코딩
# print(y)
# print(y.shape)  #(150, 3)


x_train, x_test, y_train, y_test = train_test_split(
    x, y, shuffle=True,
    # random_state=333, 
    test_size=0.2, stratify=y)   #false의 문제점은? 
# false 값 : 0~2까지 오름차순으로 정렬 -> 필요 없음!

print(y_train)
print(y_test)


#2. 모델구성
model= Sequential()
model.add(Dense(50, activation='relu', input_shape=(4,)))
model.add(Dense(40, activation='sigmoid'))
model.add(Dense(30, activation='relu'))
model.add(Dense(20, activation='linear'))
model.add(Dense(3, activation='softmax'))
# 다중 분류일 경우 마지막 레이어는 무조건 softmax. / 마지막 노드의 개수는 y의 클래스의 개수와 동일
# 원한 했을 때 나오는 숫자로 노드 개수 넣어주기


#3. 컴파일, 훈련
from tensorflow.keras.callbacks import EarlyStopping
EarlyStopping = EarlyStopping(monitor='val_loss', mode='min',
                patience=5, restore_best_weights=True,
                verbose=1)

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam',
              metrics=['accuracy'])

# model.fit(x_train, y_train, epochs=50, batch_size=1,
#           validation_split=0.2, verbose=1)

hist = model.fit(x_train, y_train, epochs=100, batch_size=1,
          validation_split=0.2, callbacks=[EarlyStopping], verbose=1)

#4. 평가, 예측
loss, accuracy = model.evaluate(x_test, y_test)
print('loss : ', loss)
print('accuracy : ', accuracy)

print(y_test[0:5])
y_predict = model.predict(x_test[0:10])
# print(y_predict)

from sklearn.metrics import accuracy_score
import numpy as np
y_predict = model.predict(x_test)
y_predict = np.argmax(y_predict, axis=1)
print("y_pred(예측값) : ", y_predict)   #예측값

# print(y_test.shape) # (30,)
# print(y_predict.shape) # (30,)
# print(type(y_test), type(y_predict)) 
# print(y_test[:10], y_predict[:10]) 


# y_test = np.argmax(y_test, axis=1)   # y_test는 원핫을 안 했기 때문에 argmax 할 필요 없음
print("y_test(원래값) : ", y_test)  #원래값

acc = accuracy_score(y_test, y_predict)
print(acc)


"""
loss :  0.10701935738325119
accuracy :  0.9666666388511658
[2 0 0 1 1]
y_pred(예측값) :  [2 0 0 1 1 0 1 1 2 2 1 0 2 0 0 2 2 2 1 2 1 2 2 0 1 0 0 2 0 1]
y_test(원래값) :  [2 0 0 1 1 0 1 1 2 2 1 0 2 0 0 2 2 2 1 2 1 2 1 0 1 0 0 2 0 1]
0.9666666666666667

loss :  0.011658295057713985
accuracy :  1.0
[0 1 0 0 0]
y_pred(예측값) :  [0 1 0 0 0 1 1 0 1 1 0 2 2 2 2 0 2 2 2 0 1 1 1 2 2 0 1 0 2 1]
y_test(원래값) :  [0 1 0 0 0 1 1 0 1 1 0 2 2 2 2 0 2 2 2 0 1 1 1 2 2 0 1 0 2 1]
1.0

loss :  0.04239465668797493
accuracy :  1.0
[1 1 0 0 0]
y_pred(예측값) :  [1 1 0 0 0 1 2 0 0 0 1 2 1 1 2 1 1 2 0 2 2 0 2 1 1 2 0 0 2 2]
y_test(원래값) :  [1 1 0 0 0 1 2 0 0 0 1 2 1 1 2 1 1 2 0 2 2 0 2 1 1 2 0 0 2 2]
1.0
"""