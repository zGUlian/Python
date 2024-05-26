def get_month_name(month_number):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(month_number, "Invalid number. Please enter a number between 1 and 12.")

# Solicitar a entrada do usuário
month_number = int(input("Enter a number between 1 and 12: "))

# Obter o nome do mês
month_name = get_month_name(month_number)

# Imprimir o resultado
print(month_name)
