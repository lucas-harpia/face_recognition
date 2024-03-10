import cv2
import face_recognition
from src.sql_insert import insert_entidades
import os

# Assumindo que 'dlib' com suporte a CUDA está instalada corretamente.

paths = [os.path.join('images', f) for f in os.listdir('images')]


def get_encodings(paths):
  print('{} imagens encontradas'.format(len(paths)))
  lista_encodings = []
  lista_nomes = []
  for img_path in paths:
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    basename = os.path.basename(img_path)
    (nome, ext) = os.path.splitext(basename)
    print(nome, ext)

    # Aqui usamos o modelo 'cnn' que pode usar a GPU para acelerar o processamento
    face_roi = face_recognition.face_locations(img, model='cnn')
    # Podemos tentar extrair os encodings de todas as faces encontradas
    face_encodings = face_recognition.face_encodings(img, face_roi)
    if face_encodings:
      lista_encodings.extend(face_encodings)  # Extend ao invés de append para adicionar todos os encodings
      lista_nomes.extend([nome] * len(face_encodings))  # Adicionamos o nome para cada encoding
    else:
      print('Não foi possível detectar a face da imagem {}'.format(img_path))
  return lista_encodings, lista_nomes


lista_encodings, lista_nomes = get_encodings(paths)

# for path in paths:
#     images = face_recognition.load_image_file(path)
#     images = cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
#     images_RGB.append(images)
#
# if images_RGB:
#     cv2.imshow('Processed Image', images_RGB[-1])
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()