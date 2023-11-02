from JPYForex import jpyforex

jpy = jpyforex.JPYForex(start_date='20211111', end_date='20220222')
df = jpy.get_data()
print(df)

