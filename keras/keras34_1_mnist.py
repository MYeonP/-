import numpy as np
from tensorflow.keras.datasets import mnist
"""
path = './_save/'

# 1. 데이터
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape, y_train.shape)     # (60000, 28, 28) (60000,)
print(x_test.shape, y_test.shape)       # (10000, 28, 28) (10000,)

x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(10000, 28, 28, 1)

print(x_train.shape, y_train.shape)     # (60000, 28, 28, 1) (60000,)
print(x_test.shape, y_test.shape)       # (10000, 28, 28, 1) (10000,)

print(np.unique(y_train, return_counts=True))
# (array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=uint8), 
# array([5923, 6742, 5958, 6131, 5842, 5421, 5918, 6265, 5851, 5949], dtype=int64))


# 2. 모델
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten

model = Sequential()
model.add(Conv2D(filters=128, kernel_size=(2,2), input_shape=(28, 28, 1), 
                 activation='relu'))                # (27, 27, 128)
model.add(Conv2D(filters=64, kernel_size=(2,2)))    # (26, 26, 64)
model.add(Conv2D(filters=64, kernel_size=(2,2)))    # (25, 25, 64)
model.add(Flatten())      # (40,000)
model.add(Dense(64, activation='relu'))     # input_shape = (40000, )
                                            # (60000, 40000) = (batch_size, input_dim)
model.add(Dense(32, activation='relu'))
model.add(Dense(10, activation='softmax'))


# 3. 컴파일, 훈련

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam',
              metrics=['acc'])

from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

es = EarlyStopping(monitor='val_loss', mode='min',
                              patience=20, 
                              # restore_best_weights=False,
                              verbose=1)       # loss = mode ='min' / accuracy = mode ='auto'  //restore_best_weights의 defalut값은 False

import datetime
date = datetime.datetime.now()
print(date)     
print(type(date))
date = date.strftime("%m%d_%H%M")   
print(date)
print(type(date))

filepath = './_save/MCP/'
filename = '{epoch:04d}-{val_loss:.4f}.hdf5'


mcp = ModelCheckpoint(monitor='val_loss', mode='auto', verbose=1, 
                      save_best_only=True, 
                     filepath = filepath + 'k34_1_' + date + '_' + filename)



model.fit(x_train, y_train, epochs=1000, batch_size=64,     
        validation_split=0.2, callbacks=[es, mcp], verbose=1)

model.save(path + "keras34_1_mnist_save_model.h5")


# 4. 평가, 예측
results = model.evaluate(x_test, y_test)
print('loss : ', results[0])
print('acc : ', results[1]) 


# es, mcp 적용 / val 적용하기


1. loss :  0.27524417638778687
   acc :  0.9657999873161316
   
2. loss :  0.17468547821044922
   acc :  0.9754999876022339
   


"""





