# Кастомные экраны - Сохранение, Загрузка, Настройки

# ============================================================================
# ЭКРАН СОХРАНЕНИЯ
# ============================================================================
screen custom_save():
    tag menu
    modal True
    
    default selected_slot = 1
    
    add Solid("#2F4F4F")
    
    frame:
        background Frame(Solid("#48484880"), 20, 20)
        xalign 0.5
        yalign 0.5
        xsize 1600
        ysize 900
        padding (30, 30)
        
        vbox:
            spacing 15
            
            # Заголовок
            hbox:
                xalign 0.5
                spacing 10
                add Solid("#FFD700"):
                    xsize 20
                    ysize 20
                text "СОХРАНЕНИЕ":
                    size 48
                    color "#FFFFFF"
                    bold True
                add Solid("#FFD700"):
                    xsize 20
                    ysize 20
            
            null height 10
            
            # Кнопки действий
            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "Сохранить":
                    background Solid("#228B22")
                    hover_background Solid("#32CD32")
                    xsize 200
                    ysize 50
                    text_color "#FFFFFF"
                    text_size 24
                    text_xalign 0.5
                    text_yalign 0.5
                    action FileSave(selected_slot)
                
                textbutton "Удалить":
                    background Solid("#DC143C")
                    hover_background Solid("#FF0000")
                    xsize 200
                    ysize 50
                    text_color "#FFFFFF"
                    text_size 24
                    text_xalign 0.5
                    text_yalign 0.5
                    action FileDelete(selected_slot)
            
            null height 10
            
            # Слоты сохранений
            viewport:
                xsize 1540
                ysize 650
                scrollbars "vertical"
                mousewheel True
                
                grid 3 4:
                    spacing 20
                    
                    for i in range(1, 13):
                        button:
                            background Frame(Solid("#1C1C1C" if i != selected_slot else "#4169E1"), 5, 5)
                            hover_background Frame(Solid("#2F4F4F" if i != selected_slot else "#5B9BD5"), 5, 5)
                            xsize 490
                            ysize 150
                            action SetScreenVariable("selected_slot", i)
                            
                            vbox:
                                spacing 5
                                xalign 0.5
                                yalign 0.5
                                
                                text "Слот {}".format(i):
                                    size 28
                                    color "#FFD700"
                                    xalign 0.5
                                
                                text FileTime(i, format='%d.%m.%y, %H:%M', empty="Пустой слот"):
                                    size 22
                                    color "#FFFFFF"
                                    xalign 0.5
                                
                                text FileSaveName(i):
                                    size 20
                                    color "#CCCCCC"
                                    xalign 0.5
            
            # Кнопка назад
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
# ЭКРАН ЗАГРУЗКИ
# ============================================================================
screen custom_load():
    tag menu
    modal True
    
    default selected_slot = 1
    
    add Solid("#2F4F4F")
    
    frame:
        background Frame(Solid("#48484880"), 20, 20)
        xalign 0.5
        yalign 0.5
        xsize 1600
        ysize 900
        padding (30, 30)
        
        vbox:
            spacing 15
            
            # Заголовок
            hbox:
                xalign 0.5
                spacing 10
                add Solid("#FFD700"):
                    xsize 20
                    ysize 20
                text "ЗАГРУЗКА":
                    size 48
                    color "#FFFFFF"
                    bold True
                add Solid("#FFD700"):
                    xsize 20
                    ysize 20
            
            null height 10
            
            # Кнопки действий
            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "Загрузить":
                    background Solid("#1E90FF")
                    hover_background Solid("#4169E1")
                    xsize 200
                    ysize 50
                    text_color "#FFFFFF"
                    text_size 24
                    text_xalign 0.5
                    text_yalign 0.5
                    action FileLoad(selected_slot)
                
                textbutton "Удалить":
                    background Solid("#DC143C")
                    hover_background Solid("#FF0000")
                    xsize 200
                    ysize 50
                    text_color "#FFFFFF"
                    text_size 24
                    text_xalign 0.5
                    text_yalign 0.5
                    action FileDelete(selected_slot)
            
            null height 10
            
            # Слоты сохранений
            viewport:
                xsize 1540
                ysize 650
                scrollbars "vertical"
                mousewheel True
                
                grid 3 4:
                    spacing 20
                    
                    for i in range(1, 13):
                        button:
                            background Frame(Solid("#1C1C1C" if i != selected_slot else "#4169E1"), 5, 5)
                            hover_background Frame(Solid("#2F4F4F" if i != selected_slot else "#5B9BD5"), 5, 5)
                            xsize 490
                            ysize 150
                            action SetScreenVariable("selected_slot", i)
                            
                            vbox:
                                spacing 5
                                xalign 0.5
                                yalign 0.5
                                
                                text "Слот {}".format(i):
                                    size 28
                                    color "#FFD700"
                                    xalign 0.5
                                
                                text FileTime(i, format='%d.%m.%y, %H:%M', empty="Пустой слот"):
                                    size 22
                                    color "#FFFFFF"
                                    xalign 0.5
                                
                                text FileSaveName(i):
                                    size 20
                                    color "#CCCCCC"
                                    xalign 0.5
            
            # Кнопка назад
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
# ЭКРАН НАСТРОЕК
# ============================================================================
screen custom_preferences():
    tag menu
    modal True
    
    add Solid("#2F4F4F")
    
    frame:
        background Frame(Solid("#48484880"), 20, 20)
        xalign 0.5
        yalign 0.5
        xsize 1400
        ysize 900
        padding (40, 40)
        
        vbox:
            spacing 20
            
            # Заголовок
            hbox:
                xalign 0.5
                spacing 10
                add Solid("#FFD700"):
                    xsize 20
                    ysize 20
                text "НАСТРОЙКИ":
                    size 48
                    color "#FFFFFF"
                    bold True
                add Solid("#FFD700"):
                    xsize 20
                    ysize 20
            
            null height 20
            
            viewport:
                xsize 1320
                ysize 700
                scrollbars "vertical"
                mousewheel True
                
                vbox:
                    spacing 30
                    
                    # Режим окна
                    vbox:
                        spacing 10
                        
                        text "Режим отображения":
                            size 36
                            color "#FFD700"
                            bold True
                        
                        hbox:
                            spacing 30
                            
                            textbutton ("Полный экран" if _preferences.fullscreen else "[ ] Полный экран"):
                                background Solid("#1E90FF" if _preferences.fullscreen else "#696969")
                                hover_background Solid("#4169E1")
                                xsize 300
                                ysize 50
                                text_color "#FFFFFF"
                                text_size 24
                                text_xalign 0.5
                                text_yalign 0.5
                                action Preference("display", "fullscreen")
                            
                            textbutton ("В окне" if not _preferences.fullscreen else "[ ] В окне"):
                                background Solid("#1E90FF" if not _preferences.fullscreen else "#696969")
                                hover_background Solid("#4169E1")
                                xsize 300
                                ysize 50
                                text_color "#FFFFFF"
                                text_size 24
                                text_xalign 0.5
                                text_yalign 0.5
                                action Preference("display", "window")
                    
                    # Пропуск текста
                    vbox:
                        spacing 10
                        
                        text "Режим пропуска":
                            size 36
                            color "#FFD700"
                            bold True
                        
                        hbox:
                            spacing 30
                            
                            textbutton ("Весь текст" if _preferences.skip_unseen else "[ ] Весь текст"):
                                background Solid("#9370DB" if _preferences.skip_unseen else "#696969")
                                hover_background Solid("#BA55D3")
                                xsize 300
                                ysize 50
                                text_color "#FFFFFF"
                                text_size 24
                                text_xalign 0.5
                                text_yalign 0.5
                                action Preference("skip", "all")
                            
                            textbutton ("Только прочитанный" if not _preferences.skip_unseen else "[ ] Только прочитанный"):
                                background Solid("#9370DB" if not _preferences.skip_unseen else "#696969")
                                hover_background Solid("#BA55D3")
                                xsize 300
                                ysize 50
                                text_color "#FFFFFF"
                                text_size 24
                                text_xalign 0.5
                                text_yalign 0.5
                                action Preference("skip", "seen")
                    
                    # Громкость музыки
                    vbox:
                        spacing 10
                        
                        text "Громкость музыки":
                            size 36
                            color "#FFD700"
                            bold True
                        
                        bar:
                            value Preference("music volume")
                            xsize 800
                            ysize 40
                            left_bar Frame(Solid("#32CD32"), 5, 5)
                            right_bar Frame(Solid("#2F4F4F"), 5, 5)
                            thumb Solid("#FFD700")
                            thumb_offset 10
                    
                    # Громкость звуков
                    vbox:
                        spacing 10
                        
                        text "Громкость звуков":
                            size 36
                            color "#FFD700"
                            bold True
                        
                        bar:
                            value Preference("sound volume")
                            xsize 800
                            ysize 40
                            left_bar Frame(Solid("#1E90FF"), 5, 5)
                            right_bar Frame(Solid("#2F4F4F"), 5, 5)
                            thumb Solid("#FFD700")
                            thumb_offset 10
                    
                    # Скорость текста
                    vbox:
                        spacing 10
                        
                        text "Скорость текста":
                            size 36
                            color "#FFD700"
                            bold True
                        
                        bar:
                            value Preference("text speed")
                            xsize 800
                            ysize 40
                            left_bar Frame(Solid("#FF8C00"), 5, 5)
                            right_bar Frame(Solid("#2F4F4F"), 5, 5)
                            thumb Solid("#FFD700")
                            thumb_offset 10
                    
                    # Автоматическое продвижение
                    vbox:
                        spacing 10
                        
                        text "Автоматическое продвижение":
                            size 36
                            color "#FFD700"
                            bold True
                        
                        bar:
                            value Preference("auto-forward time")
                            xsize 800
                            ysize 40
                            left_bar Frame(Solid("#BA55D3"), 5, 5)
                            right_bar Frame(Solid("#2F4F4F"), 5, 5)
                            thumb Solid("#FFD700")
                            thumb_offset 10
            
            # Кнопка назад
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
                xalign 0.0
