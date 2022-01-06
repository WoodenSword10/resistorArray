import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from PyQt5.QtDataVisualization import Q3DBars, QValue3DAxis, QCategory3DAxis, QBar3DSeries, QAbstract3DSeries, \
    QAbstract3DGraph, Q3DCamera, QBarDataItem
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtCore import QThread, pyqtSignal, QMutex, Qt, QSize
import Q3dBar

class Q3d(QMainWindow, Q3dBar.Ui_Dialog):
    tempOulu = (
        (1, 2, 3, 4, 5),
        (5, 3, 2, 6, 1),
        (1, 3, 6, 1, 0),
        (9, 3, 7, 8, 1),
        (0, 1, 0, 2, 1),
    )

    months = ('第一列', '第二列', '第三列', '第四列', '第五列')

    years = ('第一行', '第二行', '第三行', '第四行', '第五行')

    def __init__(self):
        super(Q3d, self).__init__()
        self.setupUi(self)
        self.my3Dbar()

    def my3Dbar(self):
        self.m_graph = Q3DBars()
        self.m_xRotation = 0.0  # 水平旋转角度
        self.m_yRotation = 0.0  # 垂直旋转角度
        self.m_fontSize = 30
        self.m_segments = 4
        self.m_subSegments = 3
        self.m_minval = -5
        self.m_maxval = 20.0
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
        self.m_temperatureAxis.setLabelFormat(u"%.1f \N{degree sign}C")

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

        dataSet = []
        for row in self.tempOulu:
            dataSet.append([QBarDataItem(v) for v in row])

        self.m_primarySeries.dataProxy().resetArray(dataSet, self.years, self.months)

        container = QWidget.createWindowContainer(self.m_graph)
        container.setMinimumSize(QSize(400, 300))
        container.setMaximumSize(QSize(400, 300))
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        container.setFocusPolicy(Qt.StrongFocus)
        widget = QWidget()
        layout = QtWidgets.QVBoxLayout(self.groupBox)
        layout.addWidget(container)
        widget.show()

if __name__ == '__main__':
    # 实现不同分辨率下的电脑上的相同显示
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    beginWin = Q3d()
    beginWin.show()
    sys.exit(app.exec_())