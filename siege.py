"""Тикет 0: парсер лога осады.

Запуск: python3 siege.py siege_log.txt
"""

import sys


def main(path: str) -> None:
    # TODO: прочитать лог, посчитать урон, напечатать строки вида
    # "Игрок <Имя> из гильдии <Тег> нанес <Урон> по воротам."
    pass
    raw_log=open(path)
    lines=[line for line in raw_log.readlines()[2:]]

    def g(line):
        if line == '':
            return None
        line = line.replace(',', '.')
        line = line.replace(' ', '')
        line = line.strip()
        et = line.find(']')
        guild = line[1:et]
        ost = line[et + 1:]
        parts = ost.split('|')
        if len(parts) != 4:
            return None
        name = parts[0].strip()
        damage = float(parts[1].strip())
        weapon = parts[2].strip()
        buffs = parts[3].strip()
        if buffs == '' or buffs == 'N/A':
            k = 0
        else:
            k = float(buffs)
        if weapon == 'Active':
            state_multiplier = 1.5
        elif weapon == 'Broken':
            state_multiplier = 0.5
        else:
            state_multiplier = 1.0
        totdam = damage * state_multiplier * (1 + 0.15 * k)
        totdam = round(damage, 2)
        result = "Игрок " + name + " из гильдии " + guild + " нанес " + str(damage) + " по воротам."
        return result

    for i in lines:
        print(g(i))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "siege_log.txt")
