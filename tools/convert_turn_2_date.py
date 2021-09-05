import math

JOJUN: str = '初旬'
CHUJUN: str = '中旬'
GEJUN: str = '下旬'


def convert_turn_2_date(turn_str: str) -> str:
    turn: int = int(turn_str)
    # 旬を取得。第1ターンは上旬
    if turn % 3 == 0:
        jun: str = GEJUN
    elif turn % 3 == 1:
        jun: str = JOJUN
    else:
        jun: str = CHUJUN

    # 月を取得。第1ターンは1月
    # 1月は3ターンなので3で除する。切り上げて-1(境界値の処理)
    tmp_int = math.ceil(turn / 3) - 1
    month: int = tmp_int % 12 + 1

    # 年を取得(第1ターンは0年)。切り上げて-1(境界値の処理)
    year: int = math.ceil(turn / (12 * 3)) - 1

    date = f'{year}年{month}月{jun}'

    return date


def main() -> None:
    while True:
        turn: str = input('turn: ')
        if not turn.isdigit():
            print('quit')
            print('---')
            break
        date: str = convert_turn_2_date(turn)
        print(date)
        print('---')
    print('---')


if __name__ == '__main__':
    main()
