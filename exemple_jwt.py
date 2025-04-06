from flask import Flask, jsonify, request
import jwt
from datetime import datetime, timedelta, timezone
app = Flask(__name__)

@app.route('/', methods=['POST'])
def login():
    token = jwt.encode(
        payload={
            'exp':datetime.now(timezone.utc)+timedelta(minutes=1),
            'email': 'lucasvizoto364@gmail.com'
            # aqui eu defini o tempo de expiração do token, no caso 
            # 1 minuto depois do now da timezone utc (global)
        }, #passo as informações que eu quiser no payload pois elas serão encriptadas no token
        key= "minhaChave",
        algorithm="HS256" #elemento de encode, algoritmo que vou encriptar 
    )

    return jsonify({"token": token }), 200 #aqui já está retornando o token JWT criado


@app.route('/secret', methods=['POST'])
def secret():
    raw_token = request.headers.get("Authorization")
    token = raw_token.split()[1] #aqui eu pego o token do header Authorization
    #reconhecimento do token
    try:
        token_information = jwt.decode(token, key="minhaChave", algorithms="HS256")
        print(token_information)
        print(token_information['email']) # acessando só o campo email 
    except Exception as exception: # se a tela expirou cai aqui, e se tiver errado tbm
        return jsonify({"error": str(exception)}), 400
    
    return jsonify({"message": "Segredo" }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
