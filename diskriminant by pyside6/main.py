import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow
from rework_app_ui import Ui_MainWindow

class Disik(QMainWindow):
    def __init__(self):
        super(Disik, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        calculate_button = self.ui.RESULT_BUTTON

        calculate_button.clicked.connect(self.result)

    def result(self):
        self.a = float(self.ui.USER_TEXT_A.text()) 
        self.b = float(self.ui.USER_TEXT_B.text())
        self.c = float(self.ui.USER_TEXT_C.text())

        discriminant = self.b ** 2 - 4 * self.a * self.c
        self.ui.RESULT_LABEL_1.setText(f'D = {self.b}^2 - 4 ({self.a} * {self.c}) = {discriminant}')

        if discriminant > 0:
            sqrt_discriminant = math.sqrt(discriminant)
            self.ui.RESULT_LABEL_2.setText(f'√D = {sqrt_discriminant}') 
            self.ui.RESULT_LABEL_3.setText(f'x1 = ({-self.b} - {sqrt_discriminant}) / (2 * {self.a}) = {(-self.b - sqrt_discriminant) / (2 * self.a)}')
            self.ui.RESULT_LABEL_4.setText(f'x2 = ({-self.b} + {sqrt_discriminant}) / (2 * {self.a}) = {(-self.b + sqrt_discriminant) / (2 * self.a)}')
            
            x = np.linspace(-10, 10, 400)
            y = self.a * x**2 + self.b * x + self.c
            plt.plot(x,y)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.grid()
            plt.show()

        elif discriminant == 0:
            self.ui.RESULT_LABEL_2.setText('D = 0, one root:')
            self.ui.RESULT_LABEL_3.setText(f'x = {-self.b} / (2 * {self.a}) = {-self.b / (2 * self.a)}')
            self.ui.RESULT_LABEL_4.setText('')

        else:
            self.ui.RESULT_LABEL_2.setText('D < 0, zero root')
            self.ui.RESULT_LABEL_3.setText('')
            self.ui.RESULT_LABEL_4.setText('')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Disik()
    window.show()
    sys.exit(app.exec())