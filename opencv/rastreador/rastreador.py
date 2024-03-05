import cv2

# Carregar o classificador pré-treinado para detecção de rostos
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
classifier = cv2.CascadeClassifier(cascade_path)

# Carregar a imagem
image_path = r"c:\Users\lucas\Downloads\world_cup_us_ghana_dempsey_goal.jpg" 
image = cv2.imread(image_path)

# Converter a imagem para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar corpos de pessoas
players = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Desenhar retângulos ao redor dos corpos detectados
for (x, y, w, h) in players:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Mostrar a imagem resultante
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
