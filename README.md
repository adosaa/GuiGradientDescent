# GuiGradientDescent
Pequeña inplementación del método de mínimos cuadrados con el método de descenso de gradiente.La aplicación esta escrita en el lenguaje de programación Python, y para su
correcto funcionamiento necesita las siguiente librerías i/o dependencias:


-PyQt4 (http://www.riverbankcomputing.com/software/pyqt/download)

-Matplotlib(http://matplotlib.org/)

-Numpy(http://www.numpy.org/)


Para su instalación en el sistema operativo Windows, solo se debe ingresar a
las paginas entre paréntesis de cada librería asociada, y descargar los archivos
binarios(.exe) de cada uno. En el sistema operativo GNU/Linux y Unix en
general, usando la librería pip, se instalan por medio de los siguientes
comandos:
sudo pip install numpy
sudo pip install matplotlib
sudo pip install pyqt4

Finalmente ejecutamos en el directorio donde esten los archivos:

python run.py

Por el momento, solo la he dejado funcionando con el dataset wine(https://archive.ics.uci.edu/ml/datasets/Wine), elimnando el feature de clase, y creando tareas de regresión con el ultimo feature(Proline). En trabajos futuros se planea dejarlo estandarizado para cualquier dataset y utilizando Validacion cruzada para la cracion de set de test y train.
