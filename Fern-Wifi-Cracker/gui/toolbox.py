import os
from main_window import font_size
from PyQt4 import QtCore, QtGui

font_setting = font_size()

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class toolbox_win(object):
    def setupUi(self, toolbox_win):
        toolbox_win.setObjectName(_fromUtf8("toolbox_win"))
        toolbox_win.resize(736, 304)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/1295905972_tool_kit.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        toolbox_win.setWindowIcon(icon)
        self.verticalLayout_5 = QtGui.QVBoxLayout(toolbox_win)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(11, 92, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(190, 10, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/map.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(78, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem3 = QtGui.QSpacerItem(11, 92, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        spacerItem4 = QtGui.QSpacerItem(190, 10, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/cookies-icon.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem5 = QtGui.QSpacerItem(78, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem6 = QtGui.QSpacerItem(11, 92, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        spacerItem7 = QtGui.QSpacerItem(190, 10, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        icon3 = QtGui.QIcon()
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.groupBox = QtGui.QGroupBox(toolbox_win)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem9 = QtGui.QSpacerItem(20, 80, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem10 = QtGui.QSpacerItem(158, 10, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem10)
        self.pushButton = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.pushButton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/1295906241_preferences-desktop-font.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(48, 49))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem11 = QtGui.QSpacerItem(63, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem12 = QtGui.QSpacerItem(20, 80, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem13 = QtGui.QSpacerItem(158, 10, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem13)
        self.attack_options_button = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attack_options_button.sizePolicy().hasHeightForWidth())
        self.attack_options_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.attack_options_button.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/wifi_4.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.attack_options_button.setIcon(icon5)
        self.attack_options_button.setIconSize(QtCore.QSize(48, 49))
        self.attack_options_button.setObjectName(_fromUtf8("attack_options_button"))
        self.verticalLayout_4.addWidget(self.attack_options_button)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem14 = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.verticalLayout_5.addWidget(self.groupBox)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem15)

        self.retranslateUi(toolbox_win)
        QtCore.QMetaObject.connectSlotsByName(toolbox_win)

    def retranslateUi(self, toolbox_win):
        toolbox_win.setWindowTitle(QtGui.QApplication.translate("toolbox_win", "Fern - ToolBox", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("toolbox_win", "General Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("toolbox_win", "Font Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.attack_options_button.setText(QtGui.QApplication.translate("toolbox_win", "WIFI Attack Options", None, QtGui.QApplication.UnicodeUTF8))

