from queue import PriorityQueue
from resource import getrusage, RUSAGE_SELF
from time import time


class Queue:
    def __init__(self, items=[]):
        self.items = items

    def __str__(self):
        return ("[" + ", ".join([str(x) for x in self.items]) + "]")

    def __len__(self):
        return len(self.items)

    def put(self, x):
        self.items.append(x)

    def get(self):
        if self.items:
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


class Stack:
    def __init__(self, items=[]):
        self.items = items

    def __str__(self):
        return ("[" + ", ".join([str(x) for x in self.items]) + "]")

    def __len__(self):
        return len(self.items)

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.items:
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


class Search:
    def __init__(self):
        self.items = []
        self.goal = tuple(range(0, 9))
        self.visited = set()
        self.found = False
        self.path_to_goal = []
        self.nodes_expanded = None
        self.max_fringe_size = None
        self.search_depth = None
        self.max_search_depth = None
        self.running_time = None

    @staticmethod
    def print_board(board):
        for i in range(0, 9, 3):
            print(' '.join([str(x) for x in board[i:i + 3]]))

    @staticmethod
    def move_up(board, start):
        if 0 <= start <= 2:
            return None
        board[start], board[start - 3] = board[start - 3], board[start]
        return tuple(board)

    @staticmethod
    def move_down(board, start):
        if 6 <= start <= 8:
            return None
        board[start], board[start + 3] = board[start + 3], board[start]
        return tuple(board)

    @staticmethod
    def move_left(board, start):
        if start in (0, 3, 6):
            return None
        board[start], board[start - 1] = board[start - 1], board[start]
        return tuple(board)

    @staticmethod
    def move_right(board, start):
        if start in (2, 5, 8):
            return None
        board[start], board[start + 1] = board[start + 1], board[start]
        return tuple(board)

    def make_viable_moves(self, board):
        # move in UDLR order -> up, down, left and right
        moves = []
        start = board.index(0)
        for move_func in [self.move_up, self.move_down, self.move_left, self.move_right]:
            move = move_func(list(board), start)
            if move:
                moves.append(move)
        return moves

    def print_statistics(self):
        # the sequence of moves taken to reach the goal
        print('path_to_goal:', self.path_to_goal)
        # the number of moves taken to reach the goal
        print('cost_of_path:', len(self.path_to_goal))
        # the number of nodes that have been expanded
        print('nodes_expanded:', self.nodes_expanded)
        # the size of the frontier set when the goal node is found
        print('fringe_size:', len(self.items))
        # the maximum size of the frontier set in the lifetime of the algorithm
        print('max_fringe_size:', self.max_fringe_size)
        # the depth within the search tree when the goal node is found
        print('search_depth:', self.search_depth)
        # the maximum depth of the search tree in the lifetime of the algorithm
        print('max_search_depth:', self.max_search_depth)
        # the total running time of the search instance, reported in seconds
        print('running_time: {:2f} secs'.format(self.running_time))
        # the maximum RAM usage in the lifetime of the process as measured by the
        # ru_maxrss attribute in the resource module, reported in megabytes
        print('max_ram_usage: {} MB'.format(getrusage(RUSAGE_SELF).ru_maxrss / (10 ** 6)))


class DFS(Search):
    def __init__(self, board):
        Search.__init__(self)
        self.board = board

    def run(self):
        start_time = time()
        self.items = Stack(self.board)

        while not (self.items.is_empty() or self.found):
            board = self.items.pop()
            moves = self.make_viable_moves(board)
            for i in range(len(moves) - 1, -1, -1):
                if moves[i] == self.goal:
                    self.running_time = time() - start_time
                    self.print_statistics()
                    self.found = True
                    break
                elif moves[i] not in self.visited:
                    self.visited.add(moves[i])
                    self.items.push(moves[i])

class BFS(Search):
    def __init__(self, board):
        Search.__init__(self)
        self.board = board

    def run(self):
        start_time = time()
        self.items = Queue(self.board)

        while not (self.items.is_empty() or self.found):
            board = self.items.get()
            moves = self.make_viable_moves(board)
            for i in range(len(moves)):
                if moves[i] == self.goal:
                    self.running_time = time() - start_time
                    self.print_statistics()
                    self.found = True
                    break
                elif moves[i] not in self.visited:
                    self.visited.add(moves[i])
                    self.items.put(moves[i])


class AST(Search):
    def __init__(self, board):
        Search.__init__(self)
        self.board = board

    def run(self):
        # TO BE IMPLEMENTED
        pass


class IDA(Search):
    def __init__(self, board):
        Search.__init__(self)
        self.board = board

    def run(self):
        # TO BE IMPLEMENTED
        pass


if __name__ == '__main__':
    #board = [(3, 1, 2, 0, 4, 5, 6, 7, 8)]
    board = [(1, 2, 5, 3, 4, 0, 6, 7, 8)]
    DFS(board).run()
