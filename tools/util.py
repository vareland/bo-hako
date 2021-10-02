import datetime
import math

import bs4
import requests

# 更新間隔（hours）
INTERVAL: int = 4
# その日の最初の更新時間
FIRST_UPDATE_HOUR: int = 0

JOJUN: str = '初旬'
CHUJUN: str = '中旬'
GEJUN: str = '下旬'


def get_current_datetime() -> datetime.datetime:
    return datetime.datetime.now().replace(microsecond=0)


def get_current_turn() -> int:
    """
    ゲーム本体から現在のターンを取得
    """
    r: requests.Response = requests.get('http://tanstafl.sakura.ne.jp/trade/hako-main.php')
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
    how_many_times_updated: int = (current_hour - FIRST_UPDATE_HOUR) // INTERVAL
    # 更新された時刻
    last_updated_hour: int = FIRST_UPDATE_HOUR + (how_many_times_updated * INTERVAL)

    return current_date + datetime.timedelta(hours=last_updated_hour)


def convert_turn_2_date(turn: int) -> str:
    # 旬を取得。第1ターンは上旬
    if turn % 3 == 0:
        jun: str = GEJUN
    elif turn % 3 == 1:
        jun: str = JOJUN
    else:
        jun: str = CHUJUN

    # 月を取得。第1ターンは1月
    # 1月は3ターンなので3で除する。切り上げて-1(境界値の処理)
    tmp_int: int = math.ceil(turn / 3) - 1
    month: int = tmp_int % 12 + 1

    # 年を取得(第1ターンは0年)。切り上げて-1(境界値の処理)
    year: int = math.ceil(turn / (12 * 3)) - 1

    date: str = f'{year}年{month}月{jun}'

    return date
