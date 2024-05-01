from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
from translator import *
import dic,about,pyperclip,os,langdetect,gtts
if not os.path.exists("data"):
        os.makedirs("data")
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("المترجم")
        self.إظهار1=qt.QLabel("الترجمة الى")
        self.اللغات=qt.QComboBox()
        self.اللغات.addItems(dic.languages.keys())        
        self.اللغات.setAccessibleName("الترجمة الى")
        self.إظهار2=qt.QLabel("أكتب النص هنا")
        self.النص=qt.QLineEdit()
        self.النص.setAccessibleName("أكتب النص هنا")
        self.ترجمة=qt.QPushButton("ترجمة")
        self.ترجمة.setDefault(True)
        self.ترجمة.clicked.connect(self.tr)
        self.إظهار3=qt.QLabel("الترجمة هي")
        self.الترجمة_هي=qt.QLineEdit()
        self.الترجمة_هي.setAccessibleName("الترجمة هي")
        self.الترجمة_هي.setReadOnly(True)
        self.نسخ=qt.QPushButton("نسخ الترجمة")
        self.نسخ.setDefault(True)
        self.نسخ.clicked.connect(self.copy)
        self.إستماع=qt.QPushButton("الاستماع الى الترجمة")
        self.إستماع.setDefault(True)
        self.إستماع.clicked.connect(self.listen)
        self.عن=qt.QPushButton("عن المطور")
        self.عن.setDefault(True)
        self.عن.clicked.connect(self.about)
        l=qt.QVBoxLayout()        
        l.addWidget(self.إظهار1)
        l.addWidget(self.اللغات)
        l.addWidget(self.إظهار2)
        l.addWidget(self.النص)
        l.addWidget(self.ترجمة)
        l.addWidget(self.إظهار3)
        l.addWidget(self.الترجمة_هي)
        l.addWidget(self.نسخ)
        l.addWidget(self.إستماع)
        l.addWidget(self.عن)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)        
    def about(self):
        about.dialog(self).exec()
    def tr(self):        
        try:
            المترجم=GoogleTranslator()
            self.الترجمة_هي.setText(المترجم.translate(self.النص.text(),dest=self.اللغات.currentText()))
            self.الترجمة_هي.setFocus()
        except:
            qt.QMessageBox.warning(self,"تنبيه","فشلت عملية الترجمة, ربما اللغة غير مدعومة, أو هناك خطأ في الإنترنت")
    def copy(self):
        pyperclip.copy(self.الترجمة_هي.text())
    def listen(self):
        try:
            النص=self.الترجمة_هي.text()
            lang=langdetect.detect(النص)
            result=gtts.gTTS(النص,lang=lang)
            result.save("data/message.mp3")
            os.startfile(os.getcwd()+"/data/message.mp3")
        except:
            qt.QMessageBox.information(self,"تنبيه","عفوا, يرجى إدخال نص أو التأكد من الإتصال بالإنترنت")
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()