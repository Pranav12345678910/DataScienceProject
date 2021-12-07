#Pranav Tatavarti, 12/6/2021

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AppleStore.csv",index_col=[0])
size_vs_current_ver = df.plot.scatter(x="size_bytes",y="rating_count_ver",title="Current version rating amount vs Size in GB")
df2 = df.sort_values(by=['price'])
df2 = df2.reset_index(drop=True)
df2.drop([7195,7196], inplace=True)
price_vs_total_ratings = df2.plot.scatter(x="price",y="rating_count_tot",title="Total amount of ratings in millions vs Price")
df4 = df2.drop(columns=["id","track_name","currency","size_bytes","rating_count_tot","rating_count_ver","user_rating_ver","cont_rating","prime_genre","sup_devices.num","ipadSc_urls.num","lang.num","vpp_lic","ver"])
df4.columns = df4.columns.str.strip()
df4 = df4.groupby("price",as_index=False).mean()
df4.plot.scatter(x="price",y="user_rating")
df3 = df.copy()
df3["size_gigabytes"] = df["size_bytes"]/1000000000
df3.drop(columns=["id","track_name","currency","size_bytes","rating_count_tot","rating_count_ver","user_rating","cont_rating","prime_genre","sup_devices.num","ipadSc_urls.num","lang.num","vpp_lic","ver"])
df3["size_gigabytes"] = df3["size_gigabytes"].astype(float).round(1)
df3 = df3.groupby("size_gigabytes",as_index=False).mean()
df3.plot.scatter(x="size_gigabytes",y="user_rating_ver")
df5 = df.groupby("prime_genre",as_index=False).mean()
df5["genre_totals"] = [112,57,10,453,535,104,63,3862,180,144,23,138,46,75,349,178,64,122,167,114,81,248,72]
df5 = df5.drop([7])
print(df5.to_string())
df5.plot.scatter(x="genre_totals",y="user_rating")
plt.show()