import datetime
import requests
import bs4

# 更新間隔（hours）
INTERVAL: int = 4
# その日の最初の更新時間
FIRST_UPDATE_HOUR: int = 0


def get_current_turn() -> int:
    """
    ゲーム本体から現在のターンを取得
    """
    r = requests.get('http://tanstafl.sakura.ne.jp/trade/hako-main.php')
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(r.content, "html.parser")
    raw_str: str = soup.find('h2', 'Turn').text
    current_turn: str = raw_str[8:13]
    if not current_turn.isdigit():
        raise ValueError
    return int(current_turn)


def get_last_updated_time(current_datetime: datetime.datetime) -> datetime.datetime:
    """
    システム日時より最後に更新された時刻を取得
    """
    # datetime型から時刻部分を切り取る
    current_date: datetime.datetime = current_datetime.combine(current_datetime, datetime.time(0))
    current_hour: int = current_datetime.hour
    # その日に更新された回数
    how_many_times_updated: int = (current_hour - FIRST_UPDATE_HOUR)//INTERVAL
    # 更新された時刻
    last_updated_hour: int = FIRST_UPDATE_HOUR + (how_many_times_updated * INTERVAL)

    return current_date + datetime.timedelta(hours=last_updated_hour)


def calc_datetime(target_turn: int, current_turn: int, last_updated_at: datetime.datetime) -> datetime.datetime:
    """
    更新日時を計算
    :param target_turn: 更新日時取得対象のターン
    :param current_turn: 現在のターン
    :param last_updated_at: 最終更新日時
    :return: 更新日時
    """
    turn_delta: int = target_turn - current_turn
    time_del: datetime.timedelta = datetime.timedelta(hours=turn_delta * INTERVAL)
    return last_updated_at + time_del


def main() -> None:
    current_datetime: datetime.datetime = datetime.datetime.now()
    last_updated_at = get_last_updated_time(current_datetime)
    current_turn: int = get_current_turn()

    print(f'システム日時:{str(current_datetime.replace(microsecond=0))}')
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
