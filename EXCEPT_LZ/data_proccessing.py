import pandas as pd
from pandas.errors import EmptyDataError

class Data_Processing:
    def __init__(self, main_file, empty_file_check, missing_file_check):
        self.main_file = main_file
        self.empty_file_check = empty_file_check
        self.missing_file_check = missing_file_check
     
    def check_file_existence(self):
        try:
            pd.read_csv(self.missing_file_check)
        except FileNotFoundError as e:
            print(f"Возникла следующая ошибка: {e}")

    def check_empty_file(self):
        try:
            pd.read_csv(self.empty_file_check)
        except EmptyDataError:
            print(f"Возникла следующая ошибка: Датафрейм {self.empty_file_check} пуст")

    def validate_data_structure(self):
        reference_df = pd.read_csv('var10.csv')
        test_df = pd.read_csv('var41.csv')
        
        ref_columns = list(reference_df.columns)
        test_columns = list(test_df.columns)

                
        if ref_columns == test_columns:
            print("Чтение датафрейма завершено успешно.") 
        else:
            print("Структура датафрейма НЕ соответствует ожидаемой:")

            if ref_columns != test_columns:
                print("- Названия столбцов НЕ совпадают")
                print(f"Ожидаемые: {ref_columns}")
                print(f"Фактические: {test_columns}")

            
            common_columns = reference_df.columns.intersection(test_df.columns)

            for col in common_columns:
                ref_dtype = reference_df[col].dtype
                test_dtype = test_df[col].dtype
                print(f"- В столбце {col} тип данных не соответствует ожидаемому.")
                print(f"Ожидается: {ref_dtype}, Фактически: {test_dtype}")

        print("Проверка структуры датафрейма завершена.")    

def main():
    reference_file = "var10.csv"
    empty_file = "var3.csv"
    missing_file = "var5.csv"
    
    processing = Data_Processing(reference_file, empty_file, missing_file)
    processing.check_file_existence()
    processing.check_empty_file()
    processing.validate_data_structure()

if __name__ == "__main__":
    main()