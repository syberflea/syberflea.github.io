def check_win(board):
    lines = board.split()
    for line in lines:
        if "XXXXX" in line:
            return "First"
        elif "OOOOO" in line:
            return "Second"

    nrows = len(lines)
    ncols = len(lines[0])

    for i in range(ncols):
        col = "".join(row[i] for row in lines)
        if "XXXXX" in col:
            return "First"
        elif "OOOOO" in col:
            return "Second"

    diag1 = "".join(lines[i][i] for i in range(nrows))
    diag2 = "".join(lines[i][nrows - 1 - i] for i in range(nrows))

    if "XXXXX" in diag1 or "XXXXX" in diag2:
        return "First"
    elif "OOOOO" in diag1 or "OOOOO" in diag2:
        return "Second"

    return "Draw"



n = int(input())
moves = [input() for _ in range(n)]
board = ""
for i in range(n):
    r, c = map(int, moves[i].split())
    x = r + c
    y = r - c
    if (i % 2) == 0:
        board += "X" + str(x) + "|" + str(y) + " "
    else:
        board += "O" + str(x) + "|" + str(y) + " "

result = check_win(board)
print(result)