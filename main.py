# [x] Прочитать весь файл в память
# [x] В каждой строке искать "опасные" имена из списка

from pathlib import Path
from rich import print

# Путь к лог-файлу на исследуемой системе
CONSOLE_HOST_HISTORY_PATH = Path(
    r"E:\Users\andrewww-dev\AppData\Roaming"
    r"\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt"
)
# Набор строк, которые будут детектироваться
MALICIOUS_NAMES = (
    "mimikatz", 
    "anydesk", 
    "nmap",
    # и ...
) 
console_host_history = CONSOLE_HOST_HISTORY_PATH.read_text()
console_host_history_lines = console_host_history.splitlines()
for line_number,line in enumerate(console_host_history_lines,start=1):
    for malicious_name in MALICIOUS_NAMES:
        
        if malicious_name.lower() in line.lower():
            print ("[",line_number,"]", line)
          
