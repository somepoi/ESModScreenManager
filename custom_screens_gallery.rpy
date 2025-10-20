# Кастомные экраны - Галерея и дополнительные экраны

# ============================================================================
# ГАЛЕРЕЯ
# ============================================================================
screen custom_gallery():
    tag menu
    modal True
    
    default page = 0
    default items_per_page = 12
    default total_items = 24  # Заглушка, можно заменить на реальное количество
    
    add Solid("#1C1C1C")
    
    frame:
        background Frame(Solid("#2F4F4F80"), 20, 20)
        xalign 0.5
        yalign 0.5
        xsize 1600
        ysize 900
        padding (30, 30)
        
        vbox:
            spacing 20
            
            # Заголовок
            hbox:
                xalign 0.5
                spacing 10
                add Solid("#FFD700"):
                    xsize 20
                    ysize 20
                text "ГАЛЕРЕЯ":
                    size 48
                    color "#FFFFFF"
                    bold True
                add Solid("#FFD700"):
                    xsize 20
                    ysize 20
            
            null height 20
            
            # Сетка изображений (заглушки)
            grid 4 3:
                spacing 20
                xalign 0.5
                
                for i in range(items_per_page):
                    python:
                        item_index = page * items_per_page + i
                        is_unlocked = item_index < 10  # Заглушка для разблокированных
                    
                    button:
                        background Frame(Solid("#4682B4" if is_unlocked else "#2F4F4F"), 5, 5)
                        hover_background Frame(Solid("#5F9EA0" if is_unlocked else "#404040"), 5, 5)
                        xsize 370
                        ysize 210
                        
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 10
                            
                            # Иконка или номер
                            if is_unlocked:
                                add Solid("#87CEEB"):
                                    xsize 80
                                    ysize 80
                                    xalign 0.5
                                text "CG {}".format(item_index + 1):
                                    size 24
                                    color "#FFFFFF"
                                    xalign 0.5
                            else:
                                add Solid("#696969"):
                                    xsize 80
                                    ysize 80
                                    xalign 0.5
                                text "Закрыто":
                                    size 24
                                    color "#808080"
                                    xalign 0.5
            
            # Навигация
            hbox:
                spacing 30
                xalign 0.5
                
                if page > 0:
                    textbutton "< Назад":
                        background Solid("#4682B4")
                        hover_background Solid("#5F9EA0")
                        xsize 150
                        ysize 50
                        text_color "#FFFFFF"
                        text_size 24
                        text_xalign 0.5
                        text_yalign 0.5
                        action SetScreenVariable("page", page - 1)
                else:
                    null width 150
                
                text "Страница {}/{}".format(page + 1, (total_items // items_per_page) + 1):
                    size 28
                    color "#FFFFFF"
                    yalign 0.5
                
                if (page + 1) * items_per_page < total_items:
                    textbutton "Вперед >":
                        background Solid("#4682B4")
                        hover_background Solid("#5F9EA0")
                        xsize 150
                        ysize 50
                        text_color "#FFFFFF"
                        text_size 24
                        text_xalign 0.5
                        text_yalign 0.5
                        action SetScreenVariable("page", page + 1)
                else:
                    null width 150
            
            # Кнопка назад
            textbutton "Вернуться в меню":
                background Solid("#696969")
                hover_background Solid("#808080")
                xsize 250
                ysize 50
                text_color "#FFFFFF"
                text_size 24
                text_xalign 0.5
                text_yalign 0.5
                action Return()
                xalign 0.5

# ============================================================================
# МУЗЫКАЛЬНАЯ КОМНАТА
# ============================================================================
screen custom_music_room():
    tag menu
    modal True
    
    default current_track = 0
    
    python:
        music_list = [
            ("Трек 1", "music/track1.ogg"),
            ("Трек 2", "music/track2.ogg"),
            ("Трек 3", "music/track3.ogg"),
            ("Трек 4", "music/track4.ogg"),
            ("Трек 5", "music/track5.ogg"),
        ]
    
    add Solid("#1C1C1C")
    
    frame:
        background Frame(Solid("#2F4F4F80"), 20, 20)
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 800
        padding (40, 40)
        
        vbox:
            spacing 30
            
            # Заголовок
            hbox:
                xalign 0.5
                spacing 10
                add Solid("#FFD700"):
                    xsize 20
                    ysize 20
                text "МУЗЫКАЛЬНАЯ КОМНАТА":
                    size 48
                    color "#FFFFFF"
                    bold True
                add Solid("#FFD700"):
                    xsize 20
                    ysize 20
            
            null height 20
            
            # Список треков
            viewport:
                xsize 1120
                ysize 550
                scrollbars "vertical"
                mousewheel True
                
                vbox:
                    spacing 15
                    
                    for i, (name, track) in enumerate(music_list):
                        textbutton name:
                            xsize 1100
                            ysize 60
                            background Solid("#4682B4" if i == current_track else "#2F4F4F")
                            hover_background Solid("#5F9EA0")
                            action [SetScreenVariable("current_track", i), Play("music", track)]
                            text_size 28
                            text_color "#FFFFFF"
                            text_xalign 0.5
                            text_yalign 0.5
            
            # Кнопки управления
            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "Стоп":
                    background Solid("#DC143C")
                    hover_background Solid("#FF0000")
                    xsize 150
                    ysize 50
                    text_color "#FFFFFF"
                    text_size 24
                    text_xalign 0.5
                    text_yalign 0.5
                    action Stop("music")
                
                textbutton "Назад":
                    background Solid("#696969")
                    hover_background Solid("#808080")
                    xsize 150
                    ysize 50
                    text_color "#FFFFFF"
                    text_size 24
                    text_xalign 0.5
                    text_yalign 0.5
                    action Return()

# ============================================================================
# ЭКРАН "ОБ ИГРЕ"
# ============================================================================
screen custom_about():
    tag menu
    modal True
    
    add Solid("#2F4F4F")
    
    frame:
        background Frame(Solid("#48484880"), 20, 20)
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 800
        padding (50, 50)
        
        vbox:
            spacing 30
            
            # Заголовок
            text "ОБ ИГРЕ":
                size 54
                color "#FFD700"
                bold True
                xalign 0.5
            
            null height 20
            
            # Информация
            viewport:
                xsize 1100
                ysize 600
                scrollbars "vertical"
                mousewheel True
                
                vbox:
                    spacing 20
                    
                    text "Название игры:":
                        size 32
                        color "#87CEEB"
                        bold True
                    
                    text "Кастомная визуальная новелла":
                        size 28
                        color "#FFFFFF"
                    
                    null height 20
                    
                    text "Версия:":
                        size 32
                        color "#87CEEB"
                        bold True
                    
                    text "1.0.0":
                        size 28
                        color "#FFFFFF"
                    
                    null height 20
                    
                    text "Описание:":
                        size 32
                        color "#87CEEB"
                        bold True
                    
                    text "Это кастомные экраны, созданные только с использованием кода, без внешних изображений и стилей. Все элементы интерфейса нарисованы с помощью заливок Solid, Frame и других примитивов Ren'Py.":
                        size 28
                        color "#FFFFFF"
                        xmaximum 1080
                    
                    null height 20
                    
                    text "Особенности:":
                        size 32
                        color "#87CEEB"
                        bold True
                    
                    text "• Динамические цветовые схемы\n• Адаптивность к времени суток\n• Полностью кодовая реализация\n• Без зависимостей от внешних ресурсов":
                        size 28
                        color "#FFFFFF"
                        xmaximum 1080
            
            # Кнопка назад
            textbutton "Назад":
                background Solid("#696969")
                hover_background Solid("#808080")
                xsize 200
                ysize 60
                text_color "#FFFFFF"
                text_size 28
                text_xalign 0.5
                text_yalign 0.5
                action Return()
                xalign 0.5

# ============================================================================
# БЫСТРОЕ МЕНЮ (для использования во время игры)
# ============================================================================
screen custom_quick_menu():
    zorder 100
    
    python:
        scheme = get_color_scheme()
    
    hbox:
        xalign 0.5
        yalign 0.97
        spacing 15
        
        textbutton "Назад":
            background Frame(Solid(scheme['button'] + "B0"), 5, 5)
            hover_background Frame(Solid(scheme['button_hover'] + "B0"), 5, 5)
            xsize 100
            ysize 40
            text_size 20
            text_color "#FFFFFF"
            text_xalign 0.5
            text_yalign 0.5
            action Rollback()
        
        textbutton "История":
            background Frame(Solid(scheme['button'] + "B0"), 5, 5)
            hover_background Frame(Solid(scheme['button_hover'] + "B0"), 5, 5)
            xsize 100
            ysize 40
            text_size 20
            text_color "#FFFFFF"
            text_xalign 0.5
            text_yalign 0.5
            action ShowMenu("custom_text_history")
        
        textbutton "Пропуск":
            background Frame(Solid(scheme['button'] + "B0"), 5, 5)
            hover_background Frame(Solid(scheme['button_hover'] + "B0"), 5, 5)
            xsize 100
            ysize 40
            text_size 20
            text_color "#FFFFFF"
            text_xalign 0.5
            text_yalign 0.5
            action Skip()
        
        textbutton "Авто":
            background Frame(Solid(scheme['button'] + "B0"), 5, 5)
            hover_background Frame(Solid(scheme['button_hover'] + "B0"), 5, 5)
            xsize 100
            ysize 40
            text_size 20
            text_color "#FFFFFF"
            text_xalign 0.5
            text_yalign 0.5
            action Preference("auto-forward", "toggle")
        
        textbutton "Сохранить":
            background Frame(Solid(scheme['button'] + "B0"), 5, 5)
            hover_background Frame(Solid(scheme['button_hover'] + "B0"), 5, 5)
            xsize 120
            ysize 40
            text_size 20
            text_color "#FFFFFF"
            text_xalign 0.5
            text_yalign 0.5
            action ShowMenu("custom_save")
        
        textbutton "Загрузить":
            background Frame(Solid(scheme['button'] + "B0"), 5, 5)
            hover_background Frame(Solid(scheme['button_hover'] + "B0"), 5, 5)
            xsize 120
            ysize 40
            text_size 20
            text_color "#FFFFFF"
            text_xalign 0.5
            text_yalign 0.5
            action ShowMenu("custom_load")
        
        textbutton "Настройки":
            background Frame(Solid(scheme['button'] + "B0"), 5, 5)
            hover_background Frame(Solid(scheme['button_hover'] + "B0"), 5, 5)
            xsize 120
            ysize 40
            text_size 20
            text_color "#FFFFFF"
            text_xalign 0.5
            text_yalign 0.5
            action ShowMenu("custom_preferences")
        
        textbutton "Меню":
            background Frame(Solid(scheme['button'] + "B0"), 5, 5)
            hover_background Frame(Solid(scheme['button_hover'] + "B0"), 5, 5)
            xsize 100
            ysize 40
            text_size 20
            text_color "#FFFFFF"
            text_xalign 0.5
            text_yalign 0.5
            action ShowMenu("custom_game_menu")
