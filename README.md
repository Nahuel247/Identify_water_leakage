# Estimating water leak location using Artificial Intelligence

It is estimated that 25% of drinking water is lost during distribution and storage, so being able to identify the location of water leaks along a pipeline is of great interest to water utilities. Is of great interest to water utilities. Now, this is not a simple task since the pipes are located underground.
In this repository you will find the methodological process to determine, through the use of Artificial Intelligence, the position of water leaks in a pipeline:

A simulated environment was developed using differential equations to replicate the behavior of water in a leaking pipeline. Studies by Guillen et al. in 2015 and Ruiz et al. in 2018 were used as a basis to construct and validate the results obtained in the simulated environment.

[![Ecuation.png](https://i.postimg.cc/rF4V7DBy/Ecuation.png)](https://postimg.cc/3dKQvxrz)

[![Parameter.png](https://i.postimg.cc/KjwWnrF6/Parameter.png)](https://postimg.cc/SYLV49nd)

During the multiple simulations: The diameter and length of the pipeline, the moment when the leak occurs, the leak coefficient and the location of the leak were modified. Finally, the information obtained was recorded.

[![tuber-a.png](https://i.postimg.cc/fLk5BtHD/tuber-a.png)](https://postimg.cc/62JdQ3Jm)


From the simulations, artificial variables related to the inflow and outflow of water were generated and the location of the leak was used as the response variable. These data were used to train an artificial intelligence model.

The model was built through a construction sample, fitted with a validation sample and tested in a test sample. Finally, the performance of the model and overfitting was estimated through the percentage error.

# Results
Here are the most relevant results related to the methodological development, the efficiency of the model and its implementation.

# Validating the simulated environment
Below, the inflow and outflow of water in a pipeline is shown. The water leak is activated after 300 seconds and the parameters were defined as indicated in Guillen et al. in 2015 and Ruiz et al. in 2018. The results are consistent with those observed in Ruiz et al. 2018.

[![validacion-simulacion.png](https://i.postimg.cc/dVB62P22/validacion-simulacion.png)](https://postimg.cc/rDD5THYs)

# Model Optimization
To reach the best model, the training data was segmented into a training, validation and testing sample. The mean squared error (RMSE) was used as the metric to optimize. Next, the effect of increasing the number of epochs on the performance of the model is shown.

[![Optimizaci-n-del-modelo.png](https://i.postimg.cc/ryDgX4qr/Optimizaci-n-del-modelo.png)](https://postimg.cc/s1R55vQj)

# Model Performance and Overfitting
To evaluate the performance and generalization ability of the model, the Mean Absolute Percentage Error (MAPE) was used as a performance measure. This indicates the average percentage error between the observed values and the values predicted by the model. In the development dataset, a value of 7.15 was obtained, while in the test dataset, a value of 7.6 was obtained. This suggests that the model has high performance and a low level of overfitting.


In addition, when plotting the observed values against the predicted values, an appropriate fit around the line on the graph is observed.

[![Desempe-o-modelo.png](https://i.postimg.cc/fbfpdN6h/Desempe-o-modelo.png)](https://postimg.cc/94zL3vmx)

With the implementation of this model, water companies have the potential to significantly reduce water losses, resulting in cost savings and a more efficient use of resources. Overall, this project highlights the potential of AI to solve real-world problems and improve the performance of industries.
