
from pexpect import pxssh

class Bot:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()  # on etabli la connexion SSH

    # methode/fonction permettant d'etablire la connexion avec un bot

    def connect(self):
        try:
            session = pxssh.pxssh(encoding='utf-8')
            session.force_password = True
            session.login(self.host, self.user, self.password, terminal_type='ansi',
                          original_prompt=r"[#$]", login_timeout=10, port=22,
                          auto_prompt_reset=False, ssh_key=None, quiet=True,
                          sync_multiplier=1, check_local_ip=True)

            print('success')
            return session
        except Exception as err:
            print("errur: impossible d'ouvrir la session")
            print(err)

        # send command to client
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


