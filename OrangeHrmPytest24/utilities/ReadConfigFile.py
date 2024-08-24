
import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\Config.ini")


class ReadConfig_Class:
    @staticmethod
    def getUsername():
        Username = config.get('login data','username')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('login data','password')
        return Password






