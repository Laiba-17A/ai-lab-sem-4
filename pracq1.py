grid = [['s', 2, 0, 0, 1],
        [0, 'x', 1, 2, 0],
        [0, 2, 0, 'x', 0],
        [0, 0, 1, 0, 2]]

class Environment:
    def __init__(self, grid):
        self.grid = grid
        self.rows = 4
        self.cols = 5

    def getscore(self, x, y):
        return self.grid[x][y]


class UtilityAgent:
    def __init__(self, x, y, energy=8):
        self.x = x
        self.y = y
        self.energy = energy
        self.totalscore = 0
        self.visited = set()
        self.visited.add((x, y))   # start position visited

    def get_posmoves(self, env):
        moves = []

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dx, dy in directions:
            nx = self.x + dx
            ny = self.y + dy

            if 0 <= nx < env.rows and 0 <= ny < env.cols:
                if env.grid[nx][ny] != 'x' and (nx, ny) not in self.visited:
                    moves.append((nx, ny))

        return moves

    def choose_best_move(self, env):
        moves = self.get_posmoves(env)

        best_move = None
        best_score = -1

        for move in moves:
            x, y = move
            score = env.getscore(x, y)

            if isinstance(score, int):
                if score > best_score:
                    best_score = score
                    best_move = move

        return best_move

    def act(self, env):
        while self.energy > 0:
            best_move = self.choose_best_move(env)

            if best_move is None:
                break

            self.x, self.y = best_move
            self.visited.add((self.x, self.y))

            self.totalscore += env.getscore(self.x, self.y)

            print(f"Moved to ({self.x},{self.y}) -> Collected {env.getscore(self.x, self.y)}")

            env.grid[self.x][self.y] = 0
            self.energy -= 1

        print("Total Cleanliness Score:", self.totalscore)


env = Environment(grid)
robot = UtilityAgent(0, 0, energy=8)
robot.act(env)