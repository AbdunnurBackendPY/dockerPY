s = input("Введите строку: ")
w = s.split()
sw = sorted(w, key=len)
print(" ".join(sw))