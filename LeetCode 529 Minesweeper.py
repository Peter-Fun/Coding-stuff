class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        r, c = click
        visited = set()
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            q = []
            q.append((r, c))
            while q:
                y, x = q.pop(0)
                if (y, x) in visited:
                    continue
                visited.add((y, x))
                num_of_mines = 0
                tmp = []
                for _y, _x in directions:
                    if 0 <= _y + y < len(board) and 0 <= _x + x < len(board[0]):
                        if board[_y + y][_x + x] == "M":
                            num_of_mines += 1
                        elif board[_y + y][_x + x] == "E":
                            tmp.append((_y + y, _x + x))
                if num_of_mines > 0:
                    board[y][x] = str(num_of_mines)
                else:
                    for _r, _c in tmp:
                        q.append((_r, _c))
                    board[y][x] = "B"
        return board
