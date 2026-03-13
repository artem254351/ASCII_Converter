@echo off
chcp 1251 > nul
title ASCII Image Converter

echo ======================================================
echo    ПРОГРАММА КОНВЕРТАЦИИ ИЗОБРАЖЕНИЙ В ASCII-АРТ
echo ======================================================
echo.

set /p source=Введите URL или путь к изображению(пример:C:\Users\Менеджер\Downloads\photo_2024-05-21_20-58-31.jpg):
set /p width=Ширина вывода (по умолчанию 80):
set /p output=Сохранить в файл (оставьте пустым для вывода в консоль):

if "%width%"=="" set width=80

if not "%output%"=="" (
    python ascii_converter.py "%source%" %width% "%output%"
) else (
    python ascii_converter.py "%source%" %width%
)

echo.
echo Готово! Нажмите любую клавишу для выхода...
pause > nul
