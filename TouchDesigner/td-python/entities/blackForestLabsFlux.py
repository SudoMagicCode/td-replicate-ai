from imgPrompt import imgPrompt
from enum import Enum
from formatTypes import imgFormats


class black_forest_labs_flux_pro_ultra(imgPrompt):
    aspect_ratios: list[str] = [
        '1:1',
        '4:3',
        '3:4',
        '16:9',
        '9:16'
    ]

    def __init__(self):
        self.model_name: str = 'black-forest-labs/flux-1.1-pro-ultra'
        super().__init__(model_name=self.model_name, output_format='jpg')
