# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_applet.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_SettingsApplet(object):
    def setupUi(self, SettingsApplet):
        if not SettingsApplet.objectName():
            SettingsApplet.setObjectName(u"SettingsApplet")
        SettingsApplet.resize(819, 640)
        self.vboxLayout = QVBoxLayout(SettingsApplet)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.label = QLabel(SettingsApplet)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))

        self.vboxLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.addressLabel = QLabel(SettingsApplet)
        self.addressLabel.setObjectName(u"addressLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.addressLabel)

        self.address_input = QLineEdit(SettingsApplet)
        self.address_input.setObjectName(u"address_input")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.address_input)

        self.save_button = QPushButton(SettingsApplet)
        self.save_button.setObjectName(u"save_button")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.save_button)

        self.portLabel = QLabel(SettingsApplet)
        self.portLabel.setObjectName(u"portLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.portLabel)

        self.port_input = QLineEdit(SettingsApplet)
        self.port_input.setObjectName(u"port_input")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.port_input)

        self.label_2 = QLabel(SettingsApplet)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(406, 406))
        self.label_2.setMaximumSize(QSize(406, 406))
        self.label_2.setPixmap(QPixmap(u"logo.png"))
        self.label_2.setScaledContents(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(SettingsApplet)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.startWebUIButton = QPushButton(SettingsApplet)
        self.startWebUIButton.setObjectName(u"startWebUIButton")

        self.horizontalLayout.addWidget(self.startWebUIButton)

        self.stopWebUIButton = QPushButton(SettingsApplet)
        self.stopWebUIButton.setObjectName(u"stopWebUIButton")
        self.stopWebUIButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.stopWebUIButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.verticalLayout)


        self.vboxLayout.addLayout(self.formLayout)


        self.retranslateUi(SettingsApplet)

        QMetaObject.connectSlotsByName(SettingsApplet)
    # setupUi

    def retranslateUi(self, SettingsApplet):
        self.label.setText(QCoreApplication.translate("SettingsApplet", u"Settings", None))
        self.addressLabel.setText(QCoreApplication.translate("SettingsApplet", u"MongoDB Address:", None))
        self.save_button.setText(QCoreApplication.translate("SettingsApplet", u"Save", None))
        self.portLabel.setText(QCoreApplication.translate("SettingsApplet", u"MongoDB Port:", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("SettingsApplet", u"WebUI on localhost:5000", None))
        self.startWebUIButton.setText(QCoreApplication.translate("SettingsApplet", u"Start WebUI", None))
        self.stopWebUIButton.setText(QCoreApplication.translate("SettingsApplet", u"Stop WebUI", None))
        pass
    # retranslateUi

