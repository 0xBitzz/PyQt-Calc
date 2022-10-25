from PyQt5.QtWidgets import QApplication, QFrame, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import sys, functools


class Window(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.display_lay = QVBoxLayout()
        self.edit = QLineEdit()
        self.edit.setPlaceholderText('0')
        self.edit.setReadOnly(True)
        self.text_edit_style(self.edit)
        self.result_edit = QLineEdit()
        self.result_edit.setPlaceholderText('0')
        self.result_edit.setReadOnly(True)
        self.text_edit_style(self.result_edit)
        self.result_edit.setAlignment(Qt.AlignRight)
        self.display_lay.addWidget(self.edit)
        self.display_lay.addWidget(self.result_edit)
        self.display_lay.setSpacing(0)
        self.clicked_buttons = []
        self.setWindowTitle('Calculator')
        self.setFixedSize(350, 500)
        self._setup()

    def _setup(self):
        button = QPushButton('AC')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.grid_layout.addWidget(button, 0, 0)
        button = QPushButton('DEL')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.grid_layout.addWidget(button, 0, 1)
        button = QPushButton('^')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.grid_layout.addWidget(button, 0, 2)
        button = QPushButton('÷')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        button.setObjectName('sign_btn')
        self.button_style(button)
        self.grid_layout.addWidget(button, 0, 3)
        button = QPushButton('7')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.grid_layout.addWidget(button, 1, 0)
        button = QPushButton('8')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.grid_layout.addWidget(button, 1, 1)
        button = QPushButton('9')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.grid_layout.addWidget(button, 1, 2)
        button = QPushButton('×')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        button.setObjectName('sign_btn')
        self.button_style(button)
        self.grid_layout.addWidget(button, 1, 3)
        button = QPushButton('4')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.grid_layout.addWidget(button, 2, 0)
        button = QPushButton('5')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.grid_layout.addWidget(button, 2, 1)
        button = QPushButton('6')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.grid_layout.addWidget(button, 2, 2)
        button = QPushButton('+')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        button.setObjectName('sign_btn')
        self.button_style(button)
        self.grid_layout.addWidget(button, 2, 3)
        button = QPushButton('1')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.grid_layout.addWidget(button, 3, 0)
        button = QPushButton('2')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.grid_layout.addWidget(button, 3, 1)
        button = QPushButton('3')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.grid_layout.addWidget(button, 3, 2)
        button = QPushButton('-')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        button.setObjectName('sign_btn')
        self.button_style(button)
        self.grid_layout.addWidget(button, 3, 3)
        button = QPushButton('0')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.grid_layout.addWidget(button, 4, 0)
        button = QPushButton('.')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.grid_layout.addWidget(button, 4, 1)
        button = QPushButton('(')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.h_layout.addWidget(button)
        button = QPushButton(')')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        self.button_style(button)
        self.h_layout.addWidget(button)
        self.grid_layout.addItem(self.h_layout, 4, 2)
        button = QPushButton('=')
        button.clicked.connect(functools.partial(self.calculate, button.text()))
        button.setObjectName('sign_btn')
        self.button_style(button)

        self.grid_layout.addWidget(button, 4, 3)
        self.v_layout.addWidget(self.edit)
        self.v_layout.addWidget(self.result_edit)
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.setSpacing(0)
        self.v_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.v_layout)
        self.show()

    def text_edit_style(self, text_edit):
        text_edit.setStyleSheet(
            '''
            QLineEdit{
                height: 70%;
                background-color: gray;
                color: white;
                font-weight: 25%;
                font-size:50px;
                border-radius: 0px;
            }
            '''
        )
        return text_edit

    def button_style(self, btn):
        btn.setStyleSheet(
            '''
            QPushButton{
                border: inset;
                background-color: white;
                height: 75%;
                color: #000;
                border-radius: 0;
                font-weight: 25%;            
                font-size: 35px;
            }

            QPushButton::hover{
                background-color: white;
                color: gray;
            }

            #sign_btn{
                background-color: orange;
                color: white;
            }
            #sign_btn::hover{
                background-color: orange;
                color: gray;
            }
            '''
        )
        return btn

    # TODO: Fix calculation problems
    def calculate(self, btn):
        signs = ['**', '*', '/', '+', '-']
        if btn not in ['DEL', 'AC', '=']:
            if btn == '.':
                btn = '0.'
            self.edit.insert(btn)
            if btn == '^':
                btn = '**'
            elif btn == '÷':
                btn = '/'
            elif btn == '×':
                btn = '*'
            elif btn == '(':
                btn = '*('
            self.clicked_buttons += btn
        elif btn == 'AC':
            self.edit.clear()
            self.result_edit.clear()
            self.clicked_buttons.clear()
        elif btn == '=':
            try:
                result = str(eval(''.join(self.clicked_buttons)))
                if '.' in result:
                    decimal_ind = result.index('.')
                    if len(result[decimal_ind + 1]) == 1 and result[decimal_ind + 1] == '0':
                        result = result[:decimal_ind]
                self.result_edit.setText(result)
                self.clicked_buttons = [result]
                self.clicked_buttons.clear()
            except ZeroDivisionError:
                self.result_edit.setText('Syntax Error')
        print(self.clicked_buttons)


app = QApplication([])
window = Window()
sys.exit(app.exec_())
