import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_products = pd.DataFrame(columns = ['Название', 'Категория', 'Цена', 'Количество продаж'])

df_products.loc[len(df_products)] = ['Keychron keyboard XXX', 'Device', 230, 9]
df_products.loc[len(df_products)] = ['Te guan yin', 'Tea', 30, 74]
df_products.loc[len(df_products)] = ['Da hong pao', 'Tea', 26, 57]
df_products.loc[len(df_products)] = ['Septolete', 'Medicine', 15, 22]
df_products.loc[len(df_products)] = ['Sven mouse RX', 'Device', 38, 5]
df_products.loc[len(df_products)] = ['Qi lan', 'Tea', 34, 10]
df_products.loc[len(df_products)] = ['Somic headset', 'Device', 180, 13]

category_sales = df_products.groupby('Категория', as_index = False)['Количество продаж'].sum()

colors = ["#0c7bc5", "#cb07ce", "#00da07"]

sns.set_style("whitegrid")
sns.barplot(data = category_sales, x = 'Категория', y = 'Количество продаж', errorbar = None, palette = colors)
plt.title('Продажи по категориям')
plt.show()