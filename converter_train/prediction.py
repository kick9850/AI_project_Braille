import operator

def alpha(num):

    if num == 26:
        return  ' '
    else:
        num_tr = num+97
        return chr(num_tr)

class Predic():
    result = []
    def Predict(self,model,real):
        my_list = model.predict(real)
        index, value = max(enumerate(my_list[0]), key=operator.itemgetter(1))
        print(index,alpha(index))
        self.result.append(alpha(index))

        return self.result

    def reset(self):
        self.result = []

def chk_trans():
    for i in range(0, 27):
        print(str(i) + ':' + alpha(i),end='  ')
        if i%3 ==2 :
            print()

def load_model():
    from keras.models import load_model
    model = load_model('BrailleNet.h5')
    return model

def acc_chk(model, val):
    acc = model.evaluate_generator(val)[1]
    print('model accuracy: {}'.format(round(acc,4)))