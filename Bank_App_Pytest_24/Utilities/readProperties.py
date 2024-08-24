
import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfigFile:
    @staticmethod
    def GetUsername():
        username = config.get('login Data','username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('login Data','password')
        return password
