import sae
from web import app

application = sae.create_wsgi_app(app)
