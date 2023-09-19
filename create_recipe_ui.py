# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_recipe.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(911, 767)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 767))
        font = QFont()
        font.setFamilies([u"Roboto"])
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.button_layout = QHBoxLayout(self.frame)
        self.button_layout.setObjectName(u"button_layout")
        self.save_button = QPushButton(self.frame)
        self.save_button.setObjectName(u"save_button")

        self.button_layout.addWidget(self.save_button)

        self.clear_button = QPushButton(self.frame)
        self.clear_button.setObjectName(u"clear_button")

        self.button_layout.addWidget(self.clear_button)

        self.open_recipe_button = QPushButton(self.frame)
        self.open_recipe_button.setObjectName(u"open_recipe_button")

        self.button_layout.addWidget(self.open_recipe_button)

        self.remove_recipe_button = QPushButton(self.frame)
        self.remove_recipe_button.setObjectName(u"remove_recipe_button")

        self.button_layout.addWidget(self.remove_recipe_button)

        self.recipes_dropdown = QComboBox(self.frame)
        self.recipes_dropdown.setObjectName(u"recipes_dropdown")

        self.button_layout.addWidget(self.recipes_dropdown)


        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalFrame = QFrame(Form)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.recipe_name_label = QLabel(self.verticalFrame)
        self.recipe_name_label.setObjectName(u"recipe_name_label")
        self.recipe_name_label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.recipe_name_label)

        self.recipe_name_input = QLineEdit(self.verticalFrame)
        self.recipe_name_input.setObjectName(u"recipe_name_input")

        self.verticalLayout_2.addWidget(self.recipe_name_input)

        self.ingredients_label = QLabel(self.verticalFrame)
        self.ingredients_label.setObjectName(u"ingredients_label")
        self.ingredients_label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.ingredients_label)

        self.ingredient_scroll_area = QScrollArea(self.verticalFrame)
        self.ingredient_scroll_area.setObjectName(u"ingredient_scroll_area")
        self.ingredient_scroll_area.setMaximumSize(QSize(16777215, 300))
        self.ingredient_scroll_area.setWidgetResizable(True)
        self.ingredient_scroll_content = QWidget()
        self.ingredient_scroll_content.setObjectName(u"ingredient_scroll_content")
        self.ingredient_scroll_content.setGeometry(QRect(0, 0, 284, 221))
        self.ingredients_layout_2 = QGridLayout(self.ingredient_scroll_content)
        self.ingredients_layout_2.setObjectName(u"ingredients_layout_2")
        self.ingredient_scroll_area.setWidget(self.ingredient_scroll_content)

        self.verticalLayout_2.addWidget(self.ingredient_scroll_area)

        self.add_ingredient_button = QPushButton(self.verticalFrame)
        self.add_ingredient_button.setObjectName(u"add_ingredient_button")

        self.verticalLayout_2.addWidget(self.add_ingredient_button)

        self.new_ingredient_input = QLineEdit(self.verticalFrame)
        self.new_ingredient_input.setObjectName(u"new_ingredient_input")

        self.verticalLayout_2.addWidget(self.new_ingredient_input)

        self.label = QLabel(self.verticalFrame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(300, 300))
        self.label.setBaseSize(QSize(300, 300))
        self.label.setPixmap(QPixmap(u"logo.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.verticalFrame)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.steps_layout = QVBoxLayout()
        self.steps_layout.setObjectName(u"steps_layout")

        self.verticalLayout_3.addLayout(self.steps_layout)

        self.add_step_button = QPushButton(Form)
        self.add_step_button.setObjectName(u"add_step_button")

        self.verticalLayout_3.addWidget(self.add_step_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.save_button.setText(QCoreApplication.translate("Form", u"Save Recipe", None))
        self.clear_button.setText(QCoreApplication.translate("Form", u"New Recipe", None))
        self.open_recipe_button.setText(QCoreApplication.translate("Form", u"Modify Recipe", None))
        self.remove_recipe_button.setText(QCoreApplication.translate("Form", u"Delete Recipe", None))
        self.recipe_name_label.setText(QCoreApplication.translate("Form", u"Recipe Name:", None))
        self.ingredients_label.setText(QCoreApplication.translate("Form", u"Ingredients:", None))
        self.add_ingredient_button.setText(QCoreApplication.translate("Form", u"Add Ingredient ", None))
        self.label.setText("")
        self.add_step_button.setText(QCoreApplication.translate("Form", u"Add Step", None))
        pass
    # retranslateUi

