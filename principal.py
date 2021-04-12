# -*- coding: utf-8 -*-

import os
import base64
from falaParaTexto import falaParaTexto
from textoParaFala import textoParaFala

def base64_encode(texto_str):
    return base64.b64encode(texto_str)

def base64_decode(texto_str_byte):
    texto_str_byte = base64.b64decode(texto_str_byte)
    return texto_str_byte.decode('ascii')

while True:
    print("Faça uma pergunta...".decode("utf8"))
    pergunta = falaParaTexto()
    resultado = os.popen("php tuxi.php " + base64_encode(pergunta)).read()
    resultado = base64_decode(resultado)
    if resultado == "No Result!":
        resultado = "Não encontrei nada, tente novamente"
    print("Resultado: " + resultado.decode("utf8"))
    textoParaFala(resultado)
