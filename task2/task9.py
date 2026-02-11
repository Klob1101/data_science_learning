import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

titanic = sns.load_dataset('titanic')

df = titanic[['sex', 'embarked', 'survived', 'age']].copy()

df = df.dropna(subset = ['sex', 'embarked'])

df = df.groupby(['sex', 'embarked']).agg(survived_mean = ('survived', 'mean'), age_mean = ('age', 'mean')).reset_index()

ports = ['C', 'Q']
df = df[df['embarked'].isin(ports)]

pivot_table = df.pivot(index = 'sex', columns = 'embarked', values = 'survived_mean')
sex_list = pivot_table.index.tolist()
port_list = pivot_table.columns.tolist()

x = np.arange(len(sex_list))
width = 0.35

fig, ax = plt.subplots(figsize = (8, 5))

bars_c = ax.bar(
    x - width / 2,
    pivot_table['C'],
    width,
    label = 'Порт C'
)

bars_q = ax.bar(
    x + width / 2,
    pivot_table['Q'],
    width,
    label = 'Порт Q'
)

ax.set_title('Средняя выживаемость по полу и порту посадки')
ax.set_xlabel('Пол')
ax.set_ylabel('Средняя выживаемость')
ax.set_xticks(x)
ax.set_xticklabels(sex_list)

ax.legend(title = 'Порт посадки')
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f'{height:.2f}',
            xy = (bar.get_x() + bar.get_width() / 2, height),
            xytext = (0, 2),
            textcoords = "offset points",
            ha = 'center',
            #va = 'bottom'
        )

add_value_labels(bars_c)
add_value_labels(bars_q)

plt.tight_layout()
plt.show()