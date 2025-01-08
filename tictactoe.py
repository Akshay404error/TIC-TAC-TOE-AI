import random

# Constants
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '


def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


def is_winner(board, player):
    # Winning combinations
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for positions in winning_positions:
        if all(board[pos] == player for pos in positions):
            return True
    return False


def is_draw(board):
    return EMPTY not in board


def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, PLAYER_X):
        return -10 + depth
    if is_winner(board, PLAYER_O):
        return 10 - depth
    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval


def best_move(board):
    best_val = float('-inf')
    best_move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_O
            move_val = minimax(board, 0, False, float('-inf'), float('inf'))
            board[i] = EMPTY
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move


def play_game():
    board = [EMPTY] * 9
    current_player = PLAYER_X
    while True:
        print_board(board)

        if current_player == PLAYER_X:
            move = int(input("Player X, choose your move (0-8): "))
            if board[move] != EMPTY:
                print("Invalid move! Try again.")
                continue
            board[move] = PLAYER_X
        else:
            print("AI is making a move...")
            move = best_move(board)
            board[move] = PLAYER_O

        if is_winner(board, PLAYER_X):
            print_board(board)
            print("Player X wins!")
            break
        elif is_winner(board, PLAYER_O):
            print_board(board)
            print("AI (Player O) wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O


if __name__ == "__main__":
    play_game()
