def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
def main():
    print("=== 闰年判断程序 ===")
    
    while True:
        try:
            user_input = input("请输入年份（输入'q'退出程序）: ")
            
            if user_input.lower() == 'q':
                print("程序已退出，再见！")
                break
            
            year = int(user_input)
            
            if year <= 0:
                print("错误：请输入一个有效的正数年份！\n")
                continue
            
            if is_leap_year(year):
                print(f"{year}年是闰年！")
            else:
                print(f"{year}年不是闰年。")
            
            print() 
            
        except ValueError:
            print("错误：请输入有效的数字年份！\n")
        except Exception as e:
            print(f"发生未知错误：{e}\n")

if __name__ == "__main__":
    main()
