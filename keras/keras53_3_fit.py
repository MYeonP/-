import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rescale=1./255,             
    # 이미지의 RGB 값이 0~255 값으로 표현되는데, 0~1 값으로 바꿔준다. 
    # 이 같은 입력값은 모델을 효과적으로 학습시키기에 너무 높음 
    # (통상적인 learning rate를 사용할 경우).
    # 그래서 이를 1/255로 스케일링하여 0-1 범위로 변환. 이는 다른 전처리 과정에 앞서 가장 먼저 적용.
    horizontal_flip=True,   
    # True로 설정할 경우, 50% 확률로 이미지를 수평으로 뒤집음.
    # 원본 이미지에 수평 비대칭성이 없을 때 효과적. 즉, 뒤집어도 자연스러울 때 사용하면 좋음.
    vertical_flip=True,     # 수직 반전
    width_shift_range=0.1,  # 좌우 이동 -> 0.1 만큼 이동한다
    height_shift_range=0.1, # 상하 이동 -> 0.1 만큼 이동한다
    rotation_range=5,       # 회전 -> 5도까지 회전 / 최대 회전 각은 180도
    zoom_range=1.2,         # 확대 -> 원래 사이즈의 1.2배까지(20%)
    shear_range=0.7,        # 기울임 -> 0.7도 기울임
    fill_mode='nearest'     # 빈 자리 채워줌 / nearest : 가장 가까운 값으로 채운다
)

test_datagen = ImageDataGenerator(
    rescale=1./255      # 이미지의 RGB 값이 0~255 값으로 표현되는데, 0~1 값으로 바꿔준다.
)

    # train 속 ad와 normal이 각각 80장씩 / 총 160장 / 150 x 150 / 흑백 
    # x = (160, 150, 150, 1) / y = (160, )



#1. 데이터
xy_train = train_datagen.flow_from_directory(
    './_data/brain/train/',  # 폴더 경로 지정
    target_size=(100, 100),  # 이미지 크기 조정 -> 사이즈를 100 x 100으로 지정함
    batch_size=1000,         # pytorch는 batch로 분리후 집어넣는다.
    class_mode='binary',     # 수치형으로 변환
    color_mode='grayscale',  # 흑백으로 변환
    shuffle=True,            # 데이터를 섞어줌
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
                 epochs=200,
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
loss :  2.269119477205095e-06
val_loss :  2.94580078125
acc :  1.0
val_acc :  0.6000000238418579


loss :  1.7273862340516644e-07
val_loss :  1.024712085723877
acc :  1.0
val_acc :  0.800000011920929

"""


