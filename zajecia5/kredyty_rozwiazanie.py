

def calculate_loan_installements(loan_amount, years, annual_interest, installment_type):

    total_interest = 0 # suma odsetek
    total_paid = 0 # suma spłąconego kapitału

    monthly_interest = annual_interest / 12 / 100
    total_months = years * 12

    # wyświetlenie podstawowych info o kredycie
    print("\nParametry kredytu:")
    print(f"Kwota kredyty: {loan_amount}")
    print(f"Liczba lat: {years}")
    print(f"Procent w skali roku: {annual_interest}")
    print(f"Typ raty: {installment_type}")

    if installment_type == "stałę":
        monthly_installment = loan_amount * monthly_interest / (1 - (1 + monthly_interest) ** -total_months)

        # q = 1 + monthly_interest
        # n = total_months
        # monthly_installment_2 = loan_amount * (q ** n) * ((q-1))/((q ** n) -1)

        print(f"Miesięczna rata: {monthly_installment:.2f}") #format do dwóch miejsc po przecinku
        for month in range(1, total_months + 1):
            # odsetkowa część raty
            interest_part = (loan_amount - total_interest) * monthly_interest
            # kapitałowa część raty
            capital_part = monthly_installment - interest_part
            #aktualizacja sumy i odsetek
            total_interest += interest_part
            total_paid += capital_part
            #pozostały kapitał do spłaty
            remaining_capital = loan_amount - total_interest
            print(f"Rata: {month}, Kapitał: {capital_part:.2f}, Odsetki: {interest_part:.2f}, Razem: {monthly_installment:.2f}, Pozostało: {remaining_capital:.2f}")

    elif installment_type == "malejace":
        for month in range(1, total_months + 1):
            # kapitałowa
            capital_part = loan_amount / total_months
            # odsetkowa
            interest_part = (loan_amount - (capital_part * (month - 1)) * monthly_interest)
            # aktualizacja sumy i odsetek
            total_interest += interest_part
            total_paid += capital_part
            # całkowita wysokość raty
            monthly_installment = capital_part + interest_part
            remaining_capital = loan_amount - total_interest
            print(
                f"Rata: {month}, Kapitał: {capital_part:.2f}, Odsetki: {interest_part:.2f}, Razem: {monthly_installment:.2f}, Pozostało: {remaining_capital:.2f}")

    print(f"\nCałkowity kredyt (kapitał): {total_paid:.2f}")
    print(f"Koszt (odsetki): {total_interest:.2f}")
    print(f"Całkowity kredyt z kosztem (kapitał + odsetki): {total_paid + total_interest:.2f}")

while True:
    # pobranie kwoty kredytu od usera
    try:
        loan_amount = float(input("Podaj kwotę kredytu: "))
        if loan_amount <= 0:
            raise ValueError
    except ValueError:
        print("Kwota kredytu musi być liczbą dodatnią")
        continue
    # pobranie liczby lat
    try:
        years = int(input("Podaj liczbę lat: "))
        if years <= 0:
            raise ValueError
    except ValueError:
        print("Liczba lat musi być liczbą dodatnią")
        continue
    # pobranie procenta w skali roku
    try:
        annual_interest = float(input("Podaj procent w skali roku: "))
        if annual_interest <= 0:
            raise ValueError
    except ValueError:
        print("Procent w skali roku musi być liczbą dodatnią")
        continue
    # pobranie typu rat - stała/malejące
    installment_type = input("Podaj typ raty (malejące/stałe): ")
    if installment_type not in ["stałe", "malejące"]:
        print("Wybierz raty stałe lub malejące")
        continue
    calculate_loan_installements(loan_amount, years, annual_interest, installment_type)
    break