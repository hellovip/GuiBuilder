#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    WebElementDocs.py

    Provides a visual UI from which to browse the accessible WebElements and their documentation.

    Copyright (C) 2013  Timothy Edmund Crosley

    This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation; either version 2
    of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''

import inspect
import copy
import os
import sys
import types
from subprocess import Popen

try:
    from PySide.QtCore import *
    from PySide.QtGui import *
    from PySide.QtWebKit import *
    from .WebElementDocsView import Ui_MainWindow
    USING_PYQT = False
    USING_PYSIDE = True
except ImportError:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtWebKit import *
    from .WebElementDocsViewPyQt import Ui_MainWindow
    USING_PYQT = True
    USING_PYSIDE = False

from WebElements.MultiplePythonSupport import *

from . import GuiBuilderConfig


class WebElementDocs(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('WebElement Documentation Browser')
        self.setWindowIcon(QIcon('icons/documentation.png'))

        self.genericElementIcon = QIcon('icons/elements/generic.png')
        self.populateElements()
        self.ui.cancelFilter.hide()

        self.connect(self.ui.filter, SIGNAL('textChanged(const QString &)'), self.filterItemBrowser)
        self.connect(self.ui.cancelFilter, SIGNAL("clicked()"), self.clearFilter)
        self.connect(self.ui.searchResults, SIGNAL("currentItemChanged(QListWidgetItem *, QListWidgetItem *)"),
                     self.updateDocumentation)

    def updateDocumentation(self, item, ignored):
        if not item or not item.text():
            return

        item = unicode(item.text())
        product = GuiBuilderConfig.Factory.build(item.lower(), "", "")
        if not product:
            self.ui.info.setText("")
            return

        text = "<h2>" + item + "</h2>"
        text += "<p>" + (product.__doc__ or "") + "</p>"

        text += "<p><b>signals:</b><br />" + "<br />".join(product.signals) + "</p>"

        for attributeName in dir(product):
            if attributeName.startswith("_"):
                continue

            attribute = getattr(product, attributeName, None)
            formattedName = attributeName
            try:
                argSpec = inspect.getargspec(attribute)
                parmeters = []
                for parameter in argSpec.args:
                    parmeters.append(str(parameter))
                for index, default in enumerate(reversed(argSpec.defaults or [])):
                    parmeters[-(index + 1)] += "=" + str(default)
                formattedName += "(" + ", ".join(parmeters) + ")"
            except:
                pass
            if type(attribute) in [types.FunctionType, types.MethodType] and attribute.__doc__:
                text += "<p><b>" + formattedName + "</b>" + \
                        attribute.__doc__.replace("\n", "<br />") + "</p>"

        self.ui.info.setText(text)

    def clearFilter(self):
        self.ui.filter.setText('')

    def filterItemBrowser(self, text):
        if not text:
            self.ui.cancelFilter.hide()
            return self.ui.browserView.setCurrentIndex(0)

        self.ui.browserView.setCurrentIndex(1)
        self.ui.searchResults.clear()
        for productName, product in iteritems(GuiBuilderConfig.Factory.products):
            if str(text).lower() in str(productName).lower():
                newElement = QListWidgetItem(self.elementIcon(productName.split('.')[-1]), productName)
                newElement.setToolTip(product.__doc__ or "")
                newElement.properties = {}
                self.ui.searchResults.addItem(newElement)
        self.ui.cancelFilter.show()

    def elementIcon(self, elementName):
        iconName = "icons/elements/" + elementName.split('.')[-1].lower() + ".png"
        if os.path.isfile(iconName):
            return QIcon(iconName)
        else:
            return self.genericElementIcon

    def populateElements(self):
        self.ui.elementsFrame.layout().removeWidget(self.ui.elements)
        self.ui.elements = QToolBox()
        self.ui.elementsFrame.layout().addWidget(self.ui.elements)

        usedProducts = []
        for data in GuiBuilderConfig.sections:
            section = data['Name']
            icon = QIcon(data['Icon'])
            factory = data['Factory']

            elementSelector = QListWidget()
            self.connect(elementSelector, SIGNAL("currentItemChanged(QListWidgetItem *, QListWidgetItem *)"),
                     self.updateDocumentation)
            elementSelector.setIconSize(QSize(32, 32))
            elementSelector.setDragDropMode(elementSelector.DragOnly)
            for productName, product in iteritems(factory.products):
                if productName in usedProducts:
                    continue
                else:
                    usedProducts.append(productName)

                newElement = QListWidgetItem(self.elementIcon(productName), productName)
                newElement.setToolTip(product.__doc__ or "")
                newElement.properties = {}
                elementSelector.addItem(newElement)

            self.ui.elements.addItem(elementSelector, icon, section)


def run():
    os.chdir(os.path.dirname(__file__) or ".")

    app = QApplication(sys.argv)

    window = WebElementDocs()
    window.resize(900, 700)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
