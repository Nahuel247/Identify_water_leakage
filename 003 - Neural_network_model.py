#################################################
#      CONSTRUCTING A NEURAL NETWORK MODEL
#################################################

############################################################################
# Author: Nahuel Canelo
# Email: nahuelcaneloaraya@gmail.com
############################################################################


#######################
#   IMPORT LIBRARY
########################

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from numpy.random import uniform
import matplotlib.pyplot as plt
import random
import tensorflow as tf


# Fijar semilla para Numpy, Python, TensorFlow y Keras
np.random.seed(123)
random.seed(123)
tf.random.set_seed(123)
tf.keras.backend.set_learning_phase(0)


#########################
#      FUNCTION
########################

def mape(actual, pred):
    actual, pred = np.array(actual), np.array(pred)
    return np.mean(np.abs((actual - pred) / actual)) * 100


##############################
# IMPORTING THE DATASET
##############################

data=pd.read_csv("data.csv", sep=";")


###############################
# PREPARING THE DATA
###############################

# Defining a vector with the name of the variables to predict
variable_respuesta = ['zl']

# Defining elements that act as "keys" and that we do not want in the model
keys=[]

data_artificial=data.drop(columns = keys)
X_data=data_artificial.drop(columns=variable_respuesta)
Y_data=data_artificial[variable_respuesta]


# Segmenting the data into Pretrain and Test sets
msk = np.random.rand(len(X_data)) < 0.8
X_train=X_data[msk]
X_test=X_data[~msk]
y_train=Y_data[msk]
y_test=Y_data[~msk]

#https://www.datatechnotes.com/2019/12/multi-output-regression-example-with.html


###############################
# TRAINING THE MODEL
###############################

in_dim = X_train.shape[1]
out_dim = y_train.shape[1]

model = Sequential()
model.add(Dense(15, input_dim=in_dim))
model.add(Dense(25, activation="relu"))
model.add(Dense(20, activation="relu"))
model.add(Dense(out_dim))

model.compile( loss='mean_squared_error', optimizer='adam', metrics='mean_squared_error')
model.summary()


history=model.fit(X_train, y_train, epochs=100, validation_split=0.5,  verbose=2)


# Plotting the model Optimization
plt.figure
plt.plot(history.history['mean_squared_error'])
plt.plot(history.history['val_mean_squared_error'])
plt.title("Model Optimization: RMSE vs Number of Epochs")
plt.ylabel("RMSE")
plt.xlabel("Epoch")
plt.legend(['train','test'])
plt.show()


#############################
#  MODEL IMPLEMENTATION
#############################

# Train
y_train_pred=model.predict(X_train)

# Test
y_test_pred = model.predict(X_test)


# Evaluating model performance and overfitting
print(round(mape(y_train,y_train_pred),2)) # error porcentual absoluto
print(round(mape(y_test,y_test_pred),2)) # error porcentual absoluto


# Percentage of population with a percentage error less than or equal to X%
print(round(np.sum(abs(np.array(y_test_pred)-np.array(y_test))/np.array(y_test)<=0.10)/(y_test.size),2))
print(round(np.sum(abs(np.array(y_test_pred)-np.array(y_test))/np.array(y_test)<=0.15)/(y_test.size),2))
print(round(np.sum(abs(np.array(y_test_pred)-np.array(y_test))/np.array(y_test)<=0.20)/(y_test.size),2))


# Visualization of the results
y_test_merged = np.concatenate((y_test, y_test_pred), axis=1)
df = pd.DataFrame(y_test_merged, columns=["observed_value", "predicted_value"])

plt.scatter(df["observed_value"], df["predicted_value"])
p1 = max(max(df["predicted_value"]), max(df["observed_value"]))
p2 = min(min(df["predicted_value"]), min(df["observed_value"]))
plt.plot([p1, p2], [p1, p2], 'b-')

plt.title("Model performance")
plt.xlabel("Observed location (m)")
plt.ylabel("Predicted location (m)")
plt.show()
