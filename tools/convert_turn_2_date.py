from tools import util


def main() -> None:
    while True:
        turn: str = input('turn: ')
        if not turn.isdigit():
            print('quit')
            print('---')
            break
        date: str = util.convert_turn_2_date(int(turn))
        print(date)
        print('---')
    print('---')


if __name__ == '__main__':
    main()
