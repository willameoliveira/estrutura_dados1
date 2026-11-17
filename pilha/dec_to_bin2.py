def decimal_para_binario(num):
    if num == 0:
        return ""
    return decimal_para_binario(num // 2) + str(num % 2)

print(decimal_para_binario(13))