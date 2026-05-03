
def ask_difficulty():
    while True:
        choice = input("\nSelect difficulty: (1) Normal  (2) Hard  → ").strip()
        if choice == '1':
            return 'normal'
        elif choice == '2':
            return 'hard'
        else:
            print("Invalid choice. Please enter 1 or 2.")

def main():
    print("=" * 30)
    print("   Welcome to Tic-Tac-Toe!")
    print("=" * 30)

    score = {'You': 0, 'Computer': 0, 'Ties': 0}

    while True:
        game = TicTacToe()
        first = ask_who_goes_first()
        difficulty = ask_difficulty()

        if first == 'human':
            human_letter = 'X'
            x_player = HumanPlayer('X')
            o_player = SmartComputerPlayer('O') if difficulty == 'hard' else RandomComputerPlayer('O')
            print(f"\nYou go first as X! [{difficulty.upper()} mode]")
        else:
            human_letter = 'O'
            x_player = SmartComputerPlayer('X') if difficulty == 'hard' else RandomComputerPlayer('X')
            o_player = HumanPlayer('O')
            print(f"\nComputer goes first as X. You are O! [{difficulty.upper()} mode]")

        winner_letter = play(game, x_player, o_player, human_letter, print_game=True)

        if winner_letter is None:
            score['Ties'] += 1
        elif winner_letter != human_letter:
            score['Computer'] += 1
        else:
            score['You'] += 1

        print("\n--- Scoreboard ---")
        print(f"  You:      {score['You']}")
        print(f"  Computer: {score['Computer']}")
        print(f"  Ties:     {score['Ties']}")
        print("------------------")

        if not ask_play_again():
            print("\nThanks for playing!")
            break


if __name__ == '__main__':
    main()