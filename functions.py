def get_data(days):
    dates = ["2024-04-05", "2024-04-04", "2024-04-03"]
    temperatures = [15, 11, 10]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures
