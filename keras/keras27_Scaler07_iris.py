from sklearn.datasets import load_iris   
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler



#1. 데이터
datasets = load_iris()
# print(datasets.DESCR)      # pandas 에서는 .describe() 혹은 .info()
# print(datasets.feature_names)   #pandas .columns 으로 씀 괄호가 

x = datasets.data
y = datasets['target']
# print(x) 
# print(y)
# print(x.shape, y.shape)   #(150, 4),  (150, ) / y의 값의 개수 만큼 열의 개수가 늘어남

from tensorflow.keras.utils import to_categorical
y = to_categorical(y)      # 원핫 인코딩
print(y)
print(y.shape)  #(150, 3)


x_train, x_test, y_train, y_test = train_test_split(
    x, y, shuffle=True,
    # random_state=333, 
    test_size=0.2, stratify=y)   #false의 문제점은? 
# false 값 : 0~2까지 오름차순으로 정렬 -> 필요 없음!

scaler = MinMaxScaler()
# scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.fit_transform(x_train)
x_tset = scaler.transform(x_test)
# x_train = scaler.transform(x_train)
# x_tset = scaler.transform(x_test)

print(y_train)
print(y_test)


#2. 모델구성
model= Sequential()
model.add(Dense(50, activation='relu', input_shape=(4,)))
model.add(Dense(40, activation='sigmoid'))
model.add(Dense(30, activation='relu'))
model.add(Dense(20, activation='linear'))
model.add(Dense(3, activation='softmax'))
# 다중 분류일 경우 마지막 레이어는 무조건 softmax. / 마지막 노드의 개수는 클래스의 개수와 동일


#3. 컴파일, 훈련
model.compile(loss='categorical_crossentropy', optimizer='adam',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=50, batch_size=1,
          validation_split=0.2, verbose=1)

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


y_test = np.argmax(y_test, axis=1)
print("y_test(원래값) : ", y_test)  #원래값

acc = accuracy_score(y_test, y_predict)
print(acc)

"""
1. MinMaxScaler
loss :  2.721029758453369
accuracy :  0.6666666865348816
accuracy_score :  0.6666666666666666

2. StandardScaler
loss :  0.08037539571523666
accuracy :  0.9666666388511658
accuracy_score :  0.9666666666666667

"""
