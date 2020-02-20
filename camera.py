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
        self.camera = gp.check_result(gp.gp_camera_new())

    def connect(self):
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


