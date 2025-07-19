import datetime
today = datetime.datetime.today()
print(f"{today:%Y-%m-%d}")
# 2022-03-11
print(f"{today:%Y}")
# 2022
x = 10
y = 25
print(f"x = {x}, y = {y}")
# x = 10, y = 25
print(f"{x = }, {y = }")  # Лучше! (3.8+)
# x = 10, y = 25

print(f"{x = :.3f}")
