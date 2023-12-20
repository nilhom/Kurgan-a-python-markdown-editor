import traceback, sys
import os
from os.path import *
import re
import shutil
import time
from html import unescape
# PyQt5
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.Qt import QDesktopServices, QUrl, QColor, Qt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QToolBar, QAction, QSpinBox, QTextEdit

# Dark theme. It is used no matter what VS-Code says
from design.darkTheme import breeze_resources
from design.generated import Ui_MainWindow

# Other .py files
from lib.mylib_pyqt import *
from lib.mylib_files import *

# Settings
logo = "icons/icon.png"

basePath = "./"
notesFolderName = "Notes"
notesPath = basePath + notesFolderName

rightSideFileName = "Archive/RightSide"
rightSidePath = notesPath + "/" + rightSideFileName

trashPath = "trash"

icons = {
    "folder": "📁",
    "app": "💾",
    "file": "🗒️",
    "list": "📓",
    "error": "❌"
}

dontIncludeBeta = [
    "🗒️desktop.ini"
]


# Emoji Helpers
def noEmoji(text):
    a = text
    for b in icons:
        a = a.replace(icons[b], "")
        if icons[b] in a: a = a[1:]
    a = a.strip()
    return a


def pathToIcon(path):
    if path.split("/")[-1].endswith(".app"): return icons["app"]
    if path.split("/")[-1].endswith(".list"): return icons["list"]
    if os.path.isfile(path): return icons["file"]
    if not os.path.isfile(path): return icons["folder"]
    return icons["error"]


def emoji_folderContents(path): return [f"{pathToIcon(path + '/' + x)}{x}" for x in getContentsFromPath(path)]


def noEmoji_getTexts(liste): return [noEmoji(a) for a in itemTexts_list(liste)]


# Path Helpers
def listToPath(liste): return basePath + f'/'.join(liste)


def getFolderOfPath(path):
    try:
        return "/".join(path.split("/")[:-1])
    except:
        return "/"


# Update
def updateBeta(self):
    self.pathFull = self.pathAlpha()
    try:
        liste = self.notesBeta
        liste.clear()
        path = self.pathAlpha()
        if self.notesAlpha.count() == 1: path = notesPath  # Just "Notes" in Alpha
        a = emoji_folderContents(path)

        a = [x for x in a if x not in dontIncludeBeta]

        for x in a:
            if icons["folder"] in x:
                liste.addItem(x)
        for y in a:
            if not icons["folder"] in y:
                liste.addItem(y)
        self.mainText.setPlainText("")
    except:
        pass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # path Stuff
    pathFull = notesPath

    def pathAlpha(self):
        return listToPath(noEmoji_getTexts(self.notesAlpha))

    # Text Toolbar colors
    red = '#d31717'
    lightred = '#ff6969'
    purple = '#9000ff'
    blue = '#1f33f1'
    orange = '#FFA500'
    yellow = '#fffc02'
    lightyellow = '#fffa69'
    preIcon = 'icons/'
    postIcon = '.png'

    # Rich Text Toolbar Create. Mostly copied from here:  https://github.com/The-Assembly/Code-A-Rich-Text-Editor-With-PyQt/blob/main/RTE/RTE.py
    def create_tool_bar(self):

        def mouseDoubleClickEvent(e):
            super(QTextEdit, self.mainText).mouseDoubleClickEvent(e)
            editor = self.mainText
            cursor = editor.textCursor()
            text = cursor.selectedText()

            html = cursor.selection().toHtml()
            if html and 'a href="' in html:
                fragment = html.split('<!--StartFragment-->')[1].split('<!--EndFragment-->')[0]
                insideHref = fragment.split('a href="')[1].split('">')[0]
                href = unescape(insideHref)

                color = re.findall(r'color:.*;', html)[0]
                color = fragment.split('color:')[1].split(';')[0]

                if color == self.blue:
                    QDesktopServices.openUrl(QUrl(href))
                elif color == self.lightyellow:
                    try:
                        t = self.mainText.toPlainText().replace('\\', '\\\\')
                        exec(f"text='''{t}'''\n{href}")  # [7:] remove "python:" at start
                        text = str(eval("out"))
                    except Exception as e:
                        traceback.print_exc()
                        text = str(e)
                    if len(text) < 250:
                        QMessageBox.about(self, "Result", text)
                    else:
                        QtWidgets.QInputDialog.getMultiLineText(self, "Python Skript", "Result:", text=text)
                elif color == self.lightred:
                    QtWidgets.QInputDialog.getMultiLineText(self, "Hidden Text", "Text:", text=href)

        self.mainText.mouseDoubleClickEvent = mouseDoubleClickEvent

        toolbar = QToolBar(parent=self.toolbarHolder_Frame)

        self.fontSizeBox = QSpinBox()
        self.fontSizeBox.setValue(16)
        self.fontSizeBox.valueChanged.connect(lambda: self.mainText.setFontPointSize(self.fontSizeBox.value()))
        toolbar.addWidget(self.fontSizeBox)

        toolbar.addSeparator()

        leftAllign = QAction(QIcon(self.preIcon + "leftalign" + self.postIcon), '', self)
        leftAllign.triggered.connect(lambda: self.mainText.setAlignment(Qt.AlignLeft))
        toolbar.addAction(leftAllign)

        centerAllign = QAction(QIcon(self.preIcon + "centeralign" + self.postIcon), '', self)
        centerAllign.triggered.connect(lambda: self.mainText.setAlignment(Qt.AlignCenter))
        toolbar.addAction(centerAllign)

        rightAllign = QAction(QIcon(self.preIcon + "rightalign" + self.postIcon), '', self)
        rightAllign.triggered.connect(lambda: self.mainText.setAlignment(Qt.AlignRight))
        toolbar.addAction(rightAllign)

        toolbar.addSeparator()

        boldBtn = QAction(QIcon(self.preIcon + "bold" + self.postIcon), '', self)
        boldBtn.triggered.connect(lambda: self.mainText.setFontWeight(QFont.Bold))
        toolbar.addAction(boldBtn)

        underlineBtn = QAction(QIcon(self.preIcon + "underline" + self.postIcon), '', self)
        underlineBtn.triggered.connect(lambda: self.mainText.setFontUnderline(True))
        toolbar.addAction(underlineBtn)

        italicBtn = QAction(QIcon(self.preIcon + "italic" + self.postIcon), '', self)
        italicBtn.triggered.connect(lambda: self.mainText.setFontItalic(True))
        toolbar.addAction(italicBtn)

        toolbar.addSeparator()

        def normal():
            self.fontSizeBox.setValue(16)
            # Clean Link
            editor = self.mainText
            cursor = editor.textCursor()
            text = cursor.selectedText()

            cursor.removeSelectedText()
            fmt = cursor.charFormat()
            fmt.setToolTip("")
            fmt.setAnchor(True)
            fmt.setAnchorHref("")
            fmt.setFontWeight(QFont.Medium)
            fmt.setFontItalic(False)
            fmt.setFontUnderline(False)
            fmt.setForeground(QtGui.QColor('#FFFFFF'))
            cursor.insertText(text, fmt)

        def h(num, color):
            self.mainText.setTextColor(QtGui.QColor(color))
            self.fontSizeBox.setValue(num)
            self.mainText.setFontWeight(QFont.Bold)

        h3 = QAction(QIcon(self.preIcon + "h3" + self.postIcon), '', self)
        h3.triggered.connect(lambda: h(18, self.yellow))
        toolbar.addAction(h3)

        h2 = QAction(QIcon(self.preIcon + "h2" + self.postIcon), '', self)
        h2.triggered.connect(lambda: h(20, self.orange))
        toolbar.addAction(h2)

        h1 = QAction(QIcon(self.preIcon + "h1" + self.postIcon), '', self)
        h1.triggered.connect(lambda: h(22, self.red))
        toolbar.addAction(h1)

        toolbar.addSeparator()

        def hrefMagic():
            editor = self.mainText
            cursor = editor.textCursor()
            text = cursor.selectedText()

            oldText = ""
            html = cursor.selection().toHtml()
            if html:
                fragment = re.findall(r'<!--StartFragment-->.*<!--EndFragment-->', html)[0]

                try:
                    color = re.findall(r'color:.*;', html)[0]
                    color = fragment.split('color:')[1].split(';')[0]
                except:
                    color = '#ffffff'
                    pass

                if 'a href="' in html:
                    insideHref = fragment.split('a href="')[1].split('">')[0]
                    oldText = unescape(insideHref)

            if re.match(r'\[.*\]\(.*\)', text):
                s = text.strip()
                text = re.findall(r'\[.*\]', s)[0][1:-1]
                inputText = re.findall(r'\(.*\)', s)[0][1:-1]
            else:
                inputText, okPressed = QtWidgets.QInputDialog.getMultiLineText(self, "Href Magic Text", "Text:",
                                                                               text=oldText)  # [7:] remove "python:" at start

            if okPressed and inputText:
                cursor.removeSelectedText()
                fmt = cursor.charFormat()
                fmt.setForeground(QColor(color))
                fmt.setFontUnderline(True)
                fmt.setAnchor(True)
                fmt.setAnchorHref(inputText)
                fmt.setToolTip(inputText)
                cursor.insertText(text, fmt)

        link = QAction(QIcon(self.preIcon + "link" + self.postIcon), '', self)
        link.triggered.connect(lambda: self.mainText.setTextColor(QtGui.QColor(self.blue)))
        toolbar.addAction(link)

        pylink = QAction(QIcon(self.preIcon + "python" + self.postIcon), '', self)
        pylink.triggered.connect(lambda: self.mainText.setTextColor(QtGui.QColor(self.lightyellow)))
        toolbar.addAction(pylink)

        hidden = QAction(QIcon(self.preIcon + "hidden" + self.postIcon), '', self)
        hidden.triggered.connect(lambda: self.mainText.setTextColor(QtGui.QColor(self.lightred)))
        toolbar.addAction(hidden)

        toolbar.addSeparator()

        t = QAction(QIcon(self.preIcon + "t" + self.postIcon), '', self)
        t.triggered.connect(hrefMagic)
        toolbar.addAction(t)

        n = QAction(QIcon(self.preIcon + "normal" + self.postIcon), '', self)
        n.triggered.connect(normal)
        toolbar.addAction(n)

    # __init__
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.notesBeta.installEventFilter(self)
        self.setWindowTitle("Kurgan")
        self.setWindowIcon(QtGui.QIcon(logo))
        self.create_tool_bar()
        self.noteWidgets = [self.notesAlpha, self.notesBeta]
        self.mainText.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextEditorInteraction)

        # Hide Button
        def hide_Button_Clicked():
            self.rightside.setVisible(not self.rightside.isVisible())

        self.hide_Button.clicked.connect(hide_Button_Clicked)

        # TextChanged
        def mainText_textChanged():
            if os.path.isfile(self.pathFull):
                text = self.mainText.toPlainText() if "." in self.pathFull.split("/")[-1] else self.mainText.toHtml()
                writeToFile(self.pathFull, text)
                if rightSidePath in self.pathFull or self.pathFull in rightSidePath: self.rightside.setHtml(
                    getTextFromFile(rightSidePath))

        self.mainText.textChanged.connect(mainText_textChanged)

        # Rightsides
        self.rightside.setHtml(getTextFromFile(rightSidePath))
        self.rightside.textChanged.connect(lambda: writeToFile(rightSidePath, self.rightside.toHtml()))

        # Icons
        kurganIcons = [self.topLeftIcon_label]

        for x in kurganIcons:
            x.setPixmap(QPixmap(logo))
            x.show()

        # First Start
        self.notesAlpha.addItem(notesFolderName)
        updateBeta(self)

        # Item Clicked / Mouse Events
        def alpha_itemClicked():
            liste = self.notesAlpha
            selText = noEmoji(getTextOfSelected_list(liste))

            if selText:
                index = indexOfSelected_list(liste)
                if liste.count() != index + 1:  # In Case Last Item in Alpha is Clicked
                    for x in reversed(range(0, liste.count())):
                        if (index or index == 0) and x > index:
                            removeItemPreserveSelection_list(liste, liste.item(x))

                updateBeta(self)
                setSelectedLastItem_list(liste)

        self.notesAlpha.itemClicked.connect(alpha_itemClicked)
        self.notesAlpha.itemSelectionChanged.connect(alpha_itemClicked)

        def beta_itemClicked():
            liste = self.notesBeta
            selText = noEmoji(getTextOfSelected_list(liste))
            self.pathFull = f"{self.pathAlpha()}/{selText}"

            if selText:
                if selText.endswith(".app"):
                    try:
                        name = selText.lower().replace(".app", "")
                        frame = eval(f"self.{name}_App_Frame")
                        frame.setHidden(False)
                        eval(f"self.{name}_show()")
                    except:
                        pass
                elif not os.path.isfile(self.pathFull):

                    self.notesAlpha.addItem(selText)
                    updateBeta(self)

                else:
                    text = getTextFromFile(self.pathFull)
                    if "." in selText:
                        self.mainText.setPlainText(text)
                    else:
                        self.mainText.setHtml(text)
                    self.mainText_Frame.setHidden(False)
                    self.mainText_Label.setText(getTextOfSelected_list(liste))

        self.beta_itemClicked = beta_itemClicked

        # 8 = MouseBack, 16 = MouseForward, 1 = leftClick, 2 = rightClick
        def notesAlpha_mousePressed(event):
            super(QtWidgets.QListWidget, self.notesAlpha).mousePressEvent(event)

            num = int(event.button())
            if num == 8:
                liste = self.notesAlpha
                select_list(liste, -2)
                alpha_itemClicked()

        self.notesAlpha.mousePressEvent = notesAlpha_mousePressed

        def notesBeta_mousePressed(event):
            super(QtWidgets.QListWidget, self.notesBeta).mousePressEvent(event)

            num = int(event.button())
            if num == 1:
                beta_itemClicked()
            elif num == 8:
                liste = self.notesAlpha
                select_list(liste, -2)
                alpha_itemClicked()

        self.notesBeta.mousePressEvent = notesBeta_mousePressed

    # Eventfilter

    # notesBeta Context Menu
    def eventFilter_createFile(self):
        text, okPressed = QtWidgets.QInputDialog.getText(self, "Create file", "File Name:", text="")
        if okPressed and text:

            folder = self.pathAlpha()
            newfilePath = f"{folder}/{text}"
            if not text in getContentsFromPath(folder): createFile(newfilePath)
            return pathToIcon(newfilePath) + text

    def eventFilter_createFolder(self):
        text, okPressed = QtWidgets.QInputDialog.getText(self, "Create Folder", "Folder Name:", text="")
        if okPressed and text:

            folder = self.pathAlpha()
            if not text in getContentsFromPath(folder): createFolder(f"{folder}/{text}")

    def eventFilter_delete(self, item):
        toDeletePath = self.pathAlpha() + "\\" + noEmoji(item.text())
        try:
            shutil.move(toDeletePath, trashPath)
        except:
            new = toDeletePath + " - " + str(time.time())
            os.rename(toDeletePath, new)
            shutil.move(new, trashPath)

    def eventFilter_rename(self, item):
        name = noEmoji(item.text())
        text, okPressed = QtWidgets.QInputDialog.getText(self, "New name", "New name:", text=name)

        if okPressed and text and text != name:
            try:
                folder = self.pathAlpha()
                oldPath = f"{folder}/{name}"
                newfilePath = f"{folder}/{text}"
                os.rename(oldPath, newfilePath)
                self.notesBeta.setCurrentItem(item)
            except:
                pass
            return pathToIcon(newfilePath) + text

    def notesBeta_contextMenu(self, source, event):
        item = source.itemAt(event.pos())
        menu = QtWidgets.QMenu()
        newItem = None

        if item == None:
            Reveal = menu.addAction("Show in Explorer")
            CreateFile = menu.addAction(icons["file"] + ' File')
            CreateFolder = menu.addAction(icons["folder"] + ' Folder')
            action = menu.exec_(event.globalPos())

            if action == CreateFile:
                newItem = self.eventFilter_createFile()
            elif action == CreateFolder:
                self.eventFilter_createFolder()
            elif action == Reveal:
                os.system("start explorer " + os.path.abspath(self.pathFull))
        else:
            Rename = menu.addAction('🔄 Rename')
            Delete = menu.addAction('❌ Delete')
            action = menu.exec_(event.globalPos())

            if action == Delete:
                self.eventFilter_delete(item)
            elif action == Rename:
                newItem = self.eventFilter_rename(item)
        updateBeta(self)
        if newItem:
            setSelectedByText_list(self.notesBeta, newItem)
            self.beta_itemClicked()

    # Eventfilter for Whole App
    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.ContextMenu:
            if source is self.notesBeta: self.notesBeta_contextMenu(source, event)
        return super(MainWindow, self).eventFilter(source, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Read the stylesheet from file
    file = QFile(":\dark\stylesheet.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    # Create and show the main window
    window = MainWindow()

    # Set the main window to use the full available screen size
    window.showMaximized()

    app.exec()
