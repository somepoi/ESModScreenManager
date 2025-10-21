init:
    $ mods["interface_test"] = u"Тест замены интерфейса"

default persistent.timeofday = 'day'

label interface_test:
    scene bg black
    
    menu test_main_menu:
        "{size=+10}{b}СИСТЕМА ЗАМЕНЫ ЭКРАНОВ{/b}{/size}\n\nВыберите режим тестирования:"
        
        "1. Управление модом (вкл/выкл)":
            jump test_mod_control
        
        "2. Частичная замена экранов":
            jump test_partial_replacement
        
        "3. Тест отдельных экранов":
            jump test_individual_screens
        
        "4. Быстрый тест всех экранов":
            jump quick_test_all_screens
        
        "5. Диагностика системы":
            jump test_diagnostics
        
        "6. Демонстрация интерфейса":
            jump demo_interface
        
        "Выход":
            return

label test_mod_control:
    scene bg black
    
    python:
        status = mod_screen_manager.get_status()
        status_text = u"Активен" if status['is_active'] else u"Неактивен"
    
    menu mod_control_menu:
        "{b}УПРАВЛЕНИЕ МОДОМ{/b}\n\nТекущий статус: [status_text]"
        
        "Активировать мод (все экраны)":
            $ result = mod_screen_manager.activate_screens()
            if result:
                "Мод успешно активирован!"
                "Все экраны заменены на кастомные."
            else:
                "Ошибка активации мода!"
            jump test_mod_control
        
        "Деактивировать мод (вернуть оригинал)":
            $ result = mod_screen_manager.deactivate_screens()
            if result:
                "Мод деактивирован!"
                "Восстановлены оригинальные экраны."
            else:
                "Ошибка деактивации!"
            jump test_mod_control
        
        "Проверить совместимость":
            $ compat = mod_screen_manager.check_compatibility()
            if compat:
                "Версия Ren'Py совместима с модом!"
            else:
                "ВНИМАНИЕ: Возможны проблемы совместимости!"
            jump test_mod_control
        
        "Назад":
            jump test_main_menu

label test_partial_replacement:
    scene bg black
    
    menu partial_menu:
        "{b}ЧАСТИЧНАЯ ЗАМЕНА ЭКРАНОВ{/b}\n\nВыберите группу экранов:"
        
        "Только диалоговые (say, nvl, choice)":
            $ screens = ["say", "nvl", "choice"]
            $ result = mod_screen_manager.activate_screens(screens, partial=True)
            if result:
                "Активированы диалоговые экраны!"
                "Тестируем диалог..."
                "Это тестовое сообщение в кастомном окне."
            jump partial_menu
        
        "Только меню (main_menu, game_menu_selector)":
            $ screens = ["main_menu", "game_menu_selector", "quit"]
            $ result = mod_screen_manager.activate_screens(screens, partial=True)
            if result:
                "Активированы экраны меню!"
            jump partial_menu
        
        "Только сохранение/загрузка":
            $ screens = ["save", "load"]
            $ result = mod_screen_manager.activate_screens(screens, partial=True)
            if result:
                "Активированы экраны сохранения!"
                call screen my_mod_save
            jump partial_menu
        
        "Переключить экран 'say'":
            $ is_active = mod_screen_manager.toggle_screen("say")
            if is_active:
                "Экран 'say' активирован!"
            else:
                "Экран 'say' деактивирован!"
            jump partial_menu
        
        "Деактивировать все":
            $ mod_screen_manager.deactivate_screens()
            "Все экраны деактивированы!"
            jump partial_menu
        
        "Назад":
            jump test_main_menu

label test_individual_screens:
    scene bg black
    
    menu individual_screens_menu:
        "{b}ТЕСТ ОТДЕЛЬНЫХ ЭКРАНОВ{/b}"
        
        "Главное меню":
            call screen my_mod_main_menu
            jump individual_screens_menu
        
        "Игровое меню":
            call screen my_mod_game_menu_selector
            jump individual_screens_menu
        
        "Сохранение":
            call screen my_mod_save
            jump individual_screens_menu
        
        "Загрузка":
            call screen my_mod_load
            jump individual_screens_menu
        
        "Настройки":
            call screen my_mod_preferences
            jump individual_screens_menu
        
        "История текста":
            call screen my_mod_text_history_screen
            jump individual_screens_menu
        
        "Помощь":
            call screen my_mod_help
            jump individual_screens_menu
        
        "Галерея":
            call screen my_mod_gallery
            jump individual_screens_menu
        
        "Музыкальная комната":
            call screen my_mod_music_room
            jump individual_screens_menu
        
        "Тест диалога":
            jump test_dialogue
        
        "Тест выбора":
            jump test_choice
        
        "Назад":
            jump test_main_menu

label test_dialogue:
    scene bg black
    "Это тест диалогового окна."
    "Обратите внимание на дизайн."
    me "Привет! Это сообщение от персонажа."
    "Можно открыть историю (H) или сохранить (S)."
    jump individual_screens_menu

label test_choice:
    scene bg black
    menu:
        "Выберите вариант:"
        "Вариант 1":
            "Выбран вариант 1"
        "Вариант 2":
            "Выбран вариант 2"
        "Длинный вариант текста для проверки переноса строк":
            "Выбран длинный вариант"
    jump individual_screens_menu

label quick_test_all_screens:
    scene bg black
    
    "Начинаем быстрое тестирование..."
    $ mod_screen_manager.activate_screens()
    
    "1. Игровое меню..."
    call screen my_mod_game_menu_selector
    
    "2. Сохранение..."
    call screen my_mod_save
    
    "3. Настройки..."
    call screen my_mod_preferences
    
    "4. Галерея..."
    call screen my_mod_gallery
    
    "5. Выбор..."
    menu:
        "Тест?"
        "Да":
            pass
        "Нет":
            pass
    
    "6. Уведомление..."
    $ renpy.notify(u"Тест!")
    pause 1.0
    
    "Быстрое тестирование завершено!"
    jump test_main_menu

label test_diagnostics:
    scene bg black
    
    python:
        manager = mod_screen_manager
        status = manager.get_status()
        
        missing_screens = []
        for screen_name in ModConfig.DEFAULT_SCREENS:
            mod_screen = "my_mod_{}".format(screen_name)
            if not manager._screen_exists(mod_screen):
                missing_screens.append(screen_name)
        
        report = u"=== ДИАГНОСТИКА ===\n\n"
        report += u"Активен: {}\n".format(u"Да" if status['is_active'] else u"Нет")
        report += u"Активных экранов: {}/{}\n\n".format(
            len(status['active_screens']), status['total_screens']
        )
        
        compat = manager.check_compatibility()
        report += u"Версия Ren'Py: {}\n".format('.'.join(builtins.map(str, renpy.version_tuple[:2])))
        report += u"Совместимость: {}\n\n".format(u"OK" if compat else u"Проблемы")
        
        if status['active_screens']:
            report += u"Активные экраны:\n"
            for screen in sorted(status['active_screens']):
                report += u"  + {}\n".format(screen)
        
        if missing_screens:
            report += u"\nОтсутствуют:\n"
            for screen in missing_screens:
                report += u"  - my_mod_{}\n".format(screen)
    
    "[report]"
    
    menu:
        "Экспортировать в лог?":
            $ manager.logger.info(u"\n" + report)
            "Экспортировано!"
        "Назад":
            jump test_main_menu

label demo_interface:
    scene bg black
    $ mod_screen_manager.activate_screens()
    
    menu demo_menu:
        "{b}ДЕМОНСТРАЦИЯ{/b}"
        
        "Тест диалога":
            "Демонстрация диалогового окна."
            me "Привет! Тестовое сообщение."
            "Используйте H для истории, S для сохранения."
            jump demo_menu
        
        "Тест выбора":
            menu:
                "Выберите:"
                "Простой":
                    "Выбран простой"
                "С форматированием {b}жирный{/b}":
                    "Форматирование работает!"
            jump demo_menu
        
        "Цветовые схемы":
            jump demo_colors
        
        "Назад":
            jump test_main_menu

label demo_colors:
    menu color_menu:
        "Выберите время суток:"
        
        "День":
            $ persistent.timeofday = 'day'
            "Дневная схема установлена."
            jump color_menu
        
        "Вечер":
            $ persistent.timeofday = 'sunset'
            "Вечерняя схема установлена."
            jump color_menu
        
        "Ночь":
            $ persistent.timeofday = 'night'
            "Ночная схема установлена."
            jump color_menu
        "Пролог":
            $ persistent.timeofday = 'prologue'
            "Прологовая схема установлена."
            jump color_menu
        
        "Назад":
            jump demo_menu