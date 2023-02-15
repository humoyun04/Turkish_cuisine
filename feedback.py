
def fedback():
    # Erros hatolarni oldini olib qoydim!
    try:
        baho = int(input("\tBizga 1 >> 5cha Baho bering: "))
        if baho >= 6:
            baxo = "\tBaholash chegarasi 5gacha kuuu!"
        elif baho <= 3:
            baxo = "\tKamtarano baho uchun Raxmat!"
        else:
            baxo = "\tSizga yoqganidan bahoyatda xursandmiz!😊😊"
    except ValueError:
        print("\tSiz raqam bilan baho bermadizku mijoz unday masda axir😏😏")

    # Faylga yozib qoydim
    with open("feedback.txt","w") as feedbak:
        feedbak.write(baxo)