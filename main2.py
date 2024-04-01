import cv2
import numpy as np
import matplotlib.pyplot as plt

def remove_background(image_path):
    # Cargar la imagen
    image = cv2.imread(image_path)
    
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplicar umbral adaptativo para obtener una máscara
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    
    # Invertir la máscara para tener el fondo en blanco y el objeto en negro
    mask = cv2.bitwise_not(mask)
    
    # Aplicar la máscara a la imagen original para eliminar el fondo
    result = cv2.bitwise_and(image, image, mask=mask)
    
    return result

def enhance_image(image):
    # Aplicar mejora de la imagen, por ejemplo, ajuste de contraste
    enhanced_image = cv2.convertScaleAbs(image, alpha=1.2, beta=0)
    
    return enhanced_image

def main():
    # Ruta de la imagen
    image_path = "header.png"
    
    # Quitar el fondo de la imagen
    image_without_background = remove_background(image_path)
    
    # Guardar la imagen sin fondo
    cv2.imwrite("sin_fondo.png", image_without_background)
    
    # Mejorar la imagen
    enhanced_image = enhance_image(image_without_background)
    
    # Guardar la imagen mejorada
    cv2.imwrite("mejorada.png", enhanced_image)
    
    # Mostrar la imagen original, sin fondo y mejorada
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    titles = ['Original', 'Sin Fondo', 'Mejorada']
    images = [cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB), 
              cv2.cvtColor(image_without_background, cv2.COLOR_BGR2RGB), 
              cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB)]
    
    for ax, title, image in zip(axes, titles, images):
        ax.imshow(image)
        ax.set_title(title)
        ax.axis('off')
    
    plt.show()

if __name__ == "__main__":
    main()
