import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rescale=1./255,             
    # 원본 영상은 0-255의 RGB 계수로 구성되는데, 
    # 이 같은 입력값은 모델을 효과적으로 학습시키기에 너무 높음 
    # (통상적인 learning rate를 사용할 경우).
    # 그래서 이를 1/255로 스케일링하여 0-1 범위로 변환. 이는 다른 전처리 과정에 앞서 가장 먼저 적용.
    horizontal_flip=True,   
    # True로 설정할 경우, 50% 확률로 이미지를 수평으로 뒤집음.
    # 원본 이미지에 수평 비대칭성이 없을 때 효과적. 즉, 뒤집어도 자연스러울 때 사용하면 좋음.
    vertical_flip=True,
    width_shift_range=0.1,
    height_shift_range=0.1,
    rotation_range=5,
    zoom_range=1.2,
    shear_range=0.7,
    fill_mode='nearest'
)

test_datagen = ImageDataGenerator(
    rescale=1./255
)

#1. 데이터
xy_train = train_datagen.flow_from_directory(
    './_data/brain/train/',
    # train 속 ad와 normal이 각각 80장씩 / 총 160장 / 150 x 150 / 흑백 
    # x = (160, 150, 150, 1) / y = (160, )
    target_size=(100, 100),
    batch_size=10,
    class_mode='binary',
    color_mode='grayscale',
    shuffle=True,
    # Found 160 images belonging to 2 classes.
)

xy_test = train_datagen.flow_from_directory(
    './_data/brain/test/',
    # test 속 ad와 normal이 각각 60장씩 / 총 120장 / 150 x 150 / 흑백 
    # x = (120, 150, 150, 1) / y = (120, )
    target_size=(100, 100),
    batch_size=10,
    class_mode='binary',
    color_mode='grayscale',
    shuffle=True,
    # Found 120 images belonging to 2 classes.
)


#2. 모델
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten

model = Sequential()
model.add(Conv2D(64, (2,2), input_shape=(100, 100, 1)))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(Conv2D(32, (3,3), activation='relu'))
model.add(Flatten())
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 3. 컴파일, 훈련
model.compile(loss = 'binary_crossentropy', optimizer='adam',
              metrics=['acc'])

hist = model.fit_generator(xy_train, steps_per_epoch=16, epochs=10,
                    validation_data=xy_test,
                    validation_steps=4, )

accuracy = hist.history['acc']
val_acc = hist.history['val_acc']
loss = hist.history['loss']
val_loss = hist.history['val_loss']

print('loss : ', loss[-1])
print('val_loss : ', val_loss[-1])
print('acc : ', accuracy[-1])
print('val_acc : ', val_acc[-1])

# 그림 그리기
import matplotlib.pyplot as plt

plt.figure(figsize=(9,6))
plt.plot(hist.history['loss'], c='red', 
         marker='.', label = 'loss')
plt.plot(hist.history['val_loss'], c='blue', 
         marker='.', label = 'val_loss')
plt.plot(hist.history['acc'], c='yellow', 
         marker='.', label = 'accuracy')
plt.plot(hist.history['val_acc'], c='pink', 
         marker='.', label = 'val_acc')
plt.grid()
plt.xlabel('epochs')
plt.ylabel('loss')
plt.title('fit_generator')
plt.legend()        # 그래프 없는 곳에 라벨 이름 표시
# plt.legend(loc='upper right')        # 위 쪽의 오른쪽에 표시
# plt.legend(loc='upper left')        # 위 쪽의 왼쪽에 표시
plt.show()



