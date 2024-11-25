import os
import sys
import select

# Détecter le système d'exploitation pour choisir le module approprié
if sys.platform == "win32":
    import msvcrt
else:
    import tty
    import termios

class Key_Controle:
    @staticmethod
    def check_keypress():
        Key_Controle.clear()
        if sys.platform == "win32":
            return msvcrt.kbhit()
        else:
            return select.select([sys.stdin], [], [], 0)[0] != []

    @staticmethod
    def get_key():
        if sys.platform == "win32":
            return msvcrt.getch().decode('utf-8')
        else:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                key = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return key
    
    @staticmethod
    def clear():
        if sys.platform == "win32":
            os.system('cls')
        else:
            os.system('clear')