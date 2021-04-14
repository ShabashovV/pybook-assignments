import curses
from life import GameOfLife
import time
from time import sleep
import argparse
from ui import UI

class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)
        self.screen = curses.initscr()
    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        self.screen.border(0)
    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        for i in range(self.life.rows):
            for j in range(self.life.cols):
                if self.life.curr_generation[i][j] == 1:
                    self.screen.addch(i + 1, j + 1, '*')
                else:
                    self.screen.addch(i + 1, j + 1, ' ')

    def run(self) -> None:
        screen = curses.initscr()

        self.draw_borders()

        running = True
        while running:
            self.draw_borders()
            self.draw_grid()
            self.screen.refresh()

            time.sleep(0.5)

            self.life.step()
            running = self.life.is_max_generations_exceed
        curses.endwin()


parser = argparse.ArgumentParser(description='Запусти программу, чтобы посмотреть ход игры в консоли')

parser.add_argument("--rows", default=10, help="Количество строк")
parser.add_argument("--cols", default=10, help="Количество столбцов")
parser.add_argument("--max_generations", default=10, help="Количество ходов")
args = parser.parse_args()
rows = int(args.rows)
cols = int(args.cols)
max=int(args.max_generations)
if __name__ == "__main__":
    game = GameOfLife(size=(rows, cols), randomize=True,max_generations=max)
    console = Console(game)
    console.run()
