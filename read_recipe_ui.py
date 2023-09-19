# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'read_recipe.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QPushButton, QScrollArea, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_ReadRecipe(object):
    def setupUi(self, ReadRecipe):
        if not ReadRecipe.objectName():
            ReadRecipe.setObjectName(u"ReadRecipe")
        ReadRecipe.resize(930, 767)
        font = QFont()
        font.setFamilies([u"Roboto"])
        ReadRecipe.setFont(font)
        self.verticalLayout = QVBoxLayout(ReadRecipe)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ReadRecipe)
        self.label.setObjectName(u"label")
        self.label.setMargin(6)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, -1, -1, -1)
        self.LeftPanel = QFrame(ReadRecipe)
        self.LeftPanel.setObjectName(u"LeftPanel")
        self.LeftPanel.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.LeftPanel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.LeftPanel)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.ingredient_filters_layout = QWidget()
        self.ingredient_filters_layout.setObjectName(u"ingredient_filters_layout")
        self.ingredient_filters_layout.setGeometry(QRect(0, 0, 184, 587))
        self.verticalLayoutWidget = QWidget(self.ingredient_filters_layout)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 771, 511))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ingredient_filters_layout_2 = QVBoxLayout()
        self.ingredient_filters_layout_2.setObjectName(u"ingredient_filters_layout_2")
        self.ingredient_filters_layout_2.setSizeConstraint(QLayout.SetNoConstraint)

        self.verticalLayout_4.addLayout(self.ingredient_filters_layout_2)

        self.scrollArea.setWidget(self.ingredient_filters_layout)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.remove_filter_button = QPushButton(self.LeftPanel)
        self.remove_filter_button.setObjectName(u"remove_filter_button")

        self.verticalLayout_3.addWidget(self.remove_filter_button)

        self.filter_button = QPushButton(self.LeftPanel)
        self.filter_button.setObjectName(u"filter_button")

        self.verticalLayout_3.addWidget(self.filter_button)

        self.filter_dropdown = QComboBox(self.LeftPanel)
        self.filter_dropdown.addItem("")
        self.filter_dropdown.addItem("")
        self.filter_dropdown.setObjectName(u"filter_dropdown")

        self.verticalLayout_3.addWidget(self.filter_dropdown)


        self.horizontalLayout.addWidget(self.LeftPanel)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.recipe_details_browser = QTextBrowser(ReadRecipe)
        self.recipe_details_browser.setObjectName(u"recipe_details_browser")
        self.recipe_details_browser.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.recipe_details_browser)

        self.recipe_list = QListWidget(ReadRecipe)
        self.recipe_list.setObjectName(u"recipe_list")

        self.verticalLayout_2.addWidget(self.recipe_list)

        self.refresh_button = QPushButton(ReadRecipe)
        self.refresh_button.setObjectName(u"refresh_button")

        self.verticalLayout_2.addWidget(self.refresh_button)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ReadRecipe)

        QMetaObject.connectSlotsByName(ReadRecipe)
    # setupUi

    def retranslateUi(self, ReadRecipe):
        ReadRecipe.setWindowTitle(QCoreApplication.translate("ReadRecipe", u"Read Recipe", None))
        self.label.setText(QCoreApplication.translate("ReadRecipe", u"Filter by Ingredients:", None))
        self.remove_filter_button.setText(QCoreApplication.translate("ReadRecipe", u"Remove Filters", None))
        self.filter_button.setText(QCoreApplication.translate("ReadRecipe", u"Apply Filter", None))
        self.filter_dropdown.setItemText(0, QCoreApplication.translate("ReadRecipe", u"Contains selected ingredients", None))
        self.filter_dropdown.setItemText(1, QCoreApplication.translate("ReadRecipe", u"Doesn't need other ingredients", None))

        self.refresh_button.setText(QCoreApplication.translate("ReadRecipe", u"Refresh", None))
    # retranslateUi

