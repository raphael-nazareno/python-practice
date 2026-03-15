chinese_dynasty = ""
japanese_period = ""
year = int(input("Pick a year in history: "))

if year > 1279 and year <= 1368:
    chinese_dynasty = "Yuan"
elif year > 1368 and year <= 1644:
    chinese_dynasty = "Ming"
elif year > 1644 and year <= 1912:
    chinese_dynasty = "Qing"
else:
    chinese_dynasty = ""

if year > 1600 and year <= 1868:
    japanese_period = "Edo"
else:
    japanese_period = ""

year = str(year)

if chinese_dynasty:
    print(chinese_dynasty + " dynasty in China")
else:
    print("No offically recorded Chinese dynasty in " + year)

if japanese_period:
    print(japanese_period + " period in Japan")
else:
    print("No offically recorded Japanese period in " + year)