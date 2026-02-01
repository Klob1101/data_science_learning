import pandas as pd
import matplotlib.pyplot as plt

df_products = pd.DataFrame(columns=['Название', 'Категория', 'Цена', 'Количество продаж'])

df_products.loc[len(df_products)] = ['Keychron keyboard XXX', 'Device', 230, 9]
df_products.loc[len(df_products)] = ['Te guan yin', 'Tea', 30, 74]
df_products.loc[len(df_products)] = ['Da hong pao', 'Tea', 26, 57]
df_products.loc[len(df_products)] = ['Septolete', 'Medicine', 15, 22]
df_products.loc[len(df_products)] = ['Sven mouse RX', 'Device', 38, 5]
df_products.loc[len(df_products)] = ['Qi lan', 'Tea', 34, 10]
df_products.loc[len(df_products)] = ['Somic headset', 'Device', 180, 13]

df_products.info()

print(df_products.describe())

plt.figure(figsize = (10, 6))
plt.hist(df_products['Цена'], bins = 30, weights = df_products['Количество продаж'],
         edgecolor = 'black', alpha = 0.7, color = 'blue')
plt.title('Распределение цен на товары')
plt.xlabel('Цена')
plt.ylabel('Количество товаров')
plt.grid(True, alpha = 0.3)
plt.show()