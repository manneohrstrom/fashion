
import os
import logging
import optparse
import sys


# PREPEND python location to pythonpath
python_path = os.path.abspath(os.path.join( os.path.dirname(__file__), "python"))
sys.path.insert(0, python_path)

from PySide import QtCore, QtGui
from app import AppDialog


# set up logging channel for this script
log = logging.getLogger("fashion")



def main():
    

    # Create a Qt application
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('plastique'))

    d = AppDialog()
    d.resize(480, 800)    

    if sys.platform != "darwin":
        d.showFullScreen()
        app.setOverrideCursor(QtCore.Qt.BlankCursor)
    else:
        d.show()

    d.setStyleSheet("""
        QPushButton { 
            border: 4px solid red; border-radius: 10px; 
        }

        QDialog { 

            background-image: url(:/tk_multi_infopanel/escheresque_ste.png);
            background-repeat: repeat-xy;
        }
        
        """)
    
    # Enter Qt application main loop
    app.exec_()

if __name__ == "__main__":
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)s %(message)s")
    ch.setFormatter(formatter)
    log.addHandler(ch)

    exit_code = 1
    try:
        main()
        exit_code = 0
    except Exception, e:
        log.exception("An exception was raised: %s" % e)
                
    log.info("Exiting with code %d. Sayonara." % exit_code)
    sys.exit(exit_code)
        