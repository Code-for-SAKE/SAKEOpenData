## 概要

- OpenDataを収集する

## Notebook

### 銘柄情報
銘柄は県別jsonとして作成する。
県別jsonの一覧を`bottles.json`として作成する。

#### ファイル名
* bottles.json
* bottles/{県名英字}.json

#### 項目
銘柄は以下が取得可能(※ない場合は空白文字)
* _id
* url
* subname
* aminoAcidContent
* alcoholContent
* price
* award
* sakeYeast
* brand
* volume
* sakeRiceExceptForKojiMaking
* sakeMeterValue
* mariage
* type
* ricePolishingRate
* brewery
* breweryYear
* matchDrinkingVessel
* matchDrinkingSceneAndTarget
* matchDrinkingTemperature
* prefecture
* starterCulture
* acidity
* description
* riceForMakingKoji


### 酒蔵情報
#### ファイル名
* breweries.json

#### 項目
酒蔵は以下が取得可能(※ない場合は空白文字)
* 蔵元
* カナ
* 都道府県
* 住所
* email
* tel
* url
* 創業

jsonファイルは全てUTF8でインデントは半角スペース*2です。

## srcs

- wikipediaの銘柄リストをパースし、MongoDBへ追加する