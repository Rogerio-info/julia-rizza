from app import app

#importe do módulo(pasta) app a variável app do arquivo __ini__.py


@app.route('/')
def index():
    return 'Configurando as pastas no projeto.'