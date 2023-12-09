import numpy as np
import random


class Scheme:
    N = 3
    # matrix = np.zeros((3, 3))
    board = np.zeros(N * N)

    def is_completed(self):
        return np.all(self.board != 0)

    def set(self, move_array):
        # self.matrix[int(move_array[0])][int(move_array[1])] = int(move_array[2])
        self.board[int(move_array[0])] = int(move_array[1])

    def add_random(self, symbol):
        free_positions = []

        for i in range(self.N * self.N):
            if self.board[i] == 0:
                free_positions.append(i)

        position = free_positions[random.randint(0, len(free_positions) - 1)]
        self.board[position] = symbol

    def print(self):
        for i in range(self.N * self.N):
            symbol = '-' if self.board[i] == 0 else ('x' if self.board[i] == 1 else 'o')
            print(symbol, end='')
            if ((i + 1) % self.N) == 0:
                print()

    def get_winner(self):
        # checks all the rows
        for i in range(self.N):
            winner = self._get_line_winner(self.board[(i * self.N):((i + 1) * self.N)])
            if winner != 0:
                return winner

        # checks all the columns
        for i in range(self.N):
            winner = self._get_line_winner(self.board[i:: self.N])
            if winner != 0:
                return winner

        # checks the principal diagonal
        winner = self._get_line_winner(self.board[:: self.N + 1])
        if winner != 0:
            return winner

        # checks the anti-diagonal
        winner = self._get_line_winner(self.board[self.N - 1: self.N ** 2 - 1: self.N - 1])
        if winner != 0:
            return winner

        return 0

    @staticmethod
    def _get_line_winner(line):
        if np.all(line == 1):
            return 1
        elif np.all(line == 2):
            return 2
        else:
            return 0
