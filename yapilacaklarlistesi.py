todo_list = []

def add_task(task):
    todo_list.append(task)

def view_tasks():
    for i, task in enumerate(todo_list):
        print(f"{i + 1}. {task}")

while True:
    print("\nYapılacaklar Listesi:")
    print("1. Görev ekle")
    print("2. Görevleri gör")
    print("3. Çıkış")

    choice = input("Seçiminizi yapın (1/2/3): ")

    if choice == '1':
        task = input("Görev girin: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        break
    else:
        print("Geçersiz seçim")
