from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten

model = Sequential()
                    # input은 (60000, 5, 5, 1)
model.add(Conv2D(filters=10, kernel_size=(2, 2), 
                 # filter=10 -> 필터를 10판으로 늘린다
                 input_shape=(5, 5, 1)))    # 5x5의 필터를 1장 가지고 있다 / # (N, 4, 4, 10)
                 # (batch_size, rows, column, channels)
model.add(Conv2D(5, (2, 2)))     # (N, 3, 3, 5)
# = model.add(Conv2D(filters=5, kernel_size=(2,2)))

model.add(Flatten())        # (N, 45)
model.add(Dense(units=10))        # (N, 10)
        # input은 (batch_size, input_dim)
model.add(Dense(4, activation = 'relu'))         # (N, 1)
model.summary()

