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
    QStatusBar, QWidget)
import Icons_rc

class Ui_w_MainWindow(object):
    def setupUi(self, w_MainWindow):
        if not w_MainWindow.objectName():
            w_MainWindow.setObjectName(u"w_MainWindow")
        w_MainWindow.resize(400, 600)
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

        self.le_user_pw = QLineEdit(self.frame_2)
        self.le_user_pw.setObjectName(u"le_user_pw")
        self.le_user_pw.setMaxLength(4)
        self.le_user_pw.setEchoMode(QLineEdit.EchoMode.Normal)
        self.le_user_pw.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.le_user_pw.setClearButtonEnabled(False)

        self.gridLayout_4.addWidget(self.le_user_pw, 3, 0, 1, 1)

        self.le_user_id = QLineEdit(self.frame_2)
        self.le_user_id.setObjectName(u"le_user_id")
        self.le_user_id.setEchoMode(QLineEdit.EchoMode.Normal)
        self.le_user_id.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.le_user_id, 1, 0, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pb_meal_out = QPushButton(self.frame_3)
        self.pb_meal_out.setObjectName(u"pb_meal_out")

        self.gridLayout_3.addWidget(self.pb_meal_out, 0, 1, 1, 1)

        self.pb_clock_in = QPushButton(self.frame_3)
        self.pb_clock_in.setObjectName(u"pb_clock_in")

        self.gridLayout_3.addWidget(self.pb_clock_in, 0, 0, 1, 1)

        self.pb_meal_in = QPushButton(self.frame_3)
        self.pb_meal_in.setObjectName(u"pb_meal_in")

        self.gridLayout_3.addWidget(self.pb_meal_in, 1, 0, 1, 1)

        self.pb_clock_out = QPushButton(self.frame_3)
        self.pb_clock_out.setObjectName(u"pb_clock_out")

        self.gridLayout_3.addWidget(self.pb_clock_out, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)


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
        self.le_user_pw.setToolTip(QCoreApplication.translate("w_MainWindow", u"Your password is a unique 4-digit code you created with HR.", None))
#endif // QT_CONFIG(tooltip)
        self.le_user_pw.setInputMask(QCoreApplication.translate("w_MainWindow", u"9999", None))
        self.le_user_pw.setText("")
        self.le_user_pw.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.le_user_id.setToolTip(QCoreApplication.translate("w_MainWindow", u"Your User ID is your 6-digit employee ID. This will be given to you by your HR or Payroll department.", None))
#endif // QT_CONFIG(tooltip)
        self.le_user_id.setInputMask(QCoreApplication.translate("w_MainWindow", u"999999", None))
        self.le_user_id.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("w_MainWindow", u"User ID", None))
        self.pb_meal_out.setText(QCoreApplication.translate("w_MainWindow", u"Meal out", None))
        self.pb_clock_in.setText(QCoreApplication.translate("w_MainWindow", u"Clock In", None))
        self.pb_meal_in.setText(QCoreApplication.translate("w_MainWindow", u"Meal In", None))
        self.pb_clock_out.setText(QCoreApplication.translate("w_MainWindow", u"Clock out", None))
    # retranslateUi

