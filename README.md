# JPYForex

JPYForexは、ドル円、ユーロ円、人民元円の為替レートを手軽に取得できるPythonパッケージです。このツールは、pandas_datareaderを利用してFRED（セントルイス連銀のデータAPI）から最新の為替レートデータを取得し、それを円建ての価格に変換しています。

JPYForex is a Python package that allows you to easily retrieve exchange rates for USD/JPY, EUR/JPY, and CNY/JPY. This tool uses pandas_datareader to fetch the latest exchange rate data from FRED (Federal Reserve Bank of St. Louis Data API) and converts it into prices denominated in yen.

## 特徴　Features
- 簡単な操作：わずか数行のコードで、円建ての為替レートを取得できます。
- 多通貨対応：ドル円、ユーロ円、人民元円のレートをサポートしています。

- Easy to Use: With just a few lines of code, you can retrieve exchange rates denominated in yen.
- Supports Multiple Currencies: Supports rates for USD/JPY, EUR/JPY, and CNY/JPY.

## 注意 Attention

FREDのデータはパーソナル、ノンコマーシャル向け専用です。商業利用はお控えください。

The data from FRED is exclusively for personal, non-commercial use. Please do not use for commercial purposes.

## インストール

```
pip install jpyforex
```

```
pip install git+https://github.com/mazarimono/JPYForex.git
```

## 使い方(How to Use)

JPYForexの基本的な使用方法は以下の通りです。
The basic usage of JPYForex is as follows.

```python
from JPYForex import jpyforex
# 米ドル建ての日足データを5年分取得

usd = jpyforex.JPYForex()
df_usd = usd.get_data()

```

## ライセンス

MIT