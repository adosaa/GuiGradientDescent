# -*- coding: utf-8 -*-

#Interfaz general de la aplicacion
#By Ariel Saavedra

from PyQt4 import QtCore, QtGui
from programa import *
import matplotlib.pyplot as plt
import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(688, 651)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.area_datos = QtGui.QFrame(self.centralwidget)
        self.area_datos.setFrameShape(QtGui.QFrame.StyledPanel)
        self.area_datos.setFrameShadow(QtGui.QFrame.Raised)
        self.area_datos.setObjectName(_fromUtf8("area_datos"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.area_datos)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.dLlanos = QtGui.QGroupBox(self.area_datos)
        self.dLlanos.setObjectName(_fromUtf8("dLlanos"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.dLlanos)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tDatos = QtGui.QTableWidget(self.dLlanos)
        self.tDatos.setObjectName(_fromUtf8("tDatos"))
        self.tDatos.setColumnCount(0)
        self.tDatos.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.tDatos)
        self.verticalLayout.addWidget(self.dLlanos)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.DFilter = QtGui.QGroupBox(self.area_datos)
        self.DFilter.setObjectName(_fromUtf8("DFilter"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.DFilter)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.isNormal = QtGui.QCheckBox(self.DFilter)
        self.isNormal.setObjectName(_fromUtf8("isNormal"))
        self.verticalLayout_6.addWidget(self.isNormal)
        self.connect(self.isNormal, QtCore.SIGNAL("stateChanged(int)"), self.cambiar)
        self.chooseDtaTrain = QtGui.QRadioButton(self.DFilter)
        self.chooseDtaTrain.setObjectName(_fromUtf8("chooseDtaTrain"))
        self.verticalLayout_6.addWidget(self.chooseDtaTrain)
        self.dTrain = QtGui.QTableWidget(self.DFilter)
        self.dTrain.setObjectName(_fromUtf8("dTrain"))
        self.dTrain.setColumnCount(0)
        self.dTrain.setRowCount(0)
        self.verticalLayout_6.addWidget(self.dTrain)
        self.chooseDtaTest = QtGui.QRadioButton(self.DFilter)
        self.chooseDtaTest.setObjectName(_fromUtf8("chooseDtaTest"))
        self.verticalLayout_6.addWidget(self.chooseDtaTest)

        self.chooseDtaTrain.toggled.connect(self.radio1_clicked)

        self.dTest = QtGui.QTableWidget(self.DFilter)
        self.dTest.setObjectName(_fromUtf8("dTest"))
        self.dTest.setColumnCount(0)
        self.dTest.setRowCount(0)
        self.verticalLayout_6.addWidget(self.dTest)
        self.verticalLayout_2.addWidget(self.DFilter)
        self.horizontalLayout.addWidget(self.area_datos)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.params_results = QtGui.QFrame(self.centralwidget)
        self.params_results.setFrameShape(QtGui.QFrame.StyledPanel)
        self.params_results.setFrameShadow(QtGui.QFrame.Raised)
        self.params_results.setObjectName(_fromUtf8("params_results"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.params_results)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Parameters = QtGui.QGroupBox(self.params_results)
        self.Parameters.setObjectName(_fromUtf8("Parameters"))
        self.gridLayout = QtGui.QGridLayout(self.Parameters)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.Parameters)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.alpha = QtGui.QLineEdit(self.Parameters)
        self.alpha.setObjectName(_fromUtf8("alpha"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.alpha)
        self.label_4 = QtGui.QLabel(self.Parameters)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.itera = QtGui.QLineEdit(self.Parameters)
        self.itera.setObjectName(_fromUtf8("itera"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.itera)
        self.label_5 = QtGui.QLabel(self.Parameters)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.converg = QtGui.QLineEdit(self.Parameters)
        self.converg.setObjectName(_fromUtf8("converg"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.converg)
        self.label_10 = QtGui.QLabel(self.Parameters)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_10)
        self.xis = QtGui.QLineEdit(self.Parameters)
        self.xis.setObjectName(_fromUtf8("xis"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.xis)
        self.label_6 = QtGui.QLabel(self.Parameters)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.yi = QtGui.QLineEdit(self.Parameters)
        self.yi.setObjectName(_fromUtf8("yi"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.yi)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(5, QtGui.QFormLayout.SpanningRole, spacerItem)
        self.graph = QtGui.QCheckBox(self.Parameters)
        self.graph.setObjectName(_fromUtf8("graph"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.graph)
        self.label_3 = QtGui.QLabel(self.Parameters)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_3)
        self.xi = QtGui.QLineEdit(self.Parameters)
        self.xi.setObjectName(_fromUtf8("xi"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.xi)
        self.Start = QtGui.QPushButton(self.Parameters)
        self.Start.setObjectName(_fromUtf8("Start"))
        #evento
        self.Start.clicked.connect(self.hola)
        self.formLayout.setWidget(9, QtGui.QFormLayout.SpanningRole, self.Start)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.Parameters)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.Result = QtGui.QGroupBox(self.params_results)
        self.Result.setObjectName(_fromUtf8("Result"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.Result)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.cajaResult = QtGui.QTextEdit(self.Result)
        self.cajaResult.setObjectName(_fromUtf8("cajaResult"))
        self.horizontalLayout_4.addWidget(self.cajaResult)
        self.verticalLayout_4.addWidget(self.Result)
        self.horizontalLayout_2.addWidget(self.params_results)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menuCerrar = QtGui.QMenu(self.menubar)
        self.menuCerrar.setObjectName(_fromUtf8("menuCerrar"))
        self.menuCreditos = QtGui.QMenu(self.menubar)
        self.menuCreditos.setObjectName(_fromUtf8("menuCreditos"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        #accion de abrir archivo
        self.actionAbrir_Archivo = QtGui.QAction(MainWindow)
        self.actionAbrir_Archivo.setObjectName(_fromUtf8("actionAbrir_Archivo"))
        self.actionAbrir_Archivo.setShortcut(self.tr("Ctrl+O"))
        self.connect(self.actionAbrir_Archivo, QtCore.SIGNAL("triggered()"), self.open)
        self.menuArchivo.addAction(self.actionAbrir_Archivo)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuCreditos.menuAction())
        self.menubar.addAction(self.menuCerrar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Regresion Lineal", None))
        self.dLlanos.setTitle(_translate("MainWindow", "Datos llanos", None))
        self.DFilter.setTitle(_translate("MainWindow", "Datos Filltrados", None))
        self.isNormal.setText(_translate("MainWindow", "Normalizar Datos", None))
        self.chooseDtaTrain.setText(_translate("MainWindow", "Conjunto de entrenamiento", None))
        self.chooseDtaTest.setText(_translate("MainWindow", "Conjunto de pruebas", None))
        self.Parameters.setTitle(_translate("MainWindow", "Asignar Parametros", None))
        self.label.setText(_translate("MainWindow", "Alpha", None))
        self.label_4.setText(_translate("MainWindow", "Iteraciones", None))
        self.label_5.setText(_translate("MainWindow", "J de convergencia", None))
        self.label_6.setText(_translate("MainWindow", "Etiqueta Y ", None))
        self.label_10.setText(_translate("MainWindow", "grupo de etiquetas X ", None))
        self.graph.setText(_translate("MainWindow", "Graficar ajuste con algun feature X", None))
        self.label_3.setText(_translate("MainWindow", "Etiqueta de X", None))
        self.Start.setText(_translate(    "MainWindow", "INICIAR", None))
        self.Result.setTitle(_translate("MainWindow", "Resultados", None))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo", None))
        self.menuCerrar.setTitle(_translate("MainWindow", "Cerrar", None))
        self.menuCreditos.setTitle(_translate("MainWindow", "Creditos", None))
        self.actionAbrir_Archivo.setText(_translate("MainWindow", "Abrir Archivo", None))

    #x,y,itera,alpha,indice
    def hola(self):
        alpha = self.alpha.text()
        itera = self.itera.text()
        indice = self.converg.text()
        yi = self.yi.text()
        xi =self.xi.text()
        listc=np.zeros(int(itera))
        cont=0
        feat_x=str(self.xis.text()).split(',')
        stock=[]
        if self.chooseDtaTrain.isChecked():
            if self.isNormal.isChecked():
                self.cajaResult.clear()
                f1=escalarFeaturesInTrain(1)
                #creamos las etiquetas con los nombre de los features
                col_names = ['x1', 'x2', 'x3', 'x4','x5','x6','x7','x8','x9','x10','x11','x12','x13']
                #creamos un diccionario que en cada clave(x1,x2...x13) tendra sus correspondientes valores de feature
                dic_dataTrain = dict(zip(col_names, f1.transpose()))
                for x in feat_x:
                    stock.append(dic_dataTrain[x])
                features_x =np.column_stack(stock)
                #feature y
                feature_y = dic_dataTrain[str(yi)]
                thetas = minimizarGradiente(features_x,feature_y,int(itera),float(alpha),float(indice))
                td = open("jota.txt")
                for line_train in td:
                    listc[cont]=float(line_train.strip())
                    cont=cont+1
                td.close()
                self.cajaResult.append("Conjunto de parametros theta: \n "+str(thetas))
                #predecir los valores segun nuestra hipotesis
                y = predecirHipotesis(features_x,thetas)
                self.cajaResult.append("Conjunto de prediccion de y: \n"+str(y))
                if self.graph.isChecked():
                    feature_x = np.column_stack((dic_dataTrain[str(xi)], np.ones(len(dic_dataTrain[str(xi)]))))
                    thetas = minimizarGradiente(feature_x,feature_y,int(itera),float(alpha),float(indice))
                    y = predecirHipotesis(feature_x,thetas)
                    plt.figure(1)
                    plt.subplot(211)
                    plt.xlabel(str(xi),fontsize=20)
                    plt.ylabel(str(yi),fontsize=28)
                    plt.scatter(dic_dataTrain[str(xi)], feature_y)
                    plt.plot(dic_dataTrain[str(xi)], y)
                    plt.subplot(212)
                    plt.xlabel("Iteraciones",fontsize=28)
                    plt.ylabel("J(theta_{n})",fontsize=28)
                    plt.plot(np.arange(0,int(itera)),listc)
                else:
                    plt.subplot(212)
                    plt.xlabel("Iteraciones",fontsize=28)
                    plt.ylabel("J(theta_{n})",fontsize=28)
                    plt.plot(np.arange(0,int(itera)),listc)
                plt.show()
            else:
                self.cajaResult.clear()
                f1=escalarFeaturesInTrain(0)
                #creamos las etiquetas con los nombre de los features
                col_names = ['x1', 'x2', 'x3', 'x4','x5','x6','x7','x8','x9','x10','x11','x12','x13']
                #creamos un diccionario que en cada clave(x1,x2...x13) tendra sus correspondientes valores de feature
                dic_dataTrain = dict(zip(col_names, f1.transpose()))
                for x in feat_x:
                    stock.append(dic_dataTrain[x])
                features_x =np.column_stack(stock)
                #feature y
                feature_y = dic_dataTrain[str(yi)]
                thetas = minimizarGradiente(features_x,feature_y,int(itera),float(alpha),float(indice))
                td = open("jota.txt")
                for line_train in td:
                    listc[cont]=float(line_train.strip())
                    cont=cont+1
                td.close()
                self.cajaResult.append("Conjunto de parametros theta: \n "+str(thetas))
                #predecir los valores segun nuestra hipotesis
                y = predecirHipotesis(features_x,thetas)
                self.cajaResult.append("Conjunto de prediccion de y: \n"+str(y))
                if self.graph.isChecked():
                    feature_x = np.column_stack((dic_dataTrain[str(xi)], np.ones(len(dic_dataTrain[str(xi)]))))
                    thetas = minimizarGradiente(feature_x,feature_y,int(itera),float(alpha),float(indice))
                    y = predecirHipotesis(feature_x,thetas)
                    plt.figure(1)
                    plt.subplot(211)
                    plt.xlabel(str(xi),fontsize=20)
                    plt.ylabel(str(yi),fontsize=28)
                    plt.scatter(dic_dataTrain[str(xi)], feature_y)
                    plt.plot(dic_dataTrain[str(xi)], y)
                    plt.subplot(212)
                    plt.xlabel("Iteraciones",fontsize=28)
                    plt.ylabel("J(theta_{n})",fontsize=28)
                    plt.plot(np.arange(0,int(itera)),listc)
                else:
                    plt.subplot(212)
                    plt.xlabel("Iteraciones",fontsize=28)
                    plt.ylabel("J(theta_{n})",fontsize=28)
                    plt.plot(np.arange(0,int(itera)),listc)
                plt.show()
        elif self.chooseDtaTest.isChecked():
            if self.isNormal.isChecked():
                self.cajaResult.clear()
                f2=escalarFeaturesInTest(1)
                #creamos las etiquetas con los nombre de los features
                col_names = ['x1', 'x2', 'x3', 'x4','x5','x6','x7','x8','x9','x10','x11','x12','x13']
                #creamos un diccionario que en cada clave(x1,x2...x13) tendra sus correspondientes valores de feature
                dic_dataTrain = dict(zip(col_names, f2.transpose()))
                for x in feat_x:
                    stock.append(dic_dataTrain[x])
                features_x =np.column_stack(stock)
                #feature y
                feature_y = dic_dataTrain[str(yi)]
                thetas = minimizarGradiente(features_x,feature_y,int(itera),float(alpha),float(indice))
                td = open("jota.txt")
                for line_train in td:
                    listc[cont]=float(line_train.strip())
                    cont=cont+1
                td.close()
                self.cajaResult.append("Conjunto de parametros theta: \n "+str(thetas))
                #predecir los valores segun nuestra hipotesis
                y = predecirHipotesis(features_x,thetas)
                self.cajaResult.append("Conjunto de prediccion de y: \n"+str(y))
                if self.graph.isChecked():
                    feature_x = np.column_stack((dic_dataTrain[str(xi)], np.ones(len(dic_dataTrain[str(xi)]))))
                    thetas = minimizarGradiente(feature_x,feature_y,int(itera),float(alpha),float(indice))
                    y = predecirHipotesis(feature_x,thetas)
                    plt.figure(1)
                    plt.subplot(211)
                    plt.xlabel(str(xi),fontsize=20)
                    plt.ylabel(str(yi),fontsize=28)
                    plt.scatter(dic_dataTrain[str(xi)], feature_y)
                    plt.plot(dic_dataTrain[str(xi)], y)
                    plt.subplot(212)
                    plt.xlabel("Iteraciones",fontsize=28)
                    plt.ylabel("J(theta_{n})",fontsize=28)
                    plt.plot(np.arange(0,int(itera)),listc)
                else:
                    plt.subplot(212)
                    plt.xlabel("Iteraciones",fontsize=28)
                    plt.ylabel("J(theta_{n})",fontsize=28)
                    plt.plot(np.arange(0,int(itera)),listc)
                plt.show()
            else:
                self.cajaResult.clear()
                f2=escalarFeaturesInTest(0)
                #creamos las etiquetas con los nombre de los features
                col_names = ['x1', 'x2', 'x3', 'x4','x5','x6','x7','x8','x9','x10','x11','x12','x13']
                #creamos un diccionario que en cada clave(x1,x2...x13) tendra sus correspondientes valores de feature
                dic_dataTrain = dict(zip(col_names, f2.transpose()))
                for x in feat_x:
                    stock.append(dic_dataTrain[x])
                features_x =np.column_stack(stock)
                #feature y
                feature_y = dic_dataTrain[str(yi)]
                thetas = minimizarGradiente(features_x,feature_y,int(itera),float(alpha),float(indice))
                td = open("jota.txt")
                for line_train in td:
                    listc[cont]=float(line_train.strip())
                    cont=cont+1
                td.close()
                self.cajaResult.append("Conjunto de parametros theta: \n "+str(thetas))
                #predecir los valores segun nuestra hipotesis
                y = predecirHipotesis(features_x,thetas)
                self.cajaResult.append("Conjunto de prediccion de y: \n"+str(y))
                if self.graph.isChecked():
                    feature_x = np.column_stack((dic_dataTrain[str(xi)], np.ones(len(dic_dataTrain[str(xi)]))))
                    thetas = minimizarGradiente(feature_x,feature_y,int(itera),float(alpha),float(indice))
                    y = predecirHipotesis(feature_x,thetas)
                    plt.figure(1)
                    plt.subplot(211)
                    plt.xlabel(str(xi),fontsize=20)
                    plt.ylabel(str(yi),fontsize=28)
                    plt.scatter(dic_dataTrain[str(xi)], feature_y)
                    plt.plot(dic_dataTrain[str(xi)], y)
                    plt.subplot(212)
                    plt.xlabel("Iteraciones",fontsize=28)
                    plt.ylabel("J(theta_{n})",fontsize=28)
                    plt.plot(np.arange(0,int(itera)),listc)
                else:
                    plt.subplot(212)
                    plt.xlabel("Iteraciones",fontsize=28)
                    plt.ylabel("J(theta_{n})",fontsize=28)
                    plt.plot(np.arange(0,int(itera)),listc)
                plt.show()

    #abrimos el archivo con los datos y los de test y train
    def open(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self)
        if not fileName.isEmpty():
            inFile = QtCore.QFile(fileName)
            if not inFile.open(QtCore.QFile.ReadOnly):
                QtGui.QMessageBox.warning(self, self.tr("Abrir"),
                                          self.tr("Cannot read file %1:\n%2")
                                          .arg(fileName).arg(inFile.errorString()))
                return
            line = inFile.readLine()
            leerDatos()
            #variable usada para separar las filas impares(traindata) y las pares(testdata)
            i=0
            self.tDatos.setColumnCount(14)
            self.tDatos.setRowCount(178)
            self.tDatos.setHorizontalHeaderLabels(['x1', 'x2', 'x3', 'x4','x5','x6','x7','x8','x9','x10','x11','x12','x13','x14'])
            #tabla de entrenamiento
            self.dTrain.setColumnCount(13)
            self.dTrain.setRowCount(89)
            self.dTrain.setHorizontalHeaderLabels(['x1', 'x2', 'x3', 'x4','x5','x6','x7','x8','x9','x10','x11','x12','x13'])
            #table de pruebas
            self.dTest.setColumnCount(13)
            self.dTest.setRowCount(89)
            self.dTest.setHorizontalHeaderLabels(['x1', 'x2', 'x3', 'x4','x5','x6','x7','x8','x9','x10','x11','x12','x13'])
            while line != "":
                line= unicode(line, encoding="UTF-8")
                self.tDatos.setItem(i, 0, QtGui.QTableWidgetItem(line.strip().split(",")[0]))
                self.tDatos.setItem(i, 1, QtGui.QTableWidgetItem(line.strip().split(",")[1]))
                self.tDatos.setItem(i, 2, QtGui.QTableWidgetItem(line.strip().split(",")[2]))
                self.tDatos.setItem(i, 3, QtGui.QTableWidgetItem(line.strip().split(",")[3]))
                self.tDatos.setItem(i, 4, QtGui.QTableWidgetItem(line.strip().split(",")[4]))
                self.tDatos.setItem(i, 5, QtGui.QTableWidgetItem(line.strip().split(",")[5]))
                self.tDatos.setItem(i, 6, QtGui.QTableWidgetItem(line.strip().split(",")[6]))
                self.tDatos.setItem(i, 7, QtGui.QTableWidgetItem(line.strip().split(",")[7]))
                self.tDatos.setItem(i, 8, QtGui.QTableWidgetItem(line.strip().split(",")[8]))
                self.tDatos.setItem(i, 9, QtGui.QTableWidgetItem(line.strip().split(",")[9]))
                self.tDatos.setItem(i, 10, QtGui.QTableWidgetItem(line.strip().split(",")[10]))
                self.tDatos.setItem(i, 11, QtGui.QTableWidgetItem(line.strip().split(",")[11]))
                self.tDatos.setItem(i, 12, QtGui.QTableWidgetItem(line.strip().split(",")[12]))
                self.tDatos.setItem(i, 13, QtGui.QTableWidgetItem(line.strip().split(",")[13]))
                line = inFile.readLine()
                i=i+1
            i=0
            f1=escalarFeaturesInTrain(0)
            f2=escalarFeaturesInTest(0)
            for k in xrange(89):
                for p in xrange(13):
                    self.dTrain.setItem(i, p, QtGui.QTableWidgetItem(str(f1[k,p])))
                    self.dTest.setItem(i, p, QtGui.QTableWidgetItem(str(f2[k,p])))
                i=i+1

    def cambiar(self):
        if self.isNormal.isChecked():
            i=0
            f1=escalarFeaturesInTrain(1)
            f2=escalarFeaturesInTest(1)
            for k in xrange(89):
                for p in xrange(13):
                    self.dTrain.setItem(i, p, QtGui.QTableWidgetItem(str(f1[k,p])))
                    self.dTest.setItem(i, p, QtGui.QTableWidgetItem(str(f2[k,p])))
                i=i+1
        else:
            i=0
            f1=escalarFeaturesInTrain(0)
            f2=escalarFeaturesInTest(0)
            for k in xrange(89):
                for p in xrange(13):
                    self.dTrain.setItem(i, p, QtGui.QTableWidgetItem(str(f1[k,p])))
                    self.dTest.setItem(i, p, QtGui.QTableWidgetItem(str(f2[k,p])))
                i=i+1

    def radio1_clicked(self, enabled):
        if enabled:
            print "asdadsads"
