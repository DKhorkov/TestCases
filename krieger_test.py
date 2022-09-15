import sys
import os
import time
import keyboard
import pyautogui
import statistics
import shutil


# Обработка полученных в качестве входных данных путей запуска файла и сохранения результатов:
input_file_dir = sys.argv[1]
outputdir = sys.argv[2]

# Запуск кригера:
os.startfile(input_file_dir)
time.sleep(20)

# Снятие скриншота о загрузке игры на сцену и запуск снятия статистики fps:
start_screen = pyautogui.screenshot(f'{outputdir}\\starting_screenshot.jpg')
time.sleep(5)
keyboard.press("Enter")
time.sleep(1)
keyboard.press("Enter")
os.startfile('fps.exe')

# Движение вперед:
for i in range(100):
    keyboard.press("w")
time.sleep(10)

# Завершение снятия статистики fps и создание завершающего скриншота:
os.system("TASKKILL /F /IM fps.exe")
end_screen = pyautogui.screenshot(f'{outputdir}\\ending_screenshot.jpg')
time.sleep(5)

# Закрытие кригера:
os.system("TASKKILL /F /IM krieger.exe")

# Обработка результатов статистики fps и занесение результатов в указанный директорий:
with open('stats.txt', "r") as f:
    stats = f.read()
shutil.copyfile('stats.txt', f'{outputdir}\\fps_stats.txt')
lst = stats.strip('[')
lst = lst.strip(']')
lst = lst.split(',')
lst2 = []
for element in lst:
    float_elem = float(element)
    lst2.append(float_elem)
avg = statistics.mean(lst2)
with open(os.path.join(outputdir, 'average_fps.txt'), "w") as f:
    f.write(str(avg))
print('Script executed')
