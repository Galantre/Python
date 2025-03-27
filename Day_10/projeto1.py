def is_leap_year(year):
# Write your code here.
# Don't change the function name.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                ehounao = True
                return ehounao
            else:
                ehounao = False
                return ehounao
        else:
            ehounao = True
            return ehounao
    else:
        ehounao = False
        return ehounao
print(is_leap_year(2025))