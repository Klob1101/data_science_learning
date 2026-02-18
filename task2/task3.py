import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('titanic')

missing = df.isnull().sum()
print(missing[missing > 0])

mean_age = df['age'].mean()
df['age'] = df['age'].fillna(mean_age)
print(f"\nMedian age: {mean_age}")
print(f"Number of missings in age: {df['age'].isnull().sum()}")

plt.figure(figsize = (10, 6))
sns.boxplot(data = df, x = 'pclass', y = 'age')
plt.title('Распределение возраста по классам пассажиров (после импутации)')
plt.xlabel('pclass')
plt.ylabel('age')
plt.tight_layout()
plt.show()