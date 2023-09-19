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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SettingsApplet(object):
    def setupUi(self, SettingsApplet):
        if not SettingsApplet.objectName():
            SettingsApplet.setObjectName(u"SettingsApplet")
        SettingsApplet.resize(819, 652)
        font = QFont()
        font.setFamilies([u"Roboto"])
        SettingsApplet.setFont(font)
        self.vboxLayout = QVBoxLayout(SettingsApplet)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(80, -1, -1, -1)
        self.addressLabel = QLabel(SettingsApplet)
        self.addressLabel.setObjectName(u"addressLabel")

        self.vboxLayout.addWidget(self.addressLabel)

        self.address_input = QLineEdit(SettingsApplet)
        self.address_input.setObjectName(u"address_input")

        self.vboxLayout.addWidget(self.address_input)

        self.portLabel = QLabel(SettingsApplet)
        self.portLabel.setObjectName(u"portLabel")

        self.vboxLayout.addWidget(self.portLabel)

        self.port_input = QLineEdit(SettingsApplet)
        self.port_input.setObjectName(u"port_input")

        self.vboxLayout.addWidget(self.port_input)

        self.save_button = QPushButton(SettingsApplet)
        self.save_button.setObjectName(u"save_button")

        self.vboxLayout.addWidget(self.save_button)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(SettingsApplet)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_2 = QLabel(SettingsApplet)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(406, 406))
        self.label_2.setMaximumSize(QSize(406, 406))
        self.label_2.setPixmap(QPixmap(u"logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_5 = QLabel(SettingsApplet)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_2.addWidget(self.label_5)


        self.vboxLayout.addLayout(self.horizontalLayout_2)

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


        self.vboxLayout.addLayout(self.verticalLayout)


        self.retranslateUi(SettingsApplet)

        QMetaObject.connectSlotsByName(SettingsApplet)
    # setupUi

    def retranslateUi(self, SettingsApplet):
        self.addressLabel.setText(QCoreApplication.translate("SettingsApplet", u"MongoDB Address:", None))
        self.address_input.setText("")
        self.portLabel.setText(QCoreApplication.translate("SettingsApplet", u"MongoDB Port:", None))
        self.save_button.setText(QCoreApplication.translate("SettingsApplet", u"Save", None))
        self.label_4.setText("")
        self.label_2.setText("")
        self.label_5.setText("")
        self.label_3.setText(QCoreApplication.translate("SettingsApplet", u"WebUI on localhost:5000", None))
        self.startWebUIButton.setText(QCoreApplication.translate("SettingsApplet", u"Start WebUI", None))
        self.stopWebUIButton.setText(QCoreApplication.translate("SettingsApplet", u"Stop WebUI", None))
        pass
    # retranslateUi

