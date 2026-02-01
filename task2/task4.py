import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv"

df = pd.read_csv(url)

df['Date'] = pd.to_datetime(df['Date'], format = '%Y-%m-%d')

plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Temp'], label = 'Температура')
plt.title('Ежедневная температура')
plt.xlabel('Дата')
plt.ylabel('Температура, °C')
plt.grid(True, alpha = 0.25)
plt.legend()
plt.show()