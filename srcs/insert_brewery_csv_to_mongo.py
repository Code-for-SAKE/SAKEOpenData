import json
import pdb
import re

import pandas as pd
from pymongo import MongoClient

if __name__ == "__main__":
    # 蔵元csvの読み込み
    path_fname_breweries = "./20210327Sakepediaデータ収集 - シート4.csv"
    df_breweries = pd.read_csv(path_fname_breweries)
    df_breweries = df_breweries.loc[~df_breweries['名前'].isna(), :]

    # mongo のセットアップ
    client = MongoClient()
    db = client['sakepedia']
    collection_breweries = db.get_collection('breweries')

    # データの追加
    for ind in df_breweries.index:
        row = df_breweries.loc[ind, :]
        name = row['名前']
        kana = row['フリガナ']
        prefecture = row['都道府県.1']
        address = row['住所']
        latitude = row['緯度']
        longitude = row['経度']
        email = row['Eメール']        
        tel = row['電話番号']
        url = row['URL']
        ecurl = row['購入URL']
        facebook = row['Facebook']
        twitter = row['Twitter']
        instagram = row['Instagram']
        othersns = row['その他SNS']
        startYear = row['創業年']
        endYear = row['廃業年']

        record_brand = {
            'name': name,
            'kana': kana,
            'prefecture': prefecture,
            'address' : address,
            'latitude' : latitude,
            'longitude' : longitude,
            'email' : email,
            'tel' : tel,
            'url' : url,
            'ecurl' : ecurl,
            'facebook' : facebook,
            'twitter' : twitter,
            'instagram' : instagram,
            'othersns' : othersns,
            'startYear' : startYear,
            'endYear' : endYear,
            'author' : None
        }
        collection_breweries.insert_one(record_brand)

