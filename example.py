import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': 'ru'.format(to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


def main(file, lang):
    with open(input("enter how to save"), 'w', encoding='utf-8') as f:
        f.write(translate_it(file, lang))


if __name__ == '__main__':
    main(open(input("enter your file to open"), encoding='utf-8'), 'ru')