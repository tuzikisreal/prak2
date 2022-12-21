import os
import sys
import shutil
import dir_path

path = ""
dir_path.start()


def help():
    print("*** Синтаксис: команда атрибут1 атрибут2 *** \n"
          "\n"
          "Команды: \n"
          "* help - справка по командам \n"
          "* current_dir - показать текущую директорию  \n"
          "* create_folder имя папки - создать папку \n"
          "* del_folder имя папки - удалить папку \n"
          "* change_dir_d имя директроии - перемещение в директории на уровень ниже \n"
          "* change_dir_up - сперемещение в директории на уровень выше \n"
          "* make_file имя файла - создать пустой файл \n"
          "* write_file имя файла - записать текст в файл \n"
          "* read_file имя файла - посмотреть содержимое файла \n"
          "* del_file имя файла - удаление файла \n"
          "* copy_file имя_файла путь - копировать файл в другую папку \n"
          "* move_file имя_файла путь - переместить файл \n"
          "* rename_file текущее имя, новое имя - переименовать файл \n"
          "* exit - выход \n")


def current_dir():
    print(os.getcwd())


def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print('Такая папка уже существует')


def del_folder(folder_name):
    try:
        os.rmdir(folder_name)
    except FileNotFoundError:
        print('Такой папки не существует')


def make_file(file_name):
    file = open(file_name, "w+")
    file.close()


def write_file(file_name, w):
    try:
        f = open(file_name, "a")
        f.write(w)
        f.close()
    except FileExistsError:
        print('Такого файла не существует')


def read_file(file_name):
    try:
        file = open(file_name, "r")
        print(file.read())
        file.close()
    except FileExistsError:
        print('Такого файла не существует')


def del_file(file_name):
    try:
        os.remove(file_name)
    except FileExistsError:
        print('Такого файла не существует')


def copy_file(file_name, new_file_name):
    try:
        shutil.copy(file_name, new_file_name)
    except FileExistsError:
        print('Такого файла не существует')


def move_file(file_name, new_path):
    try:
        shutil.move(file_name, path + new_path)
    except FileExistsError:
        print('Такого файла не существует')


def rename_file(file_name, new_file_name):
    try:
        os.rename(file_name, new_file_name)
    except FileExistsError:
        print('Такого файла не существует')


def change_dir_d(dir_name):
    try:
        OS = sys.platform
        if OS == 'darwin':
            a = os.getcwd()
            os.chdir(a + '/' + dir_name)
            print(os.getcwd())

        elif OS == 'cygwin' or OS == 'win32':
            a = os.getcwd()
            os.chdir(a + '\\' + dir_name)
            print(os.getcwd())
    except FileNotFoundError:
        print('Такой директории нет')


def change_dir_up():
    z = os.getcwd()
    if len(os.path.split(os.getcwd())[0]) < len(path):
        print('Выход за пределы рабочей папки')
    elif len(os.path.split(os.getcwd())[0]) <= len(z) or len(os.path.split(os.getcwd())[0]) + 1 <= len(z):
        OS = sys.platform
        # print(OS)
        if OS == 'darwin':
            a = os.getcwd()
            b = a.split('/')
            del b[-1]
            a = '/'.join([str(item) for item in b])
            os.chdir(a)
            print(os.getcwd())

        elif OS == 'cygwin' or OS == 'win32':
            a = os.getcwd()
            b = a.split('\\')
            del b[-1]
            a = '\\'.join([str(item) for item in b])
            os.chdir(a)
            print(os.getcwd())
    else:
        print("Невозможно перейти в директорию")
        print(os.getcwd())

