from PySide import QtCore, QtGui
from .ui.dialog import Ui_Dialog

import random

class AppDialog(QtGui.QDialog):
    """
    Main application dialog window. This defines the top level UI
    and binds all UI objects together.
    """
        
    def __init__(self, parent=None):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QDialog.__init__(self, parent)
        
        # now load in the UI that was created in the UI designer
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)


        self._background_index = 1

        self.ui.pushButton_2.clicked.connect(self._change_background)

        self.ui.pushButton_3.clicked.connect(self._take_picture)



    def _take_picture(self):

        import picamera
        import time

        camera = picamera.PiCamera()
        try:
            camera.start_preview()            
            camera.capture('foo.jpg')
            time.sleep(2)
            camera.stop_preview()
        finally:
            camera.close()


    def _change_background(self):
        
        self._background_index = random.randint(1,57)

        self.setStyleSheet("""
            QPushButton { 
                border: 4px solid red; border-radius: 10px; 
            }

            QDialog { 

                background-image: url(:/tk_multi_infopanel/bg/%d.jpg);
                background-repeat: repeat-xy;
            }
        
        """ % self._background_index)


