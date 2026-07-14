import os
import json

# Pastas de categorias no repositório de mídia
categorias = ['normal', 'oracle', 'misc', 'ren_futaba']
lista_final = []

for categoria in categorias:
    if os.path.isdir(categoria):
        for arquivo in os.listdir(categoria):
            # Filtra apenas imagens e vídeos válidos
            if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.webm', '.webp', '.gif')):
                lista_final.append({
                    "nome": arquivo,
                    "categoria": categoria,
                    "caminho": f"{categoria}/{arquivo}"
                })

# Guarda o fotos.json na raiz do repositório de mídia
with open('fotos.json', 'w', encoding='utf-8') as f:
    json.dump(lista_final, f, ensure_ascii=False, indent=4)

print(f"eba deu certo {len(lista_final)} ficheiros encontrados e listados em fotos.json")