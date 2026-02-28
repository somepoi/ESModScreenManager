"""генератор конфига - создает питоновский класс конфига"""

from typing import List
from .config_data import ConfigData


class ConfigGenerator:
    """генерирует класс ModScreenManagerConfig"""
    
    def generate(self, config: ConfigData) -> str:
        """
        сгенерировать код класса конфига
        
        Args:
            config: данные конфига
            
        Returns:
            сгенерированный код
        """
        # билдим класс
        lines = [
            "# НЕ ЗАБУДЬТЕ ЗАМЕНИТЬ {0} НА ПРЕФИКС СВОЕГО МОДА".format(config.mod_id),
            "",
            "init python:",
            "    # Кастомный конфиг на основе шаблона",
            "    class {0}_ModScreenManagerConfig(ModScreenManagerConfig):".format(config.mod_id),
            "        # Переопределяем параметры",
            "        # Для опциональных параметров можем указать \"\" или False, если не хотим менять",
            "",
            "        # Имя мода",
            "        # БЕЗ ШРИФТОВ, ЦВЕТА И ПРОЧИХ ТЕГОВ",
            '        MOD_NAME = u"{0}"'.format(config.mod_name),
            "",
            "        # Префикс мода",
            "        # МОЖЕТ БЫТЬ АБСОЛЮТНОЕ ЛЮБОЕ СЛОВО ИЛИ СЛОВОСОЧЕТАНИЕ",
            '        MOD_ID = "{0}"'.format(config.mod_id),
            "",
            "        # Имя мода в сохранении",
            '        MOD_SAVE_IDENTIFIER = "{0}"'.format(config.mod_save_identifier),
            "",
            "        # Замена имени окна",
            "        MOD_REPLACE_WINDOW_NAME = {0}".format(
                str(config.replace_window_name).lower()
            ),
            "",
            "        # Свой курсор",
        ]
        
        # добавляем путь к курсору
        if config.cursor_path:
            lines.append('        MOD_CURSOR_PATH = "{0}"'.format(config.cursor_path))
        else:
            lines.append("        MOD_CURSOR_PATH = False")
        
        lines.extend([
            "",
            "        # Свой трек в главном меню",
        ])
        
        # добавляем музыку
        if config.menu_music:
            lines.append('        MOD_MENU_MUSIC = "{0}"'.format(config.menu_music))
        else:
            lines.append("        MOD_MENU_MUSIC = False")
        
        lines.extend([
            "",
            "        # Выбираем экраны",
            "        DEFAULT_SCREENS = [",
        ])
        
        # добавляем экраны с комментами
        for screen in config.selected_screens:
            comment = self._get_screen_comment(screen)
            lines.append('            "{0}",  # {1}'.format(screen, comment))
        
        lines.extend([
            "        ]",
            "",
            "        # логирование",
            "        LOGGING = {0}".format(str(config.logging).lower()),
            "        LOG_LEVEL = {0}".format(config.log_level),
        ])
        
        return '\n'.join(lines)
    
    def _get_screen_comment(self, screen: str) -> str:
        """комментарий для экрана"""
        comments = {
            'main_menu': 'Главное меню',
            'game_menu_selector': 'Внутриигровое меню (ОБЯЗАТЕЛЬНО)',
            'say': 'Диалоговое окно',
            'nvl': 'NVL диалог',
            'preferences': 'Настройки',
            'save': 'Сохранение',
            'load': 'Загрузка',
            'choice': 'Выбор',
            'text_history_screen': 'История текста',
            'history': 'Концовки',
            'yesno_prompt': 'Подтверждение',
            'skip_indicator': 'Пропуск',
            'help': 'Помощь',
            'quit': 'Выход',
        }
        return comments.get(screen, screen)
    
