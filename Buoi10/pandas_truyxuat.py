import pandas as pd

df = pd.read_excel("Buoi10/pokemon_data.xlsx")
# cu phap thong thuong (slice) ---------------
# 1 cot => series
# data = df.Name # cach 1 - biet truoc thuoc tinh
# data = df["HP"] # cach 2 - co the tuy chinh thuoc tinh
# print(data.head(10))
# print(type(data))

# 1 hang => dataFrame
# data = df[4:5]
# print(data)
# print(type(data))

#  nhieu hang => dataFrame
# [start:stop - 1:step]
# data = df[4:30:5]
# print(data)
# print(type(data))

# nhieu cot => dataFrame
# data = df[["Name", "HP"]]
# print(data.head(3))
# print(type(data))

# truy xuat bang "loc" ------------------
# loc: duoc goi bang label (column)
# 1 cot => series
# data = df.loc[:, "Name"]
# print(data.head(3))
# print(type(data))

# 1 hang => Series
# data = df.loc[10]
# print(data)
# print(type(data))

# 1 o => phu thuoc vao kieu du lieu cua o
# data = df.loc[10, "HP"]
# print(data)
# print(type(data))

# nhieu cot => dataFrame
# data = df.loc[:, "HP":"Speed"]  # lay lien tuc
# print(data.head(2))
# data = df.loc[:, ["HP", "Speed"]] # lay tung cot cu the
# print(data.head(2))

# nhieu hang => dataFrame
# data = df.loc[1:3]
# print(data)


# nhieu cot + nhieu hang
# print(df.loc[5:50:10, ["HP", "Attack"]])

# truy xuat bang "iloc" ------------------
# iloc: duoc goi bang location (index column)
# 1 cot => series
# data = df.iloc[:, 1]
# print(data.head(3))
# print(type(data))

# # 1 hang => Series
# data = df.iloc[10]
# print(data)
# print(type(data))

# # 1 o => phu thuoc vao kieu du lieu cua o
# data = df.iloc[10, 3]
# print(data)
# print(type(data))

# # nhieu cot => dataFrame
# data = df.iloc[:, 1:5]  # lay lien tuc
# print(data.head(2))
# data = df.iloc[:, [5, 11]] # lay tung cot cu the
# print(data.head(2))

# # nhieu hang => dataFrame
# data = df.iloc[1:3]
# print(data)

# # nhieu cot + nhieu hang => dataFrame
# print(df.iloc[5:50:10, [9, 10]])

# tong ket du lieu -------------------------------------
# print(df["HP"].describe())
# print("sum", df.HP.sum())
# print("value counts", df.Legendary.value_counts())

# truy xuat co dieu kien ----------------------
# in ra ten cua poke co hp > 150
# filtered_df = df[df.HP > 150]
# print(filtered_df.Name)

# in ra poke co ten = Chansey
filtered_df = df[df.Name == "Chansey"]
print(filtered_df)