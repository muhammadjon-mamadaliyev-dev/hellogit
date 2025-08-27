def menyu():
    print("\n=== Vazifa ilovasi ===")
    print("1 - Vazifa qo'shish")
    print("2 - Ro'yxatni ko'rish")
    print("3 - Vazifani o'chirish")
    print("0 - Chiqish")

def main():
    while True:
        menyu()
        tanlov = input("Tanlang: ")

        if tanlov == "0":
            print("Dasturdan chiqildi.")
            break
        elif tanlov == "1":
            print("Vazifa qo'shish funksiyasi hali ishlamaydi")
        elif tanlov == "2":
            print("Ro'yxatni ko'rish funksiyasi hali ishlamaydi")
        elif tanlov == "3":
            print("O'chirish funksiyasi hali ishlamaydi")
        else:
            print("Xato tanlov")

if __name__ == "__main__":
    main()
