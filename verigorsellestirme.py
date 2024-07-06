import matplotlib.pyplot as plt

def plot_data(x_data, y_data, x_label, y_label, title):
    plt.figure(figsize=(8, 6))
    plt.plot(x_data, y_data, marker='o', linestyle='-', color='b', label=y_label)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

# Örnek veri
x_data = [1, 2, 3, 4, 5]
y_data = [10, 20, 25, 30, 35]
plot_data(x_data, y_data, 'X Axis', 'Y Axis', 'Sample Plot')
