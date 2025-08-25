# Родительский класс
class Vehicle:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Выводим информацию
    def info(self):
        print("Название бренда:", self.brand)
        print("Название модели:", self.model)
        print("Год выпуска:", self.year)


# Дочерний класс
class Car(Vehicle):

    def __init__(self, brand, model, year, fuel_type, max_speed, engine_capacity, rotation_speed):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type.lower()
        self.max_speed = max_speed
        self.engine_capacity = engine_capacity
        self.rotation_speed = rotation_speed

    def info(self):
        super().info()
        print(f"Тип топлива: {self.fuel_type}")
        print(f"Максимальная скорость: {self.max_speed} км/ч")
        print(f"Объём двигателя: {self.engine_capacity} л")
        print(f"Частота вращения: {self.rotation_speed} об/мин")

    # Расчёт мощности по объёму
    def engine_power_calc(self):
        # коэффициенты для разных топлив
        pe_values = {
            "бензин": 0.85,
            "дизель": 1.0
        }
        # берём коэффициент, если неизвестный тип → ставим 0.9
        pe = pe_values.get(self.fuel_type, 0.9)

        Ne = (self.engine_capacity * pe * self.rotation_speed) / 120
        print(f"Мощность по объёму = {Ne:.2f} кВт")


