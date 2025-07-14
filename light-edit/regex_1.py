import re

string = "Jun 6 17:51:24 ksmg.loc KSMG: Delete all messages in MTA queues: success, queues: [def]."

# Используем регулярное выражение для разбора даты и времени
datetime_pattern = r"(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})"

# Используем регулярное выражение для разбора имени сервера
server_pattern = r"(\w+\.loc)"

# Используем регулярное выражение для разбора названия системы
system_pattern = r"(\w+):"

# Используем регулярное выражение для разбора статуса операции
status_pattern = r"(\w+),"

# Используем регулярное выражение для разбора списка очередей
queues_pattern = r"\[([A-Za-z]+)\]"

# Извлекаем данные с помощью регулярных выражений
datetime = re.search(datetime_pattern, string).group(1)
server = re.search(server_pattern, string).group(1)
system = re.search(system_pattern, string).group(1)
status = re.search(status_pattern, string).group(1)
queues = re.search(queues_pattern, string).group(1)

# Выводим извлеченные данные
print("Дата и время:", datetime)
print("Имя сервера:", server)
print("Название системы:", system)
print("Статус операции:", status)
print("Очереди:", queues)