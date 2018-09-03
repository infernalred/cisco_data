import paramiko
import datetime

host = '192.168.100.61'
user = 'cisco'
secret = 'cisco'
port = 22

a = datetime.date.today()
a = str(a) + ".txt"
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Подключение
client.connect(hostname=host, username=user, password=secret, port=port)

# Выполнение команды
stdin, stdout, stderr = client.exec_command('show ip int brief')

# Читаем результат
data = stdout.readlines()
for ll in data:
    line = ll.strip(", ")
    p = line.split(", ")
    file = open(a, "w")
    file.writelines(p)
    file.close()
    client.close()
    print(p)


