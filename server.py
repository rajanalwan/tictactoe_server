import falcon

# Services
from services.minimax import Minimax

# Middleware
from middleware.handle_cors import HandleCORS

app = falcon.API(middleware=[HandleCORS()])

minimax = Minimax()

app.add_route('/minimax', minimax)