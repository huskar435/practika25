# Импорт нужных библиотек
import matplotlib.pyplot as plt
import math


# Класс
class Octagon:

    # Конструктор
    def __init__(self,side):
        self.angle=math.pi / 4
        self.constant=1+2**0.5
        self.side=side

    # Подсчет радиуса и площади вписанной окружности
    def info_R_in_s1(self):
        R_in=self.side*0.5*self.constant
        s1=3.14*R_in**2
        print(f'Радиус и площадь вписанной окружности соответсвенно равны: {round(R_in,2)} и {round(s1,2)}')

    # Подсчет радиуса и площади описанной окружности
    def info_R_out_s2(self):
        R_out=self.side/(2-2**0.5)**0.5
        s2=3.14*R_out**2
        print(f'Радиус и площадь описанной окружности соответсвенно равны: {round( R_out,2)} и {round(s2,2)}')

    # Подсчет периметра и площади октагона
    def info_P_S(self):
        P=self.side*8
        S=2*self.side**2*self.constant
        print(f'Площадь и периметр октагона соответсвенно равны: {round(S,2)} и {P}')

    # Построение графика
    def draw_octagon(self):
        R_out = self.side/(2-2**0.5)**0.5  
        R_in = self.side*0.5*self.constant  
        
        x = [R_out * math.cos(i * self.angle) for i in range(8)]
        y = [R_out * math.sin(i * self.angle) for i in range(8)]
        
        x.append(x[0])  
        y.append(y[0])
        
        fig, ax = plt.subplots(figsize=(6, 6))
    
        ax.plot(x, y, 'bo-', markersize=8, label='Восьмиугольник')
        ax.fill(x, y, alpha=0.3)
        
        circle_out = plt.Circle((0, 0), R_out, color='r', fill=False, linestyle='dashed', label='Описанная окружность')
        ax.add_patch(circle_out)
        
        circle_in = plt.Circle((0, 0), R_in, color='g', fill=False, linestyle='dashed', label='Вписанная окружность')
        ax.add_patch(circle_in)

        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid(True, linestyle='--', linewidth=0.5)
        ax.set_aspect('equal')
        ax.legend()
        plt.xlim(-R_out - 1, R_out + 1)
        plt.ylim(-R_out - 1, R_out + 1)
        plt.show()
    
    # Деструктор
    def __del__(self):
        pass