import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('mpg')

df.isnull().sum()

key_cols = ['mpg', 'horsepower', 'weight', 'acceleration', 'origin']

print("Amount of elements before:", len(df))
df = df.dropna(subset = key_cols)
print("Amount of elements after:", len(df))

sns.set_theme(style = 'darkgrid')

g = sns.pairplot(
    data = df,
    vars = ['mpg', 'horsepower', 'weight', 'acceleration'],
    hue = 'origin',
    diag_kind = 'hist',
    plot_kws = {'alpha': 0.7, 's': 40}
)
g.figure.suptitle('Pairplot: MPG, Horsepower, Weight, Acceleration', y = 1.02)

corr = df[['mpg', 'horsepower', 'weight', 'acceleration']].corr()

print(corr)

plt.figure(figsize=(6, 4))
sns.heatmap(
    corr,
    annot = True,
    cmap = 'coolwarm',
    fmt = '.2f',
    vmin = -1,
    vmax = 1
)
plt.title('Correlation heatmap')
plt.tight_layout()
plt.show()