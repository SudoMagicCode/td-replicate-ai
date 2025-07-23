import imgPrompt
import videoPrompt

import googleImagen4
import blackForestLabsFlux

videoPromptMap = {}

imgPromptMap: dict[str, imgPrompt.imgPrompt] = {
    'google/imagen-4-fast': googleImagen4.google_imagen_4,
    'google/imagen-4': googleImagen4.google_imagen_4,
    'google/imagen-4-ultra': googleImagen4.google_imagen_4,
    'black-forest-labs/flux-1.1-pro-ultra': blackForestLabsFlux.black_forest_labs_flux_pro_ultra
}
