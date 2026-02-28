"""
Mod Screen Manager Configurator
тут мы делаем GUI чтобы мододелы не ебали мозг с ручной настройкой
"""

import sys
import os

# чтоб импорты работали
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gui.app import ModScreenManagerApp


def main():
    """точка входа в приложуху"""
    app = ModScreenManagerApp()
    app.mainloop()


if __name__ == "__main__":
    main()
