import numpy as np
x_datasets = np.array([range(100), range(301, 401)]).transpose()
print(x_datasets.shape)    # (100, 2) / 위에서 바로 transpose(치환)해 줌
# 삼성전자 시가, 고가


y1 = np.array(range(2001, 2101)) #(100, )    # 삼성전자의 하루 뒤 종가 예측
y2 = np.array(range(201, 301)) #(100, )      # 아모레의 하루 뒤 종가 예측


from sklearn.model_selection import train_test_split
x_train, x_test, y1_train, y1_test, y2_train, y2_test = train_test_split(
    x_datasets, y1, y2, train_size=0.7, random_state=1234
)

# 파이썬 코드가 너무 길 경우, 역슬래시를 이용해 코드 작성이 가능하다
# 예시 : def test_function(  \
#       long_long_long_param1, \
#       long_long_long_param2, \
#       long_long_long_param3, \
#       ):

print(x_train.shape, y1_train.shape, y2_train.shape)
# (70, 2) (70,) (70,)
print(x_test.shape, y1_test.shape, y2_test.shape)
# (30, 2) (30,) (30,)



# 2. 모델구성
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input

# 2-1. 모델 1
input1 = Input(shape=(2, ))
dense1 = Dense(11, activation='relu', name='ds11')(input1)
dense2 = Dense(12, activation='relu', name='ds12')(dense1)
dense3 = Dense(13, activation='relu', name='ds13')(dense2)
output1 = Dense(14, activation='relu', name='ds14')(dense3)

# # 2-2. 모델 2
# input2 = Input(shape=(3, ))
# dense21 = Dense(21, activation='linear', name='ds21')(input2)
# dense22 = Dense(22, activation='linear', name='ds22')(dense21)
# output2 = Dense(23, activation='linear', name='ds23')(dense22)

# # 2-3. 모델 3
# input3 = Input(shape=(2, ))
# dense31 = Dense(31, activation='linear', name='ds31')(input3)
# dense32 = Dense(32, activation='linear', name='ds32')(dense31)
# output3 = Dense(33, activation='linear', name='ds33')(dense32)

# 2-4. 모델 병합
from tensorflow.keras.layers import concatenate     # concatenate : 사슬처럼 엮다 / 붙였다, 연결했다
merge1 = concatenate([output1], name='mg1')
merge2 = Dense(12, activation='relu', name='mg2')(merge1)
merge3 = Dense(13, name='mg3')(merge2)
last_output = Dense(1, name='last')(merge3)

# # 2-5. 모델 5 분기1.
# dense5 = Dense(31, activation='linear', name='ds51')(last_output)
# dense5 = Dense(32, activation='linear', name='ds52')(dense5)
# output5 = Dense(33, activation='linear', name='ds53')(dense5)

# # 2-6. 모델 6 분기1.
# dense6 = Dense(31, activation='linear', name='ds61')(last_output)
# dense6 = Dense(32, activation='linear', name='ds62')(dense6)
# output6 = Dense(33, activation='linear', name='ds63')(dense6)

model = Model(inputs=[input1], outputs=[last_output])


model.summary()

# 3.  컴파일, 훈련
model.compile(loss = 'mse', optimizer='adam')
model.fit([x_train], [y1_train, y2_train], epochs=300, batch_size=32)

# 4.평가
loss = model.evaluate([x_test], [y1_test, y2_test])
print('loss : ', loss)

"""

loss :  554.111083984375

"""
