import requests
from bs4 import BeautifulSoup


def get_data(url):
    #url = "https://catalog.onliner.by/notebook/asus/x507uabq040"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    table = soup.table
    dict_rows = {}
    for row in table.findAll("tr"):
        if row.get('class') is not None:
            text_attr = (row.td.div.get_text().strip())
            dict_rows[text_attr] = {}
        else:
            tds = row.findAll("td")
            name = tds[0].contents[0].strip()
            value = tds[1].span.get_text().strip()
            if value != '':
                dict_rows[text_attr][name] = value
    print(dict_rows)
    return dict_rows
