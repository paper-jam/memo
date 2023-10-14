# ------------ various test for chapter 5

import configparser

config = configparser.ConfigParser()

print(type(config))

print(config.read("config.ini"))
print("*" * 20)
print(type(config["mariadb"]))

print("Sections:", config.sections(), "\n")

print("mariadb section:")
print("Host:", config["mariadb"]["host"])
print("Database:", config["mariadb"]["name"])
print("Username:", config["mariadb"]["user"])
print("Password:", config["mariadb"]["password"], "\n")

print("redis section:")
print("Host:", config["redis"]["host"])
print("Port:", int(config["redis"]["port"]))
print("Database number:", int(config["redis"]["db"]))
