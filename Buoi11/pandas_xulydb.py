import pandas as pd

# tao data ------------------------------------------------------------------
students_df = pd.DataFrame(
    {
        "Name": [
            "Nguyen Van A",
            "Tran Thi B",
            "Lam Van C",
            "Nguyen Thi D",
            "Chau Van E",
        ],
        "Point": [0, 0, 2.6, 5.9, 9.0],
        "Qualify": [True, False, False, False, True],
    }
)

# thay doi gia tri trong dataFrame -------------------------------------------
# thay the tung o --------------
# students_df.loc[1, "Point"] = 6.8
# print(students_df)
# students_df.iloc[0, 1] = 5.8
# print(students_df)

# at (label) ----------------------
# value = students_df.at[3, "Qualify"]
# print(value)

# iat (index) ---------------------
# students_df.iat[4, 0] = "Truong Thi F"
# value = students_df.iat[4, 0]
# print(students_df)

# replace(to_replace, value, [inplace=bool]) -------------------------
# inplace = True: thay doi (ghi de) len dataFrame cu
# inplace = False: tao dataFrame moi + chen du lieu thay doi
# students_df.replace([True, False], ['yes', 'no'], inplace=True)
# print(students_df)

# thay doi gia tri cua cot & dong --------------------------------------------
# them cot -------------------
# students_df["Gender"] = pd.Series([1, 0, 1, 0, 1])
# students_df["Gender"] = [1, 0, 1, 0, 1]
# print(students_df)

# xoa cot(drop(columns= ..., [inplace=bool])) --------------------
# inplace: mac dinh: False
# students_df.drop(columns=["Name", "Qualify"], inplace=True)
# print(students_df)

# them dong append(series/ dict, ignore_index = True)-------------------
# df = students_df.append({'Name': "Tran Van F", "Point": 10.0, "Qualify": False}, ignore_index=True)
new_row = pd.DataFrame({"Name": "Tran Van F", "Point": 10.0, "Qualify": False})
df = pd.concat(
    [students_df, new_row],
    ignore_index=True,
)
print(df)

# xoa dong (drop(index= ..., [inplace=bool])) --------------------
students_df.drop(index=[1, 3], inplace=True)
print(students_df)
