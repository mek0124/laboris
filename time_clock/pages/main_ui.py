# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)
import time_clock.Icons_rc as Icons_rc

class Ui_w_MainWindow(object):
    def setupUi(self, w_MainWindow):
        if not w_MainWindow.objectName():
            w_MainWindow.setObjectName(u"w_MainWindow")
        w_MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/main/original.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        w_MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(w_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 2, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaxLength(4)
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setClearButtonEnabled(False)

        self.gridLayout_4.addWidget(self.lineEdit_2, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 1, 1, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_3.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_3.addWidget(self.pushButton_4, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 2, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        w_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(w_MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        w_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(w_MainWindow)

        QMetaObject.connectSlotsByName(w_MainWindow)
    # setupUi

    def retranslateUi(self, w_MainWindow):
        w_MainWindow.setWindowTitle(QCoreApplication.translate("w_MainWindow", u"Laboris", None))
        self.label_2.setText(QCoreApplication.translate("w_MainWindow", u"User Password", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip(QCoreApplication.translate("w_MainWindow", u"Your password is a unique 4-digit code you created with HR.", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_2.setInputMask(QCoreApplication.translate("w_MainWindow", u"9999", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("w_MainWindow", u"Your User ID is your 6-digit employee ID. This will be given to you by your HR or Payroll department.", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit.setInputMask(QCoreApplication.translate("w_MainWindow", u"999999", None))
        self.lineEdit.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("w_MainWindow", u"User ID", None))
        self.pushButton.setText(QCoreApplication.translate("w_MainWindow", u"Meal out", None))
        self.pushButton_2.setText(QCoreApplication.translate("w_MainWindow", u"Clock In", None))
        self.pushButton_3.setText(QCoreApplication.translate("w_MainWindow", u"Meal In", None))
        self.pushButton_4.setText(QCoreApplication.translate("w_MainWindow", u"Clock out", None))
    # retranslateUi

