init python:
    # Уберите из списка ненужные названия экранов, если не хотите их заменять.
    MY_MOD_SCREENS = [
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

    def my_mod_screen_save():  # Функция сохранения экранов из оригинала.
        for name in MY_MOD_SCREENS:
            renpy.display.screen.screens[
                ("my_mod_old_" + name, None)
            ] = renpy.display.screen.screens[(name, None)]


    def my_mod_screen_act():  # Функция замены экранов из оригинала на собственные.
        config.window_title = u"Мой мод"  # Здесь вводите название Вашего мода.
        for (
            name
        ) in (
            MY_MOD_SCREENS
        ):
            renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[
                ("my_mod_" + name, None)
            ]
        config.mouse["default"] = [ ("images/misc/mouse/1.png", 0, 0) ]
        default_mouse = "default"
        # Две строчки сверху - замена курсора
        config.main_menu_music = (
            "interface/music/main_menu.mp3"  # Вставьте ваш путь до музыки в главном меню.
        )


    def my_mod_screens_diact():  # Функция обратной замены.
        # Пытаемся заменить экраны.
        try:
            config.window_title = u"Бесконечное лето"
            for name in MY_MOD_SCREENS:
                renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[
                    ("my_mod_old_" + name, None)
                ]
            config.mouse["default"] = [ ("images/misc/mouse/1.png", 0, 0) ]
            default_mouse = "default"
            config.main_menu_music = "sound/music/blow_with_the_fires.ogg"
        except:  # Если возникают ошибки, то мы выходим из игры, чтобы избежать Traceback
            renpy.quit()
    
    # Функция для автоматического включения кастомного интерфейса при загрузке сохранения с названием Вашего мода
    def my_mod_activate_after_load():
        global save_name
        if "my_mod" in save_name:
            my_mod_screen_save()
            my_mod_screen_act()

    # Добавляем функцию в Callback
    config.after_load_callbacks.append(my_mod_activate_after_load)

    # Объединяем функцию сохранения экранов и замены в одну.
    def my_mod_screens_save_act():
        my_mod_screen_save()
        my_mod_screen_act()
