import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Tahmininizi girin (1-100): "))
        attempts += 1

        if guess < number:
            print("Daha büyük bir sayı girin.")
        elif guess > number:
            print("Daha küçük bir sayı girin.")
        else:
            print(f"Tebrikler! {attempts} denemede doğru tahmin ettiniz.")
            break

guess_number()
