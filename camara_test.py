import cv2
import numpy as np

def evalia_oscuridad(matriz):
    matriz_intensidad = np.mean(matriz,2)
    brillo = np.mean(matriz_intensidad)
    return brillo

def usar_camara():
    count = 0
    pausa = False
    last_frame = None
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ No se pudo acceder a la cámara.")
        return 
    print("Presiona 'q' para salir.")

    while True:
        if not pausa:
            ret, frame = cap.read()
            if not ret:
                print("Error al capturar la imagen.")
                break
            last_frame = frame
        else:
            frame = last_frame
        frame = cv2.flip(frame,1)

        # Mostrar el frame en una ventana
        cv2.imshow("Camara en vivo", frame)
        brillo = evalia_oscuridad(frame)

        if brillo<50:
            print("La imagen se ve muy oscura")

        # Salir si se presiona la tecla 'q'
        key = cv2.waitKey(1) & 0xFF
        if  key == ord('q'):
            break
        if key == ord('w'):
            count=count+1
            cv2.imwrite(f"frames/frame_guardado{count}.png", frame)
        if key == ord('p'):
            pausa = not pausa

    # Liberar la cámara y cerrar ventanas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    usar_camara()
