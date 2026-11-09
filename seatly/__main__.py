from seatly.greeting import hello   # из пакета seatly берём модуль greeting и функцию hello


def main():
    print(hello("Seatly"))


if __name__ == "__main__":          # выполнится при `python -m seatly`
    main()