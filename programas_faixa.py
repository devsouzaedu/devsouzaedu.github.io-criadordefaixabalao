from PIL import Image, ImageDraw

def criar_faixa(altura, largura_cima, largura_baixo, num_gomos, logo_path):
    # Definindo as dimensões da faixa
    altura_total = altura
    largura_total = largura_cima
    altura_gomo = altura_total
    largura_gomo_cima = largura_cima / num_gomos
    largura_gomo_baixo = largura_baixo / num_gomos

    # Criando a imagem branca para a faixa
    faixa = Image.new('RGB', (largura_total, altura_total), 'white')

    # Adicionando o logo
    logo = Image.open(logo_path)
    logo = logo.convert("RGBA")  # Convertendo para RGBA para suportar transparência
    logo_largura, logo_altura = logo.size
    margem_lateral = (largura_total - largura_cima) / 2
    faixa.paste(logo, ((largura_total - logo_largura) // 2, (altura_total - logo_altura) // 2), mask=logo.split()[3])

    # Desenhando os gomos
    draw = ImageDraw.Draw(faixa)
    for i in range(num_gomos):
        x = margem_lateral + i * largura_gomo_cima
        pontos = [(x, 0), (x + largura_gomo_cima, 0), (x + largura_gomo_baixo, altura_total),
                  (x + (largura_gomo_cima - largura_gomo_baixo), altura_total)]
        draw.polygon(pontos, outline='black')

    # Salvando cada gomo como um arquivo .jpg
    for i in range(num_gomos):
        gomo = faixa.crop((margem_lateral + i * largura_gomo_cima, 0, margem_lateral + (i + 1) * largura_gomo_cima, altura_total))
        gomo.save(f'gomo_{i+1}.jpg')

# Exemplo de uso
altura = 800
largura_cima = 1200
largura_baixo = 1000
num_gomos = 8
logo_path = 'logo_sadia.png'  # Substitua pelo caminho do arquivo de logo do cliente
criar_faixa(altura, largura_cima, largura_baixo, num_gomos, logo_path)
