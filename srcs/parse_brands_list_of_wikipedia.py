"""wikipediaの銘柄一覧から、銘柄をパースする
"""

import json
from lxml import html
import re

import requests

if __name__ == "__main__":
    url_brands_list = "https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E9%85%92%E3%81%AE%E9%8A%98%E6%9F%84%E4%B8%80%E8%A6%A7"

    res = requests.get(url_brands_list)

    load_html = html.fromstring(res.text)
    contents_in_p_or_li = load_html.xpath("//b|//ul/li|//h2|//h3/span[@class='mw-headline']")

    brewery = ""
    location = ""
    brands = []
    for content in contents_in_p_or_li:
        # 酒蔵名のパース
        if content.tag == 'b':
            if len(content.getchildren()) > 0 :
                brewery = content.getchildren()[0].text
            else:
                brewery = content.text

        # ブランド名のパース
        elif content.tag == 'li':
            brand = content.text
            if brand is None:
                if len(content.getchildren()) > 0:
                    brand = content.getchildren()[0].text
            brand = re.sub("（[^\）]+）$", "", brand)
            brands.append(
                {
                    'brand' : brand,
                    'brewery' : brewery,
                    'location' : location
                }
            )

        # 所在地のパース
        elif content.tag == 'span':
            location = content.text

        # 終わり
        elif content.tag == 'h2' and len(brands) > 1:
            break

    with open("./brands.json", "w") as f:
        json.dump(brands, f, ensure_ascii=False, indent=4)