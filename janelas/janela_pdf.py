# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janelas/janela_pdf.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pdfMerger(object):
    def setupUi(self, pdfMerger):
        pdfMerger.setObjectName("pdfMerger")
        pdfMerger.resize(748, 555)
        self.label_7 = QtWidgets.QLabel(pdfMerger)
        self.label_7.setGeometry(QtCore.QRect(-10, -11, 771, 61))
        self.label_7.setStyleSheet("background: black;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(pdfMerger)
        self.label_5.setGeometry(QtCore.QRect(4, 10, 741, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(pdfMerger)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 31, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("janelas\\../static/apple-touch-icon.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.btnSobe = QtWidgets.QPushButton(pdfMerger)
        self.btnSobe.setGeometry(QtCore.QRect(540, 60, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnSobe.setFont(font)
        self.btnSobe.setStyleSheet("border-radius: 10px; border: 1px solid rgb(0,0,0);  background-color: #CDC99B;    color: white;")
        self.btnSobe.setObjectName("btnSobe")
        self.btnDesce = QtWidgets.QPushButton(pdfMerger)
        self.btnDesce.setGeometry(QtCore.QRect(640, 60, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnDesce.setFont(font)
        self.btnDesce.setStyleSheet("border-radius: 10px; border: 1px solid rgb(0,0,0);  background-color: #CDC99B;    color: white;")
        self.btnDesce.setObjectName("btnDesce")
        self.btnJuntar = QtWidgets.QPushButton(pdfMerger)
        self.btnJuntar.setGeometry(QtCore.QRect(540, 500, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnJuntar.setFont(font)
        self.btnJuntar.setStyleSheet("border-radius: 10px; border: 1px solid rgb(0,0,0);  background-color: #CDC99B;    color: white;")
        self.btnJuntar.setObjectName("btnJuntar")
        self.btnApagar = QtWidgets.QPushButton(pdfMerger)
        self.btnApagar.setGeometry(QtCore.QRect(540, 110, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnApagar.setFont(font)
        self.btnApagar.setStyleSheet("border-radius: 10px; border: 1px solid rgb(0,0,0);  background-color: #CDC99B;    color: white;")
        self.btnApagar.setObjectName("btnApagar")
        self.btnApagarTodos = QtWidgets.QPushButton(pdfMerger)
        self.btnApagarTodos.setGeometry(QtCore.QRect(540, 160, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnApagarTodos.setFont(font)
        self.btnApagarTodos.setStyleSheet("border-radius: 10px; border: 1px solid rgb(0,0,0);  background-color: #CDC99B;    color: white;")
        self.btnApagarTodos.setObjectName("btnApagarTodos")
        self.btnHorario = QtWidgets.QPushButton(pdfMerger)
        self.btnHorario.setGeometry(QtCore.QRect(640, 210, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnHorario.setFont(font)
        self.btnHorario.setStyleSheet("border-radius: 10px; border: 1px solid rgb(0,0,0);  background-color: #CDC99B;    color: white;")
        self.btnHorario.setObjectName("btnHorario")
        self.btnAntiHorario = QtWidgets.QPushButton(pdfMerger)
        self.btnAntiHorario.setGeometry(QtCore.QRect(540, 210, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAntiHorario.setFont(font)
        self.btnAntiHorario.setStyleSheet("border-radius: 10px; border: 1px solid rgb(0,0,0);  background-color: #CDC99B;    color: white;")
        self.btnAntiHorario.setObjectName("btnAntiHorario")
        self.labelView = QtWidgets.QLabel(pdfMerger)
        self.labelView.setGeometry(QtCore.QRect(540, 290, 191, 191))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.labelView.setFont(font)
        self.labelView.setStyleSheet("border: 1px solid rgb(0,0,0);")
        self.labelView.setAlignment(QtCore.Qt.AlignCenter)
        self.labelView.setObjectName("labelView")
        self.inputSenha = QtWidgets.QLineEdit(pdfMerger)
        self.inputSenha.setGeometry(QtCore.QRect(320, 500, 101, 41))
        self.inputSenha.setStyleSheet("border-radius: 10px; border: 1px solid rgb(0,0,0);")
        self.inputSenha.setAlignment(QtCore.Qt.AlignCenter)
        self.inputSenha.setObjectName("inputSenha")
        self.inputPagInicial = QtWidgets.QLineEdit(pdfMerger)
        self.inputPagInicial.setGeometry(QtCore.QRect(130, 500, 31, 41))
        self.inputPagInicial.setStyleSheet("border-radius: 10px; border: 1px solid rgb(0,0,0);")
        self.inputPagInicial.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPagInicial.setObjectName("inputPagInicial")
        self.inputPagFinal = QtWidgets.QLineEdit(pdfMerger)
        self.inputPagFinal.setGeometry(QtCore.QRect(180, 500, 31, 41))
        self.inputPagFinal.setStyleSheet("border-radius: 10px; border: 1px solid rgb(0,0,0);")
        self.inputPagFinal.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPagFinal.setObjectName("inputPagFinal")
        self.label_2 = QtWidgets.QLabel(pdfMerger)
        self.label_2.setGeometry(QtCore.QRect(101, 500, 20, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(pdfMerger)
        self.label_3.setGeometry(QtCore.QRect(160, 500, 20, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.checkProteger = QtWidgets.QCheckBox(pdfMerger)
        self.checkProteger.setGeometry(QtCore.QRect(430, 500, 70, 21))
        self.checkProteger.setObjectName("checkProteger")
        self.checkVisualizar = QtWidgets.QCheckBox(pdfMerger)
        self.checkVisualizar.setGeometry(QtCore.QRect(540, 250, 70, 41))
        self.checkVisualizar.setObjectName("checkVisualizar")
        self.checkSuperProteger = QtWidgets.QCheckBox(pdfMerger)
        self.checkSuperProteger.setGeometry(QtCore.QRect(430, 520, 101, 21))
        self.checkSuperProteger.setObjectName("checkSuperProteger")
        self.btnSeparar = QtWidgets.QPushButton(pdfMerger)
        self.btnSeparar.setGeometry(QtCore.QRect(10, 500, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnSeparar.setFont(font)
        self.btnSeparar.setStyleSheet("border-radius: 10px; border: 1px solid rgb(0,0,0);  background-color: #CDC99B;    color: white;")
        self.btnSeparar.setObjectName("btnSeparar")
        self.line = QtWidgets.QFrame(pdfMerger)
        self.line.setGeometry(QtCore.QRect(210, 490, 20, 61))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnDesproteger = QtWidgets.QPushButton(pdfMerger)
        self.btnDesproteger.setGeometry(QtCore.QRect(230, 500, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnDesproteger.setFont(font)
        self.btnDesproteger.setStyleSheet("border-radius: 10px; border: 1px solid rgb(0,0,0);  background-color: #CDC99B;    color: white;")
        self.btnDesproteger.setObjectName("btnDesproteger")

        self.retranslateUi(pdfMerger)
        QtCore.QMetaObject.connectSlotsByName(pdfMerger)
        pdfMerger.setTabOrder(self.btnSobe, self.btnDesce)
        pdfMerger.setTabOrder(self.btnDesce, self.btnApagar)
        pdfMerger.setTabOrder(self.btnApagar, self.btnApagarTodos)
        pdfMerger.setTabOrder(self.btnApagarTodos, self.btnJuntar)

    def retranslateUi(self, pdfMerger):
        _translate = QtCore.QCoreApplication.translate
        pdfMerger.setWindowTitle(_translate("pdfMerger", "JUNTAR PDF"))
        self.label_5.setText(_translate("pdfMerger", "JUNTAR PDF"))
        self.btnSobe.setText(_translate("pdfMerger", "SOBE"))
        self.btnDesce.setText(_translate("pdfMerger", "DESCE"))
        self.btnJuntar.setText(_translate("pdfMerger", "JUNTAR PDF"))
        self.btnApagar.setText(_translate("pdfMerger", "APAGAR ARQUIVO"))
        self.btnApagarTodos.setText(_translate("pdfMerger", "APAGAR TODOS \n"
" ARQUIVOS"))
        self.btnHorario.setText(_translate("pdfMerger", "90° ->\n"
"Horario"))
        self.btnAntiHorario.setText(_translate("pdfMerger", "<- 90°\n"
"Anti-Horario"))
        self.labelView.setText(_translate("pdfMerger", "VISUALIZAÇÃO"))
        self.label_2.setText(_translate("pdfMerger", "de"))
        self.label_3.setText(_translate("pdfMerger", "a"))
        self.checkProteger.setText(_translate("pdfMerger", "Proteger"))
        self.checkVisualizar.setText(_translate("pdfMerger", "Visualizar"))
        self.checkSuperProteger.setText(_translate("pdfMerger", "Super Proteger"))
        self.btnSeparar.setText(_translate("pdfMerger", "SEPARAR\n"
" PDF"))
        self.btnDesproteger.setText(_translate("pdfMerger", "TIRAR\n"
" SENHA"))
