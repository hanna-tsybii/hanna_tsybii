import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def is_winner(board, player):
    # Перевіряємо рядки, стовпці та діагоналі для переможних комбінацій.
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Перевірка рядків.
            return True
        if all(board[j][i] == player for j in range(3)):  # Перевірка стовпців.
            return True
    if all(board[i][i] == player for i in range(3)):  # Перевірка головної діагоналі.
        return True
    if all(board[i][2-i] == player for i in range(3)):  # Перевірка побічної діагоналі.
        return True
    return False

def is_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_free_cells(board):
    free_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                free_cells.append((i, j))
    return free_cells

def computer_move(board, computer, player):
    free_cells = get_free_cells(board)
    for cell in free_cells:
        x, y = cell
        # Спробуємо робити хід і перевірити, чи комп'ютер перемагає.
        board[x][y] = computer
        if is_winner(board, computer):
            return

        # Спробуємо заблокувати перемогу гравця.
        board[x][y] = player
        if is_winner(board, player):
            board[x][y] = computer
            return

        # Відміняємо тестовий хід.
        board[x][y] = ' '

    # Якщо немає можливості перемогти або заблокувати гравця, робимо випадковий хід.
    x, y = random.choice(free_cells)
    board[x][y] = computer

def human_move(board, player):
    while True:
        try:
            x, y = map(int, input("Введіть координати (розділені пробілом): ").split())
            if 0 <= x < 3 and 0 <= y < 3 and board[x][y] == ' ':
                board[x][y] = player
                break
            else:
                print("Некоректний хід. Спробуйте знову.")
        except ValueError:
            print("Некоректний ввід. Спробуйте знову.")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    computer = random.choice(players)
    players.remove(computer)
    player = players[0]

    while True:
        print_board(board)
        if is_winner(board, computer):
            print("Комп'ютер переміг!")
            break
        if is_winner(board, player):
            print("Ви перемогли!")
            break
        if is_draw(board):
            print("Гра закінчилась внічию!")
            break

        if computer == 'X':
            computer_move(board, computer, player)
        else:
            human_move(board, player)

        # Передаємо чергу ходу другому гравцю.
        computer, player = player, computer

if __name__ == "__main__":
    main()
