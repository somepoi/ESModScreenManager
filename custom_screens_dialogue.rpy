# Кастомные экраны - Диалоги, Выборы, Уведомления

# ============================================================================
# ЭКРАН ВЫБОРА
# ============================================================================
screen custom_choice(items):
    modal True
    
    python:
        scheme = get_color_scheme()
    
    # Полупрозрачный фон
    add Solid("#00000060")
    
    frame:
        background Frame(Solid(scheme['box'] + "E0"), 20, 20)
        xalign 0.5
        yalign 0.5
        xmaximum 1200
        padding (50, 50)
        
        vbox:
            spacing 25
            xalign 0.5
            
            for i, (caption, action, chosen) in enumerate(items):
                if action:
                    textbutton caption:
                        xsize 1100
                        ysize 70
                        background Frame(Solid(scheme['button']), 10, 10)
                        hover_background Frame(Solid(scheme['button_hover']), 10, 10)
                        selected_background Frame(Solid(scheme['accent']), 10, 10)
                        action action
                        text_size 30
                        text_color scheme['text']
                        text_hover_color "#FFFFFF"
                        text_xalign 0.5
                        text_yalign 0.5
                        text_outlines [(2, "#000000", 0, 0)]
                else:
                    text caption:
                        size 36
                        color scheme['text']
                        xalign 0.5
                        bold True
                        text_align 0.5

# ============================================================================
# ДИАЛОГОВОЕ ОКНО
# ============================================================================
screen custom_say(who, what):
    
    python:
        scheme = get_color_scheme()
    
    window:
        id "window"
        background None
        
        # Диалоговое окно внизу экрана
        frame:
            background Frame(Solid(scheme['box'] + "D0"), 15, 15)
            xpos 100
            ypos 850
            xsize 1720
            ysize 200
            padding (30, 20)
            
            vbox:
                spacing 10
                
                # Имя персонажа
                if who:
                    text who:
                        size 28
                        color scheme['text']
                        bold True
                        outlines [(2, "#000000", 0, 0)]
                
                # Текст диалога
                text what:
                    id "what"
                    size 26
                    color scheme['text']
                    xmaximum 1660
                    outlines [(1, "#00000080", 0, 0)]
        
        # Кнопки управления
        hbox:
            xalign 0.98
            yalign 0.98
            spacing 10
            
            textbutton "H":
                background Solid(scheme['button'] + "C0")
                hover_background Solid(scheme['button_hover'] + "C0")
                xsize 50
                ysize 50
                text_size 24
                text_color "#FFFFFF"
                text_xalign 0.5
                text_yalign 0.5
                action ShowMenu("custom_text_history")
                tooltip "История"
            
            textbutton "S":
                background Solid(scheme['button'] + "C0")
                hover_background Solid(scheme['button_hover'] + "C0")
                xsize 50
                ysize 50
                text_size 24
                text_color "#FFFFFF"
                text_xalign 0.5
                text_yalign 0.5
                action ShowMenu('custom_save')
                tooltip "Сохранить"
            
            textbutton "M":
                background Solid(scheme['button'] + "C0")
                hover_background Solid(scheme['button_hover'] + "C0")
                xsize 50
                ysize 50
                text_size 24
                text_color "#FFFFFF"
                text_xalign 0.5
                text_yalign 0.5
                action ShowMenu('custom_game_menu')
                tooltip "Меню"
            
            if config.skipping:
                textbutton "||":
                    background Solid(scheme['button'] + "C0")
                    hover_background Solid(scheme['button_hover'] + "C0")
                    xsize 50
                    ysize 50
                    text_size 24
                    text_color "#FFFFFF"
                    text_xalign 0.5
                    text_yalign 0.5
                    action Skip()
                    tooltip "Пропуск"
            else:
                textbutton ">":
                    background Solid(scheme['button'] + "C0")
                    hover_background Solid(scheme['button_hover'] + "C0")
                    xsize 50
                    ysize 50
                text_size 24
                text_color "#FFFFFF"
                text_xalign 0.5
                text_yalign 0.5
                action Skip()
                tooltip "Пропуск"

# ============================================================================
# NVL ДИАЛОГОВОЕ ОКНО
# ============================================================================
screen custom_nvl(dialogue, items=None):
    
    python:
        scheme = get_color_scheme()
    
    window:
        background Frame(Solid(scheme['box'] + "E0"), 30, 30)
        xfill True
        yfill True
        padding (100, 100)
        
        has vbox:
            spacing 10
        
        # Отображение диалогов
        for who, what, who_id, what_id, window_id in dialogue:
            hbox:
                spacing 20
                
                if who is not None:
                    text who:
                        id who_id
                        size 28
                        color scheme['text']
                        bold True
                        min_width 200
                
                text what:
                    id what_id
                    size 26
                    color scheme['text']
        
        # Отображение выборов если есть
        if items:
            null height 20
            
            vbox:
                spacing 15
                
                for caption, action, chosen in items:
                    if action:
                        textbutton caption:
                            xsize 800
                            ysize 60
                            background Solid(scheme['button'])
                            hover_background Solid(scheme['button_hover'])
                            action action
                            text_size 26
                            text_color "#FFFFFF"
                            text_xalign 0.5
                            text_yalign 0.5
                    else:
                        text caption:
                            size 28
                            color scheme['text']
                            bold True

# ============================================================================
# ПОДТВЕРЖДЕНИЕ ДЕЙСТВИЯ
# ============================================================================
screen custom_yesno_prompt(message, yes_action, no_action):
    modal True
    
    add Solid("#00000080")
    
    frame:
        background Frame(Solid("#2F4F4F"), 20, 20)
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 350
        padding (40, 40)
        
        vbox:
            spacing 40
            xalign 0.5
            yalign 0.5
            
            text message:
                size 32
                color "#FFFFFF"
                xalign 0.5
                text_align 0.5
                xmaximum 620
            
            hbox:
                spacing 50
                xalign 0.5
                
                textbutton "ДА":
                    xsize 250
                    ysize 70
                    background Solid("#228B22")
                    hover_background Solid("#32CD32")
                    action yes_action
                    text_size 36
                    text_color "#FFFFFF"
                    text_xalign 0.5
                    text_yalign 0.5
                
                textbutton "НЕТ":
                    xsize 250
                    ysize 70
                    background Solid("#DC143C")
                    hover_background Solid("#FF0000")
                    action no_action
                    text_size 36
                    text_color "#FFFFFF"
                    text_xalign 0.5
                    text_yalign 0.5

# ============================================================================
# УВЕДОМЛЕНИЯ
# ============================================================================
screen custom_notify(message):
    modal False
    zorder 100
    
    python:
        scheme = get_color_scheme()
    
    if not config.skipping:
        frame:
            background Frame(Solid(scheme['box']), 15, 15)
            xalign 0.02
            yalign 0.02
            padding (30, 20)
            at notify_appear
            
            text message:
                size 28
                color scheme['text']
                xmaximum 400
    else:
        timer 0.01 action Hide('custom_notify')

# Трансформация для появления уведомлений
transform notify_appear:
    on show:
        alpha 0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

# ============================================================================
# ИСТОРИЯ ТЕКСТА
# ============================================================================
screen custom_text_history():
    tag menu
    modal True
    
    python:
        scheme = get_color_scheme()
    
    # Фон
    button:
        background Solid("#00000080")
        xfill True
        yfill True
        action Return()
    
    frame:
        background Frame(Solid(scheme['box']), 20, 20)
        xalign 0.5
        yalign 0.5
        xsize 1600
        ysize 900
        padding (40, 40)
        
        vbox:
            spacing 20
            
            # Заголовок
            text "ИСТОРИЯ ДИАЛОГОВ":
                size 42
                color scheme['text']
                bold True
                xalign 0.5
            
            null height 10
            
            # Прокручиваемая область с историей
            viewport:
                id "text_history_viewport"
                xsize 1520
                ysize 750
                scrollbars "vertical"
                mousewheel True
                yinitial 1.0
                
                vbox:
                    spacing 15
                    
                    for h in _history_list:
                        hbox:
                            spacing 20
                            
                            # Имя персонажа
                            if h.who:
                                text h.who:
                                    size 26
                                    color scheme['accent']
                                    bold True
                                    min_width 200
                            else:
                                null width 200
                            
                            # Текст диалога
                            textbutton h.what:
                                background None
                                hover_background None
                                action RollbackToIdentifier(h.rollback_identifier)
                                text_size 24
                                text_color scheme['text']
                                text_hover_color scheme['button_hover']
                                xmaximum 1280
            
            # Кнопка закрытия
            textbutton "Закрыть":
                background Solid("#696969")
                hover_background Solid("#808080")
                xsize 200
                ysize 50
                text_color "#FFFFFF"
                text_size 26
                text_xalign 0.5
                text_yalign 0.5
                action Return()
                xalign 0.5

# ============================================================================
# ИНДИКАТОР ПРОПУСКА
# ============================================================================
screen custom_skip_indicator():
    zorder 100
    
    python:
        scheme = get_color_scheme()
    
    frame:
        background Frame(Solid(scheme['box']), 10, 10)
        xalign 0.5
        yalign 0.98
        padding (20, 10)
        
        hbox:
            spacing 15
            
            text "ПРОПУСК":
                size 28
                color scheme['text']
                bold True
            
            # Анимированные стрелки
            text ">":
                size 28
                color scheme['accent']
                at delayed_blink(0.0, 1.0)
            
            text ">":
                size 28
                color scheme['accent']
                at delayed_blink(0.2, 1.0)
            
            text ">":
                size 28
                color scheme['accent']
                at delayed_blink(0.4, 1.0)

# Трансформация для мигающих стрелок
transform delayed_blink(delay, cycle):
    alpha 0.5
    pause delay
    block:
        linear 0.2 alpha 1.0
        pause 0.2
        linear 0.2 alpha 0.5
        pause (cycle - 0.4)
        repeat
