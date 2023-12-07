from datetime import date
from json import dump, load

from requests import get


def get_response(*args) -> dict:
    with open('Currency_Rate.json') as f:
        return load(f)


def update(*args: object) -> dict:
    present = date.today().strftime("%d %b %Y")
    response = get_response()
    file_date = response["time_last_update_utc"][5:16]
    # if present != file_date:
    #     f = open('Currency_Rate.json', 'w')
    #     url = "https://v6.exchangerate-api.com/v6/a04cc39aea88ee70a55c180c/latest/USD"
    #     response = get(url).json()
    #     dump(response, f, indent=4)
    #     f.close()
    response = response['conversion_rates']
    return response

