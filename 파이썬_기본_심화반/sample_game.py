import random
import os
import time

# 게임 보드의 크기
BOARD_WIDTH = 10
BOARD_HEIGHT = 20

# 블록 모양과 색깔 정의
EMPTY = ' '
BLOCK = '■'
COLORS = ['R', 'G', 'B', 'Y', 'P']

# 테트리스 블록 모양 정의
BLOCK_SHAPES = [
    [[BLOCK], [BLOCK], [BLOCK], [BLOCK]],  # 네모 모양
    [[BLOCK, EMPTY], [BLOCK, BLOCK]],      # 지그재그 모양
    [[EMPTY, BLOCK], [BLOCK, BLOCK]],      # 반대 지그재그 모양
    [[BLOCK, BLOCK, BLOCK], [EMPTY, EMPTY, BLOCK]],  # L 모양
    [[BLOCK, BLOCK, BLOCK], [BLOCK, EMPTY, EMPTY]],  # 반대 L 모양
    [[BLOCK, BLOCK], [BLOCK, BLOCK]],      # 사각 모양
    [[BLOCK, BLOCK, EMPTY], [EMPTY, BLOCK, BLOCK]],  # Z 모양
]

class Tetris:
    def __init__(self):
        self.board = [[EMPTY] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        self.current_block = self.get_random_block()
        self.block_x = BOARD_WIDTH // 2 - 1
        self.block_y = 0
        self.score = 0
        self.game_over = False

    def get_random_block(self):
        shape = random.choice(BLOCK_SHAPES)
        color = random.choice(COLORS)
        return (shape, color)

    def rotate_block(self):
        self.current_block = (list(zip(*self.current_block[::-1])), self.current_block[1])

    def move_block_down(self):
        self.block_y += 1
        if self.check_collision():
            self.block_y -= 1
            self.merge_block()

    def move_block_left(self):
        self.block_x -= 1
        if self.check_collision():
            self.block_x += 1

    def move_block_right(self):
        self.block_x += 1
        if self.check_collision():
            self.block_x -= 1

    def check_collision(self):
        for y, row in enumerate(self.current_block[0]):
            for x, cell in enumerate(row):
                if cell == BLOCK:
                    board_x = self.block_x + x
                    board_y = self.block_y + y
                    if (board_x < 0 or board_x >= BOARD_WIDTH or
                            board_y >= BOARD_HEIGHT or
                            self.board[board_y][board_x] != EMPTY):
                        return True
        return False

    def merge_block(self):
        for y, row in enumerate(self.current_block[0]):
            for x, cell in enumerate(row):
                if cell == BLOCK:
                    board_x = self.block_x + x
                    board_y = self.block_y + y
                    self.board[board_y][board_x] = self.current_block[1]
                    if board_y == 0:
                        self.game_over = True
        self.check_lines()

    def check_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(cell != EMPTY for cell in row)]
        for line in lines_to_clear:
            del self.board[line]
            self.board.insert(0, [EMPTY] * BOARD_WIDTH)
            self.score += 10 * (len(lines_to_clear) ** 2)

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.board:
            print(' '.join(row))
        print('Score:', self.score)
        if self.game_over:
            print('Game Over!')

    def run(self):
        while not self.game_over:
            self.print_board()
            time.sleep(0.5)
            self.move_block_down()
            if self.game_over:
                break
            self.print_board()

if __name__ == '__main__':
    tetris_game = Tetris()
    tetris_game.run()
