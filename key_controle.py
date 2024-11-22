import sys
import tty
import termios
import select

class Key_Controle:
    def check_keypress():
        return select.select([sys.stdin], [], [], 0)[0] != []

    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key