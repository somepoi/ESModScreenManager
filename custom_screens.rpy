# Кастомные экраны без внешних изображений и стилей
# Только код с заливками и примитивами

init python:
    # Цветовые схемы для разных времён суток
    color_schemes = {
        'day': {
            'bg': '#87CEEB',
            'box': '#F0E68C',
            'text': '#2F4F4F',
            'button': '#9ACD32',
            'button_hover': '#7FFF00',
            'accent': '#FFD700'
        },
        'sunset': {
            'bg': '#FF6347',
            'box': '#FFE4B5',
            'text': '#8B4513',
            'button': '#FF8C00',
            'button_hover': '#FFA500',
            'accent': '#FFD700'
        },
        'night': {
            'bg': '#191970',
            'box': '#2F4F4F',
            'text': '#F0F8FF',
            'button': '#4682B4',
            'button_hover': '#5F9EA0',
            'accent': '#87CEEB'
        },
        'prologue': {
            'bg': '#708090',
            'box': '#D3D3D3',
            'text': '#2F4F4F',
            'button': '#B0C4DE',
            'button_hover': '#ADD8E6',
            'accent': '#87CEEB'
        }
    }
    
    def get_color_scheme():
        timeofday = getattr(persistent, 'timeofday', 'day')
        return color_schemes.get(timeofday, color_schemes['day'])

# ============================================================================
# ГЛАВНОЕ МЕНЮ
# ============================================================================
screen custom_main_menu():
    tag menu
    modal True
    
    # Фон с градиентом
    add Solid("#4169E1")
    
    frame:
        background Frame(Solid("#00008B80"), 20, 20)
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        padding (40, 40)
        
        vbox:
            spacing 30
            xalign 0.5
            yalign 0.5
            
            # Заголовок
            text "ГЛАВНОЕ МЕНЮ":
                size 60
                color "#FFD700"
                xalign 0.5
                bold True
                outlines [(3, "#000000", 0, 0)]
            
            null height 30
            
            # Кнопки меню
            vbox:
                spacing 20
                xalign 0.5
                
                textbutton "НОВАЯ ИГРА":
                    xsize 500
                    ysize 60
                    background Frame(Solid("#228B22"), 10, 10)
                    hover_background Frame(Solid("#32CD32"), 10, 10)
                    action Start()
                    text_size 32
                    text_color "#FFFFFF"
                    text_hover_color "#FFFF00"
                    text_xalign 0.5
                    text_yalign 0.5
                
                textbutton "ЗАГРУЗИТЬ":
                    xsize 500
                    ysize 60
                    background Frame(Solid("#1E90FF"), 10, 10)
                    hover_background Frame(Solid("#4169E1"), 10, 10)
                    action ShowMenu('custom_load')
                    text_size 32
                    text_color "#FFFFFF"
                    text_hover_color "#FFFF00"
                    text_xalign 0.5
                    text_yalign 0.5
                
                textbutton "НАСТРОЙКИ":
                    xsize 500
                    ysize 60
                    background Frame(Solid("#9370DB"), 10, 10)
                    hover_background Frame(Solid("#BA55D3"), 10, 10)
                    action ShowMenu('custom_preferences')
                    text_size 32
                    text_color "#FFFFFF"
                    text_hover_color "#FFFF00"
                    text_xalign 0.5
                    text_yalign 0.5
                
                textbutton "ГАЛЕРЕЯ":
                    xsize 500
                    ysize 60
                    background Frame(Solid("#FF8C00"), 10, 10)
                    hover_background Frame(Solid("#FFA500"), 10, 10)
                    action ShowMenu('custom_gallery')
                    text_size 32
                    text_color "#FFFFFF"
                    text_hover_color "#FFFF00"
                    text_xalign 0.5
                    text_yalign 0.5
                
                textbutton "ВЫХОД":
                    xsize 500
                    ysize 60
                    background Frame(Solid("#DC143C"), 10, 10)
                    hover_background Frame(Solid("#FF0000"), 10, 10)
                    action Quit(confirm=False)
                    text_size 32
                    text_color "#FFFFFF"
                    text_hover_color "#FFFF00"
                    text_xalign 0.5
                    text_yalign 0.5

# ============================================================================
# МЕНЮ В ИГРЕ
# ============================================================================
screen custom_game_menu():
    tag menu
    modal True
    
    python:
        scheme = get_color_scheme()
    
    # Полупрозрачный фон
    button:
        background Solid("#00000080")
        xfill True
        yfill True
        action Return()
    
    frame:
        background Frame(Solid(scheme['box'] + "F0"), 15, 15)
        xalign 0.5
        yalign 0.5
        xsize 600
        padding (30, 30)
        
        vbox:
            spacing 20
            
            text "МЕНЮ":
                size 48
                color scheme['text']
                xalign 0.5
                bold True
            
            null height 10
            
            textbutton "Главное меню":
                xsize 540
                ysize 50
                background Solid(scheme['button'])
                hover_background Solid(scheme['button_hover'])
                action MainMenu()
                text_size 28
                text_color "#FFFFFF"
                text_xalign 0.5
                text_yalign 0.5
            
            textbutton "Сохранить":
                xsize 540
                ysize 50
                background Solid(scheme['button'])
                hover_background Solid(scheme['button_hover'])
                action ShowMenu('custom_save')
                text_size 28
                text_color "#FFFFFF"
                text_xalign 0.5
                text_yalign 0.5
            
            textbutton "Загрузить":
                xsize 540
                ysize 50
                background Solid(scheme['button'])
                hover_background Solid(scheme['button_hover'])
                action ShowMenu('custom_load')
                text_size 28
                text_color "#FFFFFF"
                text_xalign 0.5
                text_yalign 0.5
            
            textbutton "Настройки":
                xsize 540
                ysize 50
                background Solid(scheme['button'])
                hover_background Solid(scheme['button_hover'])
                action ShowMenu('custom_preferences')
                text_size 28
                text_color "#FFFFFF"
                text_xalign 0.5
                text_yalign 0.5
            
            textbutton "Вернуться":
                xsize 540
                ysize 50
                background Solid("#696969")
                hover_background Solid("#808080")
                action Return()
                text_size 28
                text_color "#FFFFFF"
                text_xalign 0.5
                text_yalign 0.5
