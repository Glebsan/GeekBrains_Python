import googletrans

translator = googletrans.Translator()
with open('eng_numbers.txt', encoding='UTF-8') as txt:
    for i in txt:
        a = translator.translate(txt.readline(), dest = 'ru')
        print(a.text)

