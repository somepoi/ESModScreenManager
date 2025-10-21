init:
    $ mods["interface_replace"] = "Замена интерфейса"

label interface_replace:
    "Оригинальный интерфейс."

    $ my_mod_screen_act()

    "Кастомный интерфейс."

    call screen developer_custom_screens_menu()

    return

label custom_screens_demo:
    
    scene bg black
    
    menu demo_menu:
        "Что вы хотите посмотреть?"
        
        "Тест диалогового окна":
            jump test_dialogue
        
        "Тест выборов":
            jump test_choices
        
        "Тест меню и навигации":
            jump test_menus

        "Тест сохранения/загрузки":
            call screen my_mod_save
            jump demo_menu

        "Тест цветовых схем":
            jump test_color_schemes
                
        "Выйти из демо":
            return

label test_dialogue:
    
    scene bg black
    
    "Это демонстрация диалогового окна."
    "Обратите внимание на кнопки управления в правом нижнем углу."
    
    me "Привет! Это тестовое сообщение от персонажа."
    me "Диалоговое окно адаптируется к времени суток."
    
    "Вы можете открыть историю диалогов с помощью кнопки 'H'."
    "Или сохранить игру кнопкой 'S'."
    
    jump demo_menu

label test_choices:
    
    scene bg black
    
    "Сейчас будет показан экран выбора с несколькими вариантами."
    
    menu:
        "Это заголовок меню выбора"
        
        "Первый вариант":
            "Вы выбрали первый вариант."
        
        "Второй вариант":
            "Вы выбрали второй вариант."
        
        "Третий вариант":
            "Вы выбрали третий вариант."
        
        "Очень длинный вариант текста, который демонстрирует, как экран выбора обрабатывает длинные строки":
            "Вы выбрали длинный вариант."
    
    jump demo_menu

label test_menus:
    
    scene bg black
    
    menu:
        "Какое меню открыть?"
        
        "Игровое меню (ESC)":
            call screen my_mod_game_menu_selector
        
        "Настройки":
            call screen my_mod_preferences
        
        "Галерея":
            call screen my_mod_gallery
        
        "Музыкальная комната":
            call screen my_mod_music_room
        
        "Об игре":
            call screen my_mod_about # TODO заменить about на help
        
        "Назад":
            jump demo_menu
    
    jump test_menus

label test_color_schemes:
    
    scene bg black
    
    menu:
        "Выберите время суток:"
        
        "День (Day)":
            $ persistent.timeofday = 'day'
            "Установлена дневная схема."
        
        "Закат (Sunset)":
            $ persistent.timeofday = 'sunset'
            "Установлена вечерняя схема."
        
        "Ночь (Night)":
            $ persistent.timeofday = 'night'
            "Установлена ночная схема."
        
        "Пролог (Prologue)":
            $ persistent.timeofday = 'prologue'
            "Установлена схема пролога."
        
        "Вернуться в меню":
            jump demo_menu
    
    jump test_color_schemes

label quick_test_all_screens:
    
    "1. Тест главного меню делайте в меню разработчика."
    
    "2. Тест игрового меню..."
    call screen my_mod_game_menu_selector
    
    "3. Тест сохранения..."
    call screen my_mod_save
    
    "4. Тест загрузки..."
    call screen my_mod_load
    
    "5. Тест настроек..."
    call screen my_mod_preferences
    
    "6. Тест галереи..."
    call screen my_mod_gallery
    
    "7. Тест выбора..."
    menu:
        "Тестовый выбор?"
        "Да":
            pass
        "Нет":
            pass
    
    "8. Тест уведомления..."
    $ renpy.notify("Тестовое уведомление!")
    pause 2.0
    
    "9. Тест истории текста..."
    call screen my_mod_text_history_screen
    
    "10. Тест подтверждения..."
    call screen my_mod_yesno_prompt(
        "Это тестовое подтверждение. Продолжить?",
        Return(),
        Return()
    )
    
    call screen developer_custom_screens_menu()

    return

screen developer_custom_screens_menu():
    modal True
    
    frame:
        background Solid("#2F4F4F")
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        
        vbox:
            spacing 20
            
            text "КАСТОМНЫЕ ЭКРАНЫ":
                size 36
                color "#FFD700"
                bold True
            
            null height 20
            
            textbutton "Запустить полное демо":
                xsize 400
                ysize 50
                background Solid("#1E90FF")
                hover_background Solid("#4169E1")
                text_color "#FFFFFF"
                text_size 24
                text_xalign 0.5
                text_yalign 0.5
                action Jump("custom_screens_demo")
            
            textbutton "Быстрое тестирование всех экранов":
                xsize 400
                ysize 50
                background Solid("#9370DB")
                hover_background Solid("#BA55D3")
                text_color "#FFFFFF"
                text_size 24
                text_xalign 0.5
                text_yalign 0.5
                action Jump("quick_test_all_screens")
            
            textbutton "Главное меню (кастомное)":
                xsize 400
                ysize 50
                background Solid("#228B22")
                hover_background Solid("#32CD32")
                text_color "#FFFFFF"
                text_size 24
                text_xalign 0.5
                text_yalign 0.5
                action ShowMenu("my_mod_main_menu")
            
            textbutton "Закрыть":
                xsize 400
                ysize 50
                background Solid("#696969")
                hover_background Solid("#808080")
                text_color "#FFFFFF"
                text_size 24
                text_xalign 0.5
                text_yalign 0.5
                action Return()
