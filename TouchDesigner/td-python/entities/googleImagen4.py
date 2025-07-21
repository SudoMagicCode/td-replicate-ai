from imgPrompt import imgPrompt
from enum import Enum
from formatTypes import imgFormats


class google_imagen_4(imgPrompt):
    aspect_ratios: list[str] = [
        '1:1',
        '4:3',
        '3:4',
        '16:9',
        '9:16'
    ]

    def __init__(self):
        self.model_name: str = 'google/imagen-4-fast'
        super().__init__(model_name=self.model_name, output_format='jpg')
