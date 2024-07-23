def Sezar_Sifrele(slide_num, text):
    alfabe = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
    lowerText = text.lower()
    newText = ""
    for sifre_harf in lowerText:
        if sifre_harf in alfabe:
            for harf in range(0, len(alfabe)):
                if sifre_harf == alfabe[harf]:
                    newIndex = (harf + int(slide_num)) % len(alfabe)
                    newNumber = alfabe[newIndex]
                    newText = newText + newNumber
        else:
            newText += sifre_harf
    return newText

elma = input("metin ")
kaydır = int(input("kaydır "))
print(Sezar_Sifrele(kaydır, elma))
input()