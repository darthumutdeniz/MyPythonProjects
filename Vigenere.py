import datetime

def Vigenere_Sifrele(key, text, bool):

    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    lowerText = text.lower()
    lowerKey = key.lower() 
    anahtarNums = []
    textNums = []
    newTextNums = []
    newText = ""

    #Anahtarın sayısal değerini, metinin sayısal değerine eklemek için çıkaracağız.
    for key_harf in lowerKey:
        if key_harf in alfabe:
            anahtarNums.append(alfabe.index(key_harf))
        else:
            anahtarNums = anahtarNums
            print("Anahtarda harf dışında bir şey olamaz '" + key_harf + "' tolare edilmeyecektir")

    if anahtarNums == []:
        anahtarNums.append(0)

    for sifre_harf in lowerText:
        if sifre_harf in alfabe:
            textNums.append(alfabe.index(sifre_harf))
        else:
            textNums.append(sifre_harf + ".")

    #Anahtarın değeri ile metininkini topluyoruz.
    j = 0
    for i in range(len(textNums)):
        if textNums[i] in range(len(alfabe)):
            newTextNums.append(
                (int(textNums[i]) + (int(bool) *
                    (int(anahtarNums[j % len(anahtarNums)]))))
                        % len(alfabe))
            j += 1
        else:
            newTextNums.append(textNums[i])

    #Yeni metnin sayısal değerini harflere çeviriyoruz.
    for i in range(len(newTextNums)):
        if newTextNums[i] in range(len(alfabe)): 
            if text[i] == lowerText[i]:
                newText += alfabe[newTextNums[i]]
            else:
                newText += alfabe[newTextNums[i]].upper()
        else:
            newText += newTextNums[i][0]
        #print(i, " ", "(", key[i%len(key)], text[i%len(text)], print(newText[i]),")" ," ",newTextNums[i], end=" ")

    return newText

i = "true"
while i == "true":
    bool = input("Şifrele ya da çöz (Şifrelemek için '1' çözmek için '-1' giriniz.):")
    if bool == "1" or bool == "-1":
        text = str(input("Dosya Adı "))
        directory = "Günlük/"+text+".txt"
        with open(str(directory), encoding="utf8") as t:
            content = t.read()
            print(content)
            anahtar = input("Anahtar : ")
            i = "false"
            newText = Vigenere_Sifrele(anahtar,content,int(bool))
            print(newText)
            #t.write(newText)
    else:
        print("Ya bunu da düzgün yap be!")
        i = "true"
input("Programı kapatmak için enter'a basın.")