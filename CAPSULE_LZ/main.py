from schedule_statistic import GraphicalStatistics

# Путь к файлу с данными
file_path = "personal_transactions.csv"  
stats = GraphicalStatistics(file_path)
print(stats.load_data())
print(stats.plot_pie_chart())