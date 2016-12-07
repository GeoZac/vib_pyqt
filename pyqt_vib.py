from __future__ import division
import sys
from PyQt4 import QtGui, uic
import matplotlib.pylab as pylab
import scipy.integrate
from pylab import arange, array

qtCreatorFile1 = "system_reponse.ui"  # Main Window.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile1)

qtCreatorFile2 = "widget.ui"  # Result Window.
Ui_Widget, QtBaseClass1 = uic.loadUiType(qtCreatorFile2)


class MyDia(QtGui.QMainWindow, Ui_Widget):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.start.clicked.connect(self.getresponse)

    def getresponse(self):
        def func(state, t):
            x, xd = state  # displacement,x and velocity x'
            # g = 9.8 # metres per second**2
            if ch == 2:
                xdd = -((k * x) / m) - ((c * xd) / m)
            else:
                xdd = ((-k * x) / m)  # + g
            return [xd, xdd]

        m = float(self.mass.toPlainText())
        k = float(self.k.toPlainText())
        c = float(self.c.toPlainText())
        if self.ch.isChecked() == True:
            ch = 2
        else:
            ch = 0
        # ch = 2
        x0 = float(self.id.value())     #Initial Displacement
        v0 = float(self.iv.value())     #Initial Velocity
        state0 = [x0, v0]               # initial conditions [x0 , v0]  [m, m/sec]
        ti = float(self.ti.value())     # initial time
        tf = float(self.tf.value())     # final time
        step = 0.0001                   # time step
        t = arange(ti, tf, step)
        state = scipy.integrate.odeint(func, state0, t)
        x = array(state[:, [0]])
        xd = array(state[:, [1]])

        # Plotting displacement and velocity
        # pylab.ion() No inline as widget is used
        pylab.rcParams['figure.figsize'] = (20, 12)
        pylab.rcParams['font.size'] = 18
        fig, ax1 = pylab.subplots()
        ax2 = ax1.twinx()
        ax2.plot(t, xd, 'g--', label=r'$\dot{x} (m/sec)$', linewidth=2.0)
        ax1.plot(t, x * 1e3, 'b', label=r'$x (mm)$', linewidth=2.0)
        ax2.legend(loc='lower right')
        ax1.legend()
        ax1.set_xlabel('time , sec')
        ax1.set_ylabel('disp (mm)', color='b')
        ax2.set_ylabel('velocity (m/s)', color='g')
        pylab.title('System Response')
        pylab.grid()
        pylab.savefig('read.png')
        window.close()  # close main window
        fig = MyDia()
        fig.show()  # open widget
        # pylab.show(block=True)
        # self.textEdit_2.setText(price_str)
        # self.textEdit.setText(tax_str)
        # self.results_window.setText(total_price_string)
        # self.fig.QGraphicsView(pylab)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
