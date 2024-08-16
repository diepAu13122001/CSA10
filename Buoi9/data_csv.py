import pandas as pd

# nhap file csv
# df = pd.read_csv('Buoi9/pokemon_data.csv')
# print(df.head())
# print("-------------------")
# print(df.tail())

# tu tao dataframe thong qua dictionary (dict)
# df = pd.DataFrame(
#     {
#         "Name": ["Anastasia", "Dima", "Katherine"],
#         "Score": [12.5, 9.0, 16.5],
#         "Attemps": [1, 3, 2],
#     }
# )

# print(df)
# # xuat file csv
# df.to_csv("new.csv")

#  ve du lieu len bang do (cho so - 2D)
import matplotlib.pyplot as plt

df = pd.read_csv("Buoi9/pokemon_data.csv")

plt.figure(figsize=(10, 6))

plt.plot(df["Name"], df["HP"], marker="o")
plt.title("HP")
plt.ylabel("HP")  # nhan truc Y
plt.xlabel("Name")  # nhan truc X

plt.grid(True)  # hien thi luoi trong bang do
plt.show()
