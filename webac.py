import webbrowser

def open_website(url):
    webbrowser.open(url)

url = input("Açmak istediğiniz web sitesinin URL'sini girin: ")
open_website(url)
