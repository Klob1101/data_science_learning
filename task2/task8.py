import seaborn as sns
import matplotlib.pyplot as plt

diamonds = sns.load_dataset('diamonds')

diamonds_sample = diamonds.sample(n = 1000)

fig, axes = plt.subplots(1, 3, figsize = (14, 5), gridspec_kw = {'width_ratios': [1, 1.7, 1]})

axes[0].hist(diamonds_sample['price'], bins = 50, color = 'steelblue', edgecolor = 'black')
axes[0].set_title('Распределение цены')
axes[0].set_xlabel('Цена')
axes[0].set_ylabel('Количество')

sns.boxplot(
    data = diamonds_sample,
    x = 'cut',
    y = 'price',
    ax = axes[1]
)
axes[1].set_title('Цена по качеству огранки')
axes[1].set_xlabel('Качество огранки')
axes[1].set_ylabel('Цена')

scatter = sns.scatterplot(
    data = diamonds_sample,
    x = 'carat',
    y = 'price',
    hue = 'clarity',
    size = 'depth',
    sizes = (20, 200),
    alpha = 0.7,
    ax = axes[2]
)
axes[2].set_title('Зависимость цены от веса карата')
axes[2].set_xlabel('Вес')
axes[2].set_ylabel('Цена')

handles, labels = axes[2].get_legend_handles_labels()
axes[2].legend(
    handles = handles,
    labels = labels,
    title = 'Ясность и глубина',
    loc = 'upper left',
    bbox_to_anchor = (1.02, 1.0),
    borderaxespad = 0
)

fig.suptitle('Анализ цен на бриллианты', fontsize = 14)

plt.tight_layout(rect = [0, 0, 0.95, 0.95])
plt.show()
