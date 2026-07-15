import os
import json
import sys

EXTENSOES_VALIDAS = ('.png', '.jpg', '.jpeg', '.webm', '.webp', '.gif')

def gerar_lista(diretorio='.'):
    categorias = sorted([
        d for d in os.listdir(diretorio)
        if os.path.isdir(os.path.join(diretorio, d)) and not d.startswith('.')
    ])

    if not categorias:
        print("Nenhuma pasta de categorias encontrada.")
        sys.exit(1)

    lista_final = []

    for categoria in categorias:
        caminho_cat = os.path.join(diretorio, categoria)
        ficheiros = sorted(os.listdir(caminho_cat))

        for arquivo in ficheiros:
            if arquivo.lower().endswith(EXTENSOES_VALIDAS):
                lista_final.append({
                    "nome": arquivo,
                    "categoria": categoria,
                    "caminho": f"{categoria}/{arquivo}"
                })

    lista_final.sort(key=lambda x: (x['categoria'], x['nome']))

    output = os.path.join(diretorio, 'fotos.json')
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(lista_final, f, ensure_ascii=False, indent=4)

    print(f"{len(lista_final)} ficheiros listados em {output}")
    for cat in categorias:
        n = sum(1 for i in lista_final if i['categoria'] == cat)
        print(f"  {cat}: {n}")

if __name__ == '__main__':
    gerar_lista()
