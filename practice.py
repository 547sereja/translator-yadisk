import sys
import yadisk
import os
from os import stat, remove
import random


class YandexDiskOperations():
    def __init__(self):
        self.get_auth()
        self.dict_func = {'copy': self.copy, 'download': self.download, 'download_public': self.download_public,
                          'mkdir': self.mkdir, 'move': self.move, 'listdir': self.listdir,
                          'is_dir': self.is_dir, 'is_file': self.is_file, 'exists': self.exists, 'get_disk_info': self.get_disk_info,
                          'get_files': self.get_files, 'get_last_uploaded': self.get_last_uploaded, 'get_meta': self.get_meta,'get_public_resourses': self.get_public_resourses,
                          'upload': self.upload,
                          'encripto': self.encripto, 'decripto': self.decripto,
                          'get_trash_meta': self.get_trash_meta, 'get_trash_type': self.get_trash_type, 'remove_trash': self.remove_trash}

    def get_auth(self):
        self.y = yadisk.YaDisk("94885fad3a5e407b8cda5af348597aae", "59d96c74713947b9bad0f691dffb5699")
        url = self.y.get_code_url()
        # with open("data.txt", "rb") as token_txt:
        #    code = token_txt
        code = input('Enter a code: ')
        try:
            response = self.y.get_token(code)
            print('Connecting')
        except yadisk.exceptions.BadRequestError:
            print('Неверный код либо его срок жизни истек')
            sys.exit(1)
        self.y.token = response.access_token
        # print('n3')

        if self.y.check_token():
            print("Токен получен")
        else:
            print("Срок жизни токена истек, либо введён не правильно")

    def upload(self, from_, to_, *kwargs):
        try:
            with open(from_, "rb") as f:
                self.y.upload(f, to_)
        except:
            print('execution error')