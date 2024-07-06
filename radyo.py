import pygame

# Radyo istasyonları ses dosyaları
stations = {
    "1": {"name": "Radyo 1", "file": "path/to/music1.mp3"},
    "2": {"name": "Radyo 2", "file": "path/to/music2.mp3"},
    "3": {"name": "Radyo 3", "file": "path/to/music3.mp3"},
}

def print_stations():
    print("Mevcut Radyo İstasyonları:")
    for key, station in stations.items():
        print(f"{key}: {station['name']}")

def play_station(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

if __name__ == "__main__":
    print_stations()
    choice = input("Dinlemek istediğiniz radyo istasyonunun numarasını girin: ")
    if choice in stations:
        print(f"{stations[choice]['name']} çalıyor...")
        play_station(stations[choice]["file"])
        try:
            while pygame.mixer.music.get_busy():
                pass
        except KeyboardInterrupt:
            pygame.mixer.music.stop()
            print("\nRadyo durduruldu.")
    else:
        print("Geçersiz seçim.")
