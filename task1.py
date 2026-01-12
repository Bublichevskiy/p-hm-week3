from datetime import datetime, date

def get_days_from_today(date):
    try:
        new_date = datetime.strptime(date, "%Y-%m-%d").date()
        now = datetime.today().date()
        difference = new_date - now
        return difference.days
    except ValueError:
        print("Формат дати є нерівним, Напишіть дату за зразком 'РРРР-ММ-ДД' ")

print(get_days_from_today("2026-10-09")) # Будь яка дата, до якої програма буде рахувати дні

