import sys

AI = 'X'
HUMAN = 'O'
EMPTY = ' '

def print_board(board):
    print("\n")
    print(f" {board} | {board} | {board} ")
    print("---|---|---")
    print(f" {board} | {board} | {board} ")
    print("---|---|---")
    print(f" {board} | {board} | {board} ")
    print("\n")

def is_moves_left(board):
    return EMPTY in board

def evaluate(board):
    win_states = [, [3, 4, 5], [6, 7, 8],
, [1, 4, 7], [2, 5, 8],
, [2, 4, 6]
    ]
    for condition in win_states:
        if board[condition[0]] == board[condition[1]] == board[condition[2]]:
            if board[condition[0]] == AI: return 10
            elif board[condition[0]] == HUMAN: return -10
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)
    if score == 10: return score - depth
    if score == -10: return score + depth
    if not is_moves_left(board): return 0

    if is_max:
        best = -sys.maxsize
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                best = max(best, minimax(board, depth + 1, False))
                board[i] = EMPTY
        return best
    else:
        best = sys.maxsize
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                best = min(best, minimax(board, depth + 1, True))
                board[i] = EMPTY
        return best

def find_best_move(board):
    best_val = -sys.maxsize
    best_move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            move_val = minimax(board, 0, False)
            board[i] = EMPTY
            if move_val > best_val:
                best_move = i
                best_val = move_val
    return best_move

def play_game():
    board = [EMPTY] * 9
    print("=== Unbeatable Tic-Tac-Toe AI ===")
    print("AI is calculating its opening move...")
    board[find_best_move(board)] = AI
    print_board(board)

    while is_moves_left(board) and evaluate(board) == 0:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != EMPTY:
                print("⚠️ Invalid move! Try again.")
                continue
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue
            
        board[move] = HUMAN
        print_board(board)
        
        if not is_moves_left(board) or evaluate(board) != 0:
            break

        print("AI is thinking...")
        board[find_best_move(board)] = AI
        print_board(board)

    final_score = evaluate(board)
    if final_score == 10: print("🤖 Game Over! The AI wins!")
    elif final_score == -10: print("🎉 You won!")
    else: print("🤝 It's a draw!")

if __name__ == "__main__":
    play_game()
