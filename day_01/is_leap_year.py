def is_leap_year(year):
    if isinstance(year, int) is not True:  # isinstance  返回参数是否为已知类型，相同则返回True，否则返回false
        raise TypeError("传入参数非整数")
    elif year == 0:
        raise ValueError("公元元年是从公元一年开始的")
    elif abs(year) != year:  # abs 返回参数绝对值
        raise ValueError("传入的参数不是正整数")
    elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        print("%d年是闰年" % year)
        return True
    else:
        print("%d年不是闰年" % year)
        return True