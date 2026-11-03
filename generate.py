# generate.py
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)


EVENTS = [
    (1, "Jazz Night", "2026-11-14", 1200),
    (2, "Python Meetup", "2026-11-20", 500),
    (3, "Rock Festival", "2026-12-05", 2500),
    (4, "Stand-up Evening", "2026-12-12", 900),
]

ROWS = 10 # рядов в зале
SEATS = 20 # мест в каждом ряду
TOTAL_SALES = 500

def make_sales():
    all_seats = [
        (event, row, seat)
        for event in EVENTS
        for row in range(1, ROWS + 1)
        for seat in range(1, SEATS + 1)
    ]
    # sample берет 500 разных мест, одно не продаться дважды
    chosen = random.sample(all_seats, TOTAL_SALES)

    start = datetime(2026,10,1)
    sales = []
    for event, row, seat in chosen:
        event_id, title, date, base_price = event
        #случайный момент в пределах 30 дней, в минутах
        sold_at = start + timedelta(minutes=random.randint(0, 30*24*60))
        price = base_price + (ROWS - row) * 50
        status = "refunded" if random.random() < 0.1 else "paid" #10% возвраты
        sales.append([
            sold_at.isoformat(sep=" ", timespec="seconds"),
            event_id, title, date, row, seat, price, status,
        ])

    sales.sort(key=lambda s: s[0]) #сортировка по времени продаж
        return sales


def main():
    out_dir = Path(__file__).parent / "data" #папка data рядом с generate
    out_dir.mkdir(exist_ok=True)             #создать, если ее еще нет
    out_file = out_dir / "sales_001.csv"

    #newline = "" и utf-8 чтобы на винде не было пустых строк и кракозябр
    with open(out_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["sold_at", "event_id", "event_title", "event_date",
                         "row", "seat", "price", "status"]) #заголовок
        writer.writerows(make_sales())                      # 500 строк данных
        print(f"Готово {out_file}")


if __name__ == "__main__":
    main()