from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from sklearn.model_selection import train_test_split

#1. 데이터
x = np.array(range(1,21))
y = np.array([1,2,4,3,5,7,9,3,8,12,13,8,14,15,9,6,17,23,21,20])

x_train, x_test, y_train, y_test = train_test_split(x, y,
    train_size=0.7, shuffle=True, random_state=123
    )

#2. 모델구성
model = Sequential()
model.add(Dense(10, input_dim=1))
model.add(Dense(10))
model.add(Dense(10))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam', metrics=['mae']) 
model.fit(x_train, y_train, epochs=100, batch_size=1)

#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

y_predict = model.predict(x_test)

print("==================")
print(y_test)
print(y_predict)
print("==================")


from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
    # 돌려줘(출력) mse에 루트를 씌워라 ( 여기가 mse 부분 )

print("RMSE : ", RMSE(y_test, y_predict))

#RMSE :  3.8629822962660154
#RMSE :  3.889354504586169
#RMSE :  3.8425668612122874  *가장 좋은 결과값을 빼서 사용


"""
 ValueError: Unknown loss function: rmse. *loss에는 rmse가 없다
 Please ensure this object is passed to the `custom_objects` argument. 
 See https://www.tensorflow.org/guide/keras/save_and_serialize#registering_the_custom_object for details.
 
 Traceback (most recent call last):
  File "c:\study\keras\keras12_rmse.py", line 23, in <module> *최상단 최초의 에러 지점
 
 -> 에러 발생시 하단 라인 확인 및 최상단 에러 내용 확인
 """