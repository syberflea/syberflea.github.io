def assess_yield(number_of_plants, average_weight):
    w = number_of_plants * average_weight / 1000
    if w > 100:
        m = "Ожидается отличный урожай."
    elif 50 <= w <= 100:
        m = "Ожидается хороший урожай."
    elif 0 < w < 50:
        m = "Урожай будет так себе."
    else:
        m = "Урожая не будет."
    return w, m

# Пример вызова функции
total_weight, rating = assess_yield(50, 0)
print(total_weight, rating)