meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }
word = input("неизвестное вам слово(БОЛЬШИМИ БУКВАМИ!):")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("я не знаю токого слова")
