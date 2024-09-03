from PIL import Image, ImageDraw, ImageFont

class Display:
    def __init__(self):
        # Inicializar o display LCD
        # Exemplo fictício, substitua pela biblioteca específica
        # self.display = SomeDisplayLibrary()
        pass

    def show_message(self, message):
        # Criar uma imagem para o display
        image = Image.new('RGB', (320, 400), color=(0, 0, 0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        # Desenhar o texto na imagem
        draw.text((50, 180), message, font=font, fill=(255, 255, 255))

        # Mostrar a imagem no display
        # self.display.show_image(image)
        print(f"Display message: {message}")  # Simula exibição no terminal
