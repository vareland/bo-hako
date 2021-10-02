import datetime
import util


def calc_datetime(target_turn: int, current_turn: int, last_updated_at: datetime.datetime) -> datetime.datetime:
    """
    更新日時を計算
    :param target_turn: 更新日時取得対象のターン
    :param current_turn: 現在のターン
    :param last_updated_at: 最終更新日時
    :return: 更新日時
    """
    turn_delta: int = target_turn - current_turn
    time_del: datetime.timedelta = datetime.timedelta(hours=turn_delta * util.INTERVAL)
    return last_updated_at + time_del


def main() -> None:
    current_datetime: datetime.datetime = util.get_current_datetime()
    last_updated_at: datetime.datetime = util.get_last_updated_time(current_datetime)
    current_turn: int = util.get_current_turn()

    print(f'システム日時:{str(current_datetime)}')
    print(f'最終更新日時:{str(last_updated_at)}')
    print(f'現在のターン:{current_turn}')
    print('------')

    while True:
        turn: str = input('turn: ')
        if not turn.isdigit():
            print('quit')
            print('---')
            break
        result: datetime.datetime = calc_datetime(int(turn), current_turn, last_updated_at)
        print(str(result))
        continue


if __name__ == '__main__':
    main()
