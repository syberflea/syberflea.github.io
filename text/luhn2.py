card = raw_input("Enter your credit card number here: ")
digit_sum = 0

for i, digit in enumerate(reversed(card)):
    n = int(digit)

    if i % 2 == 0:
        digit_sum += n
    elif i >= 5:
        digit_sum += n * 2 - 9
    else:
        digit_sum += n * 2

if digit_sum % 10 == 0:
    print("Card is valid!")
else:
    print("Card is invalid!")

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def Luhn(card_number):
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1
    for count in range(0, num_digits):
        digit = int(card_number[count])
        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9
        sum = sum + digit
    if sum % 10 == 0:
        print("Card is valid!")
    else:
        print("Card is invalid!")