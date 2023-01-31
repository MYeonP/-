import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rescale=1./255,             
    # 이미지의 RGB 값이 0~255 값으로 표현되는데, 0~1 값으로 바꿔준다. 
    # 이 같은 입력값은 모델을 효과적으로 학습시키기에 너무 높음 
    # (통상적인 learning rate를 사용할 경우).
    # 그래서 이를 1/255로 스케일링하여 0-1 범위로 변환. 이는 다른 전처리 과정에 앞서 가장 먼저 적용.
    # horizontal_flip=True,   
    # # True로 설정할 경우, 50% 확률로 이미지를 수평으로 뒤집음.
    # # 원본 이미지에 수평 비대칭성이 없을 때 효과적. 즉, 뒤집어도 자연스러울 때 사용하면 좋음.
    # vertical_flip=True,     # 수직 반전
    # width_shift_range=0.1,  # 좌우 이동 -> 0.1 만큼 이동한다
    # height_shift_range=0.1, # 상하 이동 -> 0.1 만큼 이동한다
    # rotation_range=5,       # 회전 -> 5도까지 회전 / 최대 회전 각은 180도
    # zoom_range=1.2,         # 확대 -> 원래 사이즈의 1.2배까지(20%)
    # shear_range=0.7,        # 기울임 -> 0.7도 기울임
    # fill_mode='nearest'     # 빈 자리 채워줌 / nearest : 가장 가까운 값으로 채운다
)

test_datagen = ImageDataGenerator(
    rescale=1./255      # 이미지의 RGB 값이 0~255 값으로 표현되는데, 0~1 값으로 바꿔준다.
)

    # train 속 ad와 normal이 각각 80장씩 / 총 160장 / 150 x 150 / 흑백 
    # x = (160, 150, 150, 1) / y = (160, )



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
# <keras.preprocessing.image.DirectoryIterator object at 0x0000022056E55400>

# from sklearn.datasets import load_iris
# datasets = load_iris()
# print(datasets)

# print(xy_train[0])
# print(xy_train[0][0])
print(xy_train[0][0].shape)         # (160, 200, 200, 1)
print(xy_train[0][1])               # y값 출력  [0. 0. 1. 1. 1.]
print(xy_train[0][1].shape)         # (160, )

# print(type(xy_train))                # <class 'keras.preprocessing.image.DirectoryIterator'>
# print(type(xy_train[0]))             # <class 'tuple'>  리스트와 동일하다. 튜플은 한번 생성하면 수정이 불가능하다.
# print(type(xy_train[0][0]))          # <class 'numpy.ndarray'> numpy로 변경
# print(type(xy_train[0][1]))          # <class 'numpy.ndarray'> numpy로 변경

np.save('./_data/brain/brain_x_train.npy', arr=xy_train[0][0])
np.save('./_data/brain/brain_y_train.npy', arr=xy_train[0][1])
# np.save('./_data/brain/brain_xy_train.npy', arr=xy_train[0])

np.save('./_data/brain/brain_x_test.npy', arr=xy_test[0][0])
np.save('./_data/brain/brain_y_test.npy', arr=xy_test[0][1])



