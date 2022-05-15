data = "Hello World"
print(data)

data = """
テスト
テスト
"""

print(data)

month = "2019-08"
data = month.split("-")
print(data)

# リスト
data = ["apple","orange","banana"]
print(data[0])

print(data[-1])

data.append("melon")

print(data)

data.remove("banana")

print(data)

data = ["apple","orange","banana","melon"]
print

print(data[1:2])
print(data[1:4])
print(data[1:])
print(data[2:])
print(data[:3])

data[1] = "cherry"
print(data)

# タプル
#
# イミュータブル
data = (11)
print(type(data))

data = (11,)
print(type(data))

# セット
#
# 順番を持たない
# ユニークの要素しか保持しない
data = {"apple", "orange", "banana"}
print(data)

