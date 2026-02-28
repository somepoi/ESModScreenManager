"""валидатор - проверяет что конфиг корректный"""

import os
import re
from pathlib import Path
from typing import Tuple, List
from .config_data import ConfigData


class Validator:
    """валидирует конфиг"""
    
    REQUIRED_SCREEN = 'game_menu_selector'
    
    def validate(self, config: ConfigData) -> Tuple[bool, List[str]]:
        """
        проверить конфиг
        
        Args:
            config: конфиг для проверки
            
        Returns:
            (валиден, список ошибок)
        """
        errors = []
        
        # проверяем путь
        if not config.mod_path:
            errors.append("Путь к моду не указан")
        elif not os.path.exists(config.mod_path):
            errors.append("Указанная папка мода не существует")
        elif not os.path.isdir(config.mod_path):
            errors.append("Указанный путь не является папкой")
        
        # проверяем название мода
        if not config.mod_name or not config.mod_name.strip():
            errors.append("Название мода не может быть пустым")
        
        # проверяем ID
        if not config.mod_id or not config.mod_id.strip():
            errors.append("Префикс мода не может быть пустым")
        else:
            # валидный питоновский идентификатор?
            if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', config.mod_id):
                errors.append(
                    "Префикс мода должен быть корректным идентификатором Python "
                    "(английские буквы, цифры, подчёркивание, не начинается с цифры)"
                )
        
        # проверяем ID сохранения
        if not config.mod_save_identifier or not config.mod_save_identifier.strip():
            errors.append("ID сохранения не может быть пустым")
        
        # проверяем экраны
        if not config.selected_screens:
            errors.append("Выберите хотя бы один экран для замены")
        elif self.REQUIRED_SCREEN not in config.selected_screens:
            errors.append(
                'Экран "{0}" должен быть выбран '
                '(обязателен для корректного отключения интерфейса)'.format(
                    self.REQUIRED_SCREEN
                )
            )
        
        # версия ренпая
        if config.renpy_min_version:
            if not re.match(r'^\d+(\.\d+)?$', config.renpy_min_version):
                errors.append("Версия Ren'Py должна быть в формате X.Y или X (например, 7.0 или 7)")
        
        return (len(errors) == 0, errors)
    
    def get_warning_messages(self, config: ConfigData) -> List[str]:
        """
        получить ворнинги для конфига
        
        Args:
            config: конфиг для проверки
            
        Returns:
            список ворнингов
        """
        warnings = []
        
        # ворнинг если логирование включено
        if config.logging:
            warnings.append(
                "Логирование включено. Рекомендуется отключить после настройки."
            )
        
        # ворнинг если замена окна выключена
        if not config.replace_window_name:
            warnings.append(
                "Замена названия окна отключена."
            )
        
        return warnings
