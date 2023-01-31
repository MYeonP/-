import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator     #발전기

train_datagen = ImageDataGenerator(
    rescale=1./255,             
    # horizontal_flip=True,   
    # vertical_flip=True,     # 수직 반전
    # width_shift_range=0.1,  # 좌우 이동 -> 0.1 만큼 이동한다
    # height_shift_range=0.1, # 상하 이동 -> 0.1 만큼 이동한다
    # rotation_range=5,       # 회전 -> 5도까지 회전 / 최대 회전 각은 180도
    # zoom_range=1.2,         # 확대 -> 원래 사이즈의 1.2배까지(20%)
    # shear_range=0.7,        # 기울임 -> 0.7도 기울임
    # fill_mode='nearest'     # 빈 자리 채워줌 / nearest : 가장 가까운 값으로 채운다
)

test_datagen = ImageDataGenerator(
    rescale=1./255)
# 테스트 데이터는 rescale만 한다. 왜?
# 테스트 데이터의 목적은 평가하기 위한 데이터이기 때문에 정확한 평가를 위해 증폭하지 않은 원가 데이터를 쓴다.


xy_train = train_datagen.flow_from_directory(
    'D:\\_data\\dogs-vs-cats\\train',  # 폴더 경로 지정
    target_size=(200, 200),  # 이미지 크기 조정 -> 사이즈를 200 x 200으로 지정함
    batch_size=15000,         # pytorch는 batch로 분리후 집어넣는다.
    class_mode='binary',   # 수치형으로 변환
    color_mode='rgb',      # 컬러 사진(RGB)
    shuffle=True,            # 데이터를 섞어줌
)


xy_test = train_datagen.flow_from_directory(
    'D:\\_data\dogs-vs-cats\\test1',
    # test 속 ad와 normal이 각각 60장씩 / 총 120장 / 150 x 150 / 흑백 
    # x = (120, 150, 150, 1) / y = (120, )
    target_size=(200, 200),
    batch_size=2500,
    class_mode='binary',
    color_mode='rgb',
    shuffle=True,
)

print(xy_train)
# Found 37500 images belonging to 3 classes.
# Found 12500 images belonging to 2 classes.
# <keras.preprocessing.image.DirectoryIterator object at 0x000002E864516EE0>

# print(xy_train[0][0].shape)         # (50000, 200, 200, 1)
# print(xy_train[0][1].shape)         # (50000,)
# print(xy_train[0][1])               # y값 출력 [0. 1. 2. 2. 2. 2. 2. 2. 0. 0.]

 
# print(type(xy_train))                # <class 'keras.preprocessing.image.DirectoryIterator'>
# print(type(xy_train[0]))             # <class 'tuple'>  리스트와 동일하다. 튜플은  한번 생성하면 수정이 불가능하다.
# print(type(xy_train[0][0]))          # <class 'numpy.ndarray'> numpy로 변경
# print(type(xy_train[0][1]))          # <class 'numpy.ndarray'> numpy로 변경


np.save('D:\\_data\\dogs-vs-cats\\cat_dog_x_train.npy', arr=xy_train[0][0])
np.save('D:\\_data\\dogs-vs-cats\\cat_dog_y_train.npy', arr=xy_train[0][1])

np.save('D:\\_data\\dogs-vs-cats\\cat_dog_x_test_x.npy', arr=xy_test[0][0])    # x값 저장
np.save('D:\\_data\\dogs-vs-cats\\cat_dog_y_test_y.npy', arr=xy_test[0][1])    # y값 저장
