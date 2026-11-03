# generate.py
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path
import argparse          # разбор аргументов командной строки

random.seed(42)


EVENTS = [
    (1, "Jazz Night", "2026-11-14", 1200),
    (2, "Python Meetup", "2026-11-20", 500),
    (3, "Rock Festival", "2026-12-05", 2500),
    (4, "Stand-up Evening", "2026-12-12", 900),
]

ROWS = 10 # рядов в зале
SEATS = 20 # мест в каждом ряду

def make_sales(total):
    all_seats = [
        (event, row, seat)
        for event in EVENTS
        for row in range(1, ROWS + 1)
        for seat in range(1, SEATS + 1)
    ]
    if total > len(all_seats):
        raise SystemExit(f"Максимум {len(all_seats)}")
    chosen = random.sample(all_seats, total)

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
    parser = argparse.ArgumentParser(description="Генератор выгрузки продаж билетов")
    parser.add_argument("--rows", type=int, default=500,
                        help="сколько продаж сгенерировать (по умолчанию 500)")
    args = parser.parse_args()       # читает то, что ты написал после имени файла

    out_dir = Path(__file__).parent / "data"
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / "sales_001.csv"

    with open(out_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["sold_at", "event_id", "event_title", "event_date",
                         "row", "seat", "price", "status"])
        writer.writerows(make_sales(args.rows))      # было make_sales()

    print(f"Готово: {out_file} ({args.rows} строк)")


if __name__ == "__main__":
    main()