# Демонстрационный файл для тестирования кастомных экранов

# Инициализация переменных
init python:
    # Установка времени суток по умолчанию
    if not hasattr(persistent, 'timeofday'):
        persistent.timeofday = 'day'
    
    # Переключатель для использования кастомных экранов
    if not hasattr(persistent, 'use_custom_screens'):
        persistent.use_custom_screens = False

# ============================================================================
# ДЕМО-МЕТКА ДЛЯ ТЕСТИРОВАНИЯ ЭКРАНОВ
# ============================================================================
label custom_screens_demo:
    
    scene bg black
    
    "Добро пожаловать в демонстрацию кастомных экранов!"
    "Все экраны созданы исключительно кодом, без внешних изображений."
    
    menu demo_menu:
        "Что вы хотите посмотреть?"
        
        "Тест диалогового окна":
            jump test_dialogue
        
        "Тест выборов":
            jump test_choices
        
        "Тест меню и навигации":
            jump test_menus
        
        "Тест цветовых схем":
            jump test_color_schemes
        
        "Тест сохранения/загрузки":
            call screen custom_save
            jump demo_menu
        
        "Выйти из демо":
            return

# ============================================================================
# ТЕСТ ДИАЛОГОВ
# ============================================================================
label test_dialogue:
    
    scene bg black
    
    "Это демонстрация диалогового окна."
    "Обратите внимание на кнопки управления в правом нижнем углу."
    
    me "Привет! Это тестовое сообщение от персонажа."
    me "Диалоговое окно адаптируется к времени суток."
    
    sl "Я Славя. Приятно познакомиться!"
    sl "Каждый персонаж может иметь свой цвет имени."
    
    un "А я Лена. Тоже рада знакомству."
    
    "Вы можете открыть историю диалогов с помощью кнопки 'H'."
    "Или сохранить игру кнопкой 'S'."
    
    menu:
        "Вернуться в главное меню демо?"
        
        "Да":
            jump demo_menu
        
        "Показать ещё диалоги":
            pass
    
    "Хорошо, продолжим."
    
    me "Это многострочный диалог.\nОн может содержать несколько строк текста.\nИ автоматически подстраивается под размер окна."
    
    "Теперь вернёмся в меню."
    
    jump demo_menu

# ============================================================================
# ТЕСТ ВЫБОРОВ
# ============================================================================
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
    
    "Отлично! Выбор сделан."
    
    menu:
        "Давайте попробуем выбор с разными цветами (зависит от времени суток)."
        
        "Вариант А":
            $ choice_result = "A"
        
        "Вариант Б":
            $ choice_result = "B"
        
        "Вариант В":
            $ choice_result = "C"
    
    "Вы выбрали вариант [choice_result]."
    
    jump demo_menu

# ============================================================================
# ТЕСТ МЕНЮ И НАВИГАЦИИ
# ============================================================================
label test_menus:
    
    scene bg black
    
    "Давайте протестируем различные меню."
    
    menu:
        "Какое меню открыть?"
        
        "Игровое меню (ESC)":
            call screen custom_game_menu
        
        "Настройки":
            call screen custom_preferences
        
        "Галерея":
            call screen custom_gallery
        
        "Музыкальная комната":
            call screen custom_music_room
        
        "Об игре":
            call screen custom_about
        
        "Назад":
            jump demo_menu
    
    jump test_menus

# ============================================================================
# ТЕСТ ЦВЕТОВЫХ СХЕМ
# ============================================================================
label test_color_schemes:
    
    scene bg black
    
    "Сейчас мы переключим разные цветовые схемы."
    "Каждая схема соответствует своему времени суток."
    
    menu:
        "Выберите время суток:"
        
        "День (Day)":
            $ persistent.timeofday = 'day'
            "Установлена дневная схема (светлые тона)."
        
        "Закат (Sunset)":
            $ persistent.timeofday = 'sunset'
            "Установлена закатная схема (тёплые оранжевые тона)."
        
        "Ночь (Night)":
            $ persistent.timeofday = 'night'
            "Установлена ночная схема (тёмные холодные тона)."
        
        "Пролог (Prologue)":
            $ persistent.timeofday = 'prologue'
            "Установлена схема пролога (серые тона)."
        
        "Вернуться в меню":
            jump demo_menu
    
    "Обратите внимание, как изменились цвета диалогового окна и кнопок."
    
    menu:
        "Открыть какое-нибудь меню, чтобы увидеть изменения?"
        
        "Да, открыть настройки":
            call screen custom_preferences
            jump test_color_schemes
        
        "Да, открыть игровое меню":
            call screen custom_game_menu
            jump test_color_schemes
        
        "Нет, вернуться":
            jump demo_menu

# ============================================================================
# ТЕСТОВАЯ МЕТКА ЗАПУСКА
# ============================================================================
label test_custom_screens:
    
    # Установка начальных значений
    $ persistent.timeofday = 'day'
    
    # Показываем главное меню (для демо)
    call screen custom_main_menu
    
    # Или запускаем демо напрямую
    jump custom_screens_demo

# ============================================================================
# БЫСТРОЕ ТЕСТИРОВАНИЕ ВСЕХ ЭКРАНОВ
# ============================================================================
label quick_test_all_screens:
    
    "=== БЫСТРОЕ ТЕСТИРОВАНИЕ ВСЕХ ЭКРАНОВ ==="
    
    "1. Тест главного меню..."
    # call screen custom_main_menu
    
    "2. Тест игрового меню..."
    call screen custom_game_menu
    
    "3. Тест сохранения..."
    call screen custom_save
    
    "4. Тест загрузки..."
    call screen custom_load
    
    "5. Тест настроек..."
    call screen custom_preferences
    
    "6. Тест галереи..."
    call screen custom_gallery
    
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
    "Первая строка для истории."
    "Вторая строка для истории."
    "Третья строка для истории."
    call screen custom_text_history
    
    "10. Тест подтверждения..."
    call screen custom_yesno_prompt(
        "Это тестовое подтверждение. Продолжить?",
        Return(),
        Return()
    )
    
    "=== ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ ==="
    
    return

# ============================================================================
# ИНТЕГРАЦИЯ С ОСНОВНОЙ ИГРОЙ
# ============================================================================

# Добавить в options.rpy или в начало скрипта:
# 
# init python:
#     # Если хотите использовать кастомные экраны по умолчанию
#     config.main_menu_screen = "custom_main_menu"
#     config.game_menu_screen = "custom_game_menu"

# Или создать переключатель:
# 
# init python:
#     def toggle_custom_screens():
#         persistent.use_custom_screens = not persistent.use_custom_screens
#         if persistent.use_custom_screens:
#             config.main_menu_screen = "custom_main_menu"
#             config.game_menu_screen = "custom_game_menu"
#         else:
#             config.main_menu_screen = "main_menu"
#             config.game_menu_screen = "game_menu_selector"
#         renpy.utter_restart()

# ============================================================================
# ДЕМО-МЕНЮ ДЛЯ РАЗРАБОТЧИКА
# ============================================================================
screen developer_custom_screens_menu():
    modal True
    
    frame:
        background Solid("#2F4F4F")
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        
        vbox:
            spacing 20
            
            text "МЕНЮ РАЗРАБОТЧИКА - КАСТОМНЫЕ ЭКРАНЫ":
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
                action ShowMenu("custom_main_menu")
            
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

# Для запуска меню разработчика добавьте в игру:
# call screen developer_custom_screens_menu()
