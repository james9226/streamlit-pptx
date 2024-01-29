from io import BytesIO
from src.dashboard.pages.dashboard.charts import generate_slides

from src.powerpoint.ppt import ThemedPresentation


def download_ppt() -> BytesIO:
    ppt = ThemedPresentation()

    ppt = generate_slides(ppt)

    # Add other generate slide functions here as they are built

    return ppt.to_buffer()
