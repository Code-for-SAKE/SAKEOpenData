import json
import re

import pandas as pd
from pymongo import MongoClient

if __name__ == "__main__":
    # brand json の読み込み
    path_fname_brands = "./brands.json"
    brands = []
    with open(path_fname_brands, "r", encoding="utf-8") as f:
        brands = json.load(f)

    # mongo のセットアップ
    client = MongoClient()
    db = client['sakepedia']
    collection_breweries = db.get_collection('breweries')
    collection_brands = db.get_collection('brands')

    # 蔵元検索結果の検索結果数
    df_num_breweries_in_mongo = pd.DataFrame()


    print(len(brands))
    for dict_brand_wiki in brands:
        brand = dict_brand_wiki['brand']
        brewery = dict_brand_wiki['brewery']
        prefecture = dict_brand_wiki['location']

        # 蔵元idの検索
        # カッコ内にフリガナなどを含む場合に、正しく蔵元を取得できないため、
        # カッコを除外した文字列も検索する
        brewery_without_bracket = re.sub("（[^）]+）", "", brewery)
        search_condition_brewery = brewery
        if not brewery == brewery_without_bracket:
            search_condition_brewery = {"$regex": f"^{brewery}$|^{brewery_without_bracket}$"}
        records_brewery = [data for data in collection_breweries.find(filter={
                                                                      "name": search_condition_brewery,
                                                                      "address": {"$regex": f"^{prefecture}"}})]
        # 一意の蔵元を取得できた場合のみ、データを追加
        if len(records_brewery) == 1:
            record_brewery = records_brewery[0]
            record_brand = {
                'name': brand,
                'brewery': record_brewery['_id'],
                'logo': None,
                'description': None,
                'author': None
            }
            collection_brands.insert_one(record_brand)

        df_num_breweries_in_mongo.loc[brewery, "検索結果数"] = len(records_brewery)
    df_num_breweries_in_mongo.to_csv("./search_results_of_breweries.csv")
