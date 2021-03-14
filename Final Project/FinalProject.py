import random  # To get questions randomly
import time  # to be able to wait
clear = "\n"*5  # Cleaning the screen after the competition is over is an experimental work :)


def questions_list():
    #  The function required to create our questions
    questions = []
    questions.append(["Türkiye'nin Başkenti Neresidir ?", "ankara"])
    questions.append(["İnegöl Hangi Yiyeceği İle Ünlüdür ?", "köfte"])
    questions.append(["Hava sıcaklığını ölçen, ısının birim derecesine adını veren cihazın adı nedir ?", "termometre"])
    questions.append(["Kurumuş Boğazım Sözleri İle Tanınan Ünlü Kimdir ?", "ömer cengiz"])
    questions.append(["Rumeli Hisarını Hangi Padişah Yaptırmıştır ?", "fatih sultan mehmet"])
    questions.append(["Ulvi Kelimesinin Türkçe Kökenli Eş Anlmalısı ?", "yüce"])
    questions.append(["Fransız İhtilali Hangi Yılda Başlamıştır ?", "1789"])
    questions.append(["Kuyucaklı Yusuf Adlı Eser Kime Aittir ?", "sabahattin ali"])
    questions.append(["Bir Elektrik Devresinde Direnç Hangi Harfle Gösterilir ?", "r"])
    questions.append(["Bir desimetre küp hacmindeki ölçü birimine ne ad verilir ?", "litre"])

    return questions


def final_score_check(player_point):
    # to calculate the success of the competitor
    if player_point > 50:
        print("Tebrikler Yarışmayı Başarı ile Tamamladınız")

    else:
        print("Maalesef Yarışmada Başarılı Olamadınız :(")
    time.sleep(1)
    print("Ana Menüye Yönlendiriliyorunuz...")
    time.sleep(3)
    print(clear)
    time.sleep(1)
    main_menu()

    return


def play_game():
    # required function to start our competition
    questionsList = questions_list()

    random.shuffle(questionsList)

    player_point = 0
    for q in questionsList:
        print(q[0])
        answer = input("lütfen cevabınızı Giriniz:")

        if answer.lower() == q[1]:
            print("Tebrikler Doğru Cevap!!\n")
            player_point += 10
        else:
            print("Maalesef Cevabınız Yanlış...\n")

    print("Final Skorunuz:", player_point)

    final_score_check(player_point)

    return


def main_menu():
    # a main menu to start, close the competition
    print("*****Bilgi Yarışmasına Hoşgeldiniz!!*****")
    time.sleep(.5)
    print("     Yarışmayı Başlatmak için(1)         ")
    time.sleep(.5)
    print("     Programı sonlandırmak için(2)       ")
    time.sleep(.5)
    secim = input("     Seçiminiz:")

    if secim == '1':
        print("Hazırsanız Birazdan Başlıyoruz...")
        time.sleep(1)
        print("Ufak Bir Hatırlatma...")
        time.sleep(1)
        print("Eğer Yarışmada Başarılı OLmak İstiyorsanız")
        time.sleep(1)
        print("50 Puanı Geçmelisiniz...")
        time.sleep(1)
        print("İşte İlk sorumuzla Başlıyoruz, Bol Şans...\n")
        time.sleep(1)
        play_game()
    elif secim == '2':
        print("Program Kapatılıyor")
        time.sleep(1)
        print("Yarışmak isterseniz tekrar bekleriz :)")
        exit()
    else:
        print("Hatalı Seçim Yaptınız!!")
        main_menu()

main_menu()
