import PIL
from PIL import Image, ImageDraw
import qrcode

def create_image():
    size = (100,50)             # size of the image to create
    im = Image.new('RGB', size) # create the image
    draw = ImageDraw.Draw(im)   # create a drawing object that is
                                # used to draw on the new image
    red = (255,0,0)    # color of our text
    text_pos = (10,10) # top-left position of our text
    text = "Hello World!" # text to draw
    # Now, we'll do the drawing:
    draw.text(text_pos, text, fill=red)

    del draw # I'm done drawing so I don't need this anymore

    # im.save('test.jpg')
    #
    # im.show()

def easy_qr(data):
    img = qrcode.make(data)
    img.show()

def qr():
    qr = qrcode.QRCode(version=1, error_correction=constants.ERROR_CORRECT_H, box_size=1)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.resize((int(img.size[0] * scale), int(img.size[1]
                     * scale)), PIL.Image.ANTIALIAS)
    self.image.paste(img, location)
