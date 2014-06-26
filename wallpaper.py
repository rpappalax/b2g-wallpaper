from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def generate_png(filename, width, height, message, color_bg, color_text, font):

    (R,G,B) = color_bg
    img = Image.new("RGBA", (width, height),(R,G,B))
    draw = ImageDraw.Draw(img)

    (tR,tG,tB) = color_text
    w, h = draw.textsize(message, font)
    print width
    print w
    print h
    pos_start = ((width - w)/2, (height*0.39))

    draw.text(
        pos_start,
        message,
        color_text,
        font=font
    )
    img.save(filename)

dev_serial = '9a9a9a9'
filename_wallpaper = 'wallpaper.jpg'
dev_serial = 'DEV_SERIAL: ' + dev_serial
color_rgba = (15,159,219) # #0F9FDB
color_text = (0, 0, 0)
font = ImageFont.truetype("ArialUnicode.ttf",28)
message = dev_serial

params = {
    'filename':filename_wallpaper,
    'width':320,
    'height':480,
    'message':message,
    'color_bg':color_rgba,
    'color_text':color_text,
    'font':font
}
generate_png(**params)