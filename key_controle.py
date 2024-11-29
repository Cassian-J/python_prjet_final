import os
import sys
import select

if sys.platform == "win32":
    import msvcrt
else:
    import tty
    import termios

class Key_Controle:
    """
        Classe utilitaire pour gérer l'entrée clavier en mode non-bloquant et les actions associées.
        Compatible avec les systèmes d'exploitation Windows et Unix/Linux.
    """
    @staticmethod
    def check_keypress():
        """
            Vérifie si une touche a été pressée sans bloquer le programme.
            :return: `True` si une touche a été pressée, sinon `False`.
        """
        Key_Controle.clear()
        if sys.platform == "win32":
            return msvcrt.kbhit()
        else:
            return select.select([sys.stdin], [], [], 0)[0] != []

    @staticmethod
    def get_key():
        """
            Lit une touche pressée par l'utilisateur et la retourne.
            :return: La touche pressée sous forme de chaîne de caractères.
        """
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
        """
            Efface l'écran de la console pour un affichage plus propre.
            Compatible avec Windows et Unix/Linux.
        """
        if sys.platform == "win32":
            os.system('cls')
        else:
            os.system('clear')