## Примеры использования улучшенной системы замены экранов

# ======================== PERSISTENT VARIABLES ========================
# Определение persistent переменных для примеров

default persistent.use_custom_interface = False
default persistent.use_custom_menus = False
default persistent.developer_mode = False

# ======================== БАЗОВОЕ ИСПОЛЬЗОВАНИЕ ========================

label mod_start:
    # Проверка совместимости перед активацией
    $ status = mod_screen_manager.check_compatibility()
    if not status:
        "Внимание: версия игры может быть несовместима с модом."
    
    # Активация всех экранов мода
    $ mod_screen_manager.activate_screens()
    "Мод активирован!"
    return

label mod_stop:
    # Деактивация всех экранов мода
    $ mod_screen_manager.deactivate_screens()
    "Мод деактивирован!"
    return

# ======================== ЧАСТИЧНАЯ ЗАМЕНА ЭКРАНОВ ========================

label activate_custom_menu:
    # Активация только главного меню и настроек
    $ mod_activate_partial(["main_menu", "preferences"])
    "Активировано кастомное меню!"
    return

label toggle_custom_save_screen:
    # Переключение экрана сохранения
    $ is_active = mod_toggle_screen("save")
    if is_active:
        "Экран сохранения активирован!"
    else:
        "Экран сохранения деактивирован!"
    return

# ======================== ПОЛУЧЕНИЕ СТАТУСА ========================

label check_mod_status:
    $ status = mod_get_status()
    "Статус мода:"
    "Активен: [status[is_active]]"
    "Активные экраны: [status[active_screens]]"
    "Версия мода: [status[mod_version]]"
    return

# ======================== НАСТРОЙКА КОНФИГУРАЦИИ ========================

init python:
    # Создание кастомной конфигурации
    class MyCustomConfig(ModConfig):
        # Переопределяем параметры
        MOD_NAME = u"Мой Супер Мод"
        MOD_SAVE_IDENTIFIER = "SuperMod"
        MOD_VERSION = "2.0.0"
        
        # Кастомные пути
        MOD_CURSOR_PATH = "mods/supermod/cursor.png"
        MOD_MENU_MUSIC = "mods/supermod/music/menu.mp3"
        
        # Выбираем только нужные экраны
        DEFAULT_SCREENS = [
            "main_menu",
            "save",
            "load",
            "preferences"
        ]
        
        # Включаем подробное логирование для отладки
        ENABLE_LOGGING = True
        LOG_LEVEL = logging.DEBUG
    
    # Создаем менеджер с кастомной конфигурацией
    custom_mod_manager = ModScreenManager(MyCustomConfig)

# ======================== ПРОДВИНУТОЕ ИСПОЛЬЗОВАНИЕ ========================

init python:
    def smart_mod_activation():
        """
        Умная активация мода с проверками и обработкой ошибок.
        """
        manager = mod_screen_manager
        
        # Проверяем совместимость
        if not manager.check_compatibility():
            renpy.notify("Предупреждение: возможна несовместимость с версией игры")
        
        # Пытаемся активировать экраны
        try:
            # Сначала активируем критичные экраны
            critical_screens = ["main_menu", "say", "choice"]
            if not manager.activate_screens(critical_screens, partial=False):
                renpy.notify("Ошибка активации критичных экранов!")
                return False
            
            # Затем добавляем остальные
            optional_screens = ["save", "load", "preferences", "history"]
            manager.activate_screens(optional_screens, partial=True)
            
            renpy.notify("Мод успешно активирован!")
            return True
            
        except Exception as e:
            manager.logger.error(u"Ошибка при активации мода: {}".format(e))
            renpy.notify("Произошла ошибка при активации мода")
            
            # Пытаемся откатить изменения
            manager.deactivate_screens()
            return False
    
    def selective_screen_replacement(screen_list):
        """
        Замена только выбранных экранов с проверкой их существования.
        
        Args:
            screen_list: список имен экранов для замены
        """
        manager = mod_screen_manager
        successful = []
        failed = []
        
        for screen_name in screen_list:
            # Проверяем существование модифицированного экрана
            mod_screen = "my_mod_{}".format(screen_name)
            if manager._screen_exists(mod_screen):
                if manager.activate_screens([screen_name], partial=True):
                    successful.append(screen_name)
                else:
                    failed.append(screen_name)
            else:
                manager.logger.warning(u"Модифицированный экран '{}' не найден".format(mod_screen))
                failed.append(screen_name)
        
        # Отчет о результатах
        if successful:
            renpy.notify(u"Успешно активировано: {}".format(', '.join(successful)))
        if failed:
            renpy.notify(u"Не удалось активировать: {}".format(', '.join(failed)))
        
        return successful, failed

# ======================== ИНТЕГРАЦИЯ С ИГРОЙ ========================

label game_menu_mod_options:
    menu:
        "Управление модом"
        
        "Активировать мод":
            $ smart_mod_activation()
            
        "Деактивировать мод":
            $ mod_screen_manager.deactivate_screens()
            "Мод деактивирован"
            
        "Частичная активация...":
            menu:
                "Какие экраны активировать?"
                
                "Только интерфейс":
                    $ mod_activate_partial(["say", "nvl", "choice"])
                    
                "Только меню":
                    $ mod_activate_partial(["main_menu", "game_menu_selector", "preferences"])
                    
                "Только сохранения":
                    $ mod_activate_partial(["save", "load"])
                    
                "Назад":
                    pass
                    
        "Статус мода":
            call check_mod_status
            
        "Назад":
            return

# ======================== АВТОМАТИЗАЦИЯ ========================

init python:
    # Автоматическая активация при определенных условиях
    def conditional_mod_activation():
        """
        Активация мода в зависимости от условий.
        """
        # Проверяем настройки игрока
        if persistent.use_custom_interface:
            # Активируем интерфейс
            mod_activate_partial(["say", "nvl", "choice", "text_history_screen"])
            
        if persistent.use_custom_menus:
            # Активируем меню
            mod_activate_partial(["main_menu", "preferences", "save", "load"])
            
        if persistent.developer_mode:
            # В режиме разработчика включаем логирование
            mod_screen_manager.logger.setLevel(logging.DEBUG)
    
    # Регистрируем для автозапуска
    config.start_callbacks.append(conditional_mod_activation)

# ======================== ОТЛАДКА И ДИАГНОСТИКА ========================

label debug_mod_system:
    python:
        manager = mod_screen_manager
        
        # Получаем полную информацию
        status = manager.get_status()
        
        # Проверяем все экраны
        all_screens_ok = True
        missing_screens = []
        
        for screen_name in ModConfig.DEFAULT_SCREENS:
            mod_screen = "my_mod_{}".format(screen_name)
            if not manager._screen_exists(mod_screen):
                missing_screens.append(mod_screen)
                all_screens_ok = False
        
        # Выводим отчет
        renpy.say(None, u"=== ДИАГНОСТИКА СИСТЕМЫ МОДОВ ===")
        renpy.say(None, u"Статус: {}".format(u'Активен' if status['is_active'] else u'Неактивен'))
        renpy.say(None, u"Версия мода: {}".format(status['mod_version']))
        renpy.say(None, u"Активные экраны: {}/{}".format(len(status['active_screens']), status['total_screens']))
        
        if status['active_screens']:
            renpy.say(None, u"Список активных: {}".format(', '.join(status['active_screens'])))
        
        if missing_screens:
            renpy.say(None, u"ВНИМАНИЕ! Отсутствующие экраны: {}".format(', '.join(missing_screens)))
        else:
            renpy.say(None, u"Все необходимые экраны найдены")
        
        renpy.say(None, u"Совместимость: {}".format(u'ОК' if manager.check_compatibility() else u'Возможны проблемы'))
    
    return
