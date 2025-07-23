from imgPrompt import imgPrompt
from enum import Enum
from formatTypes import imgFormats


class black_forest_labs_flux_pro_ultra(imgPrompt):
    output_formats: list[str] = [
        'jpg',
        'png'
    ]

    aspect_ratios: list[str] = [
        '21:9',
        '16:9',
        '3:2',
        '4:3',
        '5:4',
        '1:1',
        '4:5',
        '3:4',
        '2:3',
        '9:16',
        '9:21',
    ]

    def __init__(
            self,
            prompt: str,
            raw: bool = False,
            safety_tolerance: int = 2,
            image_prompt_strength: float = .1,
            aspect_ratio: str = '3:2',
            output_format: str = 'jpg',
    ):
        self.model_name: str = 'black-forest-labs/flux-1.1-pro-ultra'
        self.raw = raw
        self.image_prompt_strength = image_prompt_strength
        self.safety_tolerance = safety_tolerance

        if aspect_ratio not in black_forest_labs_flux_pro_ultra.aspect_ratios:
            raise TypeError(f'{aspect_ratio} not supported by model')

        if output_format not in black_forest_labs_flux_pro_ultra.output_formats:
            raise TypeError(f'{output_format} not supported by model')

        super().__init__(
            model_name=self.model_name,
            prompt=prompt,
            aspect_ratio=aspect_ratio,
            output_format=output_format)

    def _generate_input_dict(self):
        replicate_input_dict: dict = {
            'raw': self.raw,
            'prompt': self.prompt,
            'aspect_ratio': self.aspect_ratio,
            'output_format': self.output_format,
            'safety_tolerance': self.safety_tolerance,
            'image_prompt_strength': self.image_prompt_strength
        }
        return replicate_input_dict
