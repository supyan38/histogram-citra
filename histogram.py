import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image_path):
    image = cv2.imread(image_path)  
    if image is None:
        print(f"Gambar tidak dapat dibaca. Periksa path: {image_path}")
        return
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    colors = ('red', 'green', 'blue')
    hist_data = {}
    
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        hist_data[color] = hist
        
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    
    plt.title('Histogram of Color Channels')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.legend(colors)
    plt.show()

plot_histogram('C:/Users/LNV/Documents/semester 5/Pengolahan Citra/praktikum/percobaan 2/8bit.jpg')

