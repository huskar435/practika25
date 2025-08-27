import zadanie1 as z1
import zadanie2 as z2
import zadanie3 as z3

def main():
    user_choise = input('Введите 1 если zadanie1\nВведите 2 если zadanie2\nВведите 3 если zadanie3\nВвод:')
    if user_choise.lower() == '1':
        z1.main()
    elif user_choise.lower() == '2':
        z2.main()
    elif user_choise.lower() == '3':
        z3.main()
    else:
        print('не верно')
        main()


if __name__ == '__main__':
    main()