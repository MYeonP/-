import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rescale=1./255)

test_datagen = ImageDataGenerator(
    rescale=1./255)


# np.save('./_data/brain/brain_x_train.npy', arr=xy_train[0][0])
# np.save('./_data/brain/brain_y_train.npy', arr=xy_train[0][1])
# # np.save('./_data/brain/brain_xy_train.npy', arr=xy_train[0])

# np.save('./_data/brain/brain_x_test.npy', arr=xy_test[0][0])
# np.save('./_data/brain/brain_y_test.npy', arr=xy_test[0][1])

x_train = np.load('./_data/brain/brain_x_train.npy')
y_train = np.load('./_data/brain/brain_y_train.npy')
x_test = np.load('./_data/brain/brain_x_test.npy')
y_test = np.load('./_data/brain/brain_y_test.npy')

print(x_train.shape, x_test.shape)  # (160, 200, 200, 1) (120, 200, 200, 1)
print(y_train.shape, y_test.shape)  # (160,) (120,)
# print(x_train[100]) 

xy_train = train_datagen.flow_from_directory(
    './_data/brain/train/',  # 폴더 경로 지정
    target_size=(200, 200),  # 이미지 크기 조정 -> 사이즈를 200 x 200으로 지정함
    batch_size=10000,         # pytorch는 batch로 분리후 집어넣는다.
    # class_mode='categorical',     # 원핫 형태로 변환
    class_mode='binary',     # 수치형으로 변환
    color_mode='grayscale',  # 흑백으로 변환
    shuffle=True,            # 데이터를 섞어줌
    # Found 160 images belonging to 2 classes.
)


xy_test = train_datagen.flow_from_directory(
    './_data/brain/test/',
    # test 속 ad와 normal이 각각 60장씩 / 총 120장 / 150 x 150 / 흑백 
    # x = (120, 150, 150, 1) / y = (120, )
    target_size=(200, 200),
    batch_size=10000,
    # class_mode='categorical',
    class_mode='binary',     # 수치형으로 변환
    color_mode='grayscale',
    shuffle=True,
    # Found 120 images belonging to 2 classes.
)
print(xy_train)


# 2. 모델구성

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten

model = Sequential()
model.add(Conv2D(64, (2,2), input_shape=(200, 200, 1)))
model.add(Conv2D(128, (3,3), activation='relu'))
model.add(Conv2D(128, (3,3), activation='relu'))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(Conv2D(32, (3,3), activation='relu'))
model.add(Flatten())
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))   # 0과 1 / softmax쓰려면 2가 되어야함

# 3. 컴파일, 훈련
model.compile(loss = 'binary_crossentropy', optimizer='adam',
              metrics=['acc'])

# hist = model.fit_generator(xy_train, steps_per_epoch=16, epochs=10,
#                     validation_data=xy_test,
#                     validation_steps=4, )

hist = model.fit(xy_train[0][0], xy_train[0][1], 
                 batch_size=16,
                 # steps_per_epoch=16, 
                 epochs=100,
                 validation_data=(xy_test[0][0], xy_test[0][1])
                # validation_steps=4, 
)

accuracy = hist.history['acc']
val_acc = hist.history['val_acc']
loss = hist.history['loss']
val_loss = hist.history['val_loss']

print('loss : ', loss[-1])  # 훈련의 마지막 값을 얻기 위해 [-1]
print('val_loss : ', val_loss[-1])
print('acc : ', accuracy[-1])
print('val_acc : ', val_acc[-1])

# 그림 그리기


import matplotlib.pyplot as plt 
plt.figure(figsize=(9,6))
plt.plot(hist.history['loss'], c='red', marker='.', label='loss')          #list 형태는 그냥 넣어줘도됨
plt.plot(hist.history['val_loss'], c='blue', marker='.', label='val_loss')
# plt.plot(hist.history['accuracy'], c='green', marker='.', label='accuracy')
plt.plot(hist.history['val_acc'], c='black', marker='.', label='val_acc')
plt.grid() 
plt.title('fit_generator')
plt.legend(loc='upper left')
plt.show()



"""

loss :  5.7467486840323545e-06
val_loss :  0.04186262562870979
acc :  1.0
val_acc :  0.9916666746139526


"""





