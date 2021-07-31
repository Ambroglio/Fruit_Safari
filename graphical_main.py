import re
from settings import Settings
from board import Board
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class BoardWidget(QtWidgets.QWidget):
    def __init__(self, board : Board):
        super().__init__()

        self.__board = board
        self.__layout = QtWidgets.QGridLayout(self)
        self.__layout.setSpacing(0)
        self.__layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.__layout)
        self.build()

    def restore(self):
        for i in reversed(range(self.__layout.count())): 
            widgetToRemove = self.__layout.itemAt(i).widget()
            # remove it from the layout list
            self.__layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)

    def build(self):
        for y in range(0, self.__board.height()):
            for x in range(self.__board.width()):
                button = QtWidgets.QPushButton(QtGui.QIcon("./icons/%s.png" % str(self.__board.board()[y][x])), "")
                button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
                button.setStyleSheet("""
                background-color: %s;
                color: white;
                font-weight: bold;
                """ % self.__board.board()[y][x].color())
                self.__layout.addWidget(button, y, x)

        # self.button.clicked.connect(self.magic)

    def update_board(self, board : Board):
        self.__board = board
        self.restore()
        self.build()

    """ 
    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello)) 
    """

class SettingsWidget(QtWidgets.QWidget):
    def __init__(self, board : Board, boardWidget : BoardWidget) -> None:
        super().__init__()

        self.__board = board
        self.__settings = board.settings()
        self.__boardWidget = boardWidget
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)

        textWidget = QtWidgets.QLabel()
        textWidget.setText("SETTINGS")
        textWidget.setObjectName("title")
        textWidget.setAlignment(QtCore.Qt.AlignCenter)

        nbOfCellsRange = QtWidgets.QSlider(orientation = QtCore.Qt.Horizontal)
        nbOfCellsRange.setProperty("cssClass", "rangeInput")
        nbOfCellsRange.setMinimum(2)
        nbOfCellsRange.setMaximum(10)
        nbOfCellsRange.setTickInterval(1)
        nbOfCellsRange.setTickPosition(QtWidgets.QSlider.TicksBelow)
        nbOfCellsRange.valueChanged.connect(self.nbOfCellsRangeValueChange)

        nbOfCellsRangeText = QtWidgets.QLabel()
        nbOfCellsRangeText.setText("GROUP LENGTH : 2")
        nbOfCellsRangeText.setProperty("cssClass", "rangeLabel")

        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setObjectName("settings")

        self.layout.addWidget(textWidget)
        self.layout.addWidget(nbOfCellsRange)
        self.layout.addWidget(nbOfCellsRangeText)

        for i in range(len(self.__settings.settings()["cells"])):
            rangeSlider = QtWidgets.QSlider(orientation = QtCore.Qt.Horizontal)
            rangeSlider.setProperty("cssClass", "rangeInput")
            rangeSlider.setMinimum(1)
            rangeSlider.setMaximum(10)
            rangeSlider.setTickInterval(1)
            rangeSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
            rangeSlider.valueChanged.connect(self.rangeSliderValueChange)
            rangeSlider.setProperty("position", i)

            label = QtWidgets.QLabel()
            label.setText("%s WEIGHT : 1" % str(self.__settings.settings()["cells"][i]))
            label.setProperty("cssClass", "rangeLabel")

            self.layout.addWidget(rangeSlider)
            self.layout.addWidget(label)

        self.setLayout(self.layout)

    def nbOfCellsRangeValueChange(self):
        print(self.sender().value())
        self.layout.itemAt(2).widget().setText("GROUP LENGTH : %d" % self.sender().value())
        self.__settings.changeMinimumWidth(self.sender().value())
        self.changeSettings()

    def rangeSliderValueChange(self):
        position = int(self.sender().property("position"))
        label = self.sender().parent().layout.itemAt(position * 2 + 4).widget()
        label.setText(re.sub("(\d)+", str(self.sender().value()), label.text()))
        self.__settings.changeWeight(self.sender().value(), position)
        self.changeSettings()

    def changeSettings(self):
        newBoard = Board(self.__board.height(), self.__board.width(), settings=self.__settings)
        self.__boardWidget.update_board(newBoard)
    
class GameWidget(QtWidgets.QWidget):
    def __init__(self, board : Board) -> None:
        super().__init__()
        self.__board = board

        self.layout = QtWidgets.QHBoxLayout()
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

        self.layout.setContentsMargins(0,0,0,0)
        self.__boardWidget = BoardWidget(self.__board)
        self.layout.addWidget(SettingsWidget(self.__board, self.__boardWidget))
        self.layout.addWidget(self.__boardWidget)
        self.setLayout(self.layout)
        self.setObjectName("game")

class MyBar(QtWidgets.QWidget):

    def __init__(self, parent):
        super(MyBar, self).__init__()
        self.parent = parent
        print(self.parent.width())
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.title = QtWidgets.QLabel("Fruit Safari")

        btn_size = 35

        self.btn_close = QtWidgets.QPushButton("X")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setFixedSize(btn_size,btn_size)
        self.btn_close.setStyleSheet("background-color: rgba(255,255,255,0);color:white;")

        # self.btn_min = QtWidgets.QPushButton("-")
        # self.btn_min.clicked.connect(self.btn_min_clicked)
        # self.btn_min.setFixedSize(btn_size, btn_size)
        # self.btn_min.setStyleSheet("background-color: gray;")

        # self.btn_max = QtWidgets.QPushButton("+")
        # self.btn_max.clicked.connect(self.btn_max_clicked)
        # self.btn_max.setFixedSize(btn_size, btn_size)
        # self.btn_max.setStyleSheet("background-color: gray;")

        self.title.setFixedHeight(35)
        self.layout.addWidget(self.title)
        # self.layout.addWidget(self.btn_min)
        # self.layout.addWidget(self.btn_max)
        self.layout.addWidget(self.btn_close)

        self.title.setStyleSheet("""
            background-color: #8b181a;
            color: white;
        """)
        self.setLayout(self.layout)

        self.start = QtCore.QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(MyBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False


    def btn_close_clicked(self):
        self.parent.close()

    def btn_max_clicked(self):
        self.parent.showMaximized()

    def btn_min_clicked(self):
        self.parent.showMinimized()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = QtWidgets.QWidget()
    layout  = QtWidgets.QVBoxLayout()
    window.setLayout(layout)

    window.layout().addStretch(-1)
    window.layout().setContentsMargins(0,0,0,0)
    window.layout().setSpacing(0)
    window.setMinimumSize(200,400)
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    window.pressing = False
    
    widget = GameWidget(Board(20, 15))
    # widget.setWindowTitle("Fruit Safari")
    window.layout().addWidget(MyBar(window))
    window.layout().addWidget(widget)
    window.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())