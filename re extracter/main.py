import sys
from custome_errors import *
sys.excepthook = my_excepthook
import re
import gui
import guiTools
from settings import *
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
language.init_translation()
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        layout=qt.QVBoxLayout()
        self.code=qt.QLineEdit()
        self.code.setAccessibleName(_("Regular expression code"))
        self.text=qt.QLineEdit()
        self.text.setAccessibleName(_("text"))
        self.generate=qt.QPushButton(_("generate"))
        self.generate.setDefault(True)
        self.generate.clicked.connect(self.gene)
        self.result=qt.QComboBox()
        self.result.setAccessibleName(_("result"))
        layout.addWidget(self.code)
        layout.addWidget(self.text)
        layout.addWidget(self.generate)
        layout.addWidget(self.result)
        self.setting=qt.QPushButton(_("settings"))
        self.setting.setDefault(True)
        self.setting.clicked.connect(lambda: settings(self).exec())
        layout.addWidget(self.setting)
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/tprogrammers"))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:guiTools.OpenLink(self,"https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
    def closeEvent(self, event):
        if settings_handler.get("g","exitDialog")=="True":
            m=guiTools.ExitApp(self)
            m.exec()
            if m:
                event.ignore()
        else:
            self.close()
    def gene(self):
        try:
            self.result.clear()
            self.result.addItems(re.findall(self.code.text(),self.text.text()))
            self.result.setFocus()
        except:
            guiTools.speak(_("error"))
App=qt.QApplication([])
w=main()
w.show()
App.exec()