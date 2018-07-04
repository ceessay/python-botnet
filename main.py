from  Bot import Bot


botnet = []


mybot1 = Bot('127.0.0.1', 'test', 'test1234')
mybot2 = Bot('127.0.0.2', 'test', 'test1234')
mybot3 = Bot('127.0.0.3', 'test', 'test1234')

botnet.append(mybot1)
botnet.append(mybot2)
botnet.append(mybot3)

# envoyer une commande a teoute les machines
def command_bots(command):
    for bot in botnet:
        attack = bot.send_command(command)
        print('Output from ' + bot.host)
        print(attack)



command_bots("ls")