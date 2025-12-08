init python:
    # Кастомный конфиг на основе шаблона
    class CustomConfigForModScreenManager(ModScreenManagerConfig):
        # Переопределяем параметры
        MOD_NAME = u"Менеджер экранов"
        MOD_SAVE_IDENTIFIER = "Тест замены интерфейса с помощью менеджера экранов"
        
        # Кастомные пути
        MOD_CURSOR_PATH = "ESModScreenManager/images/1.png"
        MOD_MENU_MUSIC = "ESModScreenManager/music/main_menu.mp3"
        
        # Выбираем только нужные экраны
        DEFAULT_SCREENS = [
            "main_menu",
            "game_menu_selector",
            "quit",
            "say",
            "preferences",
            "save",
            "load",
            "nvl",
            "choice",
            "text_history_screen",
            "yesno_prompt",
            "skip_indicator",
            "history",
            "help",
        ]
        
        # логирование
        ENABLE_LOGGING = False
init:
    $ mods["mod_screen_manager_init"] = u"Менеджер экранов"
    # Создаем глобальный экземпляр менеджера с нашим кастомным шаблоном
    $ my_mod_screen_manager = ModScreenManager(CustomConfigForModScreenManager)

default persistent.timeofday = 'day'

label mod_screen_manager_init:    
    # Даём имя сохранению, чтобы при загрузке сейва из нашего мода у нас автоматически включался наш интерфейс.
    # Важно: проверяем, что в нашем имени сохранения будет присутствовать MOD_SAVE_IDENTIFIER или MOD_NAME из конфига мода, по нему мы проверяем мод, сейв которого мы грузим.
    # Пример: MOD_SAVE_IDENTIFIER = "Мой мод" или MOD_NAME = "Мой мод", значит save_name = "Мой мод. День 1.", "Мой мод начало" или "Старт Мой мод", т.е. чтобы в имени сохранения всегда присутстваол наш индентификатор мода или имя мода в том регистре, в котором он написан
    
    $ save_name = "Менеджер экранов"#"Тест замены интерфейса с помощью менеджера экранов"
    # или, если Вы боитесь забыть об указании идентификатора или имени мода, то можно сделать так:
    #$ save_name = MyCustomConfig.MOD_SAVE_IDENTIFIER
    # или
    #$ save_name = MyCustomConfig.MOD_NAME
    # если надо добавить ещё какой-то текст для например обозначения дня, то
    #$ save_name = MyCustomConfig.MOD_SAVE_IDENTIFIER + "Любой текст, который вы хотите"
    # или
    #$ save_name = MyCustomConfig.MOD_NAME + "Любой текст, который вы хотите"
    # так он всегда будет в Вашем имени сохранения

    jump mod_screen_manager_test

label mod_screen_manager_test:
    scene bg black
    
    menu mod_screen_manager_test_main_menu:
        "{size=+10}{b}МЕНЕДЖЕР ЭКРАНОВ{/b}{/size}\n\nВыберите режим тестирования:"
        
        "1. Управление модом (вкл/выкл)":
            jump mod_screen_manager_test_mod_control
        
        "2. Частичная замена экранов":
            jump mod_screen_manager_test_partial_replacement
        
        "3. Тест отдельных экранов":
            jump mod_screen_manager_test_individual_screens
        
        "4. Быстрый тест всех экранов":
            jump mod_screen_manager_quick_test_all_screens
        
        "5. Диагностика системы":
            jump mod_screen_manager_test_diagnostics
        
        "6. Демонстрация интерфейса":
            jump mod_screen_manager_demo_interface
        
        "Выход":
            jump mod_screen_manager_exit

label mod_screen_manager_exit:
    $ my_mod_screen_manager.deactivate_screens() # Обязательно отключаем наши экраны при выходе из мода, будь то просто добавив функцию на кнопку выхода или при завершении мода через вызов функции
    return

label mod_screen_manager_test_mod_control:
    scene bg black
    
    python:
        status = my_mod_screen_manager.get_status()
        status_text = u"Активен" if status['is_active'] else u"Неактивен"
    
    menu mod_screen_manager_mod_control_menu:
        "{b}УПРАВЛЕНИЕ МОДОМ{/b}\n\nТекущий статус: [status_text]"
        
        "Активировать мод (все экраны)":
            $ result = my_mod_screen_manager.activate_screens()
            if result:
                "Мод успешно активирован!"
                "Все экраны заменены на кастомные."
            else:
                "Ошибка активации мода!"
            jump mod_screen_manager_test_mod_control
        
        "Деактивировать мод (вернуть оригинал)":
            $ result = my_mod_screen_manager.deactivate_screens()
            if result:
                "Мод деактивирован!"
                "Восстановлены оригинальные экраны."
            else:
                "Ошибка деактивации!"
            jump mod_screen_manager_test_mod_control
        
        "Проверить совместимость":
            $ compat = my_mod_screen_manager.check_compatibility()
            if compat:
                "Версия Ren'Py совместима с модом!"
            else:
                "ВНИМАНИЕ: Возможны проблемы совместимости!"
            jump mod_screen_manager_test_mod_control
        
        "Назад":
            jump mod_screen_manager_test_main_menu

label mod_screen_manager_test_partial_replacement:
    scene bg black
    
    menu mod_screen_manager_partial_menu:
        "{b}ЧАСТИЧНАЯ ЗАМЕНА ЭКРАНОВ{/b}\n\nВыберите группу экранов:"
        
        "Только диалоговые (say, nvl, choice)":
            $ screens = ["say", "nvl", "choice"]
            $ result = my_mod_screen_manager.activate_screens(screens, partial=True)
            if result:
                "Активированы диалоговые экраны!"
                "Тестируем диалог..."
                "Это тестовое сообщение в кастомном окне."
            jump mod_screen_manager_partial_menu
        
        "Только меню (main_menu, game_menu_selector)":
            $ screens = ["main_menu", "game_menu_selector", "quit"]
            $ result = my_mod_screen_manager.activate_screens(screens, partial=True)
            if result:
                "Активированы экраны меню!"
            jump mod_screen_manager_partial_menu
        
        "Только сохранение/загрузка":
            $ screens = ["save", "load"]
            $ result = my_mod_screen_manager.activate_screens(screens, partial=True)
            if result:
                "Активированы экраны сохранения!"
                call screen my_mod_save
            jump mod_screen_manager_partial_menu
        
        "Переключить экран 'say'":
            $ is_active = my_mod_screen_manager.toggle_screen("say")
            if is_active:
                "Экран 'say' активирован!"
            else:
                "Экран 'say' деактивирован!"
            jump mod_screen_manager_partial_menu
        
        "Деактивировать все":
            $ my_mod_screen_manager.deactivate_screens()
            "Все экраны деактивированы!"
            jump mod_screen_manager_partial_menu
        
        "Назад":
            jump mod_screen_manager_test_main_menu

label mod_screen_manager_test_individual_screens:
    scene bg black
    
    menu mod_screen_manager_individual_screens_menu:
        "{b}ТЕСТ ОТДЕЛЬНЫХ ЭКРАНОВ{/b}"
        
        "Главное меню":
            call screen my_mod_main_menu
            jump mod_screen_manager_individual_screens_menu
        
        "Игровое меню":
            call screen my_mod_game_menu_selector
            jump mod_screen_manager_individual_screens_menu
        
        "Сохранение":
            call screen my_mod_save
            jump mod_screen_manager_individual_screens_menu
        
        "Загрузка":
            call screen my_mod_load
            jump mod_screen_manager_individual_screens_menu
        
        "Настройки":
            call screen my_mod_preferences
            jump mod_screen_manager_individual_screens_menu
        
        "История текста":
            call screen my_mod_text_history_screen
            jump mod_screen_manager_individual_screens_menu
        
        "Помощь":
            call screen my_mod_help
            jump mod_screen_manager_individual_screens_menu
        
        "Галерея":
            call screen my_mod_gallery
            jump mod_screen_manager_individual_screens_menu
        
        "Музыкальная комната":
            call screen my_mod_music_room
            jump mod_screen_manager_individual_screens_menu
        
        "Тест диалога":
            jump mod_screen_manager_test_dialogue
        
        "Тест выбора":
            jump mod_screen_manager_test_choice
        
        "Назад":
            jump mod_screen_manager_test_main_menu

label mod_screen_manager_test_dialogue:
    scene bg black
    "Это тест диалогового окна."
    "Обратите внимание на дизайн."
    me "Привет! Это сообщение от персонажа."
    "Можно открыть историю (H) или сохранить (S)."
    jump mod_screen_manager_individual_screens_menu

label mod_screen_manager_test_choice:
    scene bg black
    menu:
        "Выберите вариант:"
        "Вариант 1":
            "Выбран вариант 1"
        "Вариант 2":
            "Выбран вариант 2"
        "Длинный вариант текста для проверки переноса строк":
            "Выбран длинный вариант"
    jump mod_screen_manager_individual_screens_menu

label mod_screen_manager_quick_test_all_screens:
    scene bg black
    
    "Начинаем быстрое тестирование..."
    $ my_mod_screen_manager.activate_screens()
    
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
    jump mod_screen_manager_test_main_menu

label mod_screen_manager_test_diagnostics:
    scene bg black
    
    python:
        manager = my_mod_screen_manager
        status = manager.get_status()
        
        missing_screens = []
        for screen_name in CustomConfigForModScreenManager.DEFAULT_SCREENS:
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
    
    $ manager.logger.info(u"\n" + report)

    "Результат диагностики экспортирован в консоль Ren'Py!"
    
    jump mod_screen_manager_test_main_menu

label mod_screen_manager_demo_interface:
    scene bg black
    $ my_mod_screen_manager.activate_screens()
    
    menu mod_screen_manager_demo_menu:
        "{b}ДЕМОНСТРАЦИЯ{/b}"
        
        "Тест диалога":
            "Демонстрация диалогового окна."
            me "Привет! Тестовое сообщение."
            "Используйте H для истории, S для сохранения."
            jump mod_screen_manager_demo_menu
        
        "Тест выбора":
            menu:
                "Выберите:"
                "Простой":
                    "Выбран простой"
                "С форматированием {b}жирный{/b}":
                    "Форматирование работает!"
            jump mod_screen_manager_demo_menu
        
        "Цветовые схемы":
            jump mod_screen_manager_demo_colors
        
        "Назад":
            jump mod_screen_manager_test_main_menu

label mod_screen_manager_demo_colors:
    menu mod_screen_manager_color_menu:
        "Выберите время суток:"
        
        "День":
            $ persistent.timeofday = 'day'
            "Дневная схема установлена."
            jump mod_screen_manager_color_menu
        
        "Вечер":
            $ persistent.timeofday = 'sunset'
            "Вечерняя схема установлена."
            jump mod_screen_manager_color_menu
        
        "Ночь":
            $ persistent.timeofday = 'night'
            "Ночная схема установлена."
            jump mod_screen_manager_color_menu
        "Пролог":
            $ persistent.timeofday = 'prologue'
            "Прологовая схема установлена."
            jump mod_screen_manager_color_menu
        
        "Назад":
            jump mod_screen_manager_demo_menu