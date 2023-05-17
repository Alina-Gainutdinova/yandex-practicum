def drawBox(width, height, outline, fill):
 # Слишком маленькие прямоугольники не могут быть нарисованы при помощи этой функции
    if width < 2 or height < 2:
        print("Ошибка: ширина или высота прямоугольника слишком малы.")
        quit()
    # Рисуем верхнюю линию прямоугольника
    print(outline * width)
    # Рисуем стороны прямоугольника
    for i in range(height - 2):
        print(outline + fill * (width - 2) + outline)
    # Рисуем нижнюю линию прямоугольника
    print(outline * width)
    # Демонстрируем работу обновленной функции
drawBox(14, 5, "@", ".")