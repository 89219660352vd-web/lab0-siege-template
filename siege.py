"""Тикет 0: парсер лога осады.

Запуск: python3 siege.py siege_log.txt
"""

import sys


def main(path: str) -> None:
    # TODO: прочитать лог, посчитать урон, напечатать строки вида
    # "Игрок <Имя> из гильдии <Тег> нанес <Урон> по воротам."
    pass


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "siege_log.txt")
