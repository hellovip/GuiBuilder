# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiBuilder.ui'
#
# Created: Sat Feb  2 16:04:57 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1004, 678)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pages = QtGui.QStackedWidget(self.centralwidget)
        self.pages.setObjectName("pages")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtGui.QVBoxLayout(self.page)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtGui.QFrame(self.page)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.frame_4.setPalette(palette)
        self.frame_4.setStyleSheet("#frame_4{\n"
"    background:white;\n"
"}")
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.continueEditing = QtGui.QPushButton(self.frame_4)
        self.continueEditing.setStyleSheet("")
        self.continueEditing.setObjectName("continueEditing")
        self.verticalLayout_13.addWidget(self.continueEditing)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_5 = QtGui.QLabel(self.frame_4)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("icons/startpage.png"))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_13.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(20, 69, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem3)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.recentlyOpened = QtGui.QComboBox(self.frame_4)
        self.recentlyOpened.setMinimumSize(QtCore.QSize(300, 0))
        self.recentlyOpened.setObjectName("recentlyOpened")
        self.recentlyOpened.addItem("")
        self.horizontalLayout_10.addWidget(self.recentlyOpened)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        spacerItem6 = QtGui.QSpacerItem(20, 77, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_13.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.open = QtGui.QPushButton(self.frame_4)
        self.open.setAccessibleName("")
        self.open.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.open.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open.setIcon(icon)
        self.open.setIconSize(QtCore.QSize(64, 64))
        self.open.setDefault(False)
        self.open.setFlat(False)
        self.open.setProperty("class", "")
        self.open.setObjectName("open")
        self.horizontalLayout_4.addWidget(self.open)
        self.newTemplate = QtGui.QPushButton(self.frame_4)
        self.newTemplate.setCursor(QtCore.Qt.ArrowCursor)
        self.newTemplate.setStatusTip("")
        self.newTemplate.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newTemplate.setIcon(icon1)
        self.newTemplate.setIconSize(QtCore.QSize(64, 64))
        self.newTemplate.setDefault(False)
        self.newTemplate.setFlat(False)
        self.newTemplate.setObjectName("newTemplate")
        self.horizontalLayout_4.addWidget(self.newTemplate)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_13.addLayout(self.horizontalLayout_6)
        spacerItem9 = QtGui.QSpacerItem(20, 69, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem9)
        self.verticalLayout.addWidget(self.frame_4)
        self.pages.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.toolbar = QtGui.QFrame(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbar.sizePolicy().hasHeightForWidth())
        self.toolbar.setSizePolicy(sizePolicy)
        self.toolbar.setStyleSheet("")
        self.toolbar.setFrameShape(QtGui.QFrame.NoFrame)
        self.toolbar.setFrameShadow(QtGui.QFrame.Raised)
        self.toolbar.setObjectName("toolbar")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.toolbar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.backToStartPage = QtGui.QPushButton(self.toolbar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backToStartPage.sizePolicy().hasHeightForWidth())
        self.backToStartPage.setSizePolicy(sizePolicy)
        self.backToStartPage.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backToStartPage.setIcon(icon2)
        self.backToStartPage.setIconSize(QtCore.QSize(32, 32))
        self.backToStartPage.setFlat(False)
        self.backToStartPage.setObjectName("backToStartPage")
        self.horizontalLayout_2.addWidget(self.backToStartPage)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.reload = QtGui.QPushButton(self.toolbar)
        self.reload.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload.setIcon(icon3)
        self.reload.setIconSize(QtCore.QSize(32, 32))
        self.reload.setFlat(False)
        self.reload.setObjectName("reload")
        self.horizontalLayout_2.addWidget(self.reload)
        self.save = QtGui.QPushButton(self.toolbar)
        self.save.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/filesave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon4)
        self.save.setIconSize(QtCore.QSize(32, 32))
        self.save.setAutoDefault(False)
        self.save.setFlat(False)
        self.save.setObjectName("save")
        self.horizontalLayout_2.addWidget(self.save)
        self.saveAs = QtGui.QPushButton(self.toolbar)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/filesaveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveAs.setIcon(icon5)
        self.saveAs.setIconSize(QtCore.QSize(32, 32))
        self.saveAs.setFlat(False)
        self.saveAs.setObjectName("saveAs")
        self.horizontalLayout_2.addWidget(self.saveAs)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.documentation = QtGui.QPushButton(self.toolbar)
        self.documentation.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/documentation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.documentation.setIcon(icon6)
        self.documentation.setIconSize(QtCore.QSize(32, 32))
        self.documentation.setFlat(False)
        self.documentation.setObjectName("documentation")
        self.horizontalLayout_2.addWidget(self.documentation)
        self.verticalLayout_11.addWidget(self.toolbar)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.addElementFrame = QtGui.QFrame(self.page_2)
        self.addElementFrame.setMinimumSize(QtCore.QSize(240, 0))
        self.addElementFrame.setMaximumSize(QtCore.QSize(240, 16777215))
        self.addElementFrame.setStyleSheet("#addElementFrame{background-white;}")
        self.addElementFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.addElementFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.addElementFrame.setObjectName("addElementFrame")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.addElementFrame)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtGui.QLabel(self.addElementFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/find.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.filter = QtGui.QLineEdit(self.addElementFrame)
        self.filter.setObjectName("filter")
        self.horizontalLayout_8.addWidget(self.filter)
        self.cancelFilter = QtGui.QToolButton(self.addElementFrame)
        self.cancelFilter.setEnabled(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelFilter.setIcon(icon7)
        self.cancelFilter.setIconSize(QtCore.QSize(16, 16))
        self.cancelFilter.setAutoRaise(True)
        self.cancelFilter.setObjectName("cancelFilter")
        self.horizontalLayout_8.addWidget(self.cancelFilter)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.browserView = QtGui.QStackedWidget(self.addElementFrame)
        self.browserView.setObjectName("browserView")
        self.elementsFrame = QtGui.QWidget()
        self.elementsFrame.setObjectName("elementsFrame")
        self.gridLayout = QtGui.QGridLayout(self.elementsFrame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.elements = QtGui.QToolBox(self.elementsFrame)
        self.elements.setObjectName("elements")
        self.page_4 = QtGui.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 240, 539))
        self.page_4.setObjectName("page_4")
        self.elements.addItem(self.page_4, "")
        self.gridLayout.addWidget(self.elements, 0, 0, 1, 1)
        self.browserView.addWidget(self.elementsFrame)
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName("page_7")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.page_7)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.searchResults = QtGui.QListWidget(self.page_7)
        self.searchResults.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.searchResults.setIconSize(QtCore.QSize(32, 32))
        self.searchResults.setObjectName("searchResults")
        self.verticalLayout_12.addWidget(self.searchResults)
        self.browserView.addWidget(self.page_7)
        self.verticalLayout_8.addWidget(self.browserView)
        self.horizontalLayout_12.addWidget(self.addElementFrame)
        self.splitter = QtGui.QSplitter(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setStyleSheet("#splitter{background-color:rgb(204, 204, 204);}")
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(7)
        self.splitter.setObjectName("splitter")
        self.frame_3 = QtGui.QFrame(self.splitter)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.preview = QtWebKit.QWebView(self.frame_3)
        self.preview.setStyleSheet("")
        self.preview.setUrl(QtCore.QUrl("about:blank"))
        self.preview.setObjectName("preview")
        self.verticalLayout_2.addWidget(self.preview)
        self.treeStructureFrame = QtGui.QFrame(self.splitter)
        self.treeStructureFrame.setStyleSheet("#frame_5\n"
"{\n"
"background-color:white;\n"
"}")
        self.treeStructureFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.treeStructureFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.treeStructureFrame.setObjectName("treeStructureFrame")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.treeStructureFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtGui.QTabWidget(self.treeStructureFrame)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setStyleSheet("#tab\n"
"{\n"
"background:white;\n"
"}")
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.expand = QtGui.QPushButton(self.tab)
        self.expand.setStyleSheet("")
        self.expand.setIconSize(QtCore.QSize(22, 22))
        self.expand.setFlat(False)
        self.expand.setObjectName("expand")
        self.horizontalLayout_7.addWidget(self.expand)
        self.collapse = QtGui.QPushButton(self.tab)
        self.collapse.setStyleSheet("")
        self.collapse.setIconSize(QtCore.QSize(22, 22))
        self.collapse.setFlat(False)
        self.collapse.setObjectName("collapse")
        self.horizontalLayout_7.addWidget(self.collapse)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.baseLayout = QtGui.QComboBox(self.tab)
        self.baseLayout.setStyleSheet("background:white;")
        self.baseLayout.setObjectName("baseLayout")
        self.baseLayout.addItem("")
        self.baseLayout.addItem("")
        self.baseLayout.addItem("")
        self.baseLayout.addItem("")
        self.baseLayout.addItem("")
        self.horizontalLayout_7.addWidget(self.baseLayout)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.deleteFromTree = QtGui.QPushButton(self.tab)
        self.deleteFromTree.setStyleSheet("")
        self.deleteFromTree.setIconSize(QtCore.QSize(22, 22))
        self.deleteFromTree.setFlat(False)
        self.deleteFromTree.setObjectName("deleteFromTree")
        self.horizontalLayout_7.addWidget(self.deleteFromTree)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.tree = QtGui.QTreeWidget(self.tab)
        self.tree.setStyleSheet("background:white;")
        self.tree.setDragEnabled(True)
        self.tree.setDragDropOverwriteMode(False)
        self.tree.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.tree.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tree.setAlternatingRowColors(True)
        self.tree.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tree.setIconSize(QtCore.QSize(32, 32))
        self.tree.setHeaderHidden(True)
        self.tree.setColumnCount(5)
        self.tree.setObjectName("tree")
        self.tree.header().setVisible(False)
        self.tree.header().setCascadingSectionResizes(False)
        self.tree.header().setDefaultSectionSize(92)
        self.tree.header().setSortIndicatorShown(False)
        self.verticalLayout_5.addWidget(self.tree)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.wuiXML = QtGui.QTextEdit(self.tab_2)
        self.wuiXML.setObjectName("wuiXML")
        self.verticalLayout_4.addWidget(self.wuiXML)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.wuiSHPAML = QtGui.QTextEdit(self.tab_3)
        self.wuiSHPAML.setObjectName("wuiSHPAML")
        self.verticalLayout_7.addWidget(self.wuiSHPAML)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout_12.addWidget(self.splitter)
        self.elementFrame = QtGui.QFrame(self.page_2)
        self.elementFrame.setMinimumSize(QtCore.QSize(300, 0))
        self.elementFrame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.elementFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.elementFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.elementFrame.setObjectName("elementFrame")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.elementFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget_2 = QtGui.QTabWidget(self.elementFrame)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.propertiesTab = QtGui.QWidget()
        self.propertiesTab.setObjectName("propertiesTab")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.propertiesTab)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.scrollArea = QtGui.QScrollArea(self.propertiesTab)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 296, 572))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.properties = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        self.properties.setLineWidth(1)
        self.properties.setShowGrid(False)
        self.properties.setGridStyle(QtCore.Qt.NoPen)
        self.properties.setWordWrap(True)
        self.properties.setObjectName("properties")
        self.properties.setColumnCount(0)
        self.properties.setRowCount(0)
        self.properties.horizontalHeader().setVisible(False)
        self.properties.horizontalHeader().setHighlightSections(False)
        self.properties.verticalHeader().setVisible(False)
        self.properties.verticalHeader().setHighlightSections(False)
        self.verticalLayout_9.addWidget(self.properties)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_9.addWidget(self.scrollArea)
        self.tabWidget_2.addTab(self.propertiesTab, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.info = QtGui.QTextBrowser(self.tab_4)
        self.info.setFrameShape(QtGui.QFrame.NoFrame)
        self.info.setFrameShadow(QtGui.QFrame.Plain)
        self.info.setLineWidth(0)
        self.info.setObjectName("info")
        self.verticalLayout_10.addWidget(self.info)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.verticalLayout_6.addWidget(self.tabWidget_2)
        self.horizontalLayout_12.addWidget(self.elementFrame)
        self.verticalLayout_11.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.toggleElementsFrame = QtGui.QPushButton(self.page_2)
        self.toggleElementsFrame.setMinimumSize(QtCore.QSize(240, 0))
        self.toggleElementsFrame.setMaximumSize(QtCore.QSize(240, 16777215))
        self.toggleElementsFrame.setCheckable(True)
        self.toggleElementsFrame.setChecked(True)
        self.toggleElementsFrame.setFlat(False)
        self.toggleElementsFrame.setObjectName("toggleElementsFrame")
        self.horizontalLayout_11.addWidget(self.toggleElementsFrame)
        self.toggleTreeStructureFrame = QtGui.QPushButton(self.page_2)
        self.toggleTreeStructureFrame.setCheckable(True)
        self.toggleTreeStructureFrame.setChecked(True)
        self.toggleTreeStructureFrame.setObjectName("toggleTreeStructureFrame")
        self.horizontalLayout_11.addWidget(self.toggleTreeStructureFrame)
        self.toggleElementFrame = QtGui.QPushButton(self.page_2)
        self.toggleElementFrame.setMinimumSize(QtCore.QSize(300, 0))
        self.toggleElementFrame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.toggleElementFrame.setCheckable(True)
        self.toggleElementFrame.setChecked(True)
        self.toggleElementFrame.setObjectName("toggleElementFrame")
        self.horizontalLayout_11.addWidget(self.toggleElementFrame)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        self.pages.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.pages)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pages.setCurrentIndex(0)
        self.browserView.setCurrentIndex(0)
        self.elements.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QObject.connect(self.toggleElementsFrame, QtCore.SIGNAL("toggled(bool)"), self.addElementFrame.setVisible)
        QtCore.QObject.connect(self.toggleElementFrame, QtCore.SIGNAL("toggled(bool)"), self.elementFrame.setVisible)
        QtCore.QObject.connect(self.toggleTreeStructureFrame, QtCore.SIGNAL("toggled(bool)"), self.treeStructureFrame.setVisible)
        QtCore.QObject.connect(self.toggleElementsFrame, QtCore.SIGNAL("toggled(bool)"), self.filter.setFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.continueEditing.setText(QtGui.QApplication.translate("MainWindow", "Continues Editing \'file\' >", None, QtGui.QApplication.UnicodeUTF8))
        self.recentlyOpened.setItemText(0, QtGui.QApplication.translate("MainWindow", "Open Recent...", None, QtGui.QApplication.UnicodeUTF8))
        self.open.setText(QtGui.QApplication.translate("MainWindow", "Open Template", None, QtGui.QApplication.UnicodeUTF8))
        self.newTemplate.setText(QtGui.QApplication.translate("MainWindow", "Create New Template", None, QtGui.QApplication.UnicodeUTF8))
        self.newTemplate.setProperty("class", QtGui.QApplication.translate("MainWindow", "MainAction", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAs.setText(QtGui.QApplication.translate("MainWindow", "Save as..", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelFilter.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.elements.setItemText(self.elements.indexOf(self.page_4), QtGui.QApplication.translate("MainWindow", "Page 2", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_3.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background:white;", None, QtGui.QApplication.UnicodeUTF8))
        self.expand.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.collapse.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Layout:", None, QtGui.QApplication.UnicodeUTF8))
        self.baseLayout.setItemText(0, QtGui.QApplication.translate("MainWindow", "flow", None, QtGui.QApplication.UnicodeUTF8))
        self.baseLayout.setItemText(1, QtGui.QApplication.translate("MainWindow", "fields", None, QtGui.QApplication.UnicodeUTF8))
        self.baseLayout.setItemText(2, QtGui.QApplication.translate("MainWindow", "box", None, QtGui.QApplication.UnicodeUTF8))
        self.baseLayout.setItemText(3, QtGui.QApplication.translate("MainWindow", "vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.baseLayout.setItemText(4, QtGui.QApplication.translate("MainWindow", "horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteFromTree.setText(QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.tree.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Element", None, QtGui.QApplication.UnicodeUTF8))
        self.tree.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Id", None, QtGui.QApplication.UnicodeUTF8))
        self.tree.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tree.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Accessor", None, QtGui.QApplication.UnicodeUTF8))
        self.tree.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "renderingOrder", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tree Structure", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "XML", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "SHPAML", None, QtGui.QApplication.UnicodeUTF8))
        self.elementFrame.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background:white;", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.propertiesTab), QtGui.QApplication.translate("MainWindow", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.toggleElementsFrame.setText(QtGui.QApplication.translate("MainWindow", "Add Element", None, QtGui.QApplication.UnicodeUTF8))
        self.toggleTreeStructureFrame.setText(QtGui.QApplication.translate("MainWindow", "View / Modify Tree Structure", None, QtGui.QApplication.UnicodeUTF8))
        self.toggleElementFrame.setText(QtGui.QApplication.translate("MainWindow", "Element Information", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
