def time_conversion(hrs):
    s_value = sec % (24 * 3600)
    hr_value = s_value // 3600
    sec_value %= 3600
    min = s_value // 60
    s_value %= 60
    print("Converted sec value in hour:", hr_value)
    print("Converted sec value in minutes:", min)