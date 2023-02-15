# Faylarni import qilish!
from restaurant_places import *
from menu_foods import *
from feedback import *

#Bu yerda funksiya yaratildi jarayonni barchasi shu yerda toplandi!.
def kirish():
    print('''
    ..............................................
    .........................................
    ....................................
    ................................
    
    Assalomu alaykum Turk_oshxonasi Restaraniga ga xush kelibsiz !
                                        
     ..............................................
         .......................................... 
               .................................... 
                   ................................''')

    # Errors xatolarni ushlash user o'zining otirish joyini raqamini kritmasa!
    try:
        print("Restaranda 50 ta stol bor adashab ketmang kiritishda!")
        num = int(input("Buyurtma nechanchi stoldan: "))
    except ValueError:
        print("Iltimos stol raqamini tog'ri kritilganini tekshirib qoying!")
        return

    if deliver(num) == True:
        pass
    else:
        return

    name = input("Ismingiz: ")
    if len(name) == 0 :
        print("Ismingizni kritmadingiz!")
        return
    else:
        pass

    print(f"Menu bilan avval Taomlar nomi va narxi bilan tanishib chiqishingiz  mumkun marhamat Mr {name} ")
    foods()

    # Errors xatolarni ushlash agar taomni nomi kritilmasa!
    try:
        foo = int(input("Taomni nomini menu bo'yicha raqamini kriting: "))
        if foo >= 10 or foo == 0:
            print("Menuda mavjud mas bunday raqam!")
            return
        else:
            pass
    except ValueError:
        print("Iltimos taomni raqamini menu bo'yicha tog'ri kritganizni tekshrib qoying!")
        return

    print(f"Salatlar bilan hohlasingiz tanishib chiqishingiz mumkun Mr {name}")
    salats()

    # Errors xatolarni ushlash agar salatni nomi kritilmasa!
    try:
        sal = int(input("Salatni nomini menu bo'yicha raqamini kriting: "))
        if sal >= 6 or sal == 0:
            print("Menuda mavjud mas bunday raqam!")
            return
        else:
            pass
    except ValueError:
        print("Iltimos # Errors xatolarni ushlash agar salatni nomi kritilmasa!salatni raqamini menu bo'yicha tog'ri kritganizni tekshrib qoying!")
        return

    print(f"Ichimliklar bilan hohlasingiz tanishib chiqishingiz mumkun Mr {name}")
    drinks()

    # Errors xatolarni ushlash agar ichimlikni nomi kritilmasa!
    try:
        drink = int(input("Ichimlikni nomini menu bo'yicha raqamini kriting: "))
        if drink >= 5 or drink == 0:
            print("Menuda mavjud mas bunday raqam!")
            return
        else:
            pass
    except ValueError:
        print("Iltimos ichimlikni raqamini menu bo'yicha tog'ri kritganizni tekshrib qoying!")
        return

    print(f"Desertlar bilan hohlasingiz tanishib chiqishingiz mumkun Mr {name}")
    deserts()

    # Errors xatolarni ushlash agar desertni nomi kritilmasa!
    try:
        desert = int(input("Desertni nomini menu bo'yicha raqamini kriting: "))
        if desert >= 8 or desert == 0:
            print("Menuda mavjud mas bunday raqam!")
            return
        else:
            pass
    except ValueError:
        print("Iltimos desetni raqamini menu bo'yicha tog'ri kritganizni tekshrib qoying!")
        return

    # Dictionarydan user kritgan raqamdagi taomni nomini olish!
    eda = taom[foo]
    for ind,val in enumerate(eda):
        eda_n = val[0]
        price_eda = val[1]

    # Dictionarydan user kritgan raqamdagi ichimlikni nomini olish!
    napitok = ichimlik[drink]
    for ind,val in enumerate(napitok):
        napitok_n = val[0]
        price_napitok = val[1]

    # Dictionarydan user kritgan raqamdagi salatni nomini olish!
    salati = salat[sal]
    for ind,val in enumerate(salati):
        salat_n = val[0]
        price_salat = val[1]

    # Dictionarydan user kritgan raqamdagi desertni nomini olish!
    deserti = shrinlik[desert]
    for ind,val in enumerate(deserti):
        desert_n = val[0]
        price_desert = val[1]

    # Umumiy narxlar!
    stack = price_eda + price_salat + price_napitok + price_desert

    # Ma'lumotlar bilan ishlash
    #    Ma'lumotlarni faylga yozish jarayoni.
    with open("check.txt", "w") as file:
        file.writelines(f"\n\t\tJoy: {num},\n\t\tIsm: {name},\n\t\tTaom: {eda_n} - Narx: ${price_eda},\n\t\tSalat: {salat_n} - Narx: ${price_salat},\n\t\tIchimlik: {napitok_n} - Narx: ${price_napitok},\n\t\tDesert: {desert_n} - Narx: ${price_desert}.\n")
        file.writelines(f"\n\t\tMr {name} sizdan umumiy xisob = ${stack} bo'ldi.\n\n")

    #   Ma'lumotlarni fayldan fayl o'qish.
    with open("check.txt","r") as fayl:
        print('''
                .......................
                Marhamt checkingiz Janob!

                >>>>   Check   <<<<''')
        print(fayl.read())
        print(f"\t\tTashakkur bildiramiz yana kelishingizni kutib qolamiz Mr {name}")

    # Feedback
    fedback()

kirish()