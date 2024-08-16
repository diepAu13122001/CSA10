from data import col_list, province_list
import pandas as pd

# series ----------------
# 1 cot
# ser = pd.Series(["abc", "xyz", "mno"],index=["a", "b", "c"])
# data = {'c': 'abc', 'b': 'xyz', 'a': 'mno'} # dict
# ser = pd.Series(data=data, index=["a", "b", "c"])

# data = {"a": -1.3, "b": 11.7, "d": 2.0, "f": 10, "g": 5}
# ser = pd.Series(data, index=["a", "c", "b", "d", "e", "f"])
# print(ser[-3::]) # start, stop, step

# dataFrames -------------
# data = pd.DataFrame(data=province_list, columns=col_list)
# print(data)

data = pd.DataFrame(
    data=[
        ("abc", "abc", "abc", 7929.5, 858.1),
        ("abc", "abc", "abc", 6700.3, 530.9),
        ("abc", "abc", "abc", 4860.0, 314.4),
    ],
    columns=col_list,
)
print(data)

# luu vao xls
data.to_excel(excel_writer="Lab9/province.xlsx", index=False)
# data.to_excel("Lab9/province.xlsx")
