import io

from PIL import Image
from prettyconf import config
from simple_zpl2 import Code128_Barcode, ZPLDocument


class ZPLGenerator:
    def process(self, uuid):
        zpl = self._create_zpl(uuid)
        png = self._generate_img_png(zpl)

        return self._save(png, uuid, config("SAVE_TO_S3", cast=config.boolean))

    def _create_zpl(self, uuid):
        zdoc = ZPLDocument()
        zdoc.add_field_origin(5, 5)
        code128_data = uuid
        bc = Code128_Barcode(code128_data, "N", 30, "Y")
        zdoc.add_barcode(bc)

        return zdoc

    def _generate_img_png(self, zpl):
        return zpl.render_png(label_width=4.3, label_height=0.3)

    def _save(self, png, uuid, save_s3=False):
        fake_file = io.BytesIO(png)
        img = Image.open(fake_file)
        path = f"./zpls/{uuid}.png"
        img.save(path)

        if save_s3:
            ...

        return path
