# Импорт класса
from octagon import Octagon as cl


# Функция main
def main():
    user_octagon=cl(float(input('Введите длину стороны правильного восьмиугольника: \n')))
    user_octagon.info_R_in_s1()
    user_octagon.info_R_out_s2()
    user_octagon.info_P_S() 
    user_octagon.draw_octagon()

if __name__ == '__main__':
    main()


