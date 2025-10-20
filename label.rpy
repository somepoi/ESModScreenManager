init:
    $ mods["interface_replace"] = "Замена интерфейса"

label test_custom_screens:
    
    # Установка начальных значений
    $ persistent.timeofday = 'day'
    
    # Показываем главное меню (для демо)
    call screen custom_main_menu
    
    # Или запускаем демо напрямую
    jump custom_screens_demo


label interface_replace:
    "Оригинальный интерфейс."

    $ my_mod_screen_save()

    "Сохранение оригинального интерфейса."

    $ my_mod_screen_act()

    "Кастомный интерфейс."

    jump test_custom_screens