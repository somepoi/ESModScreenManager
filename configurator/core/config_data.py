"""структуры данных для конфига"""

from dataclasses import dataclass, field
from typing import Optional


# маппинг имен экранов: человеческое имя -> кодовое имя
SCREENS = {
    'main_menu': 'Главное меню',
    'game_menu_selector': 'Внутриигровое меню',
    'say': 'Диалог',
    'nvl': 'NVL диалог',
    'choice': 'Выбор',
    'preferences': 'Настройки',
    'save': 'Сохранение',
    'load': 'Загрузка',
    'history': 'Концовки',
    'text_history_screen': 'История текста',
    'yesno_prompt': 'Подтверждение',
    'skip_indicator': 'Пропуск',
    'help': 'Помощь',
    'quit': 'Выход',
}

# дефолтные экраны которые должны быть выбраны
DEFAULT_SCREENS = [
    'main_menu',
    'game_menu_selector',
    'say',
    'nvl',
    'preferences',
    'save',
    'load',
    'choice',
    'text_history_screen',
    'history',
    'yesno_prompt',
    'skip_indicator',
    'help',
    'quit',
]

# описания экранов для тултипов
SCREEN_DESCRIPTIONS = {
    'main_menu': 'Главное меню игры (кнопки "Новая игра", "Настройки" и т.д.)',
    'game_menu_selector': 'Меню с кнопками "В главное меню", "Сохранить", "Загрузить", "Выход". Открывается по Esc или ПКМ. ОБЯЗАТЕЛЬНО должно быть включено!',
    'say': 'Диалоговое окно с текстом персонажа',
    'nvl': 'NVL-режим (многострочный диалог)',
    'choice': 'Меню выбора ответов',
    'preferences': 'Экран настроек (звук, скорость текста, и т.д.)',
    'save': 'Экран сохранения игры',
    'load': 'Экран загрузки сохранения',
    'history': 'Экран концовок (Сова в главном меню)',
    'text_history_screen': 'История диалогов',
    'yesno_prompt': 'Окно подтверждения (выход, перезапись и т.д.)',
    'skip_indicator': 'Индикатор пропуска (при зажатом CTRL)',
    'help': 'Экран помощи / горячие клавиши',
    'quit': 'Экран выхода из игры',
}


@dataclass
class ConfigData:
    """конфиг для ModScreenManager"""
    
    mod_path: str = ""
    mod_name: str = "Мой мод"
    mod_id: str = "my_mod"
    mod_save_identifier: str = "MyMod"
    renpy_min_version: str = "7.0"
    
    # опциональные параметры
    replace_window_name: bool = False
    cursor_path: Optional[str] = None
    menu_music: Optional[str] = None
    logging: bool = False
    log_level: int = 20
    
    # выбор экранов
    selected_screens: list = field(default_factory=lambda: DEFAULT_SCREENS.copy())
    
    # дополнительные опции
    include_test_example: bool = False
    
    def get_code_screen_name(self, human_name: str) -> str:
        """получить кодовое имя экрана по человеческому"""
        for code, human in SCREENS.items():
            if human == human_name:
                return code
        return human_name
    
    def get_human_screen_name(self, code_name: str) -> str:
        """получить человеческое имя по коду"""
        return SCREENS.get(code_name, code_name)


# метаданные полей для тултипов
FIELD_METADATA = {
    'mod_name': {
        'title': 'Название мода',
        'description': 'Отображается в заголовке окна игры. Не используйте форматирование (жирный, курсив, цвета).',
        'example': '"Мой крутой мод"',
    },
    'mod_id': {
        'title': 'Префикс мода',
        'description': 'Уникальное слово/словосочетание для разделения ресурсов вашего мода от других модов. Используется как префикс для экранов и переменных.',
        'example': '"mymod", "coolmod", "supermod"\nДолжно быть: английские буквы, цифры, подчёркивание',
    },
    'mod_save_identifier': {
        'title': 'ID сохранения',
        'description': 'Ключевое слово в имени сохранения. Позволяет автоматически включить ваш интерфейс при загрузке сохранения из вашего мода.',
        'example': '"mymod", "MyModSave"\nСовет: Используйте то же значение, что и префикс',
    },
    'renpy_min_version': {
        'title': 'Версия Ren\'Py',
        'description': 'Минимальная совместимая версия Ren\'Py.',
        'example': '"7.0", "7.1", "7.3"',
    },
    'replace_window_name': {
        'title': 'Замена заголовка',
        'description': 'Заменяет стандартное "Бесконечное лето" в заголовке окна на название вашего мода',
        'example': 'По умолчанию: Выкл',
    },
    'cursor_path': {
        'title': 'Кастомный курсор',
        'description': 'Путь к PNG-файлу курсора относительно папки мода',
        'example': '"images/cursor.png"\nОставьте пустым для стандартного курсора',
    },
    'menu_music': {
        'title': 'Музыка в главном меню',
        'description': 'Путь к аудиофайлу (OGG/MP3) для фоновой музыки в главном меню',
        'example': '"music/main_menu.ogg"\nОставьте пустым для стандартной музыки',
    },
    'logging': {
        'title': 'Отладка',
        'description': 'Включает подробный вывод в консоль Ren\'Py. Полезно при настройке и поиске проблем.',
        'example': 'Рекомендуется: Вкл при первой настройке, потом выкл',
    },
    'log_level': {
        'title': 'Детализация',
        'description': 'Уровень детализации логов',
        'example': 'DEBUG (10), INFO (20), WARNING (30), ERROR (40)',
    },
}
