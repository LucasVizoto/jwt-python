from .password_handler import PasswordHandler

def test_encrypt():
    # quero verificar se a biblioteca vai se comportar da forma como deveria
    minha_senha = '123Lucas'
    password_handler = PasswordHandler()

    hashed_password = password_handler.encrypt_password(minha_senha)
    

    # todos começam com $2b$12$
    # onde $2b é o algorito de encriptação 
    # e o $12$ é o nível de complexidade para caso brute force

    password_checked = password_handler.check_password(minha_senha, hashed_password)
    assert password_checked #teste unitário para verificar se está batendo