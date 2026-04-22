import math
import copy

EMPTY = '.'
X = 'X'
O = 'O'

def local_winner(board):
    lines = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != EMPTY:
            return line[0]
    if all(board[r][c] != EMPTY for r in range(3) for c in range(3)):
        return 'D'
    return None

def init_state():
    boards = [[ [[EMPTY]*3 for _ in range(3)] for _ in range(3)] for _ in range(3)]
    result = [[None]*3 for _ in range(3)]
    return {'boards': boards, 'result': result, 'nb': None, 'turn': X}

def get_moves(state):
    moves = []
    nb = state['nb']
    res = state['result']
    if nb is None or res[nb[0]][nb[1]] is not None:
        targets = [(R, C) for R in range(3) for C in range(3) if res[R][C] is None]
    else:
        targets = [nb]
    for (R, C) in targets:
        board = state['boards'][R][C]
        for r in range(3):
            for c in range(3):
                if board[r][c] == EMPTY:
                    moves.append((R, C, r, c))
    return moves

def apply_move(state, move):
    R, C, r, c = move
    s = copy.deepcopy(state)
    player = s['turn']
    s['boards'][R][C][r][c] = player
    s['result'][R][C] = local_winner(s['boards'][R][C])
    if s['result'][r][c] is not None:
        s['nb'] = None
    else:
        s['nb'] = (r, c)
    s['turn'] = O if player == X else X
    return s

def macro_winner(res):
    lines = [
        [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)],
    ]
    for line in lines:
        vals = [res[r][c] for r, c in line]
        if vals[0] == vals[1] == vals[2] and vals[0] in (X, O):
            return vals[0]
    if all(res[r][c] is not None for r in range(3) for c in range(3)):
        return 'D'
    return None

def is_terminal(state):
    return macro_winner(state['result']) is not None or len(get_moves(state)) == 0

def evaluate(state):
    w = macro_winner(state['result'])
    if w == X:
        return 1000
    if w == O:
        return -1000
    if w == 'D':
        return 0
    score = 0
    res = state['result']
    for R in range(3):
        for C in range(3):
            if res[R][C] == X:
                score += 10
            elif res[R][C] == O:
                score -= 10
    for R in range(3):
        for C in range(3):
            if res[R][C] is None:
                board = state['boards'][R][C]
                for r in range(3):
                    for c in range(3):
                        if board[r][c] == X:
                            score += 1
                        elif board[r][c] == O:
                            score -= 1
    return score

class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, state):
        return "goal reached" if is_terminal(state) else "searching"

    def act(self, state, env):
        status = self.formulate_goal(state)
        if status == "goal reached":
            return None
        else:
            return env.compute_minimax(state, self.depth)

class MinimaxEnvironment:
    def __init__(self):
        self.nodes = 0

    def get_percept(self, state):
        return state

    def compute_minimax(self, state, depth, is_max=True):
        self.nodes += 1
        if depth == 0 or is_terminal(state):
            return evaluate(state), None
        moves = get_moves(state)
        best = None
        if is_max:
            val = -math.inf
            for move in moves:
                cv, _ = self.compute_minimax(apply_move(state, move), depth - 1, False)
                if cv > val:
                    val = cv
                    best = move
        else:
            val = math.inf
            for move in moves:
                cv, _ = self.compute_minimax(apply_move(state, move), depth - 1, True)
                if cv < val:
                    val = cv
                    best = move
        return val, best

class AlphaBetaAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, state):
        return "goal reached" if is_terminal(state) else "searching"

    def act(self, state, env):
        status = self.formulate_goal(state)
        if status == "goal reached":
            return None
        else:
            return env.alpha_beta_search(state, self.depth, -math.inf, math.inf, True)

class AlphaBetaEnvironment:
    def __init__(self):
        self.nodes = 0

    def get_percept(self, state):
        return state

    def alpha_beta_search(self, state, depth, alpha, beta, is_max=True):
        self.nodes += 1
        if depth == 0 or is_terminal(state):
            return evaluate(state), None
        moves = get_moves(state)
        best = None
        if is_max:
            val = -math.inf
            for move in moves:
                cv, _ = self.alpha_beta_search(apply_move(state, move), depth - 1, alpha, beta, False)
                if cv > val:
                    val = cv
                    best = move
                alpha = max(alpha, val)
                if beta <= alpha:
                    break
        else:
            val = math.inf
            for move in moves:
                cv, _ = self.alpha_beta_search(apply_move(state, move), depth - 1, alpha, beta, True)
                if cv < val:
                    val = cv
                    best = move
                beta = min(beta, val)
                if beta <= alpha:
                    break
        return val, best

def print_board(state):
    res = state['result']
    boards = state['boards']
    print("-"*29)
    for R in range(3):
        for r in range(3):
            row = "|"
            for C in range(3):
                if res[R][C] == X:
                    row += " X X X |"
                elif res[R][C] == O:
                    row += " O O O |"
                elif res[R][C] == 'D':
                    row += " D D D |"
                else:
                    for c in range(3):
                        row += " " + boards[R][C][r][c]
                    row += " |"
            print(row)
        print("-"*29)
    w = macro_winner(res)
    if w:
        print(f"macro winner: {w}")
    nb = state['nb']
    if nb:
        print(f"next board: {nb}")
    else:
        print("next board: any")

def run_agent(agent, env, state):
    percept = env.get_percept(state)
    return agent.act(percept, env)

def play_game(x_type='alphabeta', o_type='alphabeta', depth=2):
    state = init_state()

    def make(agent_type):
        if agent_type == 'minimax':
            return MinimaxAgent(depth), MinimaxEnvironment()
        else:
            return AlphaBetaAgent(depth), AlphaBetaEnvironment()

    x_agent, x_env = make(x_type)
    o_agent, o_env = make(o_type)

    moves = 0
    print(f"x: {x_type} | o: {o_type} | depth: {depth}")
    print_board(state)

    while not is_terminal(state):
        if state['turn'] == X:
            _, move = run_agent(x_agent, x_env, state)
            nodes = x_env.nodes
        else:
            _, move = run_agent(o_agent, o_env, state)
            nodes = o_env.nodes
        if move is None:
            break
        R, C, r, c = move
        print(f"{state['turn']} -> macro({R},{C}) local({r},{c}) | nodes: {nodes}")
        state = apply_move(state, move)
        moves += 1
        print_board(state)

    w = macro_winner(state['result'])
    print(f"result  : {'draw' if w == 'D' else w + ' wins' if w else 'no moves'}")
    print(f"moves   : {moves}")
    print(f"x nodes : {x_env.nodes}")
    print(f"o nodes : {o_env.nodes}")

play_game(x_type='alphabeta', o_type='alphabeta', depth=2)