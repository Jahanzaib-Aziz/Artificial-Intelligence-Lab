# MINIMAX ALGORITHM

class GameState:
    def __init__(self, board, is_max_turn=True):
        self.board = board  # list of values
        self.is_max_turn = is_max_turn

    def is_terminal(self):
        return len(self.board) == 1

    def evaluate(self):
        # Return final value
        return self.board[0]

    def generate_children(self):
        # Generate next possible states
        children = []

        for i in range(len(self.board) - 1):
            new_board = self.board[:i] + [max(self.board[i], self.board[i+1])] + self.board[i+2:]
            children.append(GameState(new_board, not self.is_max_turn))

            new_board = self.board[:i] + [min(self.board[i], self.board[i+1])] + self.board[i+2:]
            children.append(GameState(new_board, not self.is_max_turn))

        return children


class MinimaxSolver:
    def __init__(self):
        self.node_count = 0  

    def minimax(self, state):
        self.node_count += 1

        # Base case
        if state.is_terminal():
            return state.evaluate()

        # Recursive case
        if state.is_max_turn:
            best_value = float('-inf')
            for child in state.generate_children():
                value = self.minimax(child)
                best_value = max(best_value, value)
            return best_value
        else:
            best_value = float('inf')
            for child in state.generate_children():
                value = self.minimax(child)
                best_value = min(best_value, value)
            return best_value


# DRIVER CODE


if __name__ == "__main__":
    # Initial values 
    initial_values = [3, 5, 2, 9]

    
    game = GameState(initial_values, is_max_turn=True)

    # Create solver
    solver = MinimaxSolver()

    result = solver.minimax(game)

    print("Optimal Value:", result)
    print("Nodes Explored:", solver.node_count)