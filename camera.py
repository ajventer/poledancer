import imageio
import gphoto2 as gp
import logging
import sys
import io

from PIL import Image
from PIL.ImageQt import ImageQt


class Camera(object):
    def __init__(self):
        self.exposure = 1
        self.driftDelay = 30
        logging.basicConfig(
        format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
        callback_obj = gp.check_result(gp.use_python_logging())

    def camera_list(self):
        camera_list = []
        for name, addr in gp.check_result(gp.gp_camera_autodetect()):
            camera_list.append((name, addr))
        return camera_list


    def connect(self):
        self.camera = gp.check_result(gp.gp_camera_new())
        gp.check_result(gp.gp_camera_init(self.camera))
        # required configuration will depend on camera type!
        print('Checking camera config')
        # get configuration tree
        self.config = gp.check_result(gp.gp_camera_get_config(self.camera))


    def getImage(self):
        cfg = self.camera.get_config()
        capturetarget_cfg = cfg.get_child_by_name('capturetarget')
        capturetarget = capturetarget_cfg.get_value()
        capturetarget_cfg.set_value('Internal RAM')
        self.camera.set_config(cfg)        
        camera_file = gp.check_result(gp.gp_camera_capture_preview(self.camera))
        file_data = gp.check_result(gp.gp_file_get_data_and_size(camera_file))
        tempPath='/tmp/align.cr2'
        data = memoryview(file_data)
        image = Image.open(io.BytesIO(file_data))
        qimage = ImageQt(image)
        # TiffPath = '/tmp/align.tiff'
        # image.save(TiffPath)
        return qimage


class CameraSimulator(Camera):
    def __init__(self):
        self.exposure = 1
        self.driftDelay = 30        
        self.imageid = 0
        self.images = ['Resources/orion_simulator_1.jpg', 'Resources/orion_simulator_2.jpg']

    def connect(self):
        return True

    def getImage(self):
        image = Image.open(self.images[self.imageid])
        print ('Camera Simulator - showing:  ', self.images[self.imageid])
        qimage = ImageQt(image)
        if self.imageid  == 0:
            self.imageid = 1
        else:
            self.imageid = 0        
        return qimage
