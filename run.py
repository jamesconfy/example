from example import create_app
from utils import PrefixMiddleware

app = create_app()

if __name__ == '__main__':    
    app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/v1')
    app.run(host="0.0.0.0", port=80)