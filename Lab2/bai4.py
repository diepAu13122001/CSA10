class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def welcome(self):
        print("Welcome", self.username)

    def checkPassword(self, passInput):
        return passInput == self.password

from datetime import datetime  
class SubscribedUser(User):
    def __init__(self, username, password, expiredDate) -> None:
        super().__init__(username, password)
        self.expiredDate = expiredDate

    def isExpired(self):
        return datetime.now() > self.expiredDate
    
# driver code
user1 = SubscribedUser('Diepau', '123', datetime(2024, 5, 26))
user1.welcome()
print(user1.checkPassword('1234'))
print(user1.isExpired())
