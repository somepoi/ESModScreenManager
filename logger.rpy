init -1 python:
    # Простой логгер для Ren'Py, совместимый с сериализацией
    class ModScreenManagerLogger:
        """
        Логгер MSM с поддержкой сериализации
        """
        
        # Уровни логирования
        DEBUG = 10
        INFO = 20
        WARNING = 30
        ERROR = 40
        
        LEVEL_NAMES = {
            DEBUG: "DEBUG",
            INFO: "INFO", 
            WARNING: "WARNING",
            ERROR: "ERROR"
        }
        
        def __init__(self, name, level=INFO, enabled=True):
            """
            Инициализация логгера.
            
            Args:
                name: Имя логгера
                level: Минимальный уровень для вывода сообщений
                enabled: Включен ли логгер
            """
            self.name = name
            self.level = level
            self.enabled = enabled
        
        def _log(self, level, message):
            """Внутренний метод для вывода сообщений."""
            if not self.enabled or level < self.level:
                return

            level_name = self.LEVEL_NAMES.get(level, "UNKNOWN")
            formatted_message = u"[{}] {}: {}".format(level_name, self.name, message)

            renpy.display.log.write(formatted_message)

            # выводим в стандартный вывод для отладки
            try:
                print(formatted_message.encode('utf-8'))
            except:
                print(formatted_message)
        
        def debug(self, message):
            """Вывод отладочного сообщения."""
            self._log(self.DEBUG, message)
        
        def info(self, message):
            """Вывод информационного сообщения."""
            self._log(self.INFO, message)
        
        def warning(self, message):
            """Вывод предупреждения."""
            self._log(self.WARNING, message)
        
        def error(self, message):
            """Вывод ошибки."""
            self._log(self.ERROR, message)
        
        def setLevel(self, level):
            """Установка уровня логирования."""
            self.level = level
        
        def set_enabled(self, enabled):
            """Включение/выключение логгера."""
            self.enabled = enabled
    
    def create_logger(name, level=ModScreenManagerLogger.INFO, enabled=True):
        """
        Создание логгера
        
        Args:
            name: Имя логгера
            level: Уровень логирования (по умолчанию INFO)
            enabled: Включен ли логгер (по умолчанию True)
            
        Returns:
            ModScreenManagerLogger: Экземпляр логгера
        """
        return ModScreenManagerLogger(name, level, enabled)