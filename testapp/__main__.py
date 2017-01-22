from __future__ import print_function
import sys
import argparse

from PyQt4 import QtGui, QtCore
from Classes import mGUI


def main():
    if not len(sys.argv) > 1:
        launch_gui()
    else:
        parser = argparse.ArgumentParser(description='This app is just a test')
        parser.add_argument('--gui', dest='gui', action='store_true',
                        help='Launch a PyQt gui rather than the command line')
        parser.add_argument('--no-gui', dest='gui',
                        action='store_false')
        args = parser.parse_args()
        print(args)

    if args.gui:
        launch_gui()

def launch_gui():
    print('The GUI is launching')
    app = QtGui.QApplication(sys.argv)
    qw = mGUI.QuitWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
