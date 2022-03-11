import numpy as np

if str1[i] == '\n':
    img_file = 'C:/Users/kim98/PycharmProjects/AI_project/converter_train/ex/zz.png'
    img2 = cv2.imread(img_file, 1)
    add_image = np.hconcat(img1, img2)
    cv2.imwrite('./image_saved/%d.png' % j, add_image)
    img1 = cv2.imread(img_file, 1)
elif str1[i] == ' ' or str1[i] == '.':
    img_file = 'C:/Users/kim98/PycharmProjects/AI_project/converter_train/ex/zz.png'
    img2 = cv2.imread(img_file, 1)
    add_image = np.hconcat(img1, img2)
    img1 = add_image
else:
    img_file = 'C:/Users/kim98/PycharmProjects/AI_project/converter_train/ex/' + str1[i] + '.png'
    img2 = cv2.imread(img_file, 1)
    add_image = np.hconcat(img1, img2)
    img1 = add_image

    if str1[num2] == '\n':
        print(num2)
        if length[j] == 1:
            image1 = Image.open('C:/Users/kim98/PycharmProjects/AI_project/converter_train/ex/zz.png')
            image1 = image1.resize((97, 107))
            image1.save("C:/Users/kim98/PycharmProjects/AI_project/image_saved/conversion_image%d.jpg" % j, "JPEG")
        if Max_leg == length[j][0]:
            print('%d time done' % j)
            image1 = Image.open('C:/Users/kim98/PycharmProjects/AI_project/converter_train/ex/' + str1[num2] + '.png')
            image1 = image1.resize((97, 107))
            image1.save("C:/Users/kim98/PycharmProjects/AI_project/image_saved/conversion_image%d.jpg" % j, "JPEG")
        elif Max_leg[0] > length[j][0]:
            print('%d time done' % j)
            image1 = Image.open('C:/Users/kim98/PycharmProjects/AI_project/converter_train/ex/' + str1[num2] + '.png')
            image1 = image1.resize((97, 107))
            image1.save("C:/Users/kim98/PycharmProjects/AI_project/image_saved/conversion_image%d.jpg" % j, "JPEG")
        j = j + 1
        times = 1