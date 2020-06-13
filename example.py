import requests

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'


def translate_me(open_file, save_file,  language):
    with open(open_file, encoding='utf-8') as file_text:
        params = {
            'key': API_KEY,
            'text': file_text,
            'lang': 'ru'.format(language),
        }

        response = requests.get(URL, params=params)
        json_ = response.json()
        to_write = ''.join(json_['text'])
    with open(save_file, 'w', encoding='utf-8') as saved_file:
        saved_file.write(to_write)


translate_me('DE.txt', 'translated.txt', 'ru')

# def open_file(file):
#     with open(file, encoding='utf-8') as text:
#         return text
















#     def save_name(file):
#         with open(input("Enter file name to save"), 'w', encoding='utf-8') as f:
#             f.write(translated)
#
#
#
# # def save_name(file):
# #     with open(input("Enter file name to save"), 'w', encoding='utf-8') as f:
# #         f.write(translate_it(file))
#
#
# def open_file():
#     with open(input("Enter file name to open"), encoding='utf-8') as text:
#         return text




# if __name__ == '__main__':
#     main(open(input("enter your file to open"), encoding='utf-8'), 'ru')
