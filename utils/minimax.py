blank = 0
human = 1
computer = 2


def minimax(board, player):
    if win(board, human):
        return {'index': -1, 'score': -1}
    elif win(board, computer):
        return {'index': -1, 'score': 1}
    elif len(list(filter(lambda x: x == 0, board))) == 0:
        return {'index': -1, 'score': 0}

    moves = []

    for i in range(9):
        if board[i] == blank:
            board[i] = player

            currentMove = minimax(board, human if player ==
                                  computer else computer)

            moves.append({'index': i, 'score': currentMove['score']})

            board[i] = blank

    bestMove = max(range(len(moves)), key=lambda i: moves[i]['score']) if player == computer else min(
        range(len(moves)), key=lambda i: moves[i]['score'])

    return moves[bestMove]


def win(board, player):
    if board[0] == player and board[1] == player and board[2] == player or \
            board[3] == player and board[4] == player and board[5] == player or \
            board[6] == player and board[7] == player and board[8] == player or \
            board[0] == player and board[3] == player and board[6] == player or \
            board[1] == player and board[4] == player and board[7] == player or \
            board[2] == player and board[5] == player and board[8] == player or \
            board[0] == player and board[4] == player and board[8] == player or \
            board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False
