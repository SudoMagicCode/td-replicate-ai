from formatTypes import imgFormats


class imgPrompt:
    def __init__(self,
                 model_name: str,
                 prompt: str,
                 safety_filter: str,
                 aspect_ratio: str = '1:1',
                 output_format: imgFormats = imgFormats.JPG):
        self.model_name = model_name
        self.prompt = prompt
        self.safety_filter = safety_filter
        self.aspect_ratio = aspect_ratio
        self.output_format: str = output_format
