from dlgo.gotypes import Point

def is_point_an_eye(board, point, color):
    if board.get(point) is not None:
        