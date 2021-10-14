import sqlite3

class Baza:
    def __init__(self, baza_nomi= 'main.db'):
        self.base_name = baza_nomi

    @property
    def bazani_boglash(self):
        return sqlite3.connect(self.base_name)
    def umumiy_amallar(self, sql:str,parameters:
    tuple= None, fetchone= False, fetchall=False,commit = False):
        if not parameters:
            parameters = ()
        bazani_boglash = self.bazani_boglash
        bazani_boglash.set_trace_callback(logger)
