def is_palin(sinp):
    if sinp == sinp[::-1]:
        return True
    else:
        return False
    
sinp = input("Введите строку: ")
print(is_palin(sinp))