import os
import pandas as pd
import matplotlib.pyplot as plt
from log import log_decorator

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)  

FILE_PATH = os.path.join(DATA_DIR, "personal_transactions.csv")


if not os.path.exists(FILE_PATH):
    df_test = pd.DataFrame({
        "Account Name": ["Visa", "MasterCard", "PayPal", "Visa", "MasterCard"],
        "Amount": [1500, 2000, 500, 1200, 1800],
        "Date": ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05"]
    })
    df_test.to_csv(FILE_PATH, index=False)
    print(f"Файл {FILE_PATH} создан с тестовыми данными.")

class GraphicalStatistics:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    @log_decorator()
    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        print("Данные загружены успешно.")

    @log_decorator()
    def plot_pie_chart(self):
        if self.df is None:
            raise ValueError("Данные не загружены. Используйте load_data().")
        # Группируем данные по 'Account Name' и суммируем расходы
        expense_data = self.df.groupby('Account Name')['Amount'].sum()
        plt.figure(figsize=(7, 7))
        expense_data.plot(kind='pie', autopct='%1.1f%%', startangle=0,
                          colors=['green', 'aliceblue', 'lightslategray'])
        plt.title("Траты по типу платежной системы")
        plt.ylabel("")  # Убираем подпись оси Y
        plt.show()

# Использование класса
stats = GraphicalStatistics(FILE_PATH)
stats.load_data()
stats.plot_pie_chart()
