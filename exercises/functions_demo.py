def add_item(item, items = []):
    items.append(item)
    return items


print(add_item("a"))
print(add_item("b"))

def add_item_fixed(item, items = None):
    if items is None: # если список не передали, создаем новый
        items = []    # этот список свой на каждый вызов
    items.append(item)
    return items


print(add_item_fixed("a"))
print(add_item_fixed("b"))


def show(*args, **kwargs):
    print("позиционные", args)
    print("именованные", kwargs)

show(1,2,3, sep="-")
