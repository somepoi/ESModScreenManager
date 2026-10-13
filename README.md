# Mod Screen Manager

Менеджер экранов для модов на Бесконечное Лето

## Описание

Технический мод для Everlasting Summer, который позволяет заменять экраны интерфейса без конфликтов с другими модами.

## Важно

Mod Screen Manager работает только на Ren'Py 7.x. В восьмой версии архитектура экранов изменилась, и прямая замена через `renpy.display.screen.screens` больше не работает.

## Установка

> ⚠️ Мод распространяется как зависимость для других модов, поэтому копировать файлы `MSM.rpy`, `logger.rpy` и `01msm_cds.rpy` в папку Вашего мода **НЕЛЬЗЯ**.
> Если вы используете MSM для Non-Steam версии БЛ, пожалуйста, распространяйте MSM как **отдельный мод**.

Из `example/` возьмите:

- `example.rpy.example` — настройка конфига и лейблы для теста работы мода
- `screens.rpy.example` — шаблоны экранов

`test_example.rpy.example` копировать необязательно, он нужен только если Вы хотите расширенно проверить работу менеджера экранов.

Переименуйте их в `.rpy` (уберите `.example`).

## Настройка

Откройте `example.rpy` и настройте `my_mod_ModScreenManagerConfig` под свой мод.

Замените `my_mod` на префикс Вашего мода везде в коде (`example.rpy` и `screens.rpy`). Запустите игру и проверьте, что всё работает.

Когда убедитесь, что менеджер работает, замените шаблоны в `screens.rpy` на свои экраны.

## Пример использования

### Использование экземпляра класса

#### Настройка конфига

```renpy
init python:
    # Кастомный конфиг на основе шаблона
    class my_mod_ModScreenManagerConfig(ModScreenManagerConfig):
        # Переопределяем параметры
        # Для опциональных параметров можем указать "" или False, если не хотим менять
    
        # Имя мода
        # БЕЗ ШРИФТОВ, ЦВЕТА И ПРОЧИХ ТЕГОВ
        MOD_NAME = u"Менеджер экранов"
        
        # Префикс мода
        # МОЖЕТ БЫТЬ АБСОЛЮТНОЕ ЛЮБОЕ СЛОВО ИЛИ СЛОВОСОЧЕТАНИЕ, ОТДЕЛЯЮЩЕЕ РЕСУРСЫ ВАШЕГО МОДА ОТ ДРУГИХ
        # префикс - это когда Вы хотите добавить, например, свою переменную, или свои экраны, и в начале пишете любое слово, например, my_prefix - это и есть префикс
        # пример - my_prefix_variable или my_prefix_dialogue_screen, здесь "my_prefix" выступает префиксом
        # соотвественно, вот этот my_prefix в конце имени переменной/экрана - это уже постфикс, не префикс.
        MOD_ID = "my_mod"

        # Имя мода в сохранении (опционально)
        # НЕ ДОБАВЛЯЕТСЯ АВТОМАТИЧЕСКИ В СОХРАНЕНИЕ МОДА
        # нужно руками вносить через my_mod_ModScreenManagerConfig.MOD_SAVE_IDENTIFIER
        # или просто руками каждый раз вводить 
        MOD_SAVE_IDENTIFIER = "Имя сохранения менеджера экранов"

        # Замена имени окна БЛ на имя своего мода (опционально)
        MOD_REPLACE_WINDOW_NAME = False

        # Свой курсор (опционально)
        MOD_CURSOR_PATH = False
        
        # Свой трек в главном меню (опционально)
        MOD_MENU_MUSIC = False
        
        # Выбираем только нужные экраны
        DEFAULT_SCREENS = [
            "main_menu", # Главное меню
            "game_menu_selector", # Быстрое меню (на ПКМ/Esc), ДОЛЖЕН ОБЯЗАТЕЛЬНО БЫТЬ В СПИСКЕ ЗАМЕНЫ ЭКРАНОВ
            "say", # Диалоговое окно
            "nvl", # NVL диалоговое окно
            "preferences", # Настройки
            "save", # Сохранение
            "load", # Загрузка
            "choice", # Выбор
            "text_history_screen", # Экран истории
            "history", # Экран концовок (Сова в главном меню БЛ)
            "yesno_prompt", # Экран подтверждения действия (при выходе из игры/загрузке сохранения и т.п.)
            "skip_indicator", # Индикатор пропуска (при зажатом CTRL, например)
            "help", # Помощь
            "quit", # Выход
        ]
        
        # включить/выключить логирование в консоль Ren'Py (опционально)
        LOGGING = False
        # Уровень логирования (опционально)
        LOG_LEVEL = 20 # INFO
```

#### Инициализация

```renpy
init python:
    # Создаем глобальный экземпляр менеджера с нашим кастомным шаблоном
    my_mod_screen_manager = ModScreenManager(my_mod_ModScreenManagerConfig)

    # Инициализируем наш мод, начальным лейблом которого будет MOD_ID, а имя - MOD_NAME
    mods[my_mod_screen_manager.MOD_ID] = my_mod_screen_manager.MOD_NAME
```

#### Использование

```renpy
label my_mod:
    # Устанавливаем имя сохранения с идентификатором мода (чтобы экраны автоматически включались при загрузке сохранения Вашего мода)
    $ save_name = my_mod_ModScreenManagerConfig.MOD_SAVE_IDENTIFIER

    # Включаем экраны
    $ my_mod_screen_manager.activate_screens()
    
    "Hello World!"

    jump my_mod_exit

label my_mod_exit:
    # Обязательно выключайте экраны при выходе
    $ my_mod_screen_manager.deactivate_screens()
    return
```

### Использование CDS

#### Настройка конфига и инициализация

```renpy
msm config my_ui:
    mod_name "Мой мод"
    mod_id "my_mod"
    savename "MyMod"
    DEFAULT_SCREENS es_all
    window_name False
    cursor False
    menu_music False
```

- `my_ui` — уникальный тег менеджера
- `my_mod` — префикс экранов (`my_mod_say`, `my_mod_choice` и т.д.).

Вместо `DEFAULT_SCREENS es_all` можно задать только нужные экраны:

```renpy
    DEFAULT_SCREENS:
        "game_menu_selector"
        "say"
        "choice"
```

`game_menu_selector` обязателен.

Отключение интерфейса в кнопке выхода в главном меню при использовании CDS:

```renpy
action [Function(_msm_defined_managers["my_ui"].deactivate_screens), MainMenu()]
```

`window_name`, `cursor` и `menu_music` принимают Python-выражения, включая переменные, строковые пути и `False`.
Переменные для настроек конфигурации должны быть определены до её выполнения при init-приоритете 0.

Команда `msm savename my_ui "MyMod"` меняет идентификатор автоактивации менеджера.
Она также принимает переменные и выражения, например `msm savename my_ui save_name`.
Для автоактивации после загрузки сохраняйте идентификатор или название мода в глобальном `save_name`.

#### Использование

```renpy
label my_mod:
    $ save_name = "MyMod. День 1"

    # Заменяем экраны на свои
    msm activate my_ui

    "Hello World!"

    # Возвращаем оригинальные экраны
    msm deactivate my_ui

    return
```