#to read common data in the config.ini file
import configparser

config = configparser.RawConfigParser()
config.read('C:/myProject/pythonProject/Configurations/config.ini')

class ReadConfig:

    @staticmethod
    def applicationURL():
        url = config.get('commonVars','baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('commonVars','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('commonVars','password')
        return password