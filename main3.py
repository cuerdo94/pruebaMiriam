import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog, Tk, Button


def remove_background(image):
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


def process_image(image_path):
    # Cargar la imagen original
    original_image = cv2.imread(image_path)

    # Mejorar la imagen original
    enhanced_image = enhance_image(original_image)

    # Quitar el fondo de la imagen mejorada
    image_without_background = remove_background(enhanced_image)

    return original_image, image_without_background, enhanced_image


def save_images(original_image, image_without_background, enhanced_image):
    # Guardar las imágenes en el disco
    # file_path = filedialog.asksaveasfilename(defaultextension=".png")
    file_path = filedialog.askdirectory()
    if file_path:
        cv2.imwrite(file_path + "/" + "_original.png", original_image)
        cv2.imwrite(file_path + "/" + "_without_background.png",
                    image_without_background)
        cv2.imwrite(file_path + "/" + "_enhanced.png", enhanced_image)
        print("Imágenes guardadas exitosamente.")


def select_image_and_process():
    # Seleccionar la imagen a procesar
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal

    image_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

    if image_path:
        # Procesar la imagen
        original_image, image_without_background, enhanced_image = process_image(
            image_path)
        save_images(original_image, image_without_background, enhanced_image)
        # Guardar las imágenes al presionar un botón
        # save_button = Button(root, text="Guardar imágenes", command=lambda: save_images(
        #     original_image, image_without_background, enhanced_image))
        # save_button.pack()

        root.mainloop()


if __name__ == "__main__":
    select_image_and_process()
