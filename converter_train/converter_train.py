from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
from keras import layers as L
from keras.models import Model,load_model
from keras.regularizers import l2
from keras.callbacks import ModelCheckpoint,ReduceLROnPlateau,EarlyStopping
import matplotlib.pyplot as plt

datagen = ImageDataGenerator(rotation_range=20,
                             shear_range=10,
                             validation_split=0.2)

train_generator = datagen.flow_from_directory('./images/',
                                              target_size=(36,36),
                                              subset='training')

val_generator = datagen.flow_from_directory('./images/',
                                            target_size=(36,36),
                                            subset='validation')

K.clear_session()

model_ckpt = ModelCheckpoint('BrailleNet.h5',save_best_only=True)
reduce_lr = ReduceLROnPlateau(patience=8,verbose=0)
early_stop = EarlyStopping(patience=15,verbose=1)

entry = L.Input(shape=(36,36,3))

x = L.SeparableConv2D(256,(3,3),activation='relu')(entry)
x = L.MaxPooling2D((2,2))(x)

x = L.SeparableConv2D(512,(3,3),activation='relu')(x)
x = L.MaxPooling2D((2,2))(x)

x = L.SeparableConv2D(1024,(2,2),activation='relu')(x)
x = L.GlobalMaxPooling2D()(x)

x = L.Dense(1024)(x)
x = L.LeakyReLU()(x)
x = L.Dense(64,kernel_regularizer=l2(2e-4))(x)
x = L.LeakyReLU()(x)
x = L.Dense(26,activation='softmax')(x)

model = Model(entry,x)
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

history = model.fit_generator(train_generator,validation_data=val_generator,epochs=666,
                              callbacks=[model_ckpt,reduce_lr,early_stop],verbose=0)

model = load_model('BrailleNet.h5')
acc = model.evaluate_generator(val_generator)[1]
print('model accuracy: {}'.format(round(acc,4)))

fig, loss_ax = plt.subplots(figsize=(10, 5))
acc_ax = loss_ax.twinx()
loss_ax.plot(history.history['loss'], 'y', label='train loss')
loss_ax.plot(history.history['val_loss'], 'r', label='val loss')
acc_ax.plot(history.history['accuracy'], 'b', label='train acc')
acc_ax.plot(history.history['val_accuracy'], 'g', label='val acc')
loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')
loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')
plt.show()