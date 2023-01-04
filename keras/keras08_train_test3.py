import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. 데이터
x = np.array([1,2,3,4,5,6,7,8,9,10])    #(10, )
y = np.array(range(10))   #(10, )

# x_train = x[:7] #[1 2 3 4 5 6 7]
# x_test = x[7:]  #[8 9 10]  #[-3:]
# y_train = y[:7] #[0 1 2 3 4 5 6]
# y_test = y[7:]  #[7 8 9]   #[-3:]

# [검색] train과 test를 섞어서 7:3으로 만들자
# 힌트 : 사이킷런
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, 
    train_size=0.7, 
    #test_size=0.3,     #더 강한 숫자 위주 / 에러일 때 표시 X
    #shuffle=False,     #'True'가 기본값
    random_state=123    #다음에 돌려도 동일한 데이터로 출력
)

print('x_train : ', x_train)  #[ 6  9  4  2  7 10  3]
print('x_test : ', x_test)   #[5 1 8]
print('y_train : ', y_train)  #[5 8 3 1 6 9 2]
print('y_test : ', y_test)   #[4 0 7]


#2. 모델구성
model = Sequential()
model.add(Dense(10, input_dim=1))
model.add(Dense(1))


#3. 컴파일, 훈련
model.compile(loss='mae', optimizer='adam')
model.fit(x_train, y_train, epochs=100, batch_size=1)

#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

result = model.predict([11])
print('[11]의 결과 : ', result)

"""

1. loss : 0.3126288950443268 / [11]의 결과 : [[9.512403]]
2. loss : 0.4827960431575775 / [11]의 결과 : [[9.273046]]
3. loss : 0.013869921676814556 / [11]의 결과 : [[9.983963]]

"""
