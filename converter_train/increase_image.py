from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=5,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.05,
        zoom_range=0.01,
        fill_mode='nearest'
        )


def all_new():
    alpha = 'r'
    for j in range (0,26):

        img = load_img('./Braille Dataset/ex/'+alpha+'.png')  # PIL 이미지
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)


        i = 0
        for batch in datagen.flow(x, batch_size=1,
                                  save_to_dir='./Braille Dataset/Braille Dataset2', save_prefix=alpha, save_format='jpg'):
            i += 1
            if i > 20:
                break  # 이미지 20장을 생성하고 마칩니다

        alpha = chr(ord(alpha) + 1)


def single_new(alpha):
    img = load_img('./Braille Dataset/ex/'+alpha+'.png')  # PIL 이미지
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    i = 0
    for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='./Braille Dataset/Braille Dataset2', save_prefix=alpha, save_format='jpg'):
        i += 1
        if i > 10:
         break