import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

tips['size'] = tips['size'].astype('category')

fig, axes = plt.subplots(1, 2, figsize = (14, 6))

axes[0].hist(tips['total_bill'], bins = 20, color = 'blue', edgecolor = 'black')
axes[0].set_title('Распределение суммы счета')
axes[0].set_xlabel('Сумма счета')
axes[0].set_ylabel('Количество наблюдений')
axes[0].grid(True, alpha = 0.25)

sns.scatterplot(
    data = tips,
    x = 'total_bill',
    y = 'tip',
    hue = 'sex',
    ax = axes[1]
)

axes[1].set_title('Зависимость чаевых от суммы счета')
axes[1].set_xlabel('Сумма счета')
axes[1].set_ylabel('Чаевые')
axes[1].legend(title='Пол')
axes[1].grid(True, alpha = 0.25)

plt.show()