Основной файл скрипта - krieger_test.py
Для запуска снятия статистики был написан файл fps.py и, с помощью pyinstaller, переведен в формат .exe для параллельного запуска со скриптом.
В терминале скрипт запускается следующим образом:   python krieger_test..py <path\to\kkrieger>  <path\to\output> 
Например :  python krieger_test.py C:\Users\alexq\Desktop\krieger_test\krieger.exe C:\Users\alexq\Desktop\krieger_test\results

Все необходимые зависимости указаны в файле requirements.txt