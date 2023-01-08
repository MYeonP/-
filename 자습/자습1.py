from keras.models import Sequential
from keras.layers import Dense
import numpy as np

# 데이터
x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([1,2,3,4,5,6,7,8,9,10])

model = Sequential()
model.add(Dense(1, input_dim=1))

model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

model.fit(x, y, epochs=500, batch_size=1)
loss, acc = model.evaluate(x, y, batch_size=1)

print("loss : ", loss)
print("acc : ", acc)

