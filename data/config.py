import configparser

config = configparser.ConfigParser()

config.read('./config.ini', encoding='utf-8')

token = config['CONFIG']['token']