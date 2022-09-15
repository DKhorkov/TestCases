import sys
import os
import time
import keyboard
import pyautogui
import statistics
import shutil


class KriegerTest:

    def __init__(self, input_file_dir, outputdir):
        self.input_file_dir = input_file_dir
        self.outputdir = outputdir

    def _start_krieger(self):
        os.startfile(self.input_file_dir)
        time.sleep(20)

    def _make_first_screen_and_run_stats(self):
        pyautogui.screenshot(f'{self.outputdir}\\starting_screenshot.jpg')
        time.sleep(5)
        keyboard.press("Enter")
        time.sleep(1)
        keyboard.press("Enter")
        time.sleep(1)
        os.startfile('fps.exe')

    @staticmethod
    def _walking():
        for i in range(100):
            keyboard.press("w")
        time.sleep(10)

    def _stop_stats_and_create_second_screen(self):
        os.system("TASKKILL /F /IM fps.exe")
        pyautogui.screenshot(f'{self.outputdir}\\ending_screenshot.jpg')
        time.sleep(5)

    @staticmethod
    def _close_krieger():
        os.system("TASKKILL /F /IM krieger.exe")

    def _get_stats_and_average_fps(self):
        shutil.copyfile('stats.txt', f'{self.outputdir}\\fps_stats.txt')
        with open('stats.txt', "r") as f:
            stats = f.read()
        lst = stats.strip('[')
        lst = lst.strip(']')
        lst = lst.split(',')
        lst2 = []
        for element in lst:
            float_elem = float(element)
            lst2.append(float_elem)
        avg = statistics.mean(lst2)
        with open(os.path.join(self.outputdir, 'average_fps.txt'), "w") as f:
            f.write(str(avg))
        print('Script executed')

    def run_script(self):
        self._start_krieger()
        self._make_first_screen_and_run_stats()
        self._walking()
        self._stop_stats_and_create_second_screen()
        self._close_krieger()
        self._get_stats_and_average_fps()


if __name__ == "__main__":
    krieger_test = KriegerTest(sys.argv[1], sys.argv[2])
    krieger_test.run_script()
