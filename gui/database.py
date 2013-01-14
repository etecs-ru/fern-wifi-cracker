import os
from main_window import font_size
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

font_setting = font_size()

class database_ui(object):
    def setupUi(self, database):
        database.setObjectName(_fromUtf8("database"))
        database.resize(556, 290)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/Database-64.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        database.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(database)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(database)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(database)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.key_table = QtGui.QTableWidget(database)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.key_table.setFont(font)
        self.key_table.setObjectName(_fromUtf8("key_table"))
        self.key_table.setColumnCount(5)
        self.key_table.setRowCount(0)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/router-icone-7671-128.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtGui.QTableWidgetItem()
        self.key_table.setHorizontalHeaderItem(0, item)
        item.setIcon(icon1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/mac_address.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtGui.QTableWidgetItem()
        self.key_table.setHorizontalHeaderItem(1, item)
        item.setIcon(icon2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/binary.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtGui.QTableWidgetItem()
        self.key_table.setHorizontalHeaderItem(2, item)
        item.setIcon(icon3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/login_128.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtGui.QTableWidgetItem()
        self.key_table.setHorizontalHeaderItem(3, item)
        item.setIcon(icon4)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/wifi_5.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtGui.QTableWidgetItem()
        self.key_table.setHorizontalHeaderItem(4, item)
        item.setIcon(icon5)
        self.verticalLayout_2.addWidget(self.key_table)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.save_button = QtGui.QPushButton(database)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.save_button.setFont(font)
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.horizontalLayout.addWidget(self.save_button)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.insert_button = QtGui.QPushButton(database)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.insert_button.sizePolicy().hasHeightForWidth())
        self.insert_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.insert_button.setFont(font)
        self.insert_button.setObjectName(_fromUtf8("insert_button"))
        self.horizontalLayout.addWidget(self.insert_button)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.delete_button = QtGui.QPushButton(database)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName(_fromUtf8("delete_button"))
        self.horizontalLayout.addWidget(self.delete_button)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(database)
        QtCore.QMetaObject.connectSlotsByName(database)

    def retranslateUi(self, database):
        database.setWindowTitle(QtGui.QApplication.translate("database", "Fern - Key Database", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("database", "Decrypted wireless keys are automatically added to the sqlite database after a successful", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("database", "attack, Alternatively you can insert keys to the database manually", None, QtGui.QApplication.UnicodeUTF8))
        self.key_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("database", "Access Point", None, QtGui.QApplication.UnicodeUTF8))
        self.key_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("database", "Mac Address", None, QtGui.QApplication.UnicodeUTF8))
        self.key_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("database", "Encryption", None, QtGui.QApplication.UnicodeUTF8))
        self.key_table.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("database", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.key_table.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("database", "Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.save_button.setText(QtGui.QApplication.translate("database", "Save Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.insert_button.setText(QtGui.QApplication.translate("database", "Insert New Key", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_button.setText(QtGui.QApplication.translate("database", "Delete", None, QtGui.QApplication.UnicodeUTF8))

