from enum import Enum, auto


class Jun(Enum):
    JOJUN = auto()
    CHUJUN = auto()
    GEJUN = auto()


def convert_date_2_turn(year: int, month: int, jun: Jun) -> int:
    if not isinstance(jun, Jun):
        return -1
    turn: int = (year * 12 * 3 - 1) + (month * 3 - 1)
    if jun == Jun.JOJUN:
        pass
    elif jun == Jun.CHUJUN:
        turn += 1
    else:
        turn += 2
    return turn


def main() -> None:
    while True:
        date: str = input('yyyymm(先頭0埋め): ')
        if not date.isdigit():
            print('quit')
            print('---')
            break
        year: int = int(date[0:4])
        month: int = int(date[4:6])

        turn_jojun: int = convert_date_2_turn(year, month, Jun.JOJUN)
        print(f'{year}年{month}月初旬: {turn_jojun}期')

        turn_chujun: int = convert_date_2_turn(year, month, Jun.CHUJUN)
        print(f'{year}年{month}月中旬: {turn_chujun}期')

        turn_gejun: int = convert_date_2_turn(year, month, Jun.GEJUN)
        print(f'{year}年{month}月下旬: {turn_gejun}期')
        print('---')
    print('---')


if __name__ == '__main__':
    main()
