import datetime

import util


def calc_turn(ymd: str, update_count: int, current_turn: int, last_updated_at: datetime.datetime) -> {datetime.datetime, int}:
    # 対象年月日
    year: int = int(ymd[:4])
    month: int = int(ymd[4:6])
    day: int = int(ymd[6:])
    target_ymd: datetime.datetime = datetime.datetime(year, month, day)
    # 対象年月日と最終更新ターンとの差を取得
    time_del: datetime.timedelta = target_ymd - last_updated_at
    # 経過ターン数を取得
    turn_del: int = time_del // datetime.timedelta(hours=util.INTERVAL)

    result_turn: int = current_turn + turn_del + update_count
    result_datetime: datetime.datetime = target_ymd + datetime.timedelta(hours=update_count * util.INTERVAL)

    return {'datetime': result_datetime, 'turn': result_turn}


def main() -> None:
    current_datetime: datetime.datetime = util.get_current_datetime()
    last_updated_at: datetime.datetime = util.get_last_updated_time(current_datetime)
    current_turn: int = util.get_current_turn()

    print(f'システム日時:{str(current_datetime)}')
    print(f'最終更新日時:{str(last_updated_at)}')
    print(f'現在のターン:{current_turn}')
    print('------')

    while True:
        ymd: str = input('yyyymmdd: ')
        if not ymd.isdigit():
            print('quit')
            print('---')
            break
        if not len(ymd) == 8:
            continue
        for i in range(24//util.INTERVAL):
            result = calc_turn(ymd, i, current_turn, last_updated_at)
            fluegel_calender: str = util.convert_turn_2_date(result['turn'])
            print(f"{result['turn']}期({fluegel_calender}): {str(result['datetime'])}")
        continue


if __name__ == '__main__':
    main()
