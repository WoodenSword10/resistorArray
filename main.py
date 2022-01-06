import re
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QSizePolicy, QSlider, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtDataVisualization import Q3DBars, QBar3DSeries, QValue3DAxis, QCategory3DAxis, QAbstract3DSeries, \
    QAbstract3DGraph, Q3DCamera, QBarDataItem
import main_UI
import begin_UI
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QSize
import serial
import serial.tools.list_ports

class Find_port(QThread):
    port_change = pyqtSignal()

    def __init__(self):
        super(Find_port, self).__init__()
        self.old = list(serial.tools.list_ports.comports())

    def run(self):
        while True:
            port_list = list(serial.tools.list_ports.comports())
            if port_list != self.old:
                self.old = port_list
                self.port_change.emit()
                QThread.msleep(1000)

class Read_data_1(QThread):
    changeforce = pyqtSignal(int, int)
    '''
    子进程，用于读取数据
    '''
    def __init__(self, port):
        super(Read_data_1, self).__init__()
        self.port = port
        self.old = np.array(re.findall('\d+', str(self.port.readline()))).astype(int)

    def run(self):
        while True:
            # self.dat
            data = str(self.port.readline())
            # print(data, type(data))
            # print(re.findall('\d+', data))
            self.data = np.array(re.findall('\d+', data))
            self.data = self.data.astype(int)
            # print(self.data)
            for i in range(5):
                if self.data[i] != self.old[i]:
                    changevalue = self.data[i] - self.old[i]
                    self.changeforce.emit(i, changevalue)
        pass

class begin(QMainWindow, begin_UI.Ui_Dialog):
    baud = ['9600', '115200']
    def __init__(self):
        super(begin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.myconnect)
        self.init_baud()
        self.port_find()
        self.thread1 = Find_port()
        self.thread1.port_change.connect(self.port_find)
        self.thread1.start()

    def init_baud(self):
        self.comboBox_2.addItems(self.baud)
        self.comboBox_4.addItems(self.baud)
        self.comboBox_6.addItems(self.baud)
        self.comboBox_8.addItems(self.baud)
        self.comboBox_10.addItems(self.baud)

    def myconnect(self):
        try:
            self.port1 = serial.Serial(self.comboBox.currentText(), self.comboBox_2.currentText())
            # self.port2 = serial.Serial(self.comboBox_3.currentText(), self.comboBox_4.currentText())
            # self.port3 = serial.Serial(self.comboBox_5.currentText(), self.comboBox_6.currentText())
            # self.port4 = serial.Serial(self.comboBox_7.currentText(), self.comboBox_8.currentText())
            # self.port5 = serial.Serial(self.comboBox_9.currentText(), self.comboBox_10.currentText())
        except:
            box = QMessageBox()
            box.setText('<h1><center>连接失败！！！</center></h1>')
            box.setWindowTitle('message')
            box.setStandardButtons(QMessageBox.Ok)  # QMessageBox显示的按钮
            box.button(QMessageBox.Ok).animateClick(1000)  # t时间后自动关闭(t单位为毫秒)
            box.exec_()
        else:
            self.mainwin = main_ui()
            self.hide()
            self.mainwin.show()
        pass

    def port_find(self):
        self.comboBox.clear()
        self.comboBox_3.clear()
        self.comboBox_5.clear()
        self.comboBox_7.clear()
        self.comboBox_9.clear()
        list1 = []
        port_list = list(serial.tools.list_ports.comports())
        for item in port_list:
            pattern = re.compile('COM[\d]*')
            item = pattern.findall(str(item))[0]
            list1.append(item)
        list1.sort()
        self.comboBox.addItems(list1)
        self.comboBox_3.addItems(list1)
        self.comboBox_5.addItems(list1)
        self.comboBox_7.addItems(list1)
        self.comboBox_9.addItems(list1)

class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=3.9, height=2.7, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=100)
        super(Figure_Canvas, self).__init__(self.fig)
        self.ax = self.fig.add_subplot(111)

class main_ui(QMainWindow, main_UI.Ui_Dialog):

    my_row = ('第一列', '第二列', '第三列', '第四列', '第五列')
    my_col = ('第一行', '第二行', '第三行', '第四行', '第五行')

    def __init__(self):
        super(main_ui, self).__init__()
        self.setupUi(self)
        self.data = np.zeros(shape=(5, 5))
        self.make_list()
        self.init_xuanz()
        self.D3DBar()
        self.lineEdit_1.textChanged.connect(self.reprint)
        self.lineEdit_2.textChanged.connect(self.reprint)
        self.lineEdit_3.textChanged.connect(self.reprint)
        self.lineEdit_4.textChanged.connect(self.reprint)
        self.lineEdit_5.textChanged.connect(self.reprint)
        self.lineEdit_6.textChanged.connect(self.reprint)
        self.lineEdit_7.textChanged.connect(self.reprint)
        self.lineEdit_8.textChanged.connect(self.reprint)
        self.lineEdit_9.textChanged.connect(self.reprint)
        self.lineEdit_10.textChanged.connect(self.reprint)
        self.lineEdit_11.textChanged.connect(self.reprint)
        self.lineEdit_12.textChanged.connect(self.reprint)
        self.lineEdit_13.textChanged.connect(self.reprint)
        self.lineEdit_14.textChanged.connect(self.reprint)
        self.lineEdit_15.textChanged.connect(self.reprint)
        self.lineEdit_16.textChanged.connect(self.reprint)
        self.lineEdit_17.textChanged.connect(self.reprint)
        self.lineEdit_18.textChanged.connect(self.reprint)
        self.lineEdit_19.textChanged.connect(self.reprint)
        self.lineEdit_20.textChanged.connect(self.reprint)
        self.lineEdit_21.textChanged.connect(self.reprint)
        self.lineEdit_22.textChanged.connect(self.reprint)
        self.lineEdit_23.textChanged.connect(self.reprint)
        self.lineEdit_24.textChanged.connect(self.reprint)
        self.lineEdit_25.textChanged.connect(self.reprint)
        self.pushButton.clicked.connect(self.reback)
        self.thread2 = Read_data_1(beginWin.port1)
        self.thread2.changeforce.connect(self.ChangeForce1)
        self.thread2.start()

    def ChangeForce1(self, i, changevalue):
        if i == 0:
            # print(changevalue, type(changevalue), str(changevalue))
            self.lineEdit_1.setText(str(changevalue))
        if i == 1:
            self.lineEdit_2.setText(str(changevalue))
        if i == 2:
            self.lineEdit_3.setText(str(changevalue))
        if i == 3:
            self.lineEdit_4.setText(str(changevalue))
        if i == 4:
            self.lineEdit_5.setText(str(changevalue))

    def paint(self):
        self.SurfFigure = Figure_Canvas()

        self.X = np.arange(0, 5, step=1)  # X轴的坐标
        self.Y = np.arange(0, 5, step=1)  # Y轴的坐标
        self.make_list()
        self.Z = self.data
        xx, yy = np.meshgrid(self.X, self.Y)  # 网格化坐标
        self.X, self.Y = xx.ravel(), yy.ravel()  # 矩阵扁平化
        self.Z = self.Z.ravel()

        width = height = 0.6  # 每一个柱子的长和宽
        bottom = np.zeros_like(self.X)  # 设置柱状图的底端位值

        layout = QtWidgets.QVBoxLayout(self.groupBox_4)
        layout.addWidget(self.SurfFigure)
        self.SurfFigure.ax.remove()
        self.ax3d = self.SurfFigure.fig.gca(projection='3d')
        self.ax3d.set_title("AirTrack")
        self.ax3d.set_xlabel("x")
        self.ax3d.set_ylabel("y")
        self.ax3d.set_zlabel("z")
        self.figure = self.ax3d.plot(self.X, self.Y, self.Z, c='r')

    def reback(self):
        self.m_graph.scene().activeCamera().setCameraPreset(self.m_preset)
        # self.rotationSliderX.value(0)
        # self.rotationSlidery.value(0)

    def D3DBar(self):
        self.m_graph = Q3DBars()
        self.m_xRotation = 0.0  # 水平旋转角度
        self.m_yRotation = 0.0  # 垂直旋转角度
        self.m_fontSize = 30
        self.m_segments = 4
        self.m_subSegments = 3
        self.m_minval = 0
        self.m_maxval = 1024
        self.m_temperatureAxis = QValue3DAxis()  # 温度轴
        self.m_yearAxis = QCategory3DAxis()  # 年份轴
        self.m_monthAxis = QCategory3DAxis()  # 月份轴
        self.m_primarySeries = QBar3DSeries()  # 主序列
        self.m_barMesh = QAbstract3DSeries.MeshBevelBar  # 预定义的网格类型
        self.m_smooth = True  # 是否平滑

        # 阴影以柔化的边缘高质量渲染
        self.m_graph.setShadowQuality(QAbstract3DGraph.ShadowQualitySoftMedium)
        # 当前主题Q3DTheme设置背景是否可见
        self.m_graph.activeTheme().setBackgroundEnabled(False)
        # 当前主题Q3DTheme设置字体
        self.m_graph.activeTheme().setFont(
            QFont('Times New Roman', self.m_fontSize))
        # 当前主题Q3DTheme设置标签是使用彩色背景还是使用完全透明的背景绘制
        self.m_graph.activeTheme().setLabelBackgroundEnabled(True)
        # 是否按比例将比例尺设置为单个系列比例尺来缩放比例
        self.m_graph.setMultiSeriesUniform(True)

        self.m_temperatureAxis.setTitle("Average temperature")
        # 轴上的段数。这表明绘制了多少标签。要绘制的网格线的数量使用公式计算：segments * subsegments + 1。预设默认值为5。该值不能低于1
        self.m_temperatureAxis.setSegmentCount(self.m_segments)
        # 轴上每个段内的子段数。
        # 除每个线段外，还在每个子线段之间绘制网格线。预设默认值为1。该值不能低于1。
        self.m_temperatureAxis.setSubSegmentCount(self.m_subSegments)
        self.m_temperatureAxis.setRange(self.m_minval, self.m_maxval)
        self.m_temperatureAxis.setLabelFormat(u"%.1fV")

        self.m_yearAxis.setTitle("行数")
        self.m_monthAxis.setTitle("列数")

        self.m_graph.setValueAxis(self.m_temperatureAxis)
        # 设置活动行的轴为年份
        self.m_graph.setRowAxis(self.m_yearAxis)
        # 设置活动列的轴为月份
        self.m_graph.setColumnAxis(self.m_monthAxis)

        self.m_primarySeries.setItemLabelFormat(
            "数据 - @colLabel @rowLabel: @valueLabel")

        # 设置网格类型
        self.m_primarySeries.setMesh(QAbstract3DSeries.MeshBevelBar)
        self.m_primarySeries.setMeshSmooth(False)

        self.m_graph.addSeries(self.m_primarySeries)

        self.m_preset = Q3DCamera.CameraPresetFront

        self.m_graph.scene().activeCamera().setCameraPreset(self.m_preset)

        self.data2 = self.data.tolist()
        dataSet = []
        for row in self.data2:
            dataSet.append([QBarDataItem(v) for v in row])

        self.m_primarySeries.dataProxy().resetArray(dataSet, self.my_col, self.my_row)

        container = QWidget.createWindowContainer(self.m_graph)
        container.setMinimumSize(QSize(700, 400))
        container.setMaximumSize(QSize(700, 400))
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        container.setFocusPolicy(Qt.StrongFocus)
        widget = QWidget()
        layout = QtWidgets.QVBoxLayout(self.widget)
        layout.addWidget(container)
        widget.show()

    def reprint(self):
        self.make_list()
        self.data2 = self.data.tolist()
        dataSet = []
        for row in self.data2:
            dataSet.append([QBarDataItem(v) for v in row])

        self.m_primarySeries.dataProxy().resetArray(dataSet, self.my_col, self.my_row)

    def toint(self, str):
        try:
            res = int(str)
        except:
            return 0
        else:
            return res

    def make_list(self):
        self.data[0][0] = self.toint(self.lineEdit_1.text())
        self.data[0][1] = self.toint(self.lineEdit_2.text())
        self.data[0][2] = self.toint(self.lineEdit_3.text())
        self.data[0][3] = self.toint(self.lineEdit_4.text())
        self.data[0][4] = self.toint(self.lineEdit_5.text())
        self.data[1][0] = self.toint(self.lineEdit_6.text())
        self.data[1][1] = self.toint(self.lineEdit_7.text())
        self.data[1][2] = self.toint(self.lineEdit_8.text())
        self.data[1][3] = self.toint(self.lineEdit_9.text())
        self.data[1][4] = self.toint(self.lineEdit_10.text())
        self.data[2][0] = self.toint(self.lineEdit_11.text())
        self.data[2][1] = self.toint(self.lineEdit_12.text())
        self.data[2][2] = self.toint(self.lineEdit_13.text())
        self.data[2][3] = self.toint(self.lineEdit_14.text())
        self.data[2][4] = self.toint(self.lineEdit_15.text())
        self.data[3][0] = self.toint(self.lineEdit_16.text())
        self.data[3][1] = self.toint(self.lineEdit_17.text())
        self.data[3][2] = self.toint(self.lineEdit_18.text())
        self.data[3][3] = self.toint(self.lineEdit_19.text())
        self.data[3][4] = self.toint(self.lineEdit_20.text())
        self.data[4][0] = self.toint(self.lineEdit_21.text())
        self.data[4][1] = self.toint(self.lineEdit_22.text())
        self.data[4][2] = self.toint(self.lineEdit_23.text())
        self.data[4][3] = self.toint(self.lineEdit_24.text())
        self.data[4][4] = self.toint(self.lineEdit_25.text())

    def init_xuanz(self):
        self.rotationSliderX = QSlider(Qt.Horizontal)
        self.rotationSliderX.setTickInterval(30)
        self.rotationSliderX.setTickPosition(QSlider.TicksBelow)
        self.rotationSliderX.setMinimum(-180)
        self.rotationSliderX.setValue(0)
        self.rotationSliderX.setMaximum(180)
        self.rotationSliderY = QSlider(Qt.Horizontal)
        self.rotationSliderY.setTickInterval(15)
        self.rotationSliderY.setTickPosition(QSlider.TicksAbove)
        self.rotationSliderY.setMinimum(-90)
        self.rotationSliderY.setValue(0)
        self.rotationSliderY.setMaximum(90)
        vLayout = QtWidgets.QVBoxLayout(self.groupBox_5)
        vLayout.addWidget(QLabel("Rotate horizontally"))
        vLayout.addWidget(self.rotationSliderX, 0, Qt.AlignTop)
        vLayout.addWidget(QLabel("Rotate vertically"))
        vLayout.addWidget(self.rotationSliderY, 0, Qt.AlignTop)
        self.rotationSliderX.valueChanged.connect(self.rotateX)
        self.rotationSliderY.valueChanged.connect(self.rotateY)

    def rotateX(self, rotation):
        self.m_xRotation = rotation
        self.m_graph.scene().activeCamera().setCameraPosition(
            self.m_xRotation, self.m_yRotation)

    def rotateY(self, rotation):
        self.m_yRotation = rotation
        self.m_graph.scene().activeCamera().setCameraPosition(
            self.m_xRotation, self.m_yRotation)

if __name__ == '__main__':
    # 实现不同分辨率下的电脑上的相同显示
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    beginWin = begin()
    beginWin.show()
    sys.exit(app.exec_())