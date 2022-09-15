import time
import pathlib
import os


class Fps:

    def __init__(self):
        self.fps_list = []
        self.last = 0
        self.reset()
        self.second = 1.0
        self.current_path = pathlib.Path().resolve()

    def print_fps(self, frames):
        true_fps = frames / 100000
        print('FPS: {}'.format(true_fps))
        self.fps_list.append(true_fps)
        with open(os.path.join(self.current_path, 'stats.txt'), 'w') as f:
            f.write(str(self.fps_list))

    def reset(self):
        self.fps = 0
        self.tick = time.time()

    def update(self, *argc, **args):
        dur = time.time() - self.tick
        if dur >= self.second:
            self.last = self.fps
            if self.print_fps is not None:
                self.print_fps(self.fps, *argc, **args)
            self.reset()
        else:
            self.fps += 1


if __name__ == "__main__":
    fps = Fps()
    while True:
        fps.update()
