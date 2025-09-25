def is_leap_year():
    try:
        year_str = input("请输入年份：")
        year = int(year_str)
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print(f"{year} 是闰年")
        else:
            print(f"{year} 不是闰年")
    except ValueError:
        print(f"输入的 '{year_str}' 不是有效年份，请输入数字")

is_leap_year()
