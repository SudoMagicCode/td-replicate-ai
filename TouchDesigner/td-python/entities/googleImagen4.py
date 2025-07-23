from imgPrompt import imgPrompt
from enum import Enum
from formatTypes import imgFormats


class google_imagen_4(imgPrompt):
    output_formats: list[str] = [
        'jpg',
        'png'
    ]

    supported_models: list[str] = [
        'google/imagen-4-fast',
        'google/imagen-4-ultra'
        'google/imagen-4',
    ]

    aspect_ratios: list[str] = [
        '1:1',
        '4:3',
        '3:4',
        '16:9',
        '9:16'
    ]

    def __init__(
            self,
            model: str,
            prompt: str,
            aspect_ratio: str,
            output_format: str = 'jpg'):

        if model not in google_imagen_4.supported_models:
            raise TypeError(f'{model} is not supported by this class')

        if aspect_ratio not in google_imagen_4.aspect_ratios:
            raise TypeError(f'{aspect_ratio} not supported by model')

        if output_format not in google_imagen_4.output_formats:
            raise TypeError(f'{output_format} not supported by model')

        self.model_name: str = model

        super().__init__(
            model_name=self.model_name,
            prompt=prompt,
            aspect_ratio=aspect_ratio,
            output_format=output_format)

    def __repr__(self):
        return f'google_imagen_4 class wrapper for {self.model_name}'

    def _generate_input_dict(self):
        replicate_input_dict: dict = {
            'prompt': self.prompt,
            'aspect_ratio': self.aspect_ratio,
            'output_format': self.output_format,
            'safety_filter_level': self.safety_filter
        }
        return replicate_input_dict
