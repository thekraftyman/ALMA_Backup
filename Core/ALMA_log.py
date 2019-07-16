# displays.py
# By: Adam Kraft
# contains all of the outlines for the displays of the ALMA BACKUP
from Core.log import Log
from datetime import datetime

class ALMA_log(Log):
    '''alma log class based on the log class'''
    ct = datetime.now().strftime('%m_%d_%y')
    path = 'ALMA_Log_on_{}.txt'.format(ct)
    header = 'ALMA BACKUP'

    def __init__(self):
        super().__init__('ALMA_Log_on_{}.txt'.format(datetime.now().strftime('%m_%d_%y')),'ALMA BACKUP')

    def current_time(self):
        '''returns current time in hour:minute:second AM/PM form'''
        return datetime.now().strftime('%I:%M:%S%p')

    def check_in(self, barcode_list, task = 'Check-in'):
        '''runs a loop for the check-in process
        post: returns the barcode for an item with a time stamp'''

        string_to_write = task +':\n'
        barcodes = barcode_list
        for barcode in barcodes:
            add_string = 'Item: {} at {}\n'.format(barcode, self.current_time())
            string_to_write += add_string
        self.write(string_to_write)

    def check_out(self, ID, Barcode_list):
        '''runs a loop for the check-out process
        post: returns a student's ID number and barcode number of any items with
        a time stamp'''

        user = ID
        string_to_write = 'Check-out:\nID Number: {}\n'.format(ID)
        barcodes = Barcode_list
        for barcode in barcodes:
            add_string = 'Item: ' + barcode + ' at ' + self.current_time() + '\n'
            string_to_write += add_string
        self.write(string_to_write)
