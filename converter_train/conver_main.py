## 이미지 준비 *한번 실행되면 다시 실행할 필요 없음.
import test_converter
import prediction
import image_test


image_test.data_ready()

train_generator, val_generator = image_test.data_ready()

model = prediction.load_model()
acc = prediction.acc_chk(model, val_generator)

path = 'C:/Users/kim98/PycharmProjects/AI_project/converter_train/test.jpg'

def action(path):

    prediction.chk_trans()
    b = prediction.Predic()
    a = test_converter.img_devide(path)

    a.create_dir()
    a.set_image()
    b.reset()

    for i in range(0,a.lengh):
        a.devide_img()
        real = image_test.load_image('./test')
        b.Predict(model,real)
        a.remove_file()


    print(b.result)
    result = ''.join(b.result)
    return result

action(path)