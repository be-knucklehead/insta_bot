from getpass import getpass


class AccInfo():

    def __init__(self):
        pass

    @staticmethod
    def username():
        username = input("Enter username of instagram account: ")
        return username

    @staticmethod
    def password(username):
        password = getpass(f"Enter password of {username} account: ")
        return password
