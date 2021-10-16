import io
import logging

from azure.storage.blob import BlobClient, BlobServiceClient, ContainerClient
from PIL import Image
from prettyconf import config
from simple_zpl2 import Code128_Barcode, ZPLDocument

logger = logging.getLogger(__name__)


class ZPLGenerator:
    blob_service_client = None

    def process(self, uuid):
        self.blob_service_client = BlobServiceClient.from_connection_string(
            config("AZURE_STORAGE_CONNECTION_STRING")
        )
        zpl = self._create_zpl(uuid)
        png = self._generate_img_png(uuid, zpl)
        path = self._save(png, uuid, config("SAVE_ON_CLOUD", cast=config.boolean))

        return path

    def _create_zpl(self, uuid):
        zdoc = ZPLDocument()
        zdoc.add_field_origin(5, 5)
        code128_data = uuid
        bc = Code128_Barcode(code128_data, "N", 30, "Y")
        zdoc.add_barcode(bc)
        logger.info(f"Created ZPL {uuid}")
        return zdoc

    def _generate_img_png(self, uuid, zpl):
        png_bytes = zpl.render_png(label_width=4.3, label_height=0.3)

        logger.info(f"Generate PNG {uuid}")
        return png_bytes

    def _save(self, png, uuid, save_on_cloud=False):
        fake_file = io.BytesIO(png)

        if save_on_cloud:
            blob_client = self.blob_service_client.get_blob_client(
                container=config("FOLDER_NAME"), blob=f"{uuid}.png"
            )

            logger.info(f"Uploading to Azure Storage as blob:{uuid}.png")
            blob_client.upload_blob(fake_file, overwrite=True)
            path = blob_client.url
        else:
            img = Image.open(fake_file)
            img.save(f"./zpls/{uuid}.png")
            path = f"https://p1uc-tcc-bernardo.com/zpls/{uuid}"

        logger.info(f"Generate PATH {uuid}")
        return path
