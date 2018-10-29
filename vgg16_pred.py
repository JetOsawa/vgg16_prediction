


from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
import sys
import os


#�K�w�̊m�F
os.getcwd()


#�t�@�C���p�X�̎w��
#�o�͂�True�ɂȂ��OK
filename = "./Pictures/Camera Roll/***.jpg"
print(os.path.exists(filename))


# �w�K�ς݂�VGG16�����[�h
# �\���ƂƂ��Ɋw�K�ς݂̏d�݂��ǂݍ��܂��
model = VGG16(weights='imagenet')
# model.summary()

# �����Ŏw�肵���摜�t�@�C����ǂݍ���
# �T�C�Y��VGG16�̃f�t�H���g�ł���224x224�Ƀ��T�C�Y�����
img = image.load_img(filename, target_size=(224, 224))

# �ǂݍ���PIL�`���̉摜��array�ɕϊ�
x = image.img_to_array(img)

# 3�����e���\���irows, cols, channels) ��
# 4�����e���\�� (samples, rows, cols, channels) �ɕϊ�
# ���͉摜��1���Ȃ̂�samples=1�ł悢
x = np.expand_dims(x, axis=0)

# Top-5�̃N���X��\������
# VGG16��1000�N���X��decode_predictions()�ŕ�����ɕϊ������
preds = model.predict(preprocess_input(x))
results = decode_predictions(preds, top=5)[0]
for result in results:
    print(result)