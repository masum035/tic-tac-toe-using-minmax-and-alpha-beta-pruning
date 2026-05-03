class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # First move — pick center, no need to run minimax
            return 4
        else:
            result = self.alphabeta(
                state=game,
                depth=0,
                alpha=float('-inf'),
                beta=float('inf'),
                is_maximizing=True
            )
            return result['position']

    def alphabeta(self, state, depth, alpha, beta, is_maximizing):
        other_letter = 'O' if self.letter == 'X' else 'X'

        # ── Terminal state checks ──────────────────────────────────
        if state.current_winner == self.letter:
            return {'position': None, 'score': 10 - depth}   # faster win = higher score

        if state.current_winner == other_letter:
            return {'position': None, 'score': depth - 10}   # slower loss = less negative

        if not state.empty_squares():
            return {'position': None, 'score': 0}            # tie

        # ── Maximizing (computer's turn) ───────────────────────────
        if is_maximizing:
            best = {'position': None, 'score': float('-inf')}

            for move in state.available_moves():
                # Make the move
                state.make_move(move, self.letter)
                result = self.alphabeta(state, depth + 1, alpha, beta, False)

                # Undo the move
                state.board[move] = ' '
                state.current_winner = None
                result['position'] = move

                # Update best
                if result['score'] > best['score']:
                    best = result

                # Alpha-Beta logic
                alpha = max(alpha, best['score'])
                if beta <= alpha:
                    break   # ✂️ Beta cutoff — minimizer won't allow this path

            return best

        # ── Minimizing (human's turn) ──────────────────────────────
        else:
            best = {'position': None, 'score': float('inf')}

            for move in state.available_moves():
                # Make the move
                state.make_move(move, other_letter)
                result = self.alphabeta(state, depth + 1, alpha, beta, True)

                # Undo the move
                state.board[move] = ' '
                state.current_winner = None
                result['position'] = move

                # Update best
                if result['score'] < best['score']:
                    best = result

                # Alpha-Beta logic
                beta = min(beta, best['score'])
                if beta <= alpha:
                    break   # ✂️ Alpha cutoff — maximizer won't allow this path

            return best