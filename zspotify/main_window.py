# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(900, 750))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 60))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchInput = QtWidgets.QLineEdit(self.widget)
        self.searchInput.setMinimumSize(QtCore.QSize(250, 0))
        self.searchInput.setMaximumSize(QtCore.QSize(350, 16777215))
        self.searchInput.setObjectName("searchInput")
        self.horizontalLayout_2.addWidget(self.searchInput)
        self.searchBtn = QtWidgets.QPushButton(self.widget)
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout_2.addWidget(self.searchBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.accountTypeLabel = QtWidgets.QLabel(self.widget)
        self.accountTypeLabel.setText("")
        self.accountTypeLabel.setObjectName("accountTypeLabel")
        self.horizontalLayout_2.addWidget(self.accountTypeLabel)
        self.loginBtn = QtWidgets.QPushButton(self.widget)
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout_2.addWidget(self.loginBtn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(300, 65))
        self.label.setMaximumSize(QtCore.QSize(300, 65))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("../resources/ZSpotifyBannerTP.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.resultTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.resultTabs.setMovable(False)
        self.resultTabs.setObjectName("resultTabs")
        self.songsTab = QtWidgets.QWidget()
        self.songsTab.setObjectName("songsTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.songsTab)
        self.verticalLayout_4.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.songsTree = QtWidgets.QTreeWidget(self.songsTab)
        self.songsTree.setDragEnabled(False)
        self.songsTree.setAlternatingRowColors(True)
        self.songsTree.setAnimated(True)
        self.songsTree.setObjectName("songsTree")
        self.songsTree.header().setDefaultSectionSize(230)
        self.songsTree.header().setMinimumSectionSize(15)
        self.verticalLayout_4.addWidget(self.songsTree)
        self.resultTabs.addTab(self.songsTab, "")
        self.artistsTab = QtWidgets.QWidget()
        self.artistsTab.setObjectName("artistsTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.artistsTab)
        self.verticalLayout_5.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.artistsTree = QtWidgets.QTreeWidget(self.artistsTab)
        self.artistsTree.setAlternatingRowColors(True)
        self.artistsTree.setAnimated(True)
        self.artistsTree.setObjectName("artistsTree")
        self.artistsTree.header().setDefaultSectionSize(230)
        self.artistsTree.header().setMinimumSectionSize(15)
        self.verticalLayout_5.addWidget(self.artistsTree)
        self.resultTabs.addTab(self.artistsTab, "")
        self.albumsTab = QtWidgets.QWidget()
        self.albumsTab.setObjectName("albumsTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.albumsTab)
        self.verticalLayout_6.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.albumsTree = QtWidgets.QTreeWidget(self.albumsTab)
        self.albumsTree.setAlternatingRowColors(True)
        self.albumsTree.setAnimated(True)
        self.albumsTree.setObjectName("albumsTree")
        self.albumsTree.header().setDefaultSectionSize(230)
        self.albumsTree.header().setMinimumSectionSize(15)
        self.verticalLayout_6.addWidget(self.albumsTree)
        self.resultTabs.addTab(self.albumsTab, "")
        self.playlistsTab = QtWidgets.QWidget()
        self.playlistsTab.setObjectName("playlistsTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.playlistsTab)
        self.verticalLayout_7.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.playlistsTree = QtWidgets.QTreeWidget(self.playlistsTab)
        self.playlistsTree.setAlternatingRowColors(True)
        self.playlistsTree.setAnimated(True)
        self.playlistsTree.setObjectName("playlistsTree")
        self.playlistsTree.header().setDefaultSectionSize(230)
        self.playlistsTree.header().setMinimumSectionSize(15)
        self.verticalLayout_7.addWidget(self.playlistsTree)
        self.resultTabs.addTab(self.playlistsTab, "")
        self.horizontalLayout.addWidget(self.resultTabs)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(315, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.coverArtLabel = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coverArtLabel.sizePolicy().hasHeightForWidth())
        self.coverArtLabel.setSizePolicy(sizePolicy)
        self.coverArtLabel.setMinimumSize(QtCore.QSize(300, 300))
        self.coverArtLabel.setMaximumSize(QtCore.QSize(300, 300))
        self.coverArtLabel.setSizeIncrement(QtCore.QSize(16, 16))
        self.coverArtLabel.setText("")
        self.coverArtLabel.setTextFormat(QtCore.Qt.RichText)
        self.coverArtLabel.setPixmap(QtGui.QPixmap("../resources/cover_default.jpg"))
        self.coverArtLabel.setScaledContents(True)
        self.coverArtLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.coverArtLabel.setObjectName("coverArtLabel")
        self.horizontalLayout_3.addWidget(self.coverArtLabel)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(15, 10, -1, -1)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.infoHeader1 = QtWidgets.QLabel(self.widget_2)
        self.infoHeader1.setText("")
        self.infoHeader1.setObjectName("infoHeader1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.infoHeader1)
        self.infoLabel1 = QtWidgets.QLabel(self.widget_2)
        self.infoLabel1.setText("")
        self.infoLabel1.setObjectName("infoLabel1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.infoLabel1)
        self.infoHeader2 = QtWidgets.QLabel(self.widget_2)
        self.infoHeader2.setText("")
        self.infoHeader2.setObjectName("infoHeader2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.infoHeader2)
        self.infoLabel2 = QtWidgets.QLabel(self.widget_2)
        self.infoLabel2.setText("")
        self.infoLabel2.setObjectName("infoLabel2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.infoLabel2)
        self.infoHeader3 = QtWidgets.QLabel(self.widget_2)
        self.infoHeader3.setText("")
        self.infoHeader3.setObjectName("infoHeader3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.infoHeader3)
        self.infoLabel3 = QtWidgets.QLabel(self.widget_2)
        self.infoLabel3.setText("")
        self.infoLabel3.setObjectName("infoLabel3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.infoLabel3)
        self.infoHeader4 = QtWidgets.QLabel(self.widget_2)
        self.infoHeader4.setText("")
        self.infoHeader4.setObjectName("infoHeader4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.infoHeader4)
        self.infoLabel4 = QtWidgets.QLabel(self.widget_2)
        self.infoLabel4.setText("")
        self.infoLabel4.setObjectName("infoLabel4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.infoLabel4)
        self.infoHeader5 = QtWidgets.QLabel(self.widget_2)
        self.infoHeader5.setText("")
        self.infoHeader5.setObjectName("infoHeader5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.infoHeader5)
        self.infoLabel5 = QtWidgets.QLabel(self.widget_2)
        self.infoLabel5.setText("")
        self.infoLabel5.setObjectName("infoLabel5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.infoLabel5)
        self.infoHeader6 = QtWidgets.QLabel(self.widget_2)
        self.infoHeader6.setText("")
        self.infoHeader6.setObjectName("infoHeader6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.infoHeader6)
        self.infoLabel6 = QtWidgets.QLabel(self.widget_2)
        self.infoLabel6.setText("")
        self.infoLabel6.setObjectName("infoLabel6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.infoLabel6)
        self.verticalLayout_8.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.formLayout_2.setContentsMargins(15, 0, -1, 5)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.dlQualityHeader = QtWidgets.QLabel(self.widget_2)
        self.dlQualityHeader.setObjectName("dlQualityHeader")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dlQualityHeader)
        self.dlQualityLabel = QtWidgets.QLabel(self.widget_2)
        self.dlQualityLabel.setObjectName("dlQualityLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dlQualityLabel)
        self.fileFormatHeader = QtWidgets.QLabel(self.widget_2)
        self.fileFormatHeader.setObjectName("fileFormatHeader")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fileFormatHeader)
        self.fileFormatCombo = QtWidgets.QComboBox(self.widget_2)
        self.fileFormatCombo.setMaximumSize(QtCore.QSize(80, 16777215))
        self.fileFormatCombo.setObjectName("fileFormatCombo")
        self.fileFormatCombo.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fileFormatCombo)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.realTimeCheckBox = QtWidgets.QCheckBox(self.widget_2)
        self.realTimeCheckBox.setText("")
        self.realTimeCheckBox.setChecked(True)
        self.realTimeCheckBox.setTristate(False)
        self.realTimeCheckBox.setObjectName("realTimeCheckBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.realTimeCheckBox)
        self.verticalLayout_8.addLayout(self.formLayout_2)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.downloadInfoLabel = QtWidgets.QLabel(self.widget_2)
        self.downloadInfoLabel.setText("")
        self.downloadInfoLabel.setObjectName("downloadInfoLabel")
        self.verticalLayout_9.addWidget(self.downloadInfoLabel)
        self.progressBar = QtWidgets.QProgressBar(self.widget_2)
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 12))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_9.addWidget(self.progressBar)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.downloadBtn = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadBtn.sizePolicy().hasHeightForWidth())
        self.downloadBtn.setSizePolicy(sizePolicy)
        self.downloadBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.downloadBtn.setMaximumSize(QtCore.QSize(160, 16777215))
        self.downloadBtn.setObjectName("downloadBtn")
        self.horizontalLayout_4.addWidget(self.downloadBtn)
        self.dirBtn = QtWidgets.QPushButton(self.widget_2)
        self.dirBtn.setMinimumSize(QtCore.QSize(30, 0))
        self.dirBtn.setMaximumSize(QtCore.QSize(40, 40))
        self.dirBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/folderIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dirBtn.setIcon(icon)
        self.dirBtn.setObjectName("dirBtn")
        self.horizontalLayout_4.addWidget(self.dirBtn)
        self.horizontalLayout_4.setStretch(1, 3)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.resultTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ZSpotify"))
        self.searchInput.setPlaceholderText(_translate("MainWindow", "Search Spotify"))
        self.searchBtn.setText(_translate("MainWindow", "Search"))
        self.loginBtn.setText(_translate("MainWindow", "Login"))
        self.songsTree.headerItem().setText(0, _translate("MainWindow", "Index"))
        self.songsTree.headerItem().setText(1, _translate("MainWindow", "Title"))
        self.songsTree.headerItem().setText(2, _translate("MainWindow", "Artists"))
        self.songsTree.headerItem().setText(3, _translate("MainWindow", "Album"))
        self.songsTree.headerItem().setText(4, _translate("MainWindow", "Duration"))
        self.songsTree.headerItem().setText(5, _translate("MainWindow", "Release Date"))
        self.resultTabs.setTabText(self.resultTabs.indexOf(self.songsTab), _translate("MainWindow", "Songs"))
        self.artistsTree.headerItem().setText(0, _translate("MainWindow", "Index"))
        self.artistsTree.headerItem().setText(1, _translate("MainWindow", "Name"))
        self.resultTabs.setTabText(self.resultTabs.indexOf(self.artistsTab), _translate("MainWindow", "Artists"))
        self.albumsTree.headerItem().setText(0, _translate("MainWindow", "Index"))
        self.albumsTree.headerItem().setText(1, _translate("MainWindow", "Title"))
        self.albumsTree.headerItem().setText(2, _translate("MainWindow", "Artists"))
        self.albumsTree.headerItem().setText(3, _translate("MainWindow", "Total Tracks"))
        self.albumsTree.headerItem().setText(4, _translate("MainWindow", "Release Date"))
        self.resultTabs.setTabText(self.resultTabs.indexOf(self.albumsTab), _translate("MainWindow", "Albums"))
        self.playlistsTree.headerItem().setText(0, _translate("MainWindow", "Index"))
        self.playlistsTree.headerItem().setText(1, _translate("MainWindow", "Title"))
        self.playlistsTree.headerItem().setText(2, _translate("MainWindow", "Creator"))
        self.playlistsTree.headerItem().setText(3, _translate("MainWindow", "Total Tracks"))
        self.resultTabs.setTabText(self.resultTabs.indexOf(self.playlistsTab), _translate("MainWindow", "Playlists"))
        self.dlQualityHeader.setText(_translate("MainWindow", "Download Quality:"))
        self.dlQualityLabel.setText(_translate("MainWindow", "320kbps"))
        self.fileFormatHeader.setText(_translate("MainWindow", "File Format:"))
        self.fileFormatCombo.setItemText(0, _translate("MainWindow", ".mp3"))
        self.label_2.setText(_translate("MainWindow", "Download in real time:"))
        self.downloadBtn.setText(_translate("MainWindow", "Download "))
        self.dirBtn.setToolTip(_translate("MainWindow", "Change download directory"))
