# Замените ВСЕ my_mod на тот же уникальный префикс, что в менеджере.
# Дизайн экранов замените своим.
# Здесь только ресурсы БЛ и Solid: дополнительных картинок/музыки не нужно.

screen my_mod_game_menu_selector():
    tag menu
    modal True
    add Solid("#172334e8")
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 30)
        vbox:
            spacing 20
            text "МЕНЮ МОДА" size 40
            textbutton "Сохранить" action ShowMenu("save")
            textbutton "Загрузить" action ShowMenu("load")
            textbutton "Настройки" action ShowMenu("preferences")
            textbutton "Главное меню":
                action Show("my_mod_exit_confirm")
            textbutton "Вернуться" action Return()

screen my_mod_exit_confirm():
    modal True
    zorder 200
    add Solid("#000000b0")
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 30)
        vbox:
            spacing 30
            text "Вернуться в главное меню?" size 32
            hbox:
                spacing 40
                textbutton "Да" action [Hide("my_mod_exit_confirm"), Function(my_mod_msm_deactivate_screens), MainMenu(confirm=False)]
                textbutton "Нет" action Hide("my_mod_exit_confirm")

screen my_mod_say(who, what, **kwargs):
    window:
        id "window"
        background Solid("#172334e8")
        xalign 0.5
        yalign 1.0
        xfill True
        padding (100, 30)
        vbox:
            spacing 10
            if who:
                text who id "who" color "#f4c86a" size 32
            text what id "what" color "#ffffff" size 28

screen my_mod_choice(items):
    modal True
    add Solid("#172334b0")
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        # БЛ передаёт тройки (caption, action, chosen).
        for my_mod_choice_caption, my_mod_choice_action, my_mod_choice_chosen in items:
            if my_mod_choice_action:
                textbutton my_mod_choice_caption action my_mod_choice_action
            else:
                text my_mod_choice_caption color "#f4c86a" size 32

screen my_mod_file_slots(my_mod_file_mode):
    tag menu
    modal True
    add Solid("#172334")
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)
        vbox:
            spacing 20
            if my_mod_file_mode == "save":
                text "СОХРАНЕНИЕ" size 40
            else:
                text "ЗАГРУЗКА" size 40
            grid 3 2:
                spacing 20
                for my_mod_file_slot in range(1, 7):
                    button:
                        xsize 380
                        ysize 240
                        if my_mod_file_mode == "save":
                            action FileSave(my_mod_file_slot)
                        else:
                            action FileLoad(my_mod_file_slot)
                        vbox:
                            add FileScreenshot(my_mod_file_slot) xsize 318 ysize 179
                            text FileTime(my_mod_file_slot, empty="Пустой слот") size 20
                            text FileSaveName(my_mod_file_slot) size 18
            hbox:
                spacing 20
                textbutton "Предыдущая страница" action FilePagePrevious()
                textbutton "Следующая страница" action FilePageNext()
                textbutton "Вернуться" action Return()

screen my_mod_save():
    use my_mod_file_slots("save")

screen my_mod_load():
    use my_mod_file_slots("load")

screen my_mod_preferences():
    tag menu
    modal True
    add Solid("#172334")
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 30)
        vbox:
            spacing 20
            text "НАСТРОЙКИ" size 40
            textbutton "Оконный режим" action Preference("display", "window")
            textbutton "Полный экран" action Preference("display", "fullscreen")
            text "Музыка"
            bar value Preference("music volume") xsize 600
            text "Звуки"
            bar value Preference("sound volume") xsize 600
            text "Скорость текста"
            bar value Preference("text speed") xsize 600
            textbutton "Вернуться" action Return()

screen my_mod_skip_indicator():
    zorder 100
    text "ПРОПУСК" color "#f4c86a" size 28 xalign 0.98 yalign 0.05
