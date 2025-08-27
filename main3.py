vazifalar = []

def menyu():
    print("\n=== Vazifa ilovasi ===")
    print("1 - Vazifa qo'shish")
    print("2 - Ro'yxatni ko'rish")
    print("3 - Vazifani o'chirish")
    print("0 - Chiqish")

def vazifa_qoshish():
    vazifa = input("Yangi vazifani kiriting: ")
    vazifalar.append(vazifa)
    print("Vazifa qo'shildi.")

def royxatni_korish():
    if not vazifalar:
        print("Vazifalar ro'yxati bo'sh.")
    else:
        print("\n--- Vazifalar ---")
        for i, v in enumerate(vazifalar, start=1):
            print(f"{i}. {v}")

def vazifa_ochirish():
    royxatni_korish()
    try:
        tanlov = int(input("O'chiriladigan vazifa raqamini kiriting: "))
        if 1 <= tanlov <= len(vazifalar):
            ochirilgan = vazifalar.pop(tanlov - 1)
            print(f"🗑️ '{ochirilgan}' o'chirildi.")
        else:
            print("Noto'g'ri raqam.")
    except ValueError:
        print("Raqam kiritishingiz kerak.")

def main():
    while True:
        menyu()
        tanlov = input("Tanlang: ")

        if tanlov == "0":
            print("Dasturdan chiqildi.")
            break
        elif tanlov == "1":
            vazifa_qoshish()
        elif tanlov == "2":
            royxatni_korish()
        elif tanlov == "3":
            vazifa_ochirish()
        else:
            print("Xato tanlov!")

if __name__ == "__main__":
    main()
