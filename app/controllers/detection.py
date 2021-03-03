from app.controllers.Darknet import darknet
from app.controllers.Darknet import darknet_images
import os
from PIL import Image
import time
import cv2

#DARKNET_ROOT = './app/controllers/Darknet/'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DARKNET_ROOT = os.path.join(APP_ROOT, 'Darknet/')

image_path = os.path.join(os.getcwd(), 'app/static')

print("\n")
print(image_path)
print("\n")

darknet.set_gpu(0)

t1 = time.time()
network, class_names, class_colors = darknet.load_network(
    config_file=DARKNET_ROOT + 'yolov4_custom.cfg',
    data_file=DARKNET_ROOT + 'obj.data',
    weights=DARKNET_ROOT + 'yolov4_custom.weights'
)
t2 = time.time()
print("🦖 tempo de carregamento: {:.2f}".format(t2 - t1) + " segundos")
class_colors = {
    'circuito aberto': (154, 178, 129),
    'curto-circuito': (143, 204, 242),
    'falta de cobre': (95, 122, 224),
    'cobre excessivo': (231, 213, 182),
    'trilha voadora': (95, 122, 224),
    'sem estanho': (169, 148, 255)
}

def detect(image_name):
    t1 = time.time()

    image, detections = darknet_images.image_detection(
        image_path=image_path+'/'+image_name,
        #image_path='/home/ana/github/pcb-defect-detection-api/app/static/01_teste.JPG',
        network=network,
        class_names=class_names,
        class_colors=class_colors,
        thresh=0.25
    )

    t2 = time.time()

    darknet.print_detections(detections)

    darknet_images.save_annotations(
        name=image_path+'/'+image_name,
        image=image,
        detections=detections,
        class_names=class_names
    )

    cv2.imwrite(image_path+'/'+str.split(image_name, ".")[0]+'_defeitos.jpg', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    cv2.imwrite(image_path+'/'+'temp.jpg', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

    print("🦖 tempo de processamento: {:.2f}".format(t2 - t1) + " segundos")
    print('🦖 imagem salva: '+image_path+'/'+str.split(image_name, ".")[0]+'_defeitos.jpg')
    print('🦖 anotações salvas: '+image_path+'/'+str.split(image_name, ".")[0]+'.txt')

    return len(detections), (t2 - t1)
