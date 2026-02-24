# Mod Screen Manager

Менеджер экранов для модов на Бесконечное Лето

## Описание

Технический мод для Everlasting Summer, который позволяет модам заменять экраны интерфейса на свои, с защитой от конфликтов с другими модами, которые тоже заменяют интерфейс.

## Важно

Mod Screen Manager **не совместим** с Ren'Py 8.x (т.е. с бета-веткой БЛ в Steam), так как в восьмой версии изменена архитектура работы с экранами.

## Как работать

### Установка

Скопируйте файлы `MSM.rpy` и `logger.rpy` в папку вашего мода.

Из папки `example/` скопируйте:

- `example.rpy.example` - Настройка кастомных экранов
- `screens.rpy.example` - Кастомные экраны

Замените расширение файлов с `.rpy.example` на `.rpy`

### Настройка

Откройте `example.rpy` и настройте конфиг `my_mod_ModScreenManagerConfig`

После настройки конфига замените `my_mod` в коде (везде, в `example.rpy` и `screens.rpy`) на префикс/постфикс своего мода. После этого запустите БЛ и проверьте работу мода.

После проверки работы мода замените шаблоны кастомных экранов в `screens.rpy` на свои.

## Пример использования

```python
label my_mod_start:
    # Создаем глобальный экземпляр менеджера с нашим кастомным шаблоном
    $ my_mod_screen_manager = ModScreenManager(my_mod_ModScreenManagerConfig)

    # Устанавливаем имя сохранения с идентификатором мода (чтобы экраны автоматически включались при загрузке сохранения Вашего мода)
    $ save_name = my_mod_ModScreenManagerConfig.MOD_SAVE_IDENTIFIER

    # Включаем экраны
    $ my_mod_screen_manager.activate_screens()
    
    "Hello World!"

    jump my_mod_exit

label my_mod_exit:
    # Обязательно выключайте экраны при выходе
    $ my_mod_screen_manager.deactivate_screens()
    return
```