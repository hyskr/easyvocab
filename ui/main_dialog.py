# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_dialogUNXxYU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
import sys

# import the main window object (mw) from aqt
from aqt import mw
from aqt.qt import *

sys.path.append(os.path.join(os.path.dirname(__file__), "site-packages"))
import googletrans

from . import file_select_dialog


class MainDialog(object):
    def setupUi(self, Dialog):
       if not Dialog.objectName():
        Dialog.setObjectName(u"Dialog")
        Dialog.resize(514, 473)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 511, 471))
        self.buttonBox = QDialogButtonBox(self.groupBox)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(165, 440, 166, 25))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(61, 11, 386, 397))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 5)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(228, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(328, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 0, 2, 5)

        self.horizontalSpacer_5 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 2, 2, 2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 2)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 2)

        self.comboBox_2 = QComboBox(self.widget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 5, 0, 1, 3)

        self.comboBox_3 = QComboBox(self.widget)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 5, 3, 1, 5)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 6, 0, 1, 3)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 6, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(138, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 6, 4, 1, 1)

        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 7, 0, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(178, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 7, 3, 1, 2)

        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(2)

        self.gridLayout.addWidget(self.spinBox, 8, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 8, 1, 1, 4)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

        # perform final setup actions
        # note that these are actions outside of the ones auto generated by QtDesigner
        self.customSetup()
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Generate Foreign Language Cards", None))
        self.groupBox.setTitle("")
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter words...", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Import words file</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Select file...", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Source Language", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Target Language", None))
#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Choose or create a deck to import words into</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBox.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Deck", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Deck", None))
#if QT_CONFIG(tooltip)
        self.radioButton.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Create reverse vocab cards in addition to normal ones.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Create reverse cards", None))
#if QT_CONFIG(tooltip)
        self.spinBox.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>The default number of translations to use on the reverse side of each card</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Default number of translations", None))
    # retranslateUi

    def customSetup(self):
        # connect select file button to the select file dialog
        self.pushButton.clicked.connect(populateFileText(self, file_select_dialog.selectFile))

        # populate the deck list from anki into the combo box
        self.populateDecks(self.comboBox)

        # populate the set of source and target languages into their respective combo box
        self.populateLanguages(self.comboBox_2)
        self.populateLanguages(self.comboBox_3)

        # set the default target language to english
        index = self.comboBox_3.findData("en")
        self.comboBox_3.setCurrentIndex(index)
        print(index)

    # Set the text within the main words entry text box
    def setBoxText(self, text):
        self.textEdit.setText(text)

    def populateDecks(self, comboBox):
        decks = mw.col.decks.all_names_and_ids()

        for deck in decks:
            comboBox.addItem(deck.name, deck)

    def populateLanguages(self, comboBox):
        languages = googletrans.LANGUAGES

        for language_code, language_name in languages.items():
            comboBox.addItem(capitalize_name(language_name), language_code)


# Helper functions

# Curried function to populate the text edit field
# when user selects a file, this code will open the selected file
# and place the text inside the widget
def populateFileText(dialog: MainDialog, f):
    def _f():
        filename = f()

        if filename and filename != '':
            print(filename)
            with open(filename, 'r') as file:
                dialog.setBoxText(str(file.read()))

    return _f

def capitalize_name(name):
    return ' '.join([word.capitalize() for word in name.split(' ')])