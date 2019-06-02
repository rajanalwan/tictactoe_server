import json
import falcon
import sys

sys.path.append('./utils')
from minimax import minimax


class Minimax(object):
    def on_get(self, req, resp):
        boardString = req.params['board']
        player = int(req.params['player'])

        board = list(map(int, boardString.split(', ')))

        move = minimax(board, player)

        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps(move)
