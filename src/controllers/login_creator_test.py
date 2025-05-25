from src.drivers.password_handler import PasswordHandler
from .login_creator import LoginCreator
import pytest

username = "MyUsername"
password = "MyPassword"
hashed_password = PasswordHandler().encrypt_password(password)

class MockUserRepository:
    def get_user_by_username(self, username: str) -> tuple:
        return (10, username, hashed_password)

def test_create():
    login_creator = LoginCreator(MockUserRepository())
    response = login_creator.create(username, password)

    print()
    print(response)

    assert response["access"] == True
    assert response["username"] == username
    assert response["auth"] is not None


def test_create_with_wrong_password():
    login_creator = LoginCreator(MockUserRepository())

    with pytest.raises(Exception): #com isso daqui eu estou falando para o pytest que eu quero uma excessão aqui
        # logo, caso rodado o teste ele irá apontar que passou
        response = login_creator.create(username, "algumaSenha")