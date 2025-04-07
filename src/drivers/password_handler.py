import bcrypt

class PasswordHandler:
    def encrypt_password(self, password:str) -> str:
        salt = bcrypt.gensalt() 
        # valor aleatório adicionado à senha antes de fazer o hash. Isso garante
        # que senhas iguais resultem em hashes diferentes, melhorando a segurança.
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        # faz o hash com o salt
        return hashed_password #a idea é não ser legível
        #checagem das senhas encriptadas
    
    def check_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)