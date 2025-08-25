from vehicle import Vehicle, Car

def main():
    print("Введите название бренда:")
    brand = input()
    print("Введите название модели:")
    model = input()
    print("Введите год выпуска:")
    year = input()

    print("Введите тип топлива (бензин или дизель):")
    fuel_type = input()
    print("Введите максимальную скорость (км/ч):")
    max_speed = float(input())
    print("Введите объём двигателя (л):")
    engine_capacity = float(input())
    print("Введите частоту вращения (об/мин):")
    rotation_speed = float(input())

    # Создаём объект класса Vehicle
    vehicle = Vehicle(brand, model, year)
    print("\n--- Информация о транспорте ---")
    vehicle.info()

    # Создаём объект класса Car
    car = Car(brand, model, year, fuel_type, max_speed, engine_capacity, rotation_speed)
    print("\n--- Информация об автомобиле ---")
    car.info()
    car.engine_power_calc()


if __name__ == "__main__":
    main()
