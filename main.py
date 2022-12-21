import functions

print('*** Справку по командам можно вызвать через ENTER или командой help ***')
while True:
    command = input('Введите команду: ')
    command = command.split(' ')
    if command[0] == 'exit':
        break

    elif command[0] == 'help' or command[0] == '':
        functions.help()

    elif command[0] == 'current_dir':
        functions.current_dir()

    elif command[0] == 'create_folder':
        functions.create_folder(command[1])

    elif command[0] == 'del_folder':
        functions.del_folder(command[1])

    elif command[0] == 'change_dir_d':
        functions.change_dir_d(command[1])

    elif command[0] == 'change_dir_up':
        functions.change_dir_up()

    elif command[0] == 'make_file':
        functions.make_file(command[1])

    elif command[0] == 'write_file':
        contentWrap = input("Введите текст: ")
        functions.write_file(command[1], contentWrap)

    elif command[0] == 'read_file':
        functions.read_file(command[1])

    elif command[0] == 'del_file':
        functions.del_file(command[1])

    elif command[0] == 'copy_file':
        functions.copy_file(command[1], command[2])

    elif command[0] == 'move_file':
        functions.move_file(command[1], command[2])

    elif command[0] == 'rename_file':
        functions.rename_file(command[1], command[2])

    else:
        print('Такой команды нет. Попробуйте еще раз или воспользуйтесь справкой команд (help)')
