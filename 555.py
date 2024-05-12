from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 设置大小
plt.rcParams['figure.figsize'] = [10, 10]
# 定义饼状图的标签，标签是列表
labels = ['麻辣小龙虾', '炭烤生蚝', '花毛一体', '麻辣田螺']
# 每个标签占多大，会自动按照百分比绘制
data = [15, 30, 45, 10]
# 绘制饼图
plt.pie(data, labels=labels)
plt.savefig('figure.png',dpi =80)
#plt.show()
