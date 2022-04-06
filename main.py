
from PIL import Image, ImageDraw, ImageFont

# Создаем список из приглашенных гостей
guests = ['Адиль-Диляра', 'Ринат-Динара', 'Рүстем - Қарлығаш', 'Сәкен -Ляззат']



def make_invites():
    sample_image = Image.open('example.jpeg')
    font = ImageFont.truetype('fonts/Standart2010/vAsylm13.ttf', 40)
    drawer = ImageDraw.Draw(sample_image)
    for guest in guests:
        drawer.text((155, 435),f'{guest}', font = font, fill = '#E78E68')
        sample_image.save(f'{guest}.jpeg')
        sample_image = Image.open('example.jpeg')
        drawer = ImageDraw.Draw(sample_image)

        
        

make_invites()



