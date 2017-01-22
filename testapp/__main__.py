from __future__ import print_function
import sys
import argparse

from PyQt4 import QtGui, QtCore
from Classes import mGUI


def main():
    parser = argparse.ArgumentParser(description='This app is just a test')
    parser.add_argument('--gui', default=True,
                        help='Launch a PyQt gui rather than the command line')
    args = parser.parse_args()

    if args.gui:
        print('The GUI is launching')
        app = QtGui.QApplication(sys.argv)
        qw = mGUI.QuitWindow()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()
