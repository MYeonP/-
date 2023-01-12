
from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.layers import Dense, Input  # (Model, Input : 함수형)
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler

#1. 데이터
datasets = load_boston()
x = datasets.data
y = datasets['target'] 

x_train, x_test, y_train, y_test = train_test_split(x, y,
    train_size=0.7, shuffle=True, random_state=123)

scaler = MinMaxScaler()
# scaler = StandardScaler()
scaler.fit(x_train)
# x_train = scaler.fit_transform(x_train)
# x_tset = scaler.transform(x_test)
x_train = scaler.transform(x_train)
x_tset = scaler.transform(x_test)


print(x)
print(type(x))  # <class 'numpy.ndarray'>

# print("최소값 : ", np.min(x))
# print("최대값 : ",np.max(x))


# print(x)
# print(x.shape)  # (506, 13)
# print(y)
# print(y.shape)  # (506,)

# print(dataset.feature_names)
# # ['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT']
# print(dataset.DESCR)


#2. 모델구성(함수형)


path = './_save/'
# path = '../_save/'
# path = 'c:/study/_save/'

# model.save(path + 'keras29_1_save_model.h5')
# model.save('./_save/keras29_1_save_model.h5')

model = load_model(path + 'keras29_3_save_model.h5')
model.summary()



#3. 컴파일, 훈련


#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

y_predict = model.predict(x_test)

def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))

print("RMSE : ", RMSE(y_test, y_predict))

r2 = r2_score(y_test, y_predict)
print("R2 : ", r2)

"""

MinMaxScaler
loss :  6758.6201171875
RMSE :  7244.290064453451
R2 :  -715627.4085768127

StandardScaler
loss :  2.379150629043579
RMSE :  3.740777006497933
R2 :  0.8091819075834242

"""

