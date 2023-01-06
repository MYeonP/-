import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

# 1. 데이터
datasets = fetch_california_housing()
x = datasets.data
y = datasets.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    train_size=0.7
)

'''
Result
print(x.shape)
print(y.shape)
print(dataset.feature_names)
['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT']
print(dataset.DESCR)
DataSet Descripiton
'''


#2. 모델구성
model = Sequential()
model.add(Dense(10, input_dim=8, activation = 'relu'))
model.add(Dense(20, activation ='relu'))
model.add(Dense(30, activation ='relu'))
model.add(Dense(40, activation ='relu'))
model.add(Dense(20, activation ='relu'))
model.add(Dense(10, activation ='relu'))
model.add(Dense(10, activation ='relu'))
model.add(Dense(1, activation = 'linear'))


# 3. 컴파일, 훈련
import time
model.compile(loss='mse', optimizer = 'adam', metrics=['mae'])

start = time.time()
model.fit(x_train, y_train, epochs=100, batch_size=32, validation_split=0.25)
end = time.time()



# 4. 평가, 예측
loss = model.evaluate(x_test, y_test)   # test 데이터로 평가
print("loss: ", loss)

y_predict = model.predict(x_test)   # 최적의 가중치
# print("============")
# print(y_test)
# print(y_predict)
# print("============")

from sklearn.metrics import mean_squared_error, r2_score
def RMSE (y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE: ", RMSE(y_test, y_predict))

r2 = r2_score(y_test, y_predict)
print("R2: ", r2)
print("소요 시간: ", end - start)



"""
1. R2 :  0.5430312595296418
2. R2 :  0.5195147824443711
3. R2 :  0.5256790471852559
4. R2 :  0.5308637038368442
5. R2 :  0.5453362142711884
6. R2 :  0.5778417890480458     train_size=0.9, random_state=65
7. R2 :  0.5981663634394601

cpu 걸린시간 : 136.5838577747345
GPU 걸린시간 : 

"""