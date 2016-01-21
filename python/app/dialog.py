from PySide import QtCore, QtGui
from .ui.dialog import Ui_Dialog

class AppDialog(QtGui.QWidget):
    """
    Main application dialog window. This defines the top level UI
    and binds all UI objects together.
    """
        
    def __init__(self, parent=None):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self, parent)
        
        # now load in the UI that was created in the UI designer
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)

