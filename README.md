Landing Page para SantiClinic
Stack: Flask, python.Python 3.12.3 HTML, CSS, Bootstrap4.0
Documentação:
Antes de tudo o computador tem que ter o Python 3.12.3 instalado, se nao for o caso, favor instala porque sem o interpretador a app nao ira funcionar. Logo a seguir é favor seguir os passos
1.Clonar o repositorio do GitHub usando o comando "git clone https://github.com/SPAWNKID19XX/SC.git"
2.Junto com as pastas static, templates criar o envirment usando o comando "python -m venv venv"
3.Activar o envirment na linha dos comandos "source venv/bin/activate"
4.Instalar as dependencias de ficheiro requirements.txt usando o comando "pip install -r requirments.txt" 5. Iniciar o servidor "python app.py"
6.Abriri a Pagina web no browser da maquina local "http://127.0.0.1:5000/" 7. Para a parte logica funcionar correctamnete devem criar o ficheiro my_secret_data.py e introduzir ai o texto que vai a seguir com as suar credenciais.

MAIL_USERNAME = 'exemple@gmail.com'
MAIL_PASSWORD = 'xxx xxx xxx xxx'
MAIL_SENDER = 'exemple@gmail.com'
MAIL_SEND_TO = 'exemple@gmail.com'
RECOVERY_CODE = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
AUTH_TOKEN= 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCOUNT_SID = 'XXXXXXXXXXXXXXXXXXXXXX'

Descrieçao de App
A pagina tem algumas formas repetetivas. em qualquer 1 delas o utilizador pode introduzir os dados e o mesmo ira resseber uma msg comprovativa de inscrieçao via WhatsApp, e tambem a SantiClinic ira receber os dados de utilisador via email.
para tal precisamos ter acesso ao email e pass especifica que dependendo de cliente de emails pode nos oferecer.

#TODO
1 . Imagens de apresentaçao dos videos,(cover image pouster=)
