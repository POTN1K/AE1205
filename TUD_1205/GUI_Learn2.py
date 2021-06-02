# Using a User Interface to code faster

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic


def action():
    """Calculator function"""
    # Get parts
    operator = window.Operator.currentText()
    in1 = window.Input1.value()
    in2 = window.Input2.value()

    # Computation
    if operator == '+':
        res = in1 + in2
        window.Result.setText(str(res))
    elif operator == '-':
        res = in1 - in2
        window.Result.setText(str(res))
    elif operator == '*':
        res = in1 * in2
        window.Result.setText(str(res))
    elif operator == '/' and in2 != 0:
        res = in1 / in2
        window.Result.setText(str(res))
    else:
        window.Result.setText('Error')


# Create Qt Application
app = QApplication([])

# Load window previously created
window = uic.loadUi('./Data/GUI_Learn/Calculator.ui')

# Connect a calulator function
window.Equal.clicked.connect(action)

# Create loop of main function
window.show()
app.exec()
