import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

iris = pd.concat([iris, iris.iloc[:3], iris.iloc[:3]], ignore_index = True)

dup_mask = iris.duplicated(keep = 'first')
print("Amount of duplicates:", dup_mask.sum())
print("Table with all duplicates:\n", iris[dup_mask])
iris = iris.drop_duplicates(keep = 'first')

plt.figure(figsize = (10, 6))
sns.scatterplot(
    data = iris,
    x = 'petal_length',
    y = 'sepal_length',
    hue = 'species',
    palette = 'Set1'
)
plt.title('Зависимость длины чашелистика от длины лепестка')
plt.xlabel('Длина лепестка')
plt.ylabel('Длина чашелистика')
plt.legend(title = 'Вид ириса')
plt.grid(True)
plt.tight_layout()
plt.show()
