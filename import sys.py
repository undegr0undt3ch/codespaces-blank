import sys
import math
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget, QLabel, QLCDNumber

class MiniCalculate(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(500, 500, 420, 260)
        self.setWindowTitle("Калькулятор треугольников")

        self.inpugl1 = QLineEdit(self)
        self.inpugl1.setText('0')
        self.inpugl1.setGeometry(20, 125, 70, 30)

        self.inpugl2 = QLineEdit(self)
        self.inpugl2.setText('0')
        self.inpugl2.setGeometry(20, 175, 70, 30)

        self.inpugl3 = QLineEdit(self)
        self.inpugl3.setText('0')
        self.inpugl3.setGeometry(20, 225, 70, 30)

        self.uslovie1 = QLabel(self)
        self.uslovie1.move(10, 10)
        self.uslovie1.setText("1. Вводить только три переменные на выбор:")
        self.uslovie1 = QLabel(self)
        self.uslovie1.move(10, 25)
        self.uslovie1.setText("а) 3 стороны; б) 2 стороны и угол между ними; в) 2 угла и сторону между ними.")
        self.uslovie1 = QLabel(self)
        self.uslovie1.move(10, 40)
        self.uslovie1.setText('2. 0 обозначает пустую клетку,')
        self.uslovie1 = QLabel(self)
        self.uslovie1.move(10, 55)
        self.uslovie1.setText("то есть для пустой клетки нужно написать ноль.")

        self.oninpugl1 = QLabel(self)
        self.oninpugl1.move(22, 110)
        self.oninpugl1.setText("Первый угол")

        self.oninpugl2 = QLabel(self)
        self.oninpugl2.move(22, 160)
        self.oninpugl2.setText("Второй угол")

        self.oninpugl3 = QLabel(self)
        self.oninpugl3.move(22, 210)
        self.oninpugl3.setText("Третий угол")

        self.inpst1 = QLineEdit(self)
        self.inpst1.setText('0')
        self.inpst1.setGeometry(100, 125, 70, 30)

        self.inpst2 = QLineEdit(self)
        self.inpst2.setText('0')
        self.inpst2.setGeometry(100, 175, 70, 30)

        self.inpst3 = QLineEdit(self)
        self.inpst3.setText('0')
        self.inpst3.setGeometry(100, 225, 70, 30)

        self.oninpst1 = QLabel(self)
        self.oninpst1.move(100, 110)
        self.oninpst1.setText("Первая сторона")

        self.oninpst2 = QLabel(self)
        self.oninpst2.move(100, 160)
        self.oninpst2.setText("Вторая сторона")

        self.oninpst3 = QLabel(self)
        self.oninpst3.move(100, 210)
        self.oninpst3.setText("Третья сторона")

        self.btn = QPushButton("->", self)
        self.btn.setGeometry(185, 125, 70, 130)
        self.btn.clicked.connect(self.result)

        self.sumDisp = QLCDNumber(self)
        self.sumDisp.setGeometry(320, 127, 70, 25)

        self.differenceDisp = QLCDNumber(self)
        self.differenceDisp.setGeometry(320, 159, 70, 25)

        self.multiplicationDisp = QLCDNumber(self)
        self.multiplicationDisp.setGeometry(320, 191, 70, 25)

        self.divisionDisp = QLCDNumber(self)
        self.divisionDisp.setGeometry(320, 231, 70, 25)

        self.labelSumDisp = QLabel(self)
        self.labelSumDisp.move(260, 127)
        self.labelSumDisp.setText("Площадь")

        self.labelDifferenceDisp = QLabel(self)
        self.labelDifferenceDisp.move(260, 159)
        self.labelDifferenceDisp.setText("Периметр")

        self.labelMultiplicationDisp = QLabel(self)
        self.labelMultiplicationDisp.move(260, 191)
        self.labelMultiplicationDisp.setText("Сумма углов")

        self.labelDivisionDisp = QLabel(self)
        self.labelDivisionDisp.move(245, 223)
        self.labelDivisionDisp.setText("")

    def result(self):
        st1 = float(self.inpst1.text())
        st2 = float(self.inpst2.text())
        st3 = float(self.inpst3.text())
        ugl1 = float(self.inpugl1.text())
        ugl2 = float(self.inpugl2.text())
        ugl3 = float(self.inpugl3.text())
        uglsum = 0
        perim = 0
        s = 0
        if st1 > st2 + st3 or st2 > st1 + st3 or st3 > st2 + st1:
            self.divisionDisp.display('Error')
            self.sumDisp.display('Error')
            self.multiplicationDisp.display('Error')
            self.differenceDisp.display('Error')
        elif ugl1 != 0 and ugl2 != 0 and ugl3 != 0:
            self.divisionDisp.display('Error')
            self.sumDisp.display('Error')
            self.multiplicationDisp.display('Error')
            self.differenceDisp.display('Error')
        elif ugl1 != 0 and ugl2 != 0 and ugl3 != 0:
            self.divisionDisp.display('Error')
            self.sumDisp.display('Error')
            self.multiplicationDisp.display('Error')
            self.differenceDisp.display('Error')
        else:
            if st1 != 0 and st2 != 0 and st3 != 0:
                chisl1 = st2 ** 2 + st3 ** 2 - st1 ** 2
                znam1 = 2 * st2 * st3
                cos1 = chisl1 / znam1
                ugl1 = math.acos(cos1) * 180 / math.pi
                chisl2 = st1 ** 2 + st3 ** 2 - st2 ** 2
                znam2 = 2 * st1 * st3
                cos2 = chisl2 / znam2
                ugl2 = math.acos(cos2) * 180 / math.pi
                chisl3 = st1 ** 2 + st2 ** 2 - st3 ** 2
                znam3 = 2 * st1 * st2
                cos3 = chisl3 / znam3
                ugl3 = math.acos(cos3) * 180 / math.pi
                uglsum = ugl1 + ugl2 + ugl3
                self.multiplicationDisp.display(uglsum)
                perim = st1 + st2 + st3
                self.differenceDisp.display(perim)
                s = st2 * st3 * math.sin(ugl1 * math.pi / 180) / 2
                self.sumDisp.display(s)
            else:
                ugl3 = float(self.inpugl3.text())
                if st1 != 0 and st2 != 0 and ugl3 != 0:
                    st3 = st1 ** 2 + st2 ** 2 - 2 * st1 * st2 * math.cos(ugl3 * math.pi / 180)
                    st3 = math.sqrt(st3)
                    chisl1 = st2 ** 2 + st3 ** 2 - st1 ** 2
                    znam1 = 2 * st2 * st3
                    cos1 = chisl1 / znam1
                    ugl1 = math.acos(cos1) * 180 / math.pi
                    chisl2 = st1 ** 2 + st3 ** 2 - st2 ** 2
                    znam2 = 2 * st1 * st3
                    cos2 = chisl2 / znam2
                    ugl2 = math.acos(cos2) * 180 / math.pi
                    uglsum = ugl1 + ugl2 + ugl3
                    self.multiplicationDisp.display(uglsum)
                    perim = st1 + st2 + st3
                    self.differenceDisp.display(perim)
                    s = st2 * st3 * math.sin(ugl1 * math.pi / 180) / 2
                    self.sumDisp.display(s)
                if st2 != 0 and st3 != 0 and ugl1 != 0:
                    st1 = st3 ** 2 + st2 ** 2 - 2 * st3 * st2 * math.cos(ugl1 * math.pi / 180)
                    st1 = math.sqrt(st1)
                    chisl2 = st1 ** 2 + st3 ** 2 - st2 ** 2
                    znam2 = 2 * st1 * st3
                    cos2 = chisl2 / znam2
                    ugl2 = math.acos(cos2) * 180 / math.pi
                    chisl3 = st2 ** 2 + st1 ** 2 - st3 ** 2
                    znam3 = 2 * st2 * st1
                    cos3 = chisl3 / znam3
                    ugl3 = math.acos(cos3) * 180 / math.pi
                    uglsum = ugl1 + ugl2 + ugl3
                    self.multiplicationDisp.display(uglsum)
                    perim = st1 + st2 + st3
                    self.differenceDisp.display(perim)
                    s = st2 * st3 * math.sin(ugl1 * math.pi / 180) / 2
                    self.sumDisp.display(s)
                if st1 != 0 and st3 != 0 and ugl2 != 0:
                    st2 = st3 ** 2 + st1 ** 2 - 2 * st3 * st1 * math.cos(ugl2 * math.pi / 180)
                    st2 = math.sqrt(st2)
                    chisl1 = st2 ** 2 + st3 ** 2 - st1 ** 2
                    znam1 = 2 * st2 * st3
                    cos1 = chisl1 / znam1
                    ugl1 = math.acos(cos1) * 180 / math.pi
                    chisl3 = st2 ** 2 + st1 ** 2 - st3 ** 2
                    znam3 = 2 * st2 * st1
                    cos3 = chisl3 / znam3
                    ugl3 = math.acos(cos3) * 180 / math.pi
                    uglsum = ugl1 + ugl2 + ugl3
                    self.multiplicationDisp.display(uglsum)
                    perim = st1 + st2 + st3
                    self.differenceDisp.display(perim)
                    s = st2 * st3 * math.sin(ugl1 * math.pi / 180) / 2
                    self.sumDisp.display(s)
                else:
                    if st1 != 0 and ugl2 != 0 and ugl3 != 0:
                        ugl1 = 180 - ugl2 - ugl3
                        st2 = st1 * math.sin(ugl2 * math.pi / 180) / math.sin(ugl1 * math.pi / 180)
                        st3 = st1 * math.sin(ugl3 * math.pi / 180) / math.sin(ugl1 * math.pi / 180)
                        uglsum = ugl1 + ugl2 + ugl3
                        self.multiplicationDisp.display(uglsum)
                        perim = st1 + st2 + st3
                        self.differenceDisp.display(perim)
                        s = st2 * st3 * math.sin(ugl1 * math.pi / 180) / 2
                        self.sumDisp.display(s)
                    if st2 != 0 and ugl1 != 0 and ugl3 != 0:
                        ugl2 = 180 - ugl1 - ugl3
                        st1 = st2 * math.sin(ugl1 * math.pi / 180) / math.sin(ugl2 * math.pi / 180)
                        st3 = st2 * math.sin(ugl3 * math.pi / 180) / math.sin(ugl2 * math.pi / 180)
                        uglsum = ugl1 + ugl2 + ugl3
                        self.multiplicationDisp.display(uglsum)
                        perim = st1 + st2 + st3
                        self.differenceDisp.display(perim)
                        s = st2 * st3 * math.sin(ugl1 * math.pi / 180) / 2
                        self.sumDisp.display(s)
                    if st3 != 0 and ugl1 != 0 and ugl2 != 0:
                        ugl3 = 180 - ugl1 - ugl2
                        st1 = st3 * math.sin(ugl1 * math.pi / 180) / math.sin(ugl3 * math.pi / 180)
                        st2 = st3 * math.sin(ugl2 * math.pi / 180) / math.sin(ugl3 * math.pi / 180)
                        uglsum = ugl1 + ugl2 + ugl3
                        self.multiplicationDisp.display(uglsum)
                        perim = st1 + st2 + st3
                        self.differenceDisp.display(perim)
                        s = st2 * st3 * math.sin(ugl1 * math.pi / 180) / 2
                        self.sumDisp.display(s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiniCalculate()
    ex.show()
    sys.exit(app.exec())