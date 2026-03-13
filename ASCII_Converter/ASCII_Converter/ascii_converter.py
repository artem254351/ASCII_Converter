from PIL import Image
import sys
import os

def image_to_ascii(image, width=80):
    """Конвертирует изображение в ASCII-арт."""
    # Рассчитываем новую высоту с учётом соотношения сторон и сжатия по вертикали
    ratio = image.height / float(image.width)
    new_height = int(ratio * width * 0.55)  # 0.55 — коэффициент для компенсации высоты символов

    # Изменяем размер и преобразуем в оттенки серого
    image = image.resize((width, new_height))
    image = image.convert('L')

    # Набор символов от тёмных к светлым
    chars = "@%#*+=-:. ░▒▓█"
    ascii_img = []

    for y in range(image.height):
        row = ""
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            # Сопоставляем яркость пикселя с символом
            row += chars[pixel * (len(chars) - 1) // 255]
        ascii_img.append(row)

    return "\n".join(ascii_img)


def main():
    # Проверяем количество аргументов
    if len(sys.argv) < 2:
        print("Использование:")
        print("  python ascii_converter.py <путь_к_изображению> [ширина]")
        print("Пример:")
        print('  python ascii_converter.py "фото.jpg" 60')
        print('  python ascii_converter.py "C:\\Папка с пробелами\\фото.jpg"')
        sys.exit(1)

    # Получаем путь к изображению
    input_path = sys.argv[1]

    # Устанавливаем ширину по умолчанию
    width = 80
    if len(sys.argv) > 2:
        try:
            width = int(sys.argv[2])
            if width <= 0:
                print("Ошибка: ширина должна быть положительным числом.")
                sys.exit(1)
        except ValueError:
            print(f"Предупреждение: '{sys.argv[2]}' не является числом. Используется ширина по умолчанию: 80")

    # Проверяем существование файла
    if not os.path.exists(input_path):
        print(f"Ошибка: файл '{input_path}' не найден.")
        sys.exit(1)

    try:
        # Открываем изображение
        img = Image.open(input_path)
    except Exception as e:
        print(f"Ошибка открытия файла: {e}")
        sys.exit(1)

    print("Конвертирую в ASCII-арт...")
    result = image_to_ascii(img, width)
    print("\n" + result)

if __name__ == "__main__":
    main()
