# Кастомные экраны для Ren'Py
## Созданные без внешних изображений и стилей

### Описание
Этот набор экранов создан исключительно с использованием кода Ren'Py без зависимостей от внешних изображений, шрифтов или стилей. Все визуальные элементы реализованы через:
- **Solid** - цветовые заливки
- **Frame** - рамки с заливкой
- **RoundRect** - закругленные прямоугольники (опционально)
- Встроенные элементы Ren'Py

### Структура файлов

1. **custom_screens.rpy** - Главное меню и базовые экраны
   - Главное меню (`custom_main_menu`)
   - Меню в игре (`custom_game_menu`)

2. **custom_screens_save_load.rpy** - Сохранение и загрузка
   - Экран сохранения (`custom_save`)
   - Экран загрузки (`custom_load`)
   - Настройки (`custom_preferences`)

3. **custom_screens_dialogue.rpy** - Диалоги и взаимодействие
   - Диалоговое окно (`custom_say`)
   - Экран выбора (`custom_choice`)
   - NVL диалоги (`custom_nvl`)
   - Подтверждение действий (`custom_yesno_prompt`)
   - Уведомления (`custom_notify`)
   - История текста (`custom_text_history`)
   - Индикатор пропуска (`custom_skip_indicator`)

4. **custom_screens_gallery.rpy** - Галерея и дополнительно
   - Галерея (`custom_gallery`)
   - Музыкальная комната (`custom_music_room`)
   - Об игре (`custom_about`)
   - Быстрое меню (`custom_quick_menu`)

### Цветовые схемы

Система автоматически адаптирует цвета в зависимости от времени суток:

#### День (day)
- Фон: #87CEEB (светло-голубой)
- Окна: #F0E68C (хаки)
- Текст: #2F4F4F (темно-серый)
- Кнопки: #9ACD32 (желто-зеленый)
- Акцент: #FFD700 (золотой)

#### Закат (sunset)
- Фон: #FF6347 (томатный)
- Окна: #FFE4B5 (бисквитный)
- Текст: #8B4513 (коричневый)
- Кнопки: #FF8C00 (темно-оранжевый)
- Акцент: #FFD700 (золотой)

#### Ночь (night)
- Фон: #191970 (темно-синий)
- Окна: #2F4F4F (темно-серый)
- Текст: #F0F8FF (светло-голубой)
- Кнопки: #4682B4 (стальной синий)
- Акцент: #87CEEB (небесно-голубой)

#### Пролог (prologue)
- Фон: #708090 (серый)
- Окна: #D3D3D3 (светло-серый)
- Текст: #2F4F4F (темно-серый)
- Кнопки: #B0C4DE (светло-стальной)
- Акцент: #87CEEB (небесно-голубой)

### Как использовать

#### Вариант 1: Замена стандартных экранов (рекомендуется для тестирования)
Создайте файл `options.rpy` или добавьте в существующий:

```renpy
init python:
    # Переназначение экранов
    config.main_menu_screen = "custom_main_menu"
    config.game_menu_screen = "custom_game_menu"
```

Или переопределите экраны напрямую:

```renpy
# Замена экранов
define config.main_menu = "custom_main_menu"

screen main_menu():
    call screen custom_main_menu()

screen say(who, what):
    call screen custom_say(who, what)

screen choice(items):
    call screen custom_choice(items)

screen nvl(dialogue, items=None):
    call screen custom_nvl(dialogue, items)
```

#### Вариант 2: Вызов напрямую из кода
В вашем скрипте используйте:

```renpy
# Показать кастомное меню
$ renpy.call_screen("custom_game_menu")

# Показать сохранение
$ renpy.call_screen("custom_save")

# Показать галерею
$ renpy.call_screen("custom_gallery")
```

#### Вариант 3: Использование как альтернативная тема
Добавьте переключатель темы в настройках:

```renpy
init python:
    if not hasattr(persistent, 'use_custom_theme'):
        persistent.use_custom_theme = False

screen preferences():
    # ... ваш код настроек
    textbutton "Кастомная тема: {}".format("ВКЛ" if persistent.use_custom_theme else "ВЫКЛ"):
        action [
            ToggleField(persistent, 'use_custom_theme'),
            Function(renpy.utter_restart)
        ]

# В начале игры
label start:
    if persistent.use_custom_theme:
        $ config.main_menu_screen = "custom_main_menu"
```

### Настройка времени суток

Для правильной работы цветовых схем убедитесь, что переменная `persistent.timeofday` установлена:

```renpy
# В начале дня
$ persistent.timeofday = "day"

# На закате
$ persistent.timeofday = "sunset"

# Ночью
$ persistent.timeofday = "night"

# В прологе
$ persistent.timeofday = "prologue"
```

### Кастомизация

#### Изменение цветов
Отредактируйте словарь `color_schemes` в файле `custom_screens.rpy`:

```python
init python:
    color_schemes = {
        'day': {
            'bg': '#ВАШ_ЦВЕТ',
            'box': '#ВАШ_ЦВЕТ',
            'text': '#ВАШ_ЦВЕТ',
            'button': '#ВАШ_ЦВЕТ',
            'button_hover': '#ВАШ_ЦВЕТ',
            'accent': '#ВАШ_ЦВЕТ'
        },
        # ... другие схемы
    }
```

#### Добавление новых времён суток
```python
color_schemes['evening'] = {
    'bg': '#483D8B',
    'box': '#6A5ACD',
    'text': '#F0E68C',
    'button': '#8470FF',
    'button_hover': '#9370DB',
    'accent': '#FFD700'
}
```

#### Изменение размеров элементов
Найдите нужный экран и измените параметры `xsize`, `ysize`, `text_size` и т.д.

Например, для увеличения кнопок главного меню:
```renpy
textbutton "НОВАЯ ИГРА":
    xsize 600  # было 500
    ysize 70   # было 60
    text_size 36  # было 32
```

### Совместимость

- **Ren'Py версия**: 7.0+ (рекомендуется 8.0+)
- **Платформа**: Все платформы (Windows, Linux, macOS, Android, iOS, Web)
- **Зависимости**: Нет

### Известные ограничения

1. **Производительность**: Множество Solid-элементов могут снизить производительность на слабых устройствах
2. **Скриншоты сохранений**: Будут отображаться, но без декоративных рамок
3. **Галерея**: Требует интеграции с системой разблокировки изображений
4. **Музыкальная комната**: Требует заполнения списка треков

### Расширение функционала

#### Добавление скриншотов в слоты сохранений
```renpy
screen custom_save():
    # ... код
    for i in range(1, 13):
        button:
            # ... код кнопки
            
            # Добавьте скриншот
            add FileScreenshot(i):
                xsize 460
                ysize 120
                xalign 0.5
                ypos 5
```

#### Интеграция с галереей
```renpy
init python:
    # Создайте объект галереи
    g = Gallery()
    
    # Добавьте изображения
    g.button("image1")
    g.image("images/cg/image1.png")
    g.unlock("image1")  # Разблокировка
```

### Примеры использования

#### Простая интеграция
```renpy
label start:
    "Добро пожаловать в игру!"
    "Используем кастомные экраны."
    
    menu:
        "Выбери действие:"
        "Сохранить":
            call screen custom_save
        "Настройки":
            call screen custom_preferences
        "Продолжить":
            pass
    
    "Продолжаем историю..."
```

#### Полная замена интерфейса
Создайте файл `custom_integration.rpy`:

```renpy
init python:
    # Переопределение всех экранов
    config.main_menu_screen = "custom_main_menu"
    config.game_menu_screen = "custom_game_menu"

# Переопределение стандартных экранов
screen main_menu():
    call screen custom_main_menu()

screen save():
    call screen custom_save()

screen load():
    call screen custom_load()

screen preferences():
    call screen custom_preferences()

screen say(who, what):
    call screen custom_say(who, what)

screen choice(items):
    call screen custom_choice(items)

screen nvl(dialogue, items=None):
    call screen custom_nvl(dialogue, items)

screen notify(message):
    call screen custom_notify(message)
```

### Советы по оптимизации

1. **Используйте кэширование**: Ren'Py автоматически кэширует Solid-элементы
2. **Минимизируйте вложенность**: Избегайте излишней вложенности Frame внутри Frame
3. **Оптимизируйте прозрачность**: Используйте альфа-канал (например, `#FF000080`) только когда необходимо
4. **Объедините похожие элементы**: Создавайте переиспользуемые компоненты

### Поддержка и обновления

Эти экраны являются базовым шаблоном и могут быть свободно модифицированы под ваши нужды.

### Лицензия

Эти экраны предоставляются "как есть" для свободного использования в ваших проектах.

---

**Дата создания**: 2025  
**Версия**: 1.0.0  
**Совместимость**: Ren'Py 7.0+
