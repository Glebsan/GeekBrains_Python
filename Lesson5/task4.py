# Почемуто не принтит первую строку
# import googletrans
#
# translator = googletrans.Translator()
# with open('eng_numbers.txt', encoding='UTF-8') as txt:
#     for i in txt:
#         a = translator.translate(txt.read(), dest='ru')
#         print(a.text)

with open('translate.txt', encoding='UTF-8') as txt:
    text = txt.readlines()
    print(text)

with open('translate_rus.txt', 'w', encoding='UTF-8') as txt:
    for i in text:
        if 'One' in i:
            text = i.replace('One', 'Один')
        elif 'Two' in i:
            text = i.replace('Two', 'два')
        elif 'Three' in i:
            text = i.replace('Three', 'Три')
        elif 'Four' in i:
            text = i.replace('Four', 'Четыре')
        txt.write(text)
