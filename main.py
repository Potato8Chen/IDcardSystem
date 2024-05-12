import matplotlib.pyplot
import psycopg2
import ImageStringGet
from matplotlib import pyplot as plt
from matplotlib import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import shutil
import photocard
from LoginUI import *
from InterFaceUI import *
from NewPerson import *
import webbrowser
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QPixmap
#from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import test
from PIL import Image, ImageFont, ImageDraw
import numpy as np
from matplotlib import font_manager
import os

def check_file_exist(file_name):
    root_dir = os.getcwd()  # 根目录
    file_path = os.path.join(root_dir, file_name)
    return os.path.exists(file_path)

#全局变量：当前用户
user_now = ''

class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键

    def __init__(self, parent=None, width=11, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure

        FigureCanvas.__init__(self, fig) # 初始化父类
        self.setParent(parent)

        self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

    def test(self):
        x = [1,2,3,4,5,6,7,8,9]
        y = [23,21,32,13,3,132,13,3,1]
        self.axes.plot(x, y)
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        #隐藏外部界面如下{
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #给frame添加阴影
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0,0)
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QtCore.Qt.gray)
        self.ui.Welcomeframe.setGraphicsEffect(self.shadow)
        self.ui.pushButtonToRe.clicked.connect(lambda :self.ui.stackedWidgetLoAndRe.setCurrentIndex(1))
        self.ui.pushButtonToLo.clicked.connect(lambda :self.ui.stackedWidgetLoAndRe.setCurrentIndex(0))
        self.ui.pushButtonLogin.clicked.connect(self.login_in)
        self.ui.pushButtonRe.clicked.connect(self.register)
        self.ui.pushButton_2.clicked.connect(lambda :self.close())
        self.ui.pushButtonToRe.clicked.connect(lambda :self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButtonToLo.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.show()

    def login_in(self):
        account = self.ui.lineEditUserName.text()
        password = self.ui.lineEditPassword.text()
        account_list = []
        password_list = []
        #连接数据库时默认密码不是123456而是安装时自己设置的，可能老版本postgre默认是123456
        conn = psycopg2.connect(database='Card', user='postgres', password='potato', host='127.0.0.1', port='5432')
        cur = conn.cursor()
        cur.execute("select * from users")#显示数据库中存储的账号和密码
        # 把访问到的所有数据都递给rows
        rows = cur.fetchall()
        for row in rows:
            account_list.append(row[1])#account_list是一个只存账号的list，与row不同，row里既有账号又有密码
            password_list.append(row[2])
        '''print(rows)'''
        conn.commit()
        conn.close()#从数据库获取完数据后就关闭了，此时变量account_list与password_list已有数据
        for i in range(len(account_list)):#将输入的账号密码与已有的匹配
            if len(account) == 0 or len(password) == 0:#用户名或者密码为空
                self.ui.stackedWidget.setCurrentIndex(1)
            elif account == account_list[i] and password == password_list[i]:
                global user_now
                user_now = account
                self.win = MainWindow()
                self.close()
            else:
                self.ui.stackedWidget.setCurrentIndex(2)


    def register(self):
        account_list = []
        password_list = []
        account = self.ui.lineEditReUserName.text()
        password = self.ui.lineEditRePassword.text()
        RePassword = self.ui.lineEditReComfirm.text()
        if len(account) == 0 or len(password) == 0 or len(RePassword) == 0:#用户名或密码为空
            self.ui.stackedWidget.setCurrentIndex(1)
            a = 1
        elif password != RePassword:#两次输入密码不一致
            self.ui.stackedWidget.setCurrentIndex(4)
        else:
            conn = psycopg2.connect(database='Card', user='postgres', password='potato', host='127.0.0.1', port='5432')
            cur = conn.cursor()
            cur.execute("select * from users")
            # 把访问到的所有数据都递给rows
            rows = cur.fetchall()
            for row in rows:
                account_list.append(row[1])  # account_list是一个只存账号的list，与row不同，row里既有账号又有密码
            '''print(rows)'''
            a = 0
            for i in range(len(account_list)):
                if account == account_list[i]:#用户名已经存在
                    print("用户名已存在")
                    a = a + 1
                    self.ui.stackedWidget.setCurrentIndex(3)
        if a == 0:
            #cur.execute(f"insert into users values ('{account}','{password}')")
            p = test.users.create(accounts=account, passwords=password)
            cur.execute(f"create table {account}_card(id SERIAL PRIMARY KEY,name varchar(10),gender varchar(5),number varchar(11),email varchar(50),text varchar(50))")
            q = test.card.create(user=account)
            conn.commit()
            conn.close()
            print("注册成功！")
            self.ui.stackedWidget.setCurrentIndex(5)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #隐藏外部界面如下{
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #给frame添加阴影
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0,0)
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QtCore.Qt.gray)
        self.ui.frame.setGraphicsEffect(self.shadow)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0, 0)
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QtCore.Qt.gray)
        self.ui.frame_8.setGraphicsEffect(self.shadow)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0, 0)
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QtCore.Qt.gray)
        self.ui.frame_9.setGraphicsEffect(self.shadow)
        self.ui.pushButtonfreshC.clicked.connect(lambda:self.ui.stackedWidget_3.setCurrentIndex(0))
        self.ui.pushButtonHome.clicked.connect(lambda :self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButtonCard.clicked.connect(lambda :self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButtonEvent.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButtonSug.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.pushButtonWeb.clicked.connect(self.go_web)
        self.ui.pushButtonMe.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))
        self.ui.pushButtonBack.clicked.connect(self.log_out)
        self.ui.pushButtonClose.clicked.connect(lambda: self.close())
        self.ui.pushButtonRefresh.clicked.connect(self.RefreshMe)
        self.ui.pushButtonAdd.clicked.connect(self.AddPerson)
        self.ui.pushButtonPRefresh.clicked.connect(self.ShowTableP)
        self.ui.pushButtonPRefresh.clicked.connect(self.ShowTable)
        self.ui.pushButtonChangePas.clicked.connect(lambda :self.ui.stackedWidget_3.setCurrentIndex(1))
        self.ui.pushButtonPRefresh.clicked.connect(lambda: self.ui.stackedWidget_4.setCurrentIndex(0))
        self.ui.pushButtonDP.clicked.connect(lambda:self.ui.stackedWidget_4.setCurrentIndex(1))
        self.ui.pushButtonSearch.clicked.connect(lambda: self.ui.stackedWidget_4.setCurrentIndex(2))
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(('姓名', '性别', '电话','邮件','部门',' ',' '))
        self.ui.tableWidgetP.setColumnCount(5)
        self.ui.tableWidgetP.setHorizontalHeaderLabels(('姓名', '性别', '电话', '邮件',  '备注'))
        self.ShowTable()
        global tablePlen
        tablePlen = self.ShowTableP()
        self.ui.pushButtonDe.clicked.connect(self.DeletePerson)
        self.ui.pushButtonSe.clicked.connect(self.SearchPerson)
        #最小化窗口
        self.ui.pushButtonMin.clicked.connect(lambda :self.showMinimized())
        self.ShowMe()
        #pixmap = QPixmap('figure.png')
        # 如果图片不在屏幕上显示，可以调整大小
        #pixmap = pixmap.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio)
        # 在标签中显示图片
        #self.ui.labelFigure1.setPixmap(pixmap)
        self.showFigurePart()
        self.ui.pushButtonHome.clicked.connect(self.showFigurePart)
        self.ShowEvent()
        self.RecentEvent()
        self.ui.tableWidgetEvent.setColumnCount(4)
        self.ui.tableWidgetEvent.setHorizontalHeaderLabels(('事项描述', '参与人员', '时间', '地点'))
        self.ui.pushButtonEvent.clicked.connect(self.ShowEvent)
        self.ui.pushButtonEventAdd.clicked.connect(self.AddEvent)
        self.ui.pushButtonEventAdd.clicked.connect(self.RecentEvent)
        self.ui.pushButtonEventAdd.clicked.connect(self.ShowEvent)
        self.ui.pushButtonChangepascon.clicked.connect(self.change_password)
        self.show()

    def showFigurePart(self):
        matplotlib.pyplot.clf()
        plt.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['font.size'] = 25
        plt.rcParams['axes.unicode_minus'] = False
        # 设置大小
        plt.rcParams['figure.figsize'] = [10, 10]
        sc,cg,xs,js,zh,cw,rl,qt = 0,0,0,0,0,0,0,0
        part_check =[]
        conn = psycopg2.connect(database='Card', user='postgres', password='potato', host='127.0.0.1', port='5432')
        cur = conn.cursor()
        cur.execute("select * from card")
        # 把访问到的所有数据都递给rows
        rows = cur.fetchall()
        print(rows)
        for row in rows:
            part_check.append(row[6])  #account_list是一个只存账号的list，与row不同，row里既有账号又有密码
        print(part_check)
        for i in range(len(part_check)):
            print(part_check[i])
            if part_check[i] == "生产部":
                sc = sc + 1
            elif part_check[i] == "采购部":
                cg = cg + 1
            elif part_check[i] == "销售部":
                xs = xs + 1
            elif part_check[i] == "技术部":
                js = js + 1
            elif part_check[i] == "综合办":
                zh = zh + 1
            elif part_check[i] == "财务部":
                cw = cw + 1
            elif part_check[i] == "人力资源部":
                rl = rl + 1
            else:
                qt = qt + 1
        labels = '生产部', '采购部', '销售部', '技术部','综合办','财务部','人力资源部','其他'
        # 指定每个切片的数值，从而决定了百分比
        sizes = [sc, cg, xs, js, zh, cw, rl, qt]
        #向外扩张
        explode = (0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        fig1, ax1 = matplotlib.pyplot.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                 startangle=90)
        ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.savefig('figure.png', dpi=80)
        pixmap = QPixmap('figure.png')
        self.ui.labelFigure1.setPixmap(pixmap)
        #matplotlib.pyplot.show()

    def DeletePerson(self):
        name = self.ui.lineEdit_2.text()
        name_list = []
        conn = psycopg2.connect(database='Card', user='postgres', password='potato', host='127.0.0.1', port='5432')
        cur = conn.cursor()
        cur.execute(f"select * from {user_now}_card")
        # 把访问到的所有数据都递给rows
        rows = cur.fetchall()
        print("row is")
        print(rows)
        for row in rows:
            name_list.append(row[1])
        a = 0
        for i in range(len(name_list)):
            if name == name_list[i]:
                a = a + 1
        if a != 0:
            cur.execute(f"delete from {user_now}_card where name='{name}'")
            conn.commit()
            conn.close()
        else:
            print("删除失败")
        self.ui.tabWidgetCard.setCurrentIndex(1)
        self.ui.lineEdit_2.clear()
        self.ShowTableP()

    def SearchPerson(self):
        name = self.ui.lineEditSearch.text()
        name_list = []
        gender_list = []
        number_list = []
        email_list = []
        text_list = []
        conn = psycopg2.connect(database='Card', user='postgres', password='potato', host='127.0.0.1', port='5432')
        cur = conn.cursor()
        cur.execute(f"select * from {user_now}_card")
        # 把访问到的所有数据都递给rows
        rows = cur.fetchall()
        print("row is")
        print(rows)
        a = 0
        b = 0
        for row in rows:
            name_list.append(row[1])
            gender_list.append(row[2])
            number_list.append(row[3])
            email_list.append(row[4])
            text_list.append(row[5])
        for i in range(len(name_list)):
            if name == name_list[i]:
                a = i
                b = b + 1
        if b > 0 :
            self.ui.tableWidgetP.clearContents()
            self.ui.tableWidgetP.setItem(0, 0, QTableWidgetItem(name_list[a]))
            self.ui.tableWidgetP.setItem(0, 1, QTableWidgetItem(gender_list[a]))
            self.ui.tableWidgetP.setItem(0, 2, QTableWidgetItem(number_list[a]))
            self.ui.tableWidgetP.setItem(0, 3, QTableWidgetItem(email_list[a]))
            self.ui.tableWidgetP.setItem(0, 4, QTableWidgetItem(text_list[a]))
            self.ui.tabWidgetCard.setCurrentIndex(1)
        if b == 0 :
            self.ui.tableWidgetP.clearContents()
        self.ui.lineEdit_2.clear()

    def change_password(self):
        global user_now
        password = self.ui.lineEditChangepas1.text()
        if len(self.ui.lineEditChangepas1.text()) == 0 or len(self.ui.lineEditChangepas2.text()) == 0:
            self.ui.stackedWidget_5.setCurrentIndex(0)
        elif self.ui.lineEditChangepas1.text() == self.ui.lineEditChangepas2.text():
            self.ui.stackedWidget_5.setCurrentIndex(1)
            print("9078u89079878907987")
            conn = psycopg2.connect(database='Card', user='postgres', password='potato', host='127.0.0.1', port='5432')
            cur = conn.cursor()
            cur.execute(f"update users set passwords='{password}' where accounts='{user_now}'")
            #rows = cur.fetchall()
            '''for row in rows:
                account_list.append(row[1])
                password_list.append(row[2])
    print(account_list, password_list)'''
            conn.commit()
            conn.close()




    def go_web(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.pushButtonBli.clicked.connect(lambda:webbrowser.open("bilibili.com"))

    def log_out(self):
        global user_now
        self.close()
        self.login = LoginWindow()
        user_now = ''

    def RefreshMe(self):
        global user_now
        p = test.card.get(user = f"{user_now}")
        p.name = self.ui.lineEditName.text()
        p.gender = self.ui.lineEditGender.text()
        p.number = self.ui.lineEditNumber.text()
        p.email = self.ui.lineEditEmail.text()
        p.part = self.ui.lineEditPart.text()
        p.save()
        self.ShowTable()
        self.ShowMe()

    def ShowMe(self):
        global  user_now
        p = test.card.get(user=f"{user_now}")
        self.ui.lineEditName_2.setText(p.name)
        self.ui.lineEditGender_2.setText(p.gender)
        self.ui.lineEditNumber_2.setText(p.number)
        self.ui.lineEditEmail_2.setText(p.email)
        self.ui.lineEditPart_2.setText(p.part)

    def ShowTable(self):
        name_list = []
        gender_list = []
        number_list = []
        email_list = []
        part_list = []
        conn = psycopg2.connect(database='Card', user='postgres', password='potato', host='127.0.0.1', port='5432')
        cur = conn.cursor()
        cur.execute("select * from card")  # 显示数据库中存储的账号和密码
        # 把访问到的所有数据都递给rows
        rows = cur.fetchall()
        #print(rows)
        for row in rows:
            name_list.append(row[2])
            gender_list.append(row[3])
            number_list.append(row[4])
            email_list.append(row[5])
            part_list.append(row[6])
        l = len(name_list)
        self.ui.tableWidget.setRowCount(l)
        for i in range(l):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(name_list[i]))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(gender_list[i]))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(number_list[i]))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(email_list[i]))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(part_list[i]))
            button = QPushButton("查看".format(i))
            button.clicked.connect(self.button_clicked)
            #self.ui.tableWidget.setCellWidget(i, 0, button)
            #item = QTableWidgetItem("Row {}".format(i))
            #self.ui.tableWidget.setItem(i, 1, item)
            self.ui.tableWidget.setCellWidget(i, 6, button)
            button2 = QPushButton("更换".format(i))
            button2.clicked.connect(self.button_clicked2)
            self.ui.tableWidget.setCellWidget(i, 5, button2)
        conn.commit()
        conn.close()  # 从数据库获取完数据后就关闭了，此时变量account_list与password_list已有数据

    def button_clicked2(self):
        name_list = []
        gender_list = []
        number_list = []
        email_list = []
        part_list = []
        conn = psycopg2.connect(database='Card', user='postgres', password='potato', host='127.0.0.1', port='5432')
        cur = conn.cursor()
        cur.execute("select * from card")  # 显示数据库中存储的账号和密码
        # 把访问到的所有数据都递给rows
        rows = cur.fetchall()
        # print(rows)
        for row in rows:
            name_list.append(row[2])
            gender_list.append(row[3])
            number_list.append(row[4])
            email_list.append(row[5])
            part_list.append(row[6])
        button = self.sender()
        index = self.ui.tableWidget.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            column = index.column()
            print("Button clicked at row {}, column {}".format(row, column))
        index = index.row()
        print(index)
        print("abcdefg")
        print(name_list[index])
        the_name = f"{name_list[index]}_{part_list[index]}_名片.png"
        filename, _ = QFileDialog.getOpenFileName(self, "打开", "", "files(*.png *.jpg *.jpeg)")
        if filename:
            file_name = os.path.basename(filename)
            current_dir = os.getcwd()
            new_file_path = os.path.join(current_dir, the_name)
            shutil.copy(filename, new_file_path)
            print(f"文件 '{file_name}' 已保存在根目录下的 '123'。")

    def button_clicked(self):
        name_list = []
        gender_list = []
        number_list = []
        email_list = []
        part_list = []
        conn = psycopg2.connect(database='Card', user='postgres', password='potato', host='127.0.0.1', port='5432')
        cur = conn.cursor()
        cur.execute("select * from card")  # 显示数据库中存储的账号和密码
        # 把访问到的所有数据都递给rows
        rows = cur.fetchall()
        # print(rows)
        for row in rows:
            name_list.append(row[2])
            gender_list.append(row[3])
            number_list.append(row[4])
            email_list.append(row[5])
            part_list.append(row[6])
        button = self.sender()
        index = self.ui.tableWidget.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            column = index.column()
            print("Button clicked at row {}, column {}".format(row, column))
        index = index.row()
        print(index)
        print("abcdefg")
        print(name_list[index])
        a = 0
        file_name = f"{name_list[index]}_{part_list[index]}_名片.png"
        if check_file_exist(file_name):
            print(f"文件 '{file_name}' 存在于根目录下。")
        else:
            print(f"文件 '{file_name}' 不存在于根目录下。")
            a = a + 1
        if a != 0 :
            photocard.generate_business_card(name_list[index],gender_list[index],part_list[index],email_list[index],number_list[index])
        image2_path = f"{name_list[index]}_{part_list[index]}_名片.png"
        image2 = plt.imread(image2_path)
        # 显示图片
        #plt.figure()
        plt.clf()
        plt.close('all')
        plt.imshow(image2)
        plt.axis('off')  # 关闭坐标轴
        plt.show(block=False)
        test.save_images_from_directory()

    def ShowTableP(self):
            name_list = []
            gender_list = []
            number_list = []
            email_list = []
            text_list = []
            conn = psycopg2.connect(database='Card', user='postgres', password='potato', host='127.0.0.1', port='5432')
            cur = conn.cursor()
            cur.execute(f"select * from {user_now}_card")
            # 把访问到的所有数据都递给rows
            rows = cur.fetchall()
            #print(rows)
            for row in rows:
                name_list.append(row[1])
                gender_list.append(row[2])
                number_list.append(row[3])
                email_list.append(row[4])
                text_list.append(row[5])
            l = len(name_list)
            self.ui.tableWidgetP.setRowCount(l)
            for i in range(l):
                self.ui.tableWidgetP.setItem(i, 0, QTableWidgetItem(name_list[i]))
                self.ui.tableWidgetP.setItem(i, 1, QTableWidgetItem(gender_list[i]))
                self.ui.tableWidgetP.setItem(i, 2, QTableWidgetItem(number_list[i]))
                self.ui.tableWidgetP.setItem(i, 3, QTableWidgetItem(email_list[i]))
                self.ui.tableWidgetP.setItem(i, 4, QTableWidgetItem(text_list[i]))
            conn.commit()
            conn.close()  # 从数据库获取完数据后就关闭了，此时变量account_list与password_list已有数据
            print(l)
            return l

    def RecentEvent(self):#最近的四项事项放入首页
        all_event = test.event.select()
        all_name = [test.event.describe for test.event in all_event]
        all_time = [test.event.time for test.event in all_event]
        l = len(all_name)
        if l == 0 :
            return
        elif l == 1:
            self.ui.lineEditHE1.setText(all_name[-1])
            self.ui.lineEditHT1.setText(all_time[-1])
        elif l == 2:
            self.ui.lineEditHE1.setText(all_name[-1])
            self.ui.lineEditHT1.setText(all_time[-1])
            self.ui.lineEditHE2.setText(all_name[-2])
            self.ui.lineEditHT2.setText(all_time[-2])
        elif l == 3:
            self.ui.lineEditHE1.setText(all_name[-1])
            self.ui.lineEditHT1.setText(all_time[-1])
            self.ui.lineEditHE2.setText(all_name[-2])
            self.ui.lineEditHT2.setText(all_time[-2])
            self.ui.lineEditHE3.setText(all_name[-3])
            self.ui.lineEditHT3.setText(all_time[-3])
        else:
            self.ui.lineEditHE1.setText(all_name[-1])
            self.ui.lineEditHT1.setText(all_time[-1])
            self.ui.lineEditHE2.setText(all_name[-2])
            self.ui.lineEditHT2.setText(all_time[-2])
            self.ui.lineEditHE3.setText(all_name[-3])
            self.ui.lineEditHT3.setText(all_time[-3])
            self.ui.lineEditHE4.setText(all_name[-4])
            self.ui.lineEditHT4.setText(all_time[-4])
    def ShowEvent(self):#显示事项表
        all_event = test.event.select()
        all_name = [test.event.describe for test.event in all_event]
        all_members = [test.event.members for test.event in all_event]
        all_time = [test.event.time for test.event in all_event]
        all_place = [test.event.place for test.event in all_event]
        #print("all name is")
        #print(all_name)
        l = len(all_name)
        #print(all_event)
        #print(all_members)
        #print("llllll")
        self.ui.tableWidgetEvent.setRowCount(l)
        self.ui.tableWidgetEvent.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i in range(l):
            self.ui.tableWidgetEvent.setItem(i, 0, QTableWidgetItem(all_name[i]))
            self.ui.tableWidgetEvent.setItem(i, 1, QTableWidgetItem(all_members[i]))
            self.ui.tableWidgetEvent.setItem(i, 2, QTableWidgetItem(all_time[i]))
            self.ui.tableWidgetEvent.setItem(i, 3, QTableWidgetItem(all_place[i]))

    def AddEvent(self):#添加事项
        EventName = self.ui.lineEditEventDescribe.text()
        EventMember = self.ui.lineEditEventMember.text()
        EventTime = self.ui.lineEditEventTime.text()
        EventPlace = self.ui.lineEditEventPlace.text()
        if EventName != None and EventMember != None and EventTime != None and EventPlace != None:
            test.event.create(describe = f"{EventName}",members = f"{EventMember}",time = f"{EventTime}",place = f"{EventPlace}")
        self.ui.lineEditEventDescribe.clear()
        self.ui.lineEditEventMember.clear()
        self.ui.lineEditEventTime.clear()
        self.ui.lineEditEventPlace.clear()
    def AddPerson(self):
        child_window = AddPerson()
        child_window.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 标记是否按下
            self.m_flag = True
            # 获取鼠标相对窗口的位置
            self.m_Position = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        try:
            # 仅监听标题栏
            if Qt.LeftButton and self.m_flag and self.ui.frame_2.underMouse():
                # 更改鼠标图标
                self.setCursor(QCursor(Qt.OpenHandCursor))
                # 更改窗口位置
                self.move(QMouseEvent.globalPos() - self.m_Position)
                QMouseEvent.accept()
        except Exception as e:
            print("报错信息=", e)

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        # 恢复鼠标形状
        self.setCursor(QCursor(Qt.ArrowCursor))


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 标记是否按下
            self.m_flag = True
            # 获取鼠标相对窗口的位置
            self.m_Position = event.globalPos() - self.pos()
            event.accept()


    def mouseMoveEvent(self, QMouseEvent):
        try:
            # 仅监听标题栏
            if Qt.LeftButton and self.m_flag and self.ui.frame_2.underMouse():
                # 更改鼠标图标
                self.setCursor(QCursor(Qt.OpenHandCursor))
                # 更改窗口位置
                self.move(QMouseEvent.globalPos() - self.m_Position)
                QMouseEvent.accept()
        except Exception as e:
            print("报错信息=", e)


    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        # 恢复鼠标形状
        self.setCursor(QCursor(Qt.ArrowCursor))




class AddPerson(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddPersonWindow()
        self.ui.setupUi(self)
        # 隐藏外部界面如下{
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 给frame添加阴影
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0, 0)
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QtCore.Qt.gray)
        self.ui.frame.setGraphicsEffect(self.shadow)
        self.ui.pushButtonClose.clicked.connect(lambda: self.close())
        self.ui.pushButtonAdd.clicked.connect(self.NewPerson)
        self.ui.pushButtonAddphoto.clicked.connect(self.open_file)



    def NewPerson(self):
        name_list = []
        conn = psycopg2.connect(database='Card', user='postgres', password='potato', host='127.0.0.1', port='5432')
        cur = conn.cursor()
        cur.execute(f"select * from {user_now}_card")
        # 把访问到的所有数据都递给rows
        rows = cur.fetchall()
        print("row is")
        print(rows)
        for row in rows:
            name_list.append(row[1])
        print(name_list)
        print(len(name_list))
        name = self.ui.lineEditName.text()
        gender = self.ui.lineEditGender.text()
        number = self.ui.lineEditNumber.text()
        email = self.ui.lineEditEmail.text()
        text = self.ui.lineEditText.text()
        print("lenname is")
        print(len(name))
        a = 0
        if len(name) == 0:
                self.ui.stackedWidget.setCurrentIndex(1)
                print("lenname is 0")
                a = a + 1
        else:
            print(len(name_list))
            if len(name_list) != 0:
                for i in range(len(name_list)):
                    print(name_list[i])
                    if name == name_list[i]:  # 用户名已经存在
                        print("该联系人已存在")
                        self.ui.stackedWidget.setCurrentIndex(2)
                        a = a + 1
            else:
                cur.execute(f"insert into {user_now}_card values('1','{name}','{gender}','{number}','{email}','{text}')")
                conn.commit()
                conn.close()
                self.close()
                return
        if a == 0 :
            #c = len(name_list)+1
            last_element = rows[-1:][0][0]
            print("last element is")
            print(last_element)
            c = last_element + 1
            print("c is")
            print(c)
            cur.execute(f"insert into {user_now}_card values('{c}','{name}','{gender}','{number}','{email}','{text}')")
            conn.commit()
            conn.close()
            self.close()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "打开", "", "files(*.png *.jpg *.jpeg)")
        if filename:
            print(f"选择的文件: {filename}")
            a,b,c= ImageStringGet.ChineseGet(filename)
            self.ui.lineEditName.setText(a)
            self.ui.lineEditNumber.setText(b)
            self.ui.lineEditEmail.setText(c)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 标记是否按下
            self.m_flag = True
            # 获取鼠标相对窗口的位置
            self.m_Position = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        try:
            # 仅监听标题栏
            if Qt.LeftButton and self.m_flag and self.ui.frame_2.underMouse():
                # 更改鼠标图标
                self.setCursor(QCursor(Qt.OpenHandCursor))
                # 更改窗口位置
                self.move(QMouseEvent.globalPos() - self.m_Position)
                QMouseEvent.accept()
        except Exception as e:
            print("报错信息=", e)

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        # 恢复鼠标形状
        self.setCursor(QCursor(Qt.ArrowCursor))


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 标记是否按下
            self.m_flag = True
            # 获取鼠标相对窗口的位置
            self.m_Position = event.globalPos() - self.pos()
            event.accept()


    def mouseMoveEvent(self, QMouseEvent):
        try:
            # 仅监听标题栏
            if Qt.LeftButton and self.m_flag and self.ui.frame_2.underMouse():
                # 更改鼠标图标
                self.setCursor(QCursor(Qt.OpenHandCursor))
                # 更改窗口位置
                self.move(QMouseEvent.globalPos() - self.m_Position)
                QMouseEvent.accept()
        except Exception as e:
            print("报错信息=", e)


    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        # 恢复鼠标形状
        self.setCursor(QCursor(Qt.ArrowCursor))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())

