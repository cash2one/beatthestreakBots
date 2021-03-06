import os

from config import ROOT
from datetime import datetime

class Filepath(object):

    @classmethod
    def get_root(self):
        """
        Returns the path of btsReal
        """
        return ROOT

    @classmethod
    def get_accounts_dir(self):
        return self.get_root() + '/accountFiles'

    @classmethod
    def get_accounts_file(self):
        """
        Returns the path of the excel file containing account info
        for emails and beatthestreak accounts on mlb.com
        """
        return self.get_accounts_dir() + '/btsAccounts.xlsx'

    @classmethod
    def get_test_accounts_file(self):
        """
        Returns the path of the excel file containing account info
        for test accounts on mlb.com
        """
        return self.get_accounts_dir()  + "/nonProductionBtsAccounts.xlsx"

    @classmethod
    def get_log_file(self, activeDate, sN, vMN, test=False):
        """
        Returns the path of the .txt file containing logs
        """
        date = activeDate.strftime('%m-%d-%Y')
        # today = datetime.today().date().strftime('%m-%d-%Y')

        if test:
            rootFolder = self.get_root() + '/tests/logs/sN{}vMN{}/',format(sN,vMN)
        else:
            rootFolder = self.get_root() + '/logs/sN{}vMN{}/'.format(sN, vMN)

        if not os.path.isdir(rootFolder):
            os.mkdir(rootFolder)

        return rootFolder + date + '.txt'

    @classmethod
    def get_minion_account_file(self, sN=None, vMN=None):
        """
        int int -> None
           sN: int | strategy number
           vMN: int | virtual machine number
        Returns the path of the .xlsx file that holds account info
        for accounts operating under strategy number sN and controlled
        by virtual machine vMN
        """
        ## Type checking
        assert type(sN) == int
        assert type(sN) == int

        ## If the dir doesn't exist, create it
        dirpath = self.get_accounts_dir() + '/minionAccountFiles'
        if not os.path.isdir(dirpath):
            os.mkdir(dirpath)

        ## Return the formmatted file name for this specific sN and vMN
        return dirpath + '/sN={},vMN={}.xlsx'.format(sN, vMN)
