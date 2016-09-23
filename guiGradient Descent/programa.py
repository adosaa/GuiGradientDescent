import matplotlib.pyplot as plt
import numpy as np
#Regresion Lineal con funcion de costos y descenso de gradiente
#By Ariel Saavedra
'''
funcion que entrega el set de entrenamiento y set de pruebas en archivos
'''
def leerDatos():
    f =open("wine.data.txt")
    traindata = open("traindata.txt","w")
    testdata = open("testdata.txt","w")
    line = f.readline()
    #variable usada para separar las filas impares(traindata) y las pares(testdata)
    cont=1
    while line != "":
        if cont%2 ==0:
            #escribimos en el archivo de pruebas, ignorando el primer feature
            testdata.write(line[2:len(line)])
        else:
            #escribimos en el archivo de entrenamiento, ignorando el primer feature
            traindata.write(line[2:len(line)])
        line = f.readline()
        cont=cont+1
    f.close()
    testdata.close()
    traindata.close()
'''
Funcion que normaliza los datos de los set entrenamiento(usando la normalizacion media)
Tambien hay x^i_j con valores .58 que se deben casteados a flotantes
RETURN: una matriz con los features de entrenamiento normalizados
'''
def escalarFeaturesInTrain(iden):
    td = open("traindata.txt")
    cont=0
    f1=np.zeros((89,13))
    for line_train in td:
        #sacamos el simbolo del salto de linea del ultimo feature \n y obtenemos una lista
        #con los elementos de cada example x^i
        lTrain = line_train.strip().split(",")
        #casteamos todos los elementos a flotantes
        map(float, lTrain)
        #creamos la matriz
        for j in xrange(13):
            f1[cont,j]=lTrain[j]
        cont=cont+1
    if iden == 0:
        return f1
    else:
        #variables pre normalizacion como la suma de los valores de los features(sumCol)
        #el valor maximo(maxRange) y el minimo (minRange)
        sumCol = f1.sum(0)
        maxRange=f1.max(0)
        minRange=f1.min(0)
        for k in xrange(89):
                for p in xrange(13):
                    #regularizamos cada valor por la formula
                    # xi = (xi- mu)/si, donde si=(maxRange-minRange) y mu = media
                    f1[k,p]=((f1[k,p]-(sumCol[p]/len(f1)))/(maxRange[p]- minRange[p]))
        return f1
    td.close()

'''
Funcion que normaliza los datos de los set prueba(usando la normalizacion media)
Tambien hay x^i_j con valores .58 que se deben casteados a flotantes
RETURN: una matriz con los features de entrenamiento normalizados
'''
def escalarFeaturesInTest(iden):
    td = open("testdata.txt")
    cont=0
    f1=np.zeros((89,13))
    for line_train in td:
        #sacamos el simbolo del salto de linea del ultimo feature \n y obtenemos una lista
        #con los elementos de cada example x^i
        lTrain = line_train.strip().split(",")
        #casteamos todos los elementos a flotantes
        map(float, lTrain)
        #creamos la matriz
        for j in xrange(13):
            f1[cont,j]=lTrain[j]
        cont=cont+1
    if iden == 0:
        return f1
    else:
        #variables pre normalizacion como la suma de los valores de los features(sumCol)
        #el valor maximo(maxRange) y el minimo (minRange)
        sumCol = f1.sum(0)
        maxRange=f1.max(0)
        minRange=f1.min(0)
        for k in xrange(89):
                for p in xrange(13):
                    #regularizamos cada valor por la formula
                    # xi = (xi- mu)/si, donde si=(maxRange-minRange) y mu = media
                    f1[k,p]=((f1[k,p]-(sumCol[p]/len(f1)))/(maxRange[p]- minRange[p]))
        return f1
    td.close()


'''
Funcion que determina la hipotesis
'''
def setHipotesis(x,theta,y):
    #calcula el producto punto entre x_n y theta_n y retona la diferencia de esta con el valor actual
    return np.dot(x,theta)- y

'''
Funcion que determina nuestra funcion de costo
'''

def setFuncionDeCosto(difHip,m):
    #suma de los cuadrados
    return np.sum(difHip**2) / (2*m)

'''
Funcion de descenso de gradiente
'''
def minimizarGradiente(x,y,itera,alpha,indice):
    m, n = np.shape(x) # m y n  del train data o del test data
    thetas = np.ones(n) #vector de unos que representa los parametros, ya que theta_0=1
    cont=0
    td = open("jota.txt","w")
    for i in xrange(itera):
        difhipo= setHipotesis(x,thetas,y)
        costo = setFuncionDeCosto(difhipo,m)
        #calculamos la derivada de J para cada ejemplo
        derivada_j = np.dot(x.transpose(), difhipo) / m
        #Actualizamos los parametros
        thetas = thetas-alpha*derivada_j
        #guardamos todos los costos
        td.write(str(costo)+'\n')
        #chequeamos si el entranimiento es bueno a partir del costo
        if costo < indice:
            print "hemos convergido :D,la suma de los cuadrados de los errores J es: ",costo
            return thetas
        cont=cont+1
    td.close()
    return thetas
'''
Predecimos nuestros features y con los valores de los features x y theta, gracias a la hipotesis
'''
def predecirHipotesis(x,thetas):
    return np.dot(x,thetas)

#main solo con motivo de pruebas
if __name__ == "__main__":
    leerDatos()
    #obtenemos la matriz de datos de entrenamiento
    f1 = escalarFeaturesInTrain()
    #obtenemos la matriz de datos de prueba
    f2 = escalarFeaturesInTest()
    #creamos las etiquetas con los nombre de los features
    col_names = ['x1', 'x2', 'x3', 'x4','x5','x6','x7','x8','x9','x10','x11','x12','x13']
    #creamos un diccionario que en cada clave(x1,x2...x13) tendra sus correspondientes valores de feature
    dic_dataTrain = dict(zip(col_names, f1.transpose()))
    #agruparemos todos nuestros features x que usaremos para predecir un feature y
    features_x = np.column_stack((dic_dataTrain['x1'],dic_dataTrain['x2'],dic_dataTrain['x3'],dic_dataTrain['x4']
    ,dic_dataTrain['x5'],dic_dataTrain['x6'],dic_dataTrain['x7'],dic_dataTrain['x8'],dic_dataTrain['x9'],dic_dataTrain['x10']
    ,dic_dataTrain['x11'],dic_dataTrain['x12']))
    #prueba con menos features, para igualar la dimension hemos puesto unos
    fp = np.column_stack((dic_dataTrain['x1'], np.ones(len(dic_dataTrain['x1']))))
    #feature y
    feature_y = dic_dataTrain['x13']
    #usamos 300 iteraciones, una taza de aprendizaje de 0.01 y nuestro costo ideal de convergencia(uno bueno!)
    thetas = minimizarGradiente(fp,feature_y,300,0.01,0.03)
    print "Conjunto de parametros theta: \n ",thetas
    #predecir los valores segun nuestra hipotesis
    y = predecirHipotesis(fp,thetas)
    print "Conjunto de prediccion de y: \n",y
    #para visualizar la linea de tendencia, se debe comparar con una sola feature
    plt.scatter(dic_dataTrain['x1'], feature_y)
    plt.plot(dic_dataTrain['x1'], y)
    plt.show()
