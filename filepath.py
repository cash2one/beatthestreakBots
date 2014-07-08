from config import ROOT

class Filepath(object):

    @classmethod
    def get_root(self):
        """
        Returns the path of btsReal
        """
        return ROOT

    @classmethod
    def get_accounts_file(self):
        """
        Returns the path of the excel file containing account info
        for emails and beatthestreak accounts on mlb.com
        """
        return self.get_root() + '/btsAccounts.xlsx'

    @classmethod
    def get_test_file(self):
        """
        Returns the path of the excel file containing account info
        for test accounts on mlb.com
        """
        return self.get_root() + "/nonProductionBtsAccounts.xlsx"

    @classmethod
    def get_log_file(self, test=False):
        """
        Returns the path of the .txt file containing logs
        """
        if test:
            return self.get_root() + '/tests/logs.txt'
        else:
            return self.get_root() + '/logs.txt'