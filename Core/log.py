# log.py
# BY: Adam Kraft
# Class for a log
from datetime import datetime
import os.path

# Define Global Variables -----------------------------------------------------
divider = '-----------------------------------------------------------'
# -----------------------------------------------------------------------------


class Log:
    '''Log class that can be written to and saves itself'''

    # Define Global Variables -------------------------------------------------
    divider = '-----------------------------------------------------------'
    # -------------------------------------------------------------------------

    def __init__(self,path,header):
        '''attempts to open a log and creates one if none exists'''
        if os.path.exists(path):
            self.lg = open(path, mode='a')
        else:
            self.lg = open(path, mode='w', encoding='utf-8')
            self.lg.write(header+'\n')
            self.lg.write(divider+'\n')
        self.path = path
        self.header = header
        self.status = 'OFF'

    def _current_time(self):
        '''returns current time in hour:minute form'''
        return datetime.now().strftime('%H:%M')

    def _day_stamp(self):
        '''returns current day in M/D/Y form'''
        return datetime.now().strftime('%m/%d/%y')

    def _update(self):
        '''saves the document and re-opens it in append mode'''
        self.lg.close()
        self.lg = open(self.path, mode='a')

    def write(self, string):
        '''writes a string to the log and updates it'''
        self.lg.write(string+divider+'\n')
        self._update()

    def iter_sections(self):
        with open(self.path, 'r') as infile:
            data = infile.read().split(divider)

    def __iter__(self):
        for section in self.iter_sections():
            yield section

    def __repr__(self):
        return 'Log("{}","{}")'.format(self.path,self.header)

    def __str__(self):
        print('Log object with header: {}'.format(self.header))

    def __add__(self,other):
        self.lg.write(other)
