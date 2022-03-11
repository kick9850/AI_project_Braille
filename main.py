import hgtk.letter
from PIL import Image
import pytesseract
import converter
import numpy as np
from matplotlib import pyplot as plt

#mode kor , eng, all
#language = 'kor2'
#language = 'all'
language = 'eng'
# image text conversion test
pytesseract.pytesseract.tesseract_cmd = R'C:\Program Files\Tesseract-OCR\tesseract'
str1 = pytesseract.image_to_string(Image.open('c:/Users/kim98/PycharmProjects/AI_project/eng_test.png'), lang= language)
#str1 = pytesseract.image_to_string(Image.open('c:/Users/kim98/PycharmProjects/AI_project/kor_test2.JPG'), lang= language)
#str1 = pytesseract.image_to_string(Image.open('c:/Users/kim98/PycharmProjects/AI_project/kor_Test.jpg'), lang=language)
#str1 = pytesseract.image_to_string(Image.open('c:/Users/kim98/PycharmProjects/AI_project/eng_test.png'), lang=language)

#conversion result
print(str1)
if language == 'kor2' or language == 'all':
    str1 = hgtk.text.decompose(str1)

#param check
#print(list(str1))
#print(len(str1))

#create image
j = 0
i = 0
num = 0
length = [[0]]

#str param max length
while num < len(str1):
    if str1[num] == "\n":
        j = j+1
        length.append([0])
    num += 1
    length[j][i] += 1

#param check2
print(length)
#print(num)

Max_leg = max(length)
num2 = 0
num3 = 0
num4 = 0
j = 0
times = 1
k = 0
#concatenate images line by line
image1 = Image.open('C:/Users/kim98/PycharmProjects/AI_project/converter_train/ex/'+language +'/' + str1[0] + '.png')
image1 = image1.resize((97, 107))


#param check3
#print('C:/Users/kim98/PycharmProjects/AI_project/converter_train/ex/' + str1[0] + '.png')
#print(Max_leg)

while num2 < len(str1)-1:
    times += 1
    num2 += 1
    image1_size = image1.size

    if str1[num2] == "\n":
        j = j + 1
        num2 += 1
        string = str1[num2]
        print(string + '%d' %j)
        if string == '\n':
            j = j + 1
            num2 += 1
            string = str1[num2]
            print(string + '%d' % j)
        if string == '\x0c':
            string = 'zz'

        if length[j][0] <= 3:
            image1 = Image.open('C:/Users/kim98/PycharmProjects/AI_project/converter_train/ex/eng/zz.png')
            image1 = image1.resize((97, 107))
            image1.save("C:/Users/kim98/PycharmProjects/AI_project/image_saved/conversion_image%d.jpg" % j, "JPEG")

        if Max_leg == length[j][0]:
            print('%d time done' % j)
            image1 = Image.open('C:/Users/kim98/PycharmProjects/AI_project/converter_train/ex/'+ language +'/' + string + '.png')
            image1 = image1.resize((97, 107))

        elif Max_leg[0] > length[j][0]:
            print('%d time done' % j)
            image1 = Image.open('C:/Users/kim98/PycharmProjects/AI_project/converter_train/ex/'+language +'/' + string + '.png')
            image1 = image1.resize((97, 107))
        times = 1

    elif str1[num2] == ' ' or str1[num2] == '.' or str1[num2] == 'ᴥ':
        image2 = Image.open('C:/Users/kim98/PycharmProjects/AI_project/converter_train/ex/eng/zz.png')
        image2 = image2.resize((97, 107))
        image2_size = image2.size
        new_image = Image.new('RGB', (times * image2_size[0], image2_size[1]), (250, 250, 250))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1_size[0], 0))
        image1 = new_image
        image1.save("C:/Users/kim98/PycharmProjects/AI_project/image_saved/conversion_image%d.jpg" % j, "JPEG")
    else:
        image2 = Image.open('C:/Users/kim98/PycharmProjects/AI_project/converter_train/ex/'+ language +'/' + str1[num2] +'.png')
        image2 = image2.resize((97, 107))
        image2_size = image2.size
        new_image = Image.new('RGB', (times * image2_size[0], image2_size[1]), (250, 250, 250))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1_size[0], 0))
        image1 = new_image
        image1.save("C:/Users/kim98/PycharmProjects/AI_project/image_saved/conversion_image%d.jpg" % j, "JPEG")
#check param4
#print(j)
#print(Max_leg[0] - length[3][0])

#Make Equal image length
while num3 < j:
    num3 += 1
    image1 = Image.open('C:/Users/kim98/PycharmProjects/AI_project/image_saved/conversion_image%d.jpg' % num3)
    if not Max_leg[0] - length[num3][0] == 0 or Max_leg[0] - length[num3][0] == 1:
        for k in range(Max_leg[0] - length[num3][0]):
            image2 = Image.open('C:/Users/kim98/PycharmProjects/AI_project/converter_train/ex/eng/zz.png')
            image2 = image2.resize((97, 107))
            image2_size = image2.size
            new_image = Image.new('RGB', ((length[num3][0] + k) * image2_size[0], image2_size[1]), (250, 250, 250))
            new_image.paste(image1, (0, 0))
            new_image.paste(image2, (image1_size[0], 0))
            new_image.save("C:/Users/kim98/PycharmProjects/AI_project/image_saved/conversion_image%d.jpg" % num3, "JPEG")



image1 = Image.open('C:/Users/kim98/PycharmProjects/AI_project/image_saved/conversion_image0.jpg')
image_size = image1.size
#combine images
while num4 < j:
    image2 = Image.open('C:/Users/kim98/PycharmProjects/AI_project/image_saved/conversion_image%d.jpg' % num4)
    image2_size = image2.size
    num4 += 1
    new_image = Image.new('RGB', (image_size[0], num4 * image_size[1]), (250, 250, 250))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (0, image1_size[1]))
    new_image.save("C:/Users/kim98/PycharmProjects/AI_project/image_saved/last_conversion_image.jpg","JPEG")
    image1 = new_image
    image1_size = image1.size

#last image!
#image1.show()