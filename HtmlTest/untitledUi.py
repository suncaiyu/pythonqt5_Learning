import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from untitled import *
import Test1
import re
from Resource import *  # 导入这个文件，会自动调用资源初始化函数


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.myclick)
        self.pushButton.clicked.connect(self.btnclick)
        self.treeWidget.setSortingEnabled(1)

    def myclick(self):
        goods = self.lineEdit.text()
        depth = 4
        start_url = 'https://s.taobao.com/search?q=' + goods
        for i in range(depth):  # 循环3次
            try:
                url = start_url + '&s=' + str(44 * i)  # 淘宝商品页面列表从0,44,88。
                html = Test1.getHTMLText(url)  # 两个函数
                plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',
                                 html)  # 以列表类型返回形如  "view_price":"186.2" ,反斜杠\" \"表示"view_price"
                tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
                for i in range(len(plt)):
                    price = eval(plt[i].split(':')[1])  # 详见淘宝商品信息爬虫（1）
                    title = eval(tlt[i].split(':')[1])
                    item = QtWidgets.QTreeWidgetItem()
                    item.setText(0, title)
                    item.setData(1,QtCore.Qt.DisplayRole,float(price))
                    self.treeWidget.addTopLevelItem(item)
            except:
                continue
        print("222")
    def btnclick(self):
        self.treeWidget.clear()
        self.lineEdit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    styleFile = './orange-dark.qss'
    with open(styleFile, encoding='utf-8') as file_obj:
        contents = file_obj.read()
    myWin.setStyleSheet(contents)
    myWin.setWindowTitle("淘淘看")
    myWin.setWindowIcon(QIcon(":/123.jpg"))
    myWin.show()
    sys.exit(app.exec_())