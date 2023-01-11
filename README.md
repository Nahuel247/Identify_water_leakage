# Estimación de la ubicación de fuga de agua utilizando Inteligencia artificial

Se estima que el 25% del agua potable se pierde durante su distribución y almacenamiento, por lo cual, el poder identificar la ubicación de fugas de agua a lo largo de
una cañería es de gran interés para empresas sanitarias. Ahora, esto no es una tarea sencilla ya que las tuberías se encuentran bajo tierra.
En este repositorio encontrarán el proceso metodológico para determinar, mediante el uso de la Inteligencia Artificial, la posición de las fugas de agua en una tubería:


* Se desarrolló un ambiente simulado mediante ecuaciones diferenciales para replicar el comportamiento del agua en una tubería con fugas. Se tomaron como base los 
estudios realizados por Guillen et al. en 2015 y Ruiz et al. en 2018 para construir y validar los resultados obtenidos en el ambiente simulado.


[![Ecuation.png](https://i.postimg.cc/rF4V7DBy/Ecuation.png)](https://postimg.cc/3dKQvxrz)

[![Parameter.png](https://i.postimg.cc/KjwWnrF6/Parameter.png)](https://postimg.cc/SYLV49nd)

* Se procedió a modificar el diámetro y la longitud de la tubería, el momento en que ocurre la fuga, el coeficiente de fuga y la ubicación de la fuga. Finalmente, 
se registró la información obtenida.

[![tuber-a.png](https://i.postimg.cc/fLk5BtHD/tuber-a.png)](https://postimg.cc/62JdQ3Jm)

* A partir de las simulaciones se generaron variables artificiales relacionadas al flujo de entrada y salida del agua y se utilizó como variable respuesta la ubicación
de la fuga, estos datos se utilizaron para entrenar un modelo de inteligencia artificial.

* El modelo fue construido a través de una muestra de construcción, ajustado con una muestra de validación y testeado en una muestra test. Finalmente,
el desempeño del modelo y el sobreajuste fue estimado a través del error porcentual. 

# Resultados
A continuación, se presentan aquellos resultados más relevantes relacionados al desarrollo metodológico, la eficiencia del modelo y su implementación.

# Validación del entorno simulado.
A continuación, se muestra el flujo de entrada y salida de agua en una cañería. La fuga de agua se activa pasado los 300 segundos y los
parámetros fueron definidos siguiendo lo indicado en Guillen et al. en 2015 y Ruiz et al. en 2018. Los resultados se condicen con los observados en Ruiz et al. 2018.

[![validacion-simulacion.png](https://i.postimg.cc/dVB62P22/validacion-simulacion.png)](https://postimg.cc/rDD5THYs)

# Optimización del modelo
Para llegar al mejor modelo, se segmentó la data de entrenamiento en una muestra de entrenamiento, validación y testeo.
Se utilizó el error cuadrático medio (RMSE) como métrica a optimizar. A continuación, se muestra el efecto que tiene el aumento de épocas sobre el desempeño del 
modelo.

[![Optimizaci-n-del-modelo.png](https://i.postimg.cc/ryDgX4qr/Optimizaci-n-del-modelo.png)](https://postimg.cc/s1R55vQj)

# Desempeño y sobreajuste del modelo
Para evaluar el desempeño y el sobreajuste del modelo se utilizó el error absoluto medio porcentual (MAPE), es decir, el promedio porcentual del error. En la muestra de desarrollo se obtuvo un valor igual a 7.15 y en testeo de 7.6. Lo que nos indicaría que el modelo tiene un alto desempeño y un bajo sobreajuste.
 
Por otro lado al plotear el valor observado vs el predicho se observa un buen ajuste entorno la recta del gráfico.

[![Desempe-o-modelo.png](https://i.postimg.cc/fbfpdN6h/Desempe-o-modelo.png)](https://postimg.cc/94zL3vmx)




