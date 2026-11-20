import math, os, random, subprocess, wave
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = os.path.dirname(os.path.abspath(__file__)) + "/build"
os.makedirs(OUT, exist_ok=True)
W, H = 1920, 1080
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

SCENES = [
    ("O Planeta Azul", "Uma viagem de cinco minutos pelos oceanos", [],
     "Olá! Seja bem-vindo. Nos próximos cinco minutos, vamos fazer uma viagem pelo lugar mais misterioso do nosso planeta. Não estamos falando do espaço sideral, mas de algo muito mais próximo: o oceano. Ele cobre a maior parte da Terra, produz boa parte do ar que respiramos e, mesmo assim, ainda guarda segredos que a ciência mal começou a desvendar. Vamos mergulhar juntos?"),
    ("Um mundo de água", "71% da superfície da Terra",
     ["Cinco oceanos, um só sistema", "97% de toda a água do planeta", "Profundidade média: cerca de 3.700 metros"],
     "Cerca de setenta e um por cento da superfície da Terra é coberta por água, e quase toda ela, noventa e sete por cento, está nos oceanos. Costumamos dividi-los em cinco: Pacífico, Atlântico, Índico, Antártico e Ártico. Mas, na verdade, todos estão conectados, formando um único oceano global. A profundidade média é de cerca de três mil e setecentos metros. Se a Terra fosse uma bola lisa, ela ficaria inteira submersa sob mais de dois quilômetros de água."),
    ("O pulmão escondido", "O oceano produz grande parte do nosso oxigênio",
     ["Fitoplâncton: algas microscópicas", "Cerca de metade do oxigênio da Terra", "Absorve cerca de um quarto do CO2 emitido"],
     "Quando pensamos no pulmão do mundo, lembramos das florestas. Mas uma grande parte do oxigênio que respiramos vem do mar. Ele é produzido pelo fitoplâncton, algas microscópicas que flutuam perto da superfície e fazem fotossíntese, assim como as plantas. Estima-se que esses seres minúsculos sejam responsáveis por cerca de metade do oxigênio do planeta. Além disso, o oceano absorve cerca de um quarto do gás carbônico que a humanidade lança na atmosfera, ajudando a frear o aquecimento global."),
    ("As camadas do mar", "Quanto mais fundo, mais escuro e frio",
     ["Zona iluminada: até 200 m", "Zona do crepúsculo: até 1.000 m", "Zona da meia-noite: escuridão total", "Zona abissal: pressão esmagadora"],
     "O oceano é dividido em camadas. Nos primeiros duzentos metros fica a zona iluminada, onde a luz do sol chega e a vida é abundante. Abaixo dela vem a zona do crepúsculo, onde a luz vai sumindo até quase nada. Depois dos mil metros começa a zona da meia-noite: escuridão total, frio intenso e uma pressão enorme. E ainda mais fundo está a zona abissal, onde a pressão da água é centenas de vezes maior do que na superfície."),
    ("A Fossa das Marianas", "O ponto mais profundo do planeta",
     ["Quase 11.000 metros de profundidade", "O Everest caberia lá dentro", "Pressão mais de 1.000 vezes maior"],
     "No oceano Pacífico fica a Fossa das Marianas, o ponto mais profundo conhecido da Terra. Ela chega a quase onze mil metros de profundidade. Para ter uma ideia, se colocássemos o Monte Everest lá dentro, o seu pico ainda ficaria a mais de dois quilômetros abaixo da superfície. Lá embaixo, a pressão é mais de mil vezes maior do que a que sentimos ao nível do mar. Mais pessoas já pisaram na Lua do que visitaram o fundo dessa fossa."),
    ("Luz na escuridão", "A bioluminescência",
     ["Seres que produzem a própria luz", "Usada para caçar, fugir e se comunicar", "Comum na maioria dos animais das profundezas"],
     "Mesmo na escuridão total, o fundo do mar brilha. Muitos animais das profundezas produzem a sua própria luz, um fenômeno chamado bioluminescência. O peixe-pescador, por exemplo, tem uma espécie de lanterna na cabeça para atrair presas. Algumas lulas soltam uma nuvem brilhante para confundir predadores. Cientistas acreditam que a grande maioria dos animais que vivem em águas profundas tem alguma capacidade de produzir luz. É como um céu estrelado, só que debaixo d'água."),
    ("Um mistério a explorar", "Conhecemos melhor a Lua do que o fundo do mar",
     ["Grande parte do fundo ainda sem mapa detalhado", "Novas espécies descobertas todos os anos", "Milhares de espécies ainda sem nome"],
     "Por incrível que pareça, temos mapas mais detalhados da superfície da Lua e de Marte do que do fundo do nosso próprio oceano. Uma grande parte do leito marinho ainda não foi mapeada em alta resolução. E todos os anos, cientistas descrevem centenas de novas espécies marinhas. Calcula-se que a maioria das formas de vida do oceano ainda nem tenha sido identificada. O mar continua sendo uma das últimas grandes fronteiras de exploração."),
    ("Recifes de coral", "As florestas tropicais do mar",
     ["Menos de 1% do fundo do oceano", "Abrigam cerca de 25% das espécies marinhas", "Ameaçados pelo aquecimento das águas"],
     "Os recifes de coral ocupam menos de um por cento do fundo do oceano, mas abrigam cerca de um quarto de todas as espécies marinhas. Por isso, são chamados de florestas tropicais do mar. Os corais são animais que vivem em parceria com algas, que lhes dão cor e alimento. Quando a água esquenta demais, essa parceria se rompe e o coral fica branco, um fenômeno chamado branqueamento. Se o calor dura muito tempo, o coral pode morrer."),
    ("O oceano pede ajuda", "Os maiores desafios",
     ["Milhões de toneladas de plástico por ano", "Pesca acima do limite", "Aquecimento e acidificação das águas"],
     "Infelizmente, o oceano enfrenta grandes ameaças. Todos os anos, milhões de toneladas de plástico chegam ao mar, prejudicando tartarugas, aves e peixes. A pesca excessiva retira peixes mais rápido do que eles conseguem se reproduzir. E, ao absorver tanto gás carbônico, a água do mar fica mais quente e mais ácida, o que afeta corais, conchas e toda a cadeia alimentar."),
    ("O que você pode fazer", "Pequenas atitudes, grande impacto",
     ["Reduza o plástico descartável", "Prefira pescado de fontes sustentáveis", "Não deixe lixo na praia", "Compartilhe o que aprendeu"],
     "A boa notícia é que todos nós podemos ajudar. Reduza o uso de plásticos descartáveis, como sacolas, canudos e garrafas. Prefira peixes e frutos do mar de fontes sustentáveis. Quando for à praia, leve o seu lixo de volta e, se puder, recolha algum que encontrar pelo caminho. E, principalmente, compartilhe o que aprendeu. Quanto mais pessoas conhecem o oceano, mais pessoas querem protegê-lo."),
    ("Obrigado por mergulhar conosco!", "Cuide do planeta azul", [],
     "O oceano nos dá oxigênio, alimento, regula o clima e ainda guarda mistérios incríveis esperando para serem descobertos. Ele cuida de nós todos os dias. Agora é a nossa vez de cuidar dele. Obrigado por assistir, e até a próxima viagem!"),
]

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def background(idx, n):
    depth = idx / (n - 1)
    # deeper scenes get darker
    top = lerp((40, 160, 210), (5, 20, 50), min(1, depth * 1.4))
    bot = lerp((5, 50, 110), (0, 4, 15), min(1, depth * 1.4))
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    for y in range(H):
        d.line([(0, y), (W, y)], fill=lerp(top, bot, y / H))
    rnd = random.Random(idx * 7 + 3)
    # light rays
    rays = Image.new("L", (W, H), 0)
    rd = ImageDraw.Draw(rays)
    for _ in range(7):
        x = rnd.randint(-200, W)
        w = rnd.randint(60, 180)
        rd.polygon([(x, 0), (x + w, 0), (x + w * 3 + 400, H), (x + 400, H)],
                   fill=int(rnd.randint(15, 35) * (1 - depth)))
    rays = rays.filter(ImageFilter.GaussianBlur(40))
    img = Image.composite(Image.new("RGB", (W, H), (200, 240, 255)), img, rays)
    # bubbles / glowing particles
    over = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(over)
    glow = depth > 0.4
    for _ in range(90):
        x, y = rnd.randint(0, W), rnd.randint(0, H)
        r = rnd.randint(2, 14)
        if glow and rnd.random() < 0.5:
            c = rnd.choice([(80, 255, 220), (120, 180, 255), (200, 120, 255)])
            od.ellipse([x - r, y - r, x + r, y + r], fill=c + (rnd.randint(60, 160),))
        else:
            od.ellipse([x - r, y - r, x + r, y + r], outline=(220, 245, 255, 110), width=2)
    over = over.filter(ImageFilter.GaussianBlur(1.5))
    img = Image.alpha_composite(img.convert("RGBA"), over)
    # seabed silhouette
    sd = ImageDraw.Draw(img)
    pts = [(0, H)]
    for x in range(0, W + 40, 40):
        pts.append((x, H - 70 - 40 * math.sin(x / 210 + idx) - 25 * math.sin(x / 73)))
    pts.append((W, H))
    sd.polygon(pts, fill=(0, 10, 25, 255))
    return img

def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    lines.append(cur)
    return lines

def slide(idx, n, title, sub, bullets):
    img = background(idx, n)
    d = ImageDraw.Draw(img)
    ft, fs, fb, fn = (ImageFont.truetype(FB, 96), ImageFont.truetype(FR, 48),
                      ImageFont.truetype(FR, 50), ImageFont.truetype(FB, 30))
    if not bullets:  # title card
        y = 360
        for line in wrap(d, title, ft, 1600):
            tw = d.textlength(line, font=ft)
            d.text(((W - tw) / 2 + 4, y + 4), line, font=ft, fill=(0, 0, 0, 140))
            d.text(((W - tw) / 2, y), line, font=ft, fill="white")
            y += 115
        tw = d.textlength(sub, font=fs)
        d.text(((W - tw) / 2, y + 30), sub, font=fs, fill=(170, 230, 255))
    else:
        d.text((150, 50), f"{idx:02d} / {n - 2:02d}", font=fn, fill=(150, 220, 255))
        d.text((154, 124), title, font=ft, fill=(0, 0, 0, 140))
        d.text((150, 120), title, font=ft, fill="white")
        d.text((150, 250), sub, font=fs, fill=(170, 230, 255))
        d.rectangle([150, 330, 350, 336], fill=(80, 220, 255))
        panel = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(panel).rounded_rectangle([120, 390, 1500, 420 + 120 * len(bullets)],
                                                radius=30, fill=(0, 20, 40, 120))
        img = Image.alpha_composite(img, panel)
        d = ImageDraw.Draw(img)
        y = 430
        for b in bullets:
            d.ellipse([170, y + 18, 194, y + 42], fill=(80, 220, 255))
            d.text((225, y), b, font=fb, fill="white")
            y += 120
    return img.convert("RGB")

def dur(path):
    with wave.open(path) as w:
        return w.getnframes() / w.getframerate()

parts = []
for i, (title, sub, bullets, text) in enumerate(SCENES):
    png, wav, mp4 = f"{OUT}/s{i:02d}.png", f"{OUT}/s{i:02d}.wav", f"{OUT}/s{i:02d}.mp4"
    slide(i, len(SCENES), title, sub, bullets).save(png)
    subprocess.run(["espeak-ng", "-v", "mb-br3", "-s", "170", "-g", "6", "-w", wav, text],
                   check=True, stderr=subprocess.DEVNULL)
    d = dur(wav) + 1.1
    fr = int(d * 30)
    vf = (f"scale=2304:1296,zoompan=z='1+0.06*on/{fr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d={fr}:s={W}x{H}:fps=30,fade=t=in:st=0:d=0.6,fade=t=out:st={d-0.6:.2f}:d=0.6,format=yuv420p")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", png,
                    "-i", wav, "-filter_complex",
                    f"[0:v]{vf}[v];[1:a]adelay=700|700,apad,aformat=sample_rates=44100:channel_layouts=stereo[a]",
                    "-map", "[v]", "-map", "[a]", "-t", f"{d:.2f}",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "22",
                    "-c:a", "aac", "-b:a", "160k", mp4], check=True)
    parts.append(mp4)
    print(i, title, round(d, 1))

with open(f"{OUT}/list.txt", "w") as f:
    f.writelines(f"file '{p}'\n" for p in parts)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                "-i", f"{OUT}/list.txt", "-c", "copy", f"{OUT}/narrado.mp4"], check=True)
