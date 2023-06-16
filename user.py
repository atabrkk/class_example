

class User:
    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.password = password
        self.login_attempts = 0

    def login(self, username, password):
        if self.username == username and self.password == password:
            self.login_attempts += 1
            print(f"Sisteme Hoşgeldiniz Sayın {self.first_name} {self.last_name}")
        else:
            print("Lütfen Tekrar Deneyiniz")

    def read_login_attempts(self):
        print(f"Merhaba {self.first_name} {self.last_name} Toplam Giriş Sayınız: {self.login_attempts}")

    def login_attempts_reset(self):
        self.login_attempts = 0



user1 = User("ali", "veli", "aliveli", "aliveli@gmail.com", "veli123")
user1.login("aliveli", "veli123")
user1.read_login_attempts()
user1.login("aliveli", "veli123")
user1.read_login_attempts()

user2 = User("Eda", "karaca", "eda", "eda1@gmail.com", "eda1")
user2.login("eda", "eda1")
user2.read_login_attempts()
user2.login_attempts_reset()
user2.read_login_attempts()
