import sys
import tty
import termios
import select

class Key_Controle:
    def check_keypress(self):
        return select.select([sys.stdin], [], [], 0)[0] != []

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key