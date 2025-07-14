from datetime import datetime, timedelta, date
from decimal import Decimal


def add(items, title, good_amount, expiration_date=None):
    if expiration_date is not None:
        expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()
    if title not in items:
        items[title] = []

    items[title].append({'amount': Decimal(good_amount), 'expiration_date': expiration_date})


def add_by_note(items, note):
    notes = note.split()
    try:
        expiration_date = str(datetime.strptime(val := notes.pop(), '%Y-%m-%d').date())
    except TypeError:
        expiration_date = None
        notes.append(val)
    except ValueError:
        expiration_date = None
        notes.append(val)
    good_amount = Decimal(notes.pop())
    title = " ".join(notes)
    add(items, title, good_amount, expiration_date)


def find(items, needle):
    find_goods = []
    for item in items:
        if needle.lower() in item.lower():
            find_goods.append(item)
    return find_goods


def amount(items, needle):
    total = Decimal('0')
    find_goods = find(items, needle)
    for each in find_goods:
        for elem in items[each]:
            total += elem['amount']
    return total


def expire(items, in_advance_days=0):
    expired_goods = []
    delta = timedelta(days=in_advance_days)
    today = date.today()
    for elem, params in items.items():
        total = Decimal('0')
        for param in params:
            expiration_date = param['expiration_date']
            if expiration_date is not None and (today + delta >= expiration_date):
                total += param['amount']
        if total > 0:
            expired_goods.append((elem, total))

    return expired_goods


if __name__ == '__main__':
    # goods = {}
    # add(goods, 'яйца', Decimal('10'), '2023-07-10')
    # add(goods, 'яйца', Decimal('3'))
    # add_by_note(goods, 'Яйца 4 2023-07-11')
    # add_by_note(goods, 'Яйца Фабрики №1 4 2023-07-12')
    # add_by_note(goods, 'Яйца Фабрики №1 4')
    # add_by_note(goods, ' Яйца  4')
    # print(goods)
    # print(find(goods, 'яйца'))
    # print(amount(goods, 'яйца'))
    goods = {
        'Хлеб': [
            {'amount': Decimal('1'), 'expiration_date': None},
            {'amount': Decimal('1'), 'expiration_date': date(2023, 12, 2)}
        ],
        'Яйца': [
            {'amount': Decimal('2'), 'expiration_date': date(2023, 12, 7)},
            {'amount': Decimal('5'), 'expiration_date': date(2023, 12, 8)},
            {'amount': Decimal('3'), 'expiration_date': date(2023, 12, 13)}
        ],
        'Вода': [{'amount': Decimal('100'), 'expiration_date': None}]
    }

    print(expire(goods))
    # Вывод: [('Яйца', Decimal('2'))]
    print(expire(goods, 1))
    # Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('2'))]
    print(expire(goods, 2))
    # Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('5'))]
