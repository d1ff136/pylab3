# Лабораторна робота №3
# Варіант 4
# Номери вправ: 1, 3, 6, 7, 8, 12, 13, 14, 15, 16, 17, 19, 20, 22, 24, 25, 26, 27

import os
import pandas as pd
import matplotlib.pyplot as plt



# Завдання №1. Завантаження набору даних


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, 'NationalNames.csv'))

print("-" * 10)
print("ЛАБОРАТОРНА РОБОТА №3")
print("Варіант 4")
print("-" * 10)

print("\nРозмір набору даних:")
print(df.shape)



# Завдання №2. Вправи - Варіант 4




# Вправа 1. Перші 8 рядків набору даних


print("\n" + "-" * 10)
print("Вправа 1. Перші 8 рядків набору даних")
print("-" * 10)

print(df.head(8))



# Вправа 3. Імена стовпців набору даних


print("\n" + "-" * 10)
print("Вправа 3. Імена стовпців набору даних")
print("-" * 10)

print(df.columns.tolist())



# Вправа 6. Кількість унікальних жіночих та чоловічих імен


print("\n" + "-" * 10)
print("Вправа 6. Кількість унікальних жіночих та чоловічих імен")
print("-" * 10)

n_female = df[df.Gender == 'F']['Name'].nunique()
n_male = df[df.Gender == 'M']['Name'].nunique()

print("Жіночих імен:", n_female)
print("Чоловічих імен:", n_male)



# Вправа 7. 5 найпопулярніших чоловічих імен у 2010 році


print("\n" + "-" * 10)
print("Вправа 7. 5 найпопулярніших чоловічих імен у 2010 році")
print("-" * 10)

top_5_male_2010 = (
    df[(df.Year == 2010) & (df.Gender == 'M')]
    .sort_values('Count', ascending=False)
    .head(5)
)

print(top_5_male_2010)



# Вправа 8. Найпопулярніше ім'я за результатами одного року


print("\n" + "-" * 10)
print("Вправа 8. Найпопулярніше ім'я за результатами одного року")
print("-" * 10)

most_popular = df.loc[df['Count'].idxmax()]

print("Рік:", most_popular['Year'])
print("Ім'я:", most_popular['Name'])
print("Стать:", most_popular['Gender'])
print("Кількість:", most_popular['Count'])



# Вправа 12. Найпопулярніше ім'я в році
# з найбільшою кількістю унікальних імен


print("\n" + "-" * 10)
print("Вправа 12. Найпопулярніше ім'я в році з найбільшою")
print("кількістю унікальних імен")
print("-" * 10)

unique_per_year = df.groupby('Year')['Name'].nunique()
year_max_unique = unique_per_year.idxmax()

print("Рік з найбільшою кількістю унікальних імен:", year_max_unique)
print("Кількість унікальних імен:", unique_per_year.max())

top_name_year_max_unique = (
    df[df.Year == year_max_unique]
    .sort_values('Count', ascending=False)
    .head(1)
)

print("\nНайпопулярніше ім'я цього року:")
print(top_name_year_max_unique)



# Вправа 13. Рік, коли ім'я "Jacob" було найпопулярнішим серед жіночих імен


print("\n" + "-" * 10)
print("Вправа 13. Рік, коли ім'я Jacob було найпопулярнішим")
print("серед жіночих імен")
print("-" * 10)

jacob_f = df[
    (df.Name == 'Jacob') &
    (df.Gender == 'F')
]

if not jacob_f.empty:
    jacob_f_max = jacob_f.loc[jacob_f['Count'].idxmax()]
    print("Рік:", jacob_f_max['Year'])
    print("Ім'я:", jacob_f_max['Name'])
    print("Стать:", jacob_f_max['Gender'])
    print("Кількість:", jacob_f_max['Count'])
else:
    print("Жіноче ім'я Jacob у наборі даних не знайдено.")



# Вправа 14. Рік із найбільшою кількістю гендерно нейтральних імен


print("\n" + "-" * 10)
print("Вправа 14. Рік із найбільшою кількістю")
print("гендерно нейтральних імен")
print("-" * 10)


def neutral_count(g):
    m = set(g[g.Gender == 'M']['Name'])
    f = set(g[g.Gender == 'F']['Name'])
    return len(m & f)


neutral_per_year = df.groupby('Year').apply(neutral_count)
year_max_neutral = neutral_per_year.idxmax()

print("Рік:", year_max_neutral)
print("Кількість гендерно нейтральних імен:",
    neutral_per_year.max())



# Вправа 15. Загальна кількість народжень за рік


print("\n" + "-" * 10)
print("Вправа 15. Загальна кількість народжень за рік")
print("-" * 10)

births_per_year = df.groupby('Year')['Count'].sum()

print(births_per_year)



# Вправа 16. Рік, коли народилося найбільше дітей


print("\n" + "-" * 10)
print("Вправа 16. Рік, коли народилося найбільше дітей")
print("-" * 10)

year_most_births = births_per_year.idxmax()

print("Рік:", year_most_births)
print("Кількість народжень:", births_per_year.max())



# Вправа 17. Кількість дівчаток та хлопчиків,
# які народились кожного року


print("\n" + "-" * 10)
print("Вправа 17. Кількість дівчаток та хлопчиків")
print("які народились кожного року")
print("-" * 10)

girls_boys_per_year = (
    df.groupby(['Year', 'Gender'])['Count']
    .sum()
    .unstack(fill_value=0)
)

print(girls_boys_per_year)



# Вправа 19. Графік загальної кількості народжень
# хлопчиків та дівчаток на рік


print("\n" + "-" * 10)
print("Вправа 19. Графік кількості народжень")
print("хлопчиків та дівчаток за роками")
print("-" * 10)

plt.figure(figsize=(10, 5))

plt.plot(
    girls_boys_per_year.index,
    girls_boys_per_year['F'],
    label='Дівчатка (F)'
)

plt.plot(
    girls_boys_per_year.index,
    girls_boys_per_year['M'],
    label='Хлопчики (M)'
)

plt.xlabel('Рік')
plt.ylabel('Кількість народжень')
plt.title('Кількість народжень хлопчиків та дівчаток за рік')
plt.legend()
plt.tight_layout()
plt.show()



# Вправа 20. Кількість гендерно-нейтральних імен
# у всьому наборі


print("\n" + "-" * 10)
print("Вправа 20. Кількість гендерно-нейтральних імен")
print("у всьому наборі")
print("-" * 10)

names_m = set(df[df.Gender == 'M']['Name'])
names_f = set(df[df.Gender == 'F']['Name'])

neutral_all = names_m & names_f

print("Кількість гендерно-нейтральних імен:",
      len(neutral_all))

print("\nПриклади гендерно-нейтральних імен:")
print(sorted(neutral_all)[:20])



# Вправа 22. Скільки років проводилось спостереження


print("\n" + "-" * 10)
print("Вправа 22. Кількість років спостереження")
print("-" * 10)

years_count = df['Year'].nunique()

print("Кількість років спостереження:", years_count)

print("Період:",
      df['Year'].min(),
      "-",
      df['Year'].max())



# Вправа 24. Найпопулярніше серед непопулярних імен


print("\n" + "-" * 10)
print("Вправа 24. Найпопулярніше серед непопулярних імен")
print("-" * 10)

min_count = df['Count'].min()

min_records = df[df['Count'] == min_count]

unpopular_names = min_records['Name'].unique()

totals = (
    df[df['Name'].isin(unpopular_names)]
    .groupby('Name')['Count']
    .sum()
    .sort_values(ascending=False)
)

print("Мінімальна кількість використань імені:",
      min_count)

print("\nНепопулярні імена з найбільшою сумарною кількістю:")
print(totals.head(5))



# Вправа 25. Графіки розподілення кількості імен John та Mary по роках без залежності від статі


print("\n" + "-" * 10)
print("Вправа 25. Графік розподілу імен John та Mary")
print("по роках, обидві статі разом")
print("-" * 10)

jm = (
    df[df['Name'].isin(['John', 'Mary'])]
    .groupby(['Year', 'Name'])['Count']
    .sum()
    .unstack(fill_value=0)
)

print(jm)

plt.figure(figsize=(10, 5))

plt.plot(
    jm.index,
    jm['John'],
    label='John'
)

plt.plot(
    jm.index,
    jm['Mary'],
    label='Mary'
)

plt.xlabel('Рік')
plt.ylabel('Кількість')
plt.title('Розподіл імен John та Mary по роках (обидві статі разом)')
plt.legend()
plt.tight_layout()
plt.show()



# Вправа 26. Графіки розподілення жіночих імен John та чоловічих імен Mary по роках


print("\n" + "-" * 10)
print("Вправа 26. Жіноче ім'я John та чоловіче ім'я Mary")
print("по роках")
print("-" * 10)

john_f = (
    df[
        (df.Name == 'John') &
        (df.Gender == 'F')
    ]
    .set_index('Year')['Count']
)

mary_m = (
    df[
        (df.Name == 'Mary') &
        (df.Gender == 'M')
    ]
    .set_index('Year')['Count']
)

print("\nJohn як жіноче ім'я:")
print(john_f)

print("\nMary як чоловіче ім'я:")
print(mary_m)

plt.figure(figsize=(10, 5))

plt.plot(
    john_f.index,
    john_f.values,
    label='John (жіноче)',
    marker='o'
)

plt.plot(
    mary_m.index,
    mary_m.values,
    label='Mary (чоловіче)',
    marker='o'
)

plt.xlabel('Рік')
plt.ylabel('Кількість')
plt.title("Жіноче ім'я John та чоловіче ім'я Mary по роках")
plt.legend()
plt.tight_layout()
plt.show()



# Вправа 27. Найпопулярніше ім'я в кожному році


print("\n" + "-" * 10)
print("Вправа 27. Найпопулярніше ім'я в кожному році")
print("-" * 10)

idx_per_year = df.groupby('Year')['Count'].idxmax()

top_per_year = (
    df.loc[
        idx_per_year,
        ['Year', 'Name', 'Gender', 'Count']
    ]
    .reset_index(drop=True)
)

print(top_per_year)