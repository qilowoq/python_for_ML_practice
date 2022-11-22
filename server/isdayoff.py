import requests


class IsDayOff:
    def __init__(self) -> None:
        pass

    def _req(self, year, month) -> str:
        r = requests.get('https://isdayoff.ru/api/getdata?year={}&month={}'.format(year, month))
        r.raise_for_status() 
        return r.text
        

    def number_of_work_days_in_month(self, year, month) -> int:
        ans = self._req(year, month)
        return sum(map(lambda x: 1 - int(x), ans))


if __name__ == "__main__":
    sdo = IsDayOff()
    print(sdo.number_of_work_days_in_month(2022, 8))
