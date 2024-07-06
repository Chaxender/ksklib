def write_note():
    note = input("Notunuzu girin: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

def read_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            for note in notes:
                print(note.strip())
    except FileNotFoundError:
        print("Notlar dosyası bulunamadı.")

while True:
    print("\nNot Defteri:")
    print("1. Not ekle")
    print("2. Notları oku")
    print("3. Çıkış")

    choice = input("Seçiminizi yapın (1/2/3): ")

    if choice == '1':
        write_note()
    elif choice == '2':
        read_notes()
    elif choice == '3':
        break
    else:
        print("Geçersiz seçim")
