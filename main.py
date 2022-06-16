import sys
import time
import sqlite3

import API_functions
from KILOVIEWS_DASHBOARD_v8 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QTimer, QDateTime

class main_GUI(QMainWindow, Ui_MainWindow):

    take_app = None
    take_stream = None
    source_ident = '12a34s56d'
    source_status = None
    take_iden = None
    status_dest = None
    status_app = None
    status_stream = None


    def __init__(self, parent=None):
        super(main_GUI, self).__init__(parent)
        self.showMaximized()
        self.setupUi(self)
        self.menuMATRIU.setCurrentIndex(0)

        # inicialitzem timer per actualitzar el dashboard
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(5000)

        # ===================================================================================
        # NAS
        # botons per cambiar el bitrate amb les funcions setBitrate1 i setBitrate20
        self.nas1_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.17.146.31'))
        self.nas1_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.17.146.31'))
        self.nas2_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.17.146.32'))
        self.nas2_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.17.146.32'))
        self.nas3_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.17.146.33'))
        self.nas3_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.17.146.33'))
        self.nas4_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.17.146.34'))
        self.nas4_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.17.146.34'))
        self.nas5_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.17.146.35'))
        self.nas5_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.17.146.35'))
        self.nas6_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.17.146.36'))
        self.nas6_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.17.146.36'))
        self.nas7_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.17.146.37'))
        self.nas7_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.17.146.37'))
        self.nas8_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.17.146.38'))
        self.nas8_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.17.146.38'))
        self.nas9_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.17.146.39'))
        self.nas9_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.17.146.39'))
        self.nas10_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.17.146.40'))
        self.nas10_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.17.146.40'))

        # botons setBitrate
        self.nas1_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.17.146.31', self.nas1_setbitrate.text()))
        self.nas1_setbitrate_button.clicked.connect(lambda: self.nas1_setbitrate.clear())
        self.nas2_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.17.146.32', self.nas2_setbitrate.text()))
        self.nas2_setbitrate_button.clicked.connect(lambda: self.nas2_setbitrate.clear())
        self.nas3_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.17.146.33', self.nas3_setbitrate.text()))
        self.nas3_setbitrate_button.clicked.connect(lambda: self.nas3_setbitrate.clear())
        self.nas4_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.17.146.34', self.nas4_setbitrate.text()))
        self.nas4_setbitrate_button.clicked.connect(lambda: self.nas4_setbitrate.clear())
        self.nas5_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.17.146.35', self.nas5_setbitrate.text()))
        self.nas5_setbitrate_button.clicked.connect(lambda: self.nas5_setbitrate.clear())
        self.nas6_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.17.146.36', self.nas6_setbitrate.text()))
        self.nas6_setbitrate_button.clicked.connect(lambda: self.nas6_setbitrate.clear())
        self.nas7_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.17.146.37', self.nas7_setbitrate.text()))
        self.nas7_setbitrate_button.clicked.connect(lambda: self.nas7_setbitrate.clear())
        self.nas8_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.17.146.38', self.nas8_setbitrate.text()))
        self.nas8_setbitrate_button.clicked.connect(lambda: self.nas8_setbitrate.clear())
        self.nas9_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.17.146.39', self.nas9_setbitrate.text()))
        self.nas9_setbitrate_button.clicked.connect(lambda: self.nas9_setbitrate.clear())
        self.nas10_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.17.146.40', self.nas10_setbitrate.text()))
        self.nas10_setbitrate_button.clicked.connect(lambda: self.nas10_setbitrate.clear())

        # botons per fer la putivuelta
        self.nas1_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.17.146.31'))
        self.nas2_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.17.146.32'))
        self.nas3_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.17.146.33'))
        self.nas4_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.17.146.34'))
        self.nas5_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.17.146.35'))
        self.nas6_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.17.146.36'))
        self.nas7_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.17.146.37'))
        self.nas8_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.17.146.38'))
        self.nas9_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.17.146.39'))
        self.nas10_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.17.146.40'))

        # ===================================================================================
        # OB23
        # botons per cambiar el bitrate amb les funcions setBitrate1 i setBitrate20
        self.ob23_1_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.66.11'))
        self.ob23_1_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.66.11'))
        self.ob23_2_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.66.12'))
        self.ob23_2_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.66.12'))
        self.ob23_3_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.66.13'))
        self.ob23_3_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.66.13'))
        self.ob23_4_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.66.14'))
        self.ob23_4_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.66.14'))
        self.ob23_5_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.66.15'))
        self.ob23_5_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.66.15'))
        self.ob23_6_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.66.16'))
        self.ob23_6_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.66.16'))
        self.ob23_7_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.66.17'))
        self.ob23_7_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.66.17'))
        self.ob23_8_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.66.18'))
        self.ob23_8_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.66.18'))


        # botons setBitrate
        self.ob23_1_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.66.11', self.ob23_1_setbitrate.text()))
        self.ob23_1_setbitrate_button.clicked.connect(lambda: self.ob23_1_setbitrate.clear())
        self.ob23_2_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.66.12', self.ob23_2_setbitrate.text()))
        self.ob23_2_setbitrate_button.clicked.connect(lambda: self.ob23_2_setbitrate.clear())
        self.ob23_3_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.66.13', self.ob23_3_setbitrate.text()))
        self.ob23_3_setbitrate_button.clicked.connect(lambda: self.ob23_3_setbitrate.clear())
        self.ob23_4_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.66.14', self.ob23_4_setbitrate.text()))
        self.ob23_4_setbitrate_button.clicked.connect(lambda: self.ob23_4_setbitrate.clear())
        self.ob23_5_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.66.15', self.ob23_5_setbitrate.text()))
        self.ob23_5_setbitrate_button.clicked.connect(lambda: self.ob23_5_setbitrate.clear())
        self.ob23_6_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.66.16', self.ob23_6_setbitrate.text()))
        self.ob23_6_setbitrate_button.clicked.connect(lambda: self.ob23_6_setbitrate.clear())
        self.ob23_7_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.66.17', self.ob23_7_setbitrate.text()))
        self.ob23_7_setbitrate_button.clicked.connect(lambda: self.ob23_7_setbitrate.clear())
        self.ob23_8_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.66.18', self.ob23_8_setbitrate.text()))
        self.ob23_8_setbitrate_button.clicked.connect(lambda: self.ob23_8_setbitrate.clear())

        # botons per fer la putivuelta
        self.ob23_1_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.66.11'))
        self.ob23_2_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.66.12'))
        self.ob23_3_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.66.13'))
        self.ob23_4_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.66.14'))
        self.ob23_5_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.66.15'))
        self.ob23_6_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.66.16'))
        self.ob23_7_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.66.17'))
        self.ob23_8_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.66.18'))

        # ===================================================================================
        # OB39
        # botons per cambiar el bitrate amb les funcions setBitrate1 i setBitrate20
        self.ob39_1_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.64.11'))
        self.ob39_1_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.64.11'))
        self.ob39_2_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.64.12'))
        self.ob39_2_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.64.12'))
        self.ob39_3_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.64.13'))
        self.ob39_3_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.64.13'))
        self.ob39_4_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.64.14'))
        self.ob39_4_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.64.14'))
        self.ob39_5_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.64.15'))
        self.ob39_5_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.64.15'))
        self.ob39_6_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.64.16'))
        self.ob39_6_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.64.16'))
        self.ob39_7_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.64.17'))
        self.ob39_7_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.64.17'))
        self.ob39_8_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.64.18'))
        self.ob39_8_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.64.18'))

        # botons setBitrate
        self.ob39_1_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.64.11', self.ob39_1_setbitrate.text()))
        self.ob39_1_setbitrate_button.clicked.connect(lambda: self.ob39_1_setbitrate.clear())
        self.ob39_2_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.64.12', self.ob39_2_setbitrate.text()))
        self.ob39_2_setbitrate_button.clicked.connect(lambda: self.ob39_2_setbitrate.clear())
        self.ob39_3_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.64.13', self.ob39_3_setbitrate.text()))
        self.ob39_3_setbitrate_button.clicked.connect(lambda: self.ob39_3_setbitrate.clear())
        self.ob39_4_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.64.14', self.ob39_4_setbitrate.text()))
        self.ob39_4_setbitrate_button.clicked.connect(lambda: self.ob39_4_setbitrate.clear())
        self.ob39_5_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.64.15', self.ob39_5_setbitrate.text()))
        self.ob39_5_setbitrate_button.clicked.connect(lambda: self.ob39_5_setbitrate.clear())
        self.ob39_6_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.64.16', self.ob39_6_setbitrate.text()))
        self.ob39_6_setbitrate_button.clicked.connect(lambda: self.ob39_6_setbitrate.clear())
        self.ob39_7_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.64.17', self.ob39_7_setbitrate.text()))
        self.ob39_7_setbitrate_button.clicked.connect(lambda: self.ob39_7_setbitrate.clear())
        self.ob39_8_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.64.18', self.ob39_8_setbitrate.text()))
        self.ob39_8_setbitrate_button.clicked.connect(lambda: self.ob39_8_setbitrate.clear())

        #botons per fer la putivuelta
        self.ob39_1_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.64.11'))
        self.ob39_2_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.64.12'))
        self.ob39_3_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.64.13'))
        self.ob39_4_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.64.14'))
        self.ob39_5_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.64.15'))
        self.ob39_6_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.64.16'))
        self.ob39_7_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.64.17'))
        self.ob39_8_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.64.18'))

        # ===================================================================================
        # OB40
        # botons per cambiar el bitrate amb les funcions setBitrate1 i setBitrate20
        self.ob40_1_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.67.11'))
        self.ob40_1_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.67.11'))
        self.ob40_2_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.67.12'))
        self.ob40_2_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.67.12'))
        self.ob40_3_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.67.13'))
        self.ob40_3_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.67.13'))
        self.ob40_4_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.67.14'))
        self.ob40_4_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.67.14'))
        self.ob40_5_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.67.15'))
        self.ob40_5_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.67.15'))
        self.ob40_6_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.67.16'))
        self.ob40_6_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.67.16'))
        self.ob40_7_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.67.17'))
        self.ob40_7_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.67.17'))
        self.ob40_8_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.67.18'))
        self.ob40_8_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.67.18'))

        # botons setBitrate
        self.ob40_1_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.67.11', self.ob40_1_setbitrate.text()))
        self.ob40_1_setbitrate_button.clicked.connect(lambda: self.ob40_1_setbitrate.clear())
        self.ob40_2_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.67.12', self.ob40_2_setbitrate.text()))
        self.ob40_2_setbitrate_button.clicked.connect(lambda: self.ob40_2_setbitrate.clear())
        self.ob40_3_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.67.13', self.ob40_3_setbitrate.text()))
        self.ob40_3_setbitrate_button.clicked.connect(lambda: self.ob40_3_setbitrate.clear())
        self.ob40_4_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.67.14', self.ob40_4_setbitrate.text()))
        self.ob40_4_setbitrate_button.clicked.connect(lambda: self.ob40_4_setbitrate.clear())
        self.ob40_5_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.67.15', self.ob40_5_setbitrate.text()))
        self.ob40_5_setbitrate_button.clicked.connect(lambda: self.ob40_5_setbitrate.clear())
        self.ob40_6_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.67.16', self.ob40_6_setbitrate.text()))
        self.ob40_6_setbitrate_button.clicked.connect(lambda: self.ob40_6_setbitrate.clear())
        self.ob40_7_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.67.17', self.ob40_7_setbitrate.text()))
        self.ob40_7_setbitrate_button.clicked.connect(lambda: self.ob40_7_setbitrate.clear())
        self.ob40_8_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.67.18', self.ob40_8_setbitrate.text()))
        self.ob40_8_setbitrate_button.clicked.connect(lambda: self.ob40_8_setbitrate.clear())

        # botons per fer la putivuelta
        self.ob40_1_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.67.11'))
        self.ob40_2_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.67.12'))
        self.ob40_3_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.67.13'))
        self.ob40_4_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.67.14'))
        self.ob40_5_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.67.15'))
        self.ob40_6_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.67.16'))
        self.ob40_7_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.67.17'))
        self.ob40_8_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.67.18'))

        # ===================================================================================
        # OB53
        # botons per cambiar el bitrate amb les funcions setBitrate1 i setBitrate20
        self.ob53_1_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.63.11'))
        self.ob53_1_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.63.11'))
        self.ob53_2_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.63.12'))
        self.ob53_2_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.63.12'))
        self.ob53_3_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.63.13'))
        self.ob53_3_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.63.13'))
        self.ob53_4_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.63.14'))
        self.ob53_4_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.63.14'))
        self.ob53_5_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.63.15'))
        self.ob53_5_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.63.15'))
        self.ob53_6_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.63.16'))
        self.ob53_6_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.63.16'))
        self.ob53_7_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.63.17'))
        self.ob53_7_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.63.17'))
        self.ob53_8_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.63.18'))
        self.ob53_8_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.63.18'))

        # botons setBitrate
        self.ob53_1_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.63.11', self.ob53_1_setbitrate.text()))
        self.ob53_1_setbitrate_button.clicked.connect(lambda: self.ob53_1_setbitrate.clear())
        self.ob53_2_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.63.12', self.ob53_2_setbitrate.text()))
        self.ob53_2_setbitrate_button.clicked.connect(lambda: self.ob53_2_setbitrate.clear())
        self.ob53_3_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.63.13', self.ob53_3_setbitrate.text()))
        self.ob53_3_setbitrate_button.clicked.connect(lambda: self.ob53_3_setbitrate.clear())
        self.ob53_4_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.63.14', self.ob53_4_setbitrate.text()))
        self.ob53_4_setbitrate_button.clicked.connect(lambda: self.ob53_4_setbitrate.clear())
        self.ob53_5_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.63.15', self.ob53_5_setbitrate.text()))
        self.ob53_5_setbitrate_button.clicked.connect(lambda: self.ob53_5_setbitrate.clear())
        self.ob53_6_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.63.16', self.ob53_6_setbitrate.text()))
        self.ob53_6_setbitrate_button.clicked.connect(lambda: self.ob53_6_setbitrate.clear())
        self.ob53_7_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.63.17', self.ob53_7_setbitrate.text()))
        self.ob53_7_setbitrate_button.clicked.connect(lambda: self.ob53_7_setbitrate.clear())
        self.ob53_8_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.63.18', self.ob53_8_setbitrate.text()))
        self.ob53_8_setbitrate_button.clicked.connect(lambda: self.ob53_8_setbitrate.clear())

        # botons per fer la putivuelta
        self.ob53_1_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.63.11'))
        self.ob53_2_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.63.12'))
        self.ob53_3_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.63.13'))
        self.ob53_4_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.63.14'))
        self.ob53_5_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.63.15'))
        self.ob53_6_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.63.16'))
        self.ob53_7_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.63.17'))
        self.ob53_8_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.63.18'))

        # ===================================================================================
        # OB86
        # botons per cambiar el bitrate amb les funcions setBitrate1 i setBitrate20
        self.ob86_1_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.68.11'))
        self.ob86_1_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.68.11'))
        self.ob86_2_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.68.12'))
        self.ob86_2_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.68.12'))
        self.ob86_3_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.68.13'))
        self.ob86_3_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.68.13'))
        self.ob86_4_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.68.14'))
        self.ob86_4_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.68.14'))
        self.ob86_5_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.68.15'))
        self.ob86_5_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.68.15'))
        self.ob86_6_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.68.16'))
        self.ob86_6_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.68.16'))
        self.ob86_7_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.68.17'))
        self.ob86_7_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.68.17'))
        self.ob86_8_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.68.18'))
        self.ob86_8_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.68.18'))

        # botons setBitrate
        self.ob86_1_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.68.11', self.ob86_1_setbitrate.text()))
        self.ob86_1_setbitrate_button.clicked.connect(lambda: self.ob86_1_setbitrate.clear())
        self.ob86_2_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.68.12', self.ob86_2_setbitrate.text()))
        self.ob86_2_setbitrate_button.clicked.connect(lambda: self.ob86_2_setbitrate.clear())
        self.ob86_3_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.68.13', self.ob86_3_setbitrate.text()))
        self.ob86_3_setbitrate_button.clicked.connect(lambda: self.ob86_3_setbitrate.clear())
        self.ob86_4_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.68.14', self.ob86_4_setbitrate.text()))
        self.ob86_4_setbitrate_button.clicked.connect(lambda: self.ob86_4_setbitrate.clear())
        self.ob86_5_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.68.15', self.ob86_5_setbitrate.text()))
        self.ob86_5_setbitrate_button.clicked.connect(lambda: self.ob86_5_setbitrate.clear())
        self.ob86_6_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.68.16', self.ob86_6_setbitrate.text()))
        self.ob86_6_setbitrate_button.clicked.connect(lambda: self.ob86_6_setbitrate.clear())
        self.ob86_7_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.68.17', self.ob86_7_setbitrate.text()))
        self.ob86_7_setbitrate_button.clicked.connect(lambda: self.ob86_7_setbitrate.clear())
        self.ob86_8_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.68.18', self.ob86_8_setbitrate.text()))
        self.ob86_8_setbitrate_button.clicked.connect(lambda: self.ob86_8_setbitrate.clear())


        # botons per fer la putivuelta
        self.ob86_1_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.68.11'))
        self.ob86_2_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.68.12'))
        self.ob86_3_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.68.13'))
        self.ob86_4_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.68.14'))
        self.ob86_5_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.68.15'))
        self.ob86_6_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.68.16'))
        self.ob86_7_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.68.17'))
        self.ob86_8_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.68.18'))

        # ===================================================================================
        # OB89
        # botons per cambiar el bitrate amb les funcions setBitrate1 i setBitrate20
        self.ob89_1_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.42.11'))
        self.ob89_1_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.42.11'))
        self.ob89_2_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.42.12'))
        self.ob89_2_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.42.12'))
        self.ob89_3_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.42.13'))
        self.ob89_3_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.42.13'))
        self.ob89_4_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.42.14'))
        self.ob89_4_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.42.14'))
        self.ob89_5_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.42.15'))
        self.ob89_5_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.42.15'))
        self.ob89_6_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.42.16'))
        self.ob89_6_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.42.16'))
        self.ob89_7_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.42.17'))
        self.ob89_7_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.42.17'))
        self.ob89_8_bitrate1.clicked.connect(lambda: API_functions.setBitrate1('10.28.42.18'))
        self.ob89_8_bitrate20.clicked.connect(lambda: API_functions.setBitrate20('10.28.42.18'))

        #botons setBitrate
        self.ob89_1_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.42.11', self.ob89_1_setbitrate.text()))
        self.ob89_1_setbitrate_button.clicked.connect(lambda: self.ob89_1_setbitrate.clear())
        self.ob89_2_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.42.12', self.ob89_2_setbitrate.text()))
        self.ob89_2_setbitrate_button.clicked.connect(lambda: self.ob89_2_setbitrate.clear())
        self.ob89_3_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.42.13', self.ob89_3_setbitrate.text()))
        self.ob89_3_setbitrate_button.clicked.connect(lambda: self.ob89_3_setbitrate.clear())
        self.ob89_4_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.42.14', self.ob89_4_setbitrate.text()))
        self.ob89_4_setbitrate_button.clicked.connect(lambda: self.ob89_4_setbitrate.clear())
        self.ob89_5_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.42.15', self.ob89_5_setbitrate.text()))
        self.ob89_5_setbitrate_button.clicked.connect(lambda: self.ob89_5_setbitrate.clear())
        self.ob89_6_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.42.16', self.ob89_6_setbitrate.text()))
        self.ob89_6_setbitrate_button.clicked.connect(lambda: self.ob89_6_setbitrate.clear())
        self.ob89_7_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.42.17', self.ob89_7_setbitrate.text()))
        self.ob89_7_setbitrate_button.clicked.connect(lambda: self.ob89_7_setbitrate.clear())
        self.ob89_8_setbitrate_button.clicked.connect(lambda: API_functions.setPort('10.28.42.18', self.ob89_8_setbitrate.text()))
        self.ob89_8_setbitrate_button.clicked.connect(lambda: self.ob89_8_setbitrate.clear())

        # botons per fer la putivuelta
        self.ob89_1_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.42.11'))
        self.ob89_2_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.42.12'))
        self.ob89_3_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.42.13'))
        self.ob89_4_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.42.14'))
        self.ob89_5_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.42.15'))
        self.ob89_6_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.42.16'))
        self.ob89_7_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.42.17'))
        self.ob89_8_putivuelta.clicked.connect(lambda: API_functions.putiVuelta('10.28.42.18'))

        # BOTONS LABEL canviar D300-1
        # NAS

        self.nas1_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'Kiloview NAS', 'Kiloview NAS 1'))
        self.nas2_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'Kiloview NAS', 'Kiloview NAS 2'))
        self.nas3_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'Kiloview NAS', 'Kiloview NAS 3'))
        self.nas4_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'Kiloview NAS', 'Kiloview NAS 4'))
        self.nas5_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'Kiloview NAS', 'Kiloview NAS 5'))
        self.nas6_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'Kiloview NAS', 'Kiloview NAS 6'))
        self.nas7_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'Kiloview NAS', 'Kiloview NAS 7'))
        self.nas8_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'Kiloview NAS', 'Kiloview NAS 8'))
        self.nas9_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'Kiloview NAS', 'Kiloview NAS 9'))
        self.nas10_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'Kiloview NAS', 'Kiloview NAS 10'))

        # OB23
        self.ob231_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB23', 'ENCODER OB23-1'))
        self.ob232_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB23', 'ENCODER OB23-2'))
        self.ob233_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB23', 'ENCODER OB23-3'))
        self.ob234_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB23', 'ENCODER OB23-4'))
        self.ob235_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB23', 'ENCODER OB23-5'))
        self.ob236_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB23', 'ENCODER OB23-6'))
        self.ob237_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB23', 'ENCODER OB23-7'))
        self.ob238_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB23', 'ENCODER OB23-8'))

        # OB39
        self.ob391_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB39', 'ENCODER OB39-1'))
        self.ob392_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB39', 'ENCODER OB39-2'))
        self.ob393_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB39', 'ENCODER OB39-3'))
        self.ob394_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB39', 'ENCODER OB39-4'))
        self.ob395_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB39', 'ENCODER OB39-5'))
        self.ob396_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB39', 'ENCODER OB39-6'))
        self.ob397_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB39', 'ENCODER OB39-7'))
        self.ob398_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB39', 'ENCODER OB39-8'))

        # OB40
        self.ob401_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB40', 'ENCODER OB40-1'))
        self.ob402_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB40', 'ENCODER OB40-2'))
        self.ob403_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB40', 'ENCODER OB40-3'))
        self.ob404_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB40', 'ENCODER OB40-4'))
        self.ob405_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB40', 'ENCODER OB40-5'))
        self.ob406_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB40', 'ENCODER OB40-6'))
        self.ob407_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB40', 'ENCODER OB40-7'))
        self.ob408_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB40', 'ENCODER OB40-8'))

        # OB53
        self.ob531_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB53', 'ENCODER OB53-1'))
        self.ob532_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB53', 'ENCODER OB53-2'))
        self.ob533_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB53', 'ENCODER OB53-3'))
        self.ob534_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB53', 'ENCODER OB53-4'))
        self.ob535_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB53', 'ENCODER OB53-5'))
        self.ob536_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB53', 'ENCODER OB53-6'))
        self.ob537_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB53', 'ENCODER OB53-7'))
        self.ob538_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB53', 'ENCODER OB53-8'))

        # OB86
        self.ob861_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB86', 'ENCODER OB86-1'))
        self.ob862_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB86', 'ENCODER OB86-2'))
        self.ob863_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB86', 'ENCODER OB86-3'))
        self.ob864_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB86', 'ENCODER OB86-4'))
        self.ob865_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB86', 'ENCODER OB86-5'))
        self.ob866_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB86', 'ENCODER OB86-6'))
        self.ob867_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB86', 'ENCODER OB86-7'))
        self.ob868_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB86', 'ENCODER OB86-8'))

        # OB89
        self.ob891_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB89', 'ENCODER OB89-1'))
        self.ob892_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB89', 'ENCODER OB89-2'))
        self.ob893_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB89', 'ENCODER OB89-3'))
        self.ob894_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB89', 'ENCODER OB89-4'))
        self.ob895_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB89', 'ENCODER OB89-5'))
        self.ob896_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB89', 'ENCODER OB89-6'))
        self.ob897_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB89', 'ENCODER OB89-7'))
        self.ob898_label.clicked.connect(lambda: API_functions.setOutStream('62272fe045475e21ba3621a7', 'OB89', 'ENCODER OB89-8'))

        # llistes streams id
        vmix1_id = []
        vmix1_id.append('6228accc45475e40ecb79abd')
        vmix1_id.append('6228ad41796db41a4006bb9d')
        vmix1_id.append('6228ad57796db41a4006bba2')
        vmix1_id.append('6228ad5a45475e40f1b79b4c')
        vmix1_id.append('6228ad85796db41a4006bbab')
        vmix1_id.append('6228ad8c796db41a4006bbaf')
        vmix1_id.append('6228ad8e45475e40ecb79ac3')
        vmix1_id.append('6228ad92796db41a4006bbb3')

        # llistes sortida

        NAS_id = []
        NAS_id.append(['Kiloview NAS', 'Kiloview NAS 1'])
        NAS_id.append(['Kiloview NAS', 'Kiloview NAS 2'])
        NAS_id.append(['Kiloview NAS', 'Kiloview NAS 3'])
        NAS_id.append(['Kiloview NAS', 'Kiloview NAS 4'])
        NAS_id.append(['Kiloview NAS', 'Kiloview NAS 5'])
        NAS_id.append(['Kiloview NAS', 'Kiloview NAS 6'])
        NAS_id.append(['Kiloview NAS', 'Kiloview NAS 7'])
        NAS_id.append(['Kiloview NAS', 'Kiloview NAS 8'])


        ob_23_id = []
        ob_23_id.append(['OB23', 'ENCODER OB23-1'])
        ob_23_id.append(['OB23', 'ENCODER OB23-2'])
        ob_23_id.append(['OB23', 'ENCODER OB23-3'])
        ob_23_id.append(['OB23', 'ENCODER OB23-4'])
        ob_23_id.append(['OB23', 'ENCODER OB23-5'])
        ob_23_id.append(['OB23', 'ENCODER OB23-6'])
        ob_23_id.append(['OB23', 'ENCODER OB23-7'])
        ob_23_id.append(['OB23', 'ENCODER OB23-8'])

        ob_39_id = []
        ob_39_id.append(['OB39', 'ENCODER OB39-1'])
        ob_39_id.append(['OB39', 'ENCODER OB39-2'])
        ob_39_id.append(['OB39', 'ENCODER OB39-3'])
        ob_39_id.append(['OB39', 'ENCODER OB39-4'])
        ob_39_id.append(['OB39', 'ENCODER OB39-5'])
        ob_39_id.append(['OB39', 'ENCODER OB39-6'])
        ob_39_id.append(['OB39', 'ENCODER OB39-7'])
        ob_39_id.append(['OB39', 'ENCODER OB39-8'])

        ob_40_id = []
        ob_40_id.append(['OB40', 'ENCODER OB40-1'])
        ob_40_id.append(['OB40', 'ENCODER OB40-2'])
        ob_40_id.append(['OB40', 'ENCODER OB40-3'])
        ob_40_id.append(['OB40', 'ENCODER OB40-4'])
        ob_40_id.append(['OB40', 'ENCODER OB40-5'])
        ob_40_id.append(['OB40', 'ENCODER OB40-6'])
        ob_40_id.append(['OB40', 'ENCODER OB40-7'])
        ob_40_id.append(['OB40', 'ENCODER OB40-8'])

        ob_53_id = []
        ob_53_id.append(['OB53', 'ENCODER OB53-1'])
        ob_53_id.append(['OB53', 'ENCODER OB53-2'])
        ob_53_id.append(['OB53', 'ENCODER OB53-3'])
        ob_53_id.append(['OB53', 'ENCODER OB53-4'])
        ob_53_id.append(['OB53', 'ENCODER OB53-5'])
        ob_53_id.append(['OB53', 'ENCODER OB53-6'])
        ob_53_id.append(['OB53', 'ENCODER OB53-7'])
        ob_53_id.append(['OB53', 'ENCODER OB53-8'])

        ob_86_id = []
        ob_86_id.append(['OB86', 'ENCODER OB86-1'])
        ob_86_id.append(['OB86', 'ENCODER OB86-2'])
        ob_86_id.append(['OB86', 'ENCODER OB86-3'])
        ob_86_id.append(['OB86', 'ENCODER OB86-4'])
        ob_86_id.append(['OB86', 'ENCODER OB86-5'])
        ob_86_id.append(['OB86', 'ENCODER OB86-6'])
        ob_86_id.append(['OB86', 'ENCODER OB86-7'])
        ob_86_id.append(['OB86', 'ENCODER OB86-8'])



        # Botons VMIX1
        # self.vmix3_ob23.clicked.connect(lambda: API_functions.setVmix(vmix1_id, NAS_id))
        # self.vmix3_ob39.clicked.connect(lambda: API_functions.setVmix(vmix1_id, ob_39_id))
        # self.vmix3_ob40.clicked.connect(lambda: API_functions.setVmix(vmix1_id, NAS_id))
        # self.vmix3_ob53.clicked.connect(lambda: API_functions.setVmix(vmix1_id, NAS_id))
        # self.vmix3_ob86.clicked.connect(lambda: API_functions.setVmix(vmix1_id, NAS_id))
        # self.vmix3_oo89.clicked.connect(lambda: API_functions.setVmix(vmix1_id, NAS_id))

    # ===================================
    # ========== MATRIU SRT =============
    # ===================================

        self.buttonGroup.setExclusive(True)
        self.buttonGroup_2.setExclusive(True)

        self.buttonGroup.buttonClicked.connect(self.changeStatus_source)
        self.buttonGroup_2.buttonClicked.connect(self.changeStatus_dest)

        #source status buttons
        self.port_set_source.setEnabled(False)
        self.play_source_status.setEnabled(False)
        self.play_source_status.clicked.connect(lambda: self.changeSourcePlayStatus())
        self.port_set_source.clicked.connect(lambda: API_functions.setPortSource(self.source_ident, self.port_input_source.text()))
        self.port_set_source.clicked.connect(lambda: self.port_input_source.clear())
        self.restart_source_status.clicked.connect(lambda: API_functions.restartSource(self.source_ident))

        #dest status buttons
        self.port_set.clicked.connect(lambda: API_functions.setPortDest(self.source_ident, self.port_input.text()))
        self.port_set.clicked.connect(lambda: self.port_input.clear())


        # take
        self.take.clicked.connect(lambda: API_functions.take())

    def changeSourcePlayStatus(self):
        API_functions.resumePausedSource(main_GUI.source_ident, main_GUI.source_status)
        if self.play_source_status.text() == 'PLAY':
            self.source_status1.setStyleSheet("background-color: lightgreen")
            self.play_source_status.setText('PAUSE')
            self.source_status = 'paused'
        else:
            self.source_status1.setStyleSheet("background-color: red")
            self.play_source_status.setText('PLAY')
            self.source_status = 'online'



    def changeStatus_source(self, button):
        # print(button.text())
        identificador = API_functions.source_assignation(button)
        main_GUI.source_ident = identificador
        stream_status, port, mode = API_functions.get_status_source(identificador)
        # print(stream, port, latency, paused, mode)
        main_GUI.source_status = stream_status
        #print(main_GUI.source_status)
        self.port_set_source.setEnabled(True)
        self.play_source_status.setEnabled(True)
        self.source_status1.setText(' {}'.format(button.text()))
        #cambiar color boto
        if stream_status == 'online':
            self.source_status1.setStyleSheet("background-color: lightgreen")
            self.play_source_status.setText('PAUSE')
        elif stream_status == 'pending':
            self.source_status1.setStyleSheet("background-color: yellow")
            self.play_source_status.setText('PENDING')
            self.play_source_status.setEnabled(False)
        else:
            self.source_status1.setStyleSheet("background-color: red")
            self.play_source_status.setText('PLAY')

        self.source_status2.setText(' STATUS: {}'.format(stream_status))
        self.source_status3.setText(' PORT: {}'.format(port))
        self.source_status4.setText(' MODE: {}'.format(mode))


    def changeStatus_dest(self, button):
        #print(button.text())
        identificador = API_functions.dest_assignation(button)
        stream, port, latency, paused, mode = API_functions.get_status_dest(identificador)
        # print(stream, port, latency, paused, mode)
        self.mtx_destination.setText(' {}'.format(button.text()))
        self.mtx_destination_2.setText(' SOURCE: {}'.format(stream))
        self.mtx_destination_3.setText(' PORT: {}'.format(port))
        self.mtx_destination_4.setText(' LATENCY: {}'.format(latency))
        self.mtx_destination_5.setText(' MODE: {}'.format(mode))
        # if not paused:
        #     self.stream_on.setEnabled(False)
        #     self.stream_off.setEnabled(True)
        # else:
        #     self.stream_on.setEnabled(True)
        #     self.stream_off.setEnabled(False)

    def showTime(self):
        self.actualize_dashboard()

    # finestra error
    def show_dialog(self, message):
        QMessageBox.critical(self, "ERROR", '{}'.format(message))

    # finestra confirmació
    def show_dialog_confirmation(self, message):
        button_confirm = QMessageBox.question(self, "ATENCIÓ", '{}'.format(message))
        return button_confirm

    def actualize_dashboard(self):

        bd_kv = sqlite3.connect('bd_kv.db')  # creem connexio
        cur = bd_kv.cursor()  # creem cursor
        # Ejecuta la consulta
        cur.execute('SELECT ob, name, bitrate, port FROM Kiloviews')
        # Extrae todos los datos
        data = cur.fetchall()
        bd_kv.close()

        # ================================
        # DUDE
        # ================================
        # actulitzem DUDE
        # NAS
        dude_labels = list()
        dude_labels.append(self.nas1_label)
        dude_labels.append(self.nas2_label)
        dude_labels.append(self.nas3_label)
        dude_labels.append(self.nas4_label)
        dude_labels.append(self.nas5_label)
        dude_labels.append(self.nas6_label)
        dude_labels.append(self.nas7_label)
        dude_labels.append(self.nas8_label)
        dude_labels.append(self.nas9_label)
        dude_labels.append(self.nas10_label)

        # OB23
        dude_labels.append(self.ob231_label)
        dude_labels.append(self.ob232_label)
        dude_labels.append(self.ob233_label)
        dude_labels.append(self.ob234_label)
        dude_labels.append(self.ob235_label)
        dude_labels.append(self.ob236_label)
        dude_labels.append(self.ob237_label)
        dude_labels.append(self.ob238_label)

        # OB39
        dude_labels.append(self.ob391_label)
        dude_labels.append(self.ob392_label)
        dude_labels.append(self.ob393_label)
        dude_labels.append(self.ob394_label)
        dude_labels.append(self.ob395_label)
        dude_labels.append(self.ob396_label)
        dude_labels.append(self.ob397_label)
        dude_labels.append(self.ob398_label)

        # OB40
        dude_labels.append(self.ob401_label)
        dude_labels.append(self.ob402_label)
        dude_labels.append(self.ob403_label)
        dude_labels.append(self.ob404_label)
        dude_labels.append(self.ob405_label)
        dude_labels.append(self.ob406_label)
        dude_labels.append(self.ob407_label)
        dude_labels.append(self.ob408_label)

        # OB53
        dude_labels.append(self.ob531_label)
        dude_labels.append(self.ob532_label)
        dude_labels.append(self.ob533_label)
        dude_labels.append(self.ob534_label)
        dude_labels.append(self.ob535_label)
        dude_labels.append(self.ob536_label)
        dude_labels.append(self.ob537_label)
        dude_labels.append(self.ob538_label)

        # OB86
        dude_labels.append(self.ob861_label)
        dude_labels.append(self.ob862_label)
        dude_labels.append(self.ob863_label)
        dude_labels.append(self.ob864_label)
        dude_labels.append(self.ob865_label)
        dude_labels.append(self.ob866_label)
        dude_labels.append(self.ob867_label)
        dude_labels.append(self.ob868_label)

        # OB89
        dude_labels.append(self.ob891_label)
        dude_labels.append(self.ob892_label)
        dude_labels.append(self.ob893_label)
        dude_labels.append(self.ob894_label)
        dude_labels.append(self.ob895_label)
        dude_labels.append(self.ob896_label)
        dude_labels.append(self.ob897_label)
        dude_labels.append(self.ob898_label)

        j = 0
        for dude_label in dude_labels:
            if data[j][2] == 0:
                dude_label.setStyleSheet("background-color: red")
                dude_label.setEnabled(False)
            else:
                dude_label.setStyleSheet("background-color: lightgreen")
                dude_label.setEnabled(True)
            j = j + 1

        # ================================
        # NAS
        # ================================

        # actualitzem bitrate
        self.nas1_bitrate.setText('{} Mbps'.format(data[0][2]))
        self.nas2_bitrate.setText('{} Mbps'.format(data[1][2]))
        self.nas3_bitrate.setText('{} Mbps'.format(data[2][2]))
        self.nas4_bitrate.setText('{} Mbps'.format(data[3][2]))
        self.nas5_bitrate.setText('{} Mbps'.format(data[4][2]))
        self.nas6_bitrate.setText('{} Mbps'.format(data[5][2]))
        self.nas7_bitrate.setText('{} Mbps'.format(data[6][2]))
        self.nas8_bitrate.setText('{} Mbps'.format(data[7][2]))
        self.nas9_bitrate.setText('{} Mbps'.format(data[8][2]))
        self.nas10_bitrate.setText('{} Mbps'.format(data[9][2]))

        # actualitzem port
        self.nas1_port.setText('{}'.format(data[0][3]))
        self.nas2_port.setText('{}'.format(data[1][3]))
        self.nas3_port.setText('{}'.format(data[2][3]))
        self.nas4_port.setText('{}'.format(data[3][3]))
        self.nas5_port.setText('{}'.format(data[4][3]))
        self.nas6_port.setText('{}'.format(data[5][3]))
        self.nas7_port.setText('{}'.format(data[6][3]))
        self.nas8_port.setText('{}'.format(data[7][3]))
        self.nas9_port.setText('{}'.format(data[8][3]))
        self.nas10_port.setText('{}'.format(data[9][3]))

        # ===============================
        # OB23
        # ===============================

        # actualitzem bitrate
        self.ob23_1_bitrate.setText('{} Mbps'.format(data[10][2]))
        self.ob23_2_bitrate.setText('{} Mbps'.format(data[11][2]))
        self.ob23_3_bitrate.setText('{} Mbps'.format(data[12][2]))
        self.ob23_4_bitrate.setText('{} Mbps'.format(data[13][2]))
        self.ob23_5_bitrate.setText('{} Mbps'.format(data[14][2]))
        self.ob23_6_bitrate.setText('{} Mbps'.format(data[15][2]))
        self.ob23_7_bitrate.setText('{} Mbps'.format(data[16][2]))
        self.ob23_8_bitrate.setText('{} Mbps'.format(data[17][2]))

        # actualitzem port
        self.ob23_1_port.setText('{}'.format(data[10][3]))
        self.ob23_2_port.setText('{}'.format(data[11][3]))
        self.ob23_3_port.setText('{}'.format(data[12][3]))
        self.ob23_4_port.setText('{}'.format(data[13][3]))
        self.ob23_5_port.setText('{}'.format(data[14][3]))
        self.ob23_6_port.setText('{}'.format(data[15][3]))
        self.ob23_7_port.setText('{}'.format(data[16][3]))
        self.ob23_8_port.setText('{}'.format(data[17][3]))

        # ================================
        # OB39
        # ================================

        # actualitzem bitrate
        self.ob39_1_bitrate.setText('{} Mbps'.format(data[18][2]))
        self.ob39_2_bitrate.setText('{} Mbps'.format(data[19][2]))
        self.ob39_3_bitrate.setText('{} Mbps'.format(data[20][2]))
        self.ob39_4_bitrate.setText('{} Mbps'.format(data[21][2]))
        self.ob39_5_bitrate.setText('{} Mbps'.format(data[22][2]))
        self.ob39_6_bitrate.setText('{} Mbps'.format(data[23][2]))
        self.ob39_7_bitrate.setText('{} Mbps'.format(data[24][2]))
        self.ob39_8_bitrate.setText('{} Mbps'.format(data[25][2]))

        # actualitzem port
        self.ob39_1_port.setText('{}'.format(data[18][3]))
        self.ob39_2_port.setText('{}'.format(data[19][3]))
        self.ob39_3_port.setText('{}'.format(data[20][3]))
        self.ob39_4_port.setText('{}'.format(data[21][3]))
        self.ob39_5_port.setText('{}'.format(data[22][3]))
        self.ob39_6_port.setText('{}'.format(data[23][3]))
        self.ob39_7_port.setText('{}'.format(data[24][3]))
        self.ob39_8_port.setText('{}'.format(data[25][3]))

        # ================================
        # OB40
        # ================================

        # actualitzem bitrate
        self.ob40_1_bitrate.setText('{} Mbps'.format(data[26][2]))
        self.ob40_2_bitrate.setText('{} Mbps'.format(data[27][2]))
        self.ob40_3_bitrate.setText('{} Mbps'.format(data[28][2]))
        self.ob40_4_bitrate.setText('{} Mbps'.format(data[29][2]))
        self.ob40_5_bitrate.setText('{} Mbps'.format(data[30][2]))
        self.ob40_6_bitrate.setText('{} Mbps'.format(data[31][2]))
        self.ob40_7_bitrate.setText('{} Mbps'.format(data[32][2]))
        self.ob40_8_bitrate.setText('{} Mbps'.format(data[33][2]))

        # actualitzem port
        self.ob40_1_port.setText('{}'.format(data[26][3]))
        self.ob40_2_port.setText('{}'.format(data[27][3]))
        self.ob40_3_port.setText('{}'.format(data[28][3]))
        self.ob40_4_port.setText('{}'.format(data[29][3]))
        self.ob40_5_port.setText('{}'.format(data[30][3]))
        self.ob40_6_port.setText('{}'.format(data[31][3]))
        self.ob40_7_port.setText('{}'.format(data[32][3]))
        self.ob40_8_port.setText('{}'.format(data[33][3]))

        # ===============================
        # OB53
        #================================

        # actualitzem bitrate
        self.ob53_1_bitrate.setText('{} Mbps'.format(data[34][2]))
        self.ob53_2_bitrate.setText('{} Mbps'.format(data[35][2]))
        self.ob53_3_bitrate.setText('{} Mbps'.format(data[36][2]))
        self.ob53_4_bitrate.setText('{} Mbps'.format(data[37][2]))
        self.ob53_5_bitrate.setText('{} Mbps'.format(data[38][2]))
        self.ob53_6_bitrate.setText('{} Mbps'.format(data[39][2]))
        self.ob53_7_bitrate.setText('{} Mbps'.format(data[40][2]))
        self.ob53_8_bitrate.setText('{} Mbps'.format(data[41][2]))

        # actualitzem port
        self.ob53_1_port.setText('{}'.format(data[34][3]))
        self.ob53_2_port.setText('{}'.format(data[35][3]))
        self.ob53_3_port.setText('{}'.format(data[36][3]))
        self.ob53_4_port.setText('{}'.format(data[37][3]))
        self.ob53_5_port.setText('{}'.format(data[38][3]))
        self.ob53_6_port.setText('{}'.format(data[39][3]))
        self.ob53_7_port.setText('{}'.format(data[40][3]))
        self.ob53_8_port.setText('{}'.format(data[41][3]))

        # ===============================
        # OB86
        #================================

        # actualitzem bitrate
        self.ob86_1_bitrate.setText('{} Mbps'.format(data[42][2]))
        self.ob86_2_bitrate.setText('{} Mbps'.format(data[43][2]))
        self.ob86_3_bitrate.setText('{} Mbps'.format(data[44][2]))
        self.ob86_4_bitrate.setText('{} Mbps'.format(data[45][2]))
        self.ob86_5_bitrate.setText('{} Mbps'.format(data[46][2]))
        self.ob86_6_bitrate.setText('{} Mbps'.format(data[47][2]))
        self.ob86_7_bitrate.setText('{} Mbps'.format(data[48][2]))
        self.ob86_8_bitrate.setText('{} Mbps'.format(data[49][2]))

        # actualitzem port
        self.ob86_1_port.setText('{}'.format(data[42][3]))
        self.ob86_2_port.setText('{}'.format(data[43][3]))
        self.ob86_3_port.setText('{}'.format(data[44][3]))
        self.ob86_4_port.setText('{}'.format(data[45][3]))
        self.ob86_5_port.setText('{}'.format(data[46][3]))
        self.ob86_6_port.setText('{}'.format(data[47][3]))
        self.ob86_7_port.setText('{}'.format(data[48][3]))
        self.ob86_8_port.setText('{}'.format(data[49][3]))

        # ===============================
        # OB89
        # ================================

        # actualitzem bitrate
        self.ob89_1_bitrate.setText('{} Mbps'.format(data[50][2]))
        self.ob89_2_bitrate.setText('{} Mbps'.format(data[51][2]))
        self.ob89_3_bitrate.setText('{} Mbps'.format(data[52][2]))
        self.ob89_4_bitrate.setText('{} Mbps'.format(data[53][2]))
        self.ob89_5_bitrate.setText('{} Mbps'.format(data[54][2]))
        self.ob89_6_bitrate.setText('{} Mbps'.format(data[55][2]))
        self.ob89_7_bitrate.setText('{} Mbps'.format(data[56][2]))
        self.ob89_8_bitrate.setText('{} Mbps'.format(data[57][2]))

        # actualitzem port
        self.ob89_1_port.setText('{}'.format(data[50][3]))
        self.ob89_2_port.setText('{}'.format(data[51][3]))
        self.ob89_3_port.setText('{}'.format(data[52][3]))
        self.ob89_4_port.setText('{}'.format(data[53][3]))
        self.ob89_5_port.setText('{}'.format(data[54][3]))
        self.ob89_6_port.setText('{}'.format(data[55][3]))
        self.ob89_7_port.setText('{}'.format(data[56][3]))
        self.ob89_8_port.setText('{}'.format(data[57][3]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = main_GUI()
    # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("")
    GUI.setWindowTitle('KILOVIEW DASHBOARD')
    GUI.show()
    sys.exit(app.exec_())
