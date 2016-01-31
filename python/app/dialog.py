from PySide import QtCore, QtGui
from .ui.dialog import Ui_Dialog

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


        self.ui.pushButton_2.clicked.connect(self.close)

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
        pass

