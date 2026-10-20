# Автономная версия MSM для БЛетонька
# Замените ВСЕ my_mod на уникальный префикс.

default my_mod_msm_saved_screens = None

init -1 python:
    try:
        import __builtin__ as my_mod_msm_builtins
    except ImportError:
        import builtins as my_mod_msm_builtins

    my_mod_msm_config = {
        "MOD_NAME": u"Мой мод",
        "MOD_ID": "my_mod",
        "MOD_SAVE_IDENTIFIER": "my_mod",
        "RENPY_MIN_VERSION": (7, 0),
        "MOD_REPLACE_WINDOW_NAME": False,
        "MOD_CURSOR_PATH": False,
        "MOD_MENU_MUSIC": False,
        "DEFAULT_SCREENS": (
            "game_menu_selector", "say", "choice",
            "save", "load", "preferences", "skip_indicator",
        ),
        "LOGGING": False,
        "LOG_LEVEL": 20,
    }

    # питон контейнеры
    # поскольку реестр экранов не откатывается Ren'Py, поэтому его резервные копии тоже не должны откатываться/попадать в сейв
    # Ссылка на runtime создаётся в init и больше не переназначается
    my_mod_msm_runtime = my_mod_msm_builtins.dict(
        originals=my_mod_msm_builtins.dict(),
        applied=my_mod_msm_builtins.dict(),
        config_originals=my_mod_msm_builtins.dict(),
        config_applied=my_mod_msm_builtins.dict(),
        active=my_mod_msm_builtins.set(),
        cursor_captured=False,
        cursor_original_defined=False,
        cursor_original=None,
        cursor_applied=None,
    )
    my_mod_msm_missing = my_mod_msm_builtins.object()
    my_mod_msm_cursor_name = "msm_{}_cursor".format(my_mod_msm_config["MOD_ID"])

    def my_mod_msm_apply_cursor():
        if not my_mod_msm_config["MOD_CURSOR_PATH"]:
            return

        if not my_mod_msm_runtime["cursor_captured"]:
            if renpy.version_tuple[:2] >= (7, 4):
                my_mod_msm_runtime["cursor_original_defined"] = hasattr(renpy.store, "default_mouse")
                my_mod_msm_runtime["cursor_original"] = getattr(renpy.store, "default_mouse", None)
            else:
                mouse_config = config.mouse or {}
                my_mod_msm_runtime["cursor_original_defined"] = "default" in mouse_config
                my_mod_msm_runtime["cursor_original"] = mouse_config.get("default")
            my_mod_msm_runtime["cursor_captured"] = True

        if renpy.version_tuple[:2] >= (7, 4):
            my_mod_msm_runtime["cursor_applied"] = my_mod_msm_cursor_name
            renpy.store.default_mouse = my_mod_msm_cursor_name
        else:
            my_mod_msm_runtime["cursor_applied"] = [(my_mod_msm_config["MOD_CURSOR_PATH"], 0, 0)]
            config.mouse["default"] = my_mod_msm_runtime["cursor_applied"]

    def my_mod_msm_restore_cursor():
        if not my_mod_msm_runtime["cursor_captured"]:
            return

        if renpy.version_tuple[:2] >= (7, 4):
            current = getattr(renpy.store, "default_mouse", None)
            if current == my_mod_msm_runtime["cursor_applied"]:
                if my_mod_msm_runtime["cursor_original_defined"]:
                    renpy.store.default_mouse = my_mod_msm_runtime["cursor_original"]
                elif hasattr(renpy.store, "default_mouse"):
                    delattr(renpy.store, "default_mouse")
        elif config.mouse and config.mouse.get("default", my_mod_msm_missing) == my_mod_msm_runtime["cursor_applied"]:
            if my_mod_msm_runtime["cursor_original_defined"]:
                config.mouse["default"] = my_mod_msm_runtime["cursor_original"]
            else:
                config.mouse.pop("default", None)

        my_mod_msm_runtime["cursor_captured"] = False
        my_mod_msm_runtime["cursor_original_defined"] = False
        my_mod_msm_runtime["cursor_original"] = None
        my_mod_msm_runtime["cursor_applied"] = None

    def my_mod_msm_log(level, message):
        if level >= 40 or (my_mod_msm_config["LOGGING"] and level >= my_mod_msm_config["LOG_LEVEL"]):
            renpy.display.log.write(u"[MSM: {}] {}".format(my_mod_msm_config["MOD_ID"], message))

    def my_mod_msm_check_compatibility():
        version = renpy.version_tuple[:2]
        if not (my_mod_msm_config["RENPY_MIN_VERSION"] <= version < (8, 0)):
            my_mod_msm_log(40, u"Требуется Ren'Py 7.x, версия: {}".format(version))
            return False
        return True

    def my_mod_msm_validate_configuration():
        if "game_menu_selector" not in my_mod_msm_config["DEFAULT_SCREENS"]:
            my_mod_msm_log(40, u"Добавьте game_menu_selector в DEFAULT_SCREENS.")
            return False
        if not my_mod_msm_config["MOD_ID"]:
            my_mod_msm_log(40, u"MOD_ID не должен быть пустым.")
            return False
        return True

    def my_mod_msm_screen_variants(name):
        return my_mod_msm_builtins.dict(
            (variant, screen) for (screen_name, variant), screen
            in renpy.display.screen.screens.items() if screen_name == name
        )

    def my_mod_msm_set_screen(key, screen):
        registry = renpy.display.screen.screens
        by_name = getattr(renpy.display.screen, "screens_by_name", None)
        if screen is my_mod_msm_missing:
            registry.pop(key, None)
            if by_name is not None and key[0] in by_name:
                by_name[key[0]].pop(key[1], None)
                if not by_name[key[0]]:
                    by_name.pop(key[0], None)
        else:
            registry[key] = screen
            if by_name is not None:
                by_name.setdefault(key[0], {})[key[1]] = screen

    def my_mod_msm_restore_config():
        for name, original in my_mod_msm_runtime["config_originals"].items():
            # Не перезаписываем настройку, уже изменённую другим кодом.
            if getattr(config, name) == my_mod_msm_runtime["config_applied"][name]:
                setattr(config, name, original)
        my_mod_msm_restore_cursor()
        my_mod_msm_runtime["config_originals"].clear()
        my_mod_msm_runtime["config_applied"].clear()

    def my_mod_msm_apply_config():
        changes = {}
        if my_mod_msm_config["MOD_REPLACE_WINDOW_NAME"]:
            changes["window_title"] = my_mod_msm_config["MOD_NAME"]
        if my_mod_msm_config["MOD_MENU_MUSIC"]:
            changes["main_menu_music"] = my_mod_msm_config["MOD_MENU_MUSIC"]
        for name, value in changes.items():
            if name not in my_mod_msm_runtime["config_originals"]:
                my_mod_msm_runtime["config_originals"][name] = getattr(config, name)
            my_mod_msm_runtime["config_applied"][name] = value
            setattr(config, name, value)
        my_mod_msm_apply_cursor()

    def my_mod_msm_reset_runtime(screen_names=None):
        names = (my_mod_msm_builtins.set(my_mod_msm_runtime["active"])
                if screen_names is None else my_mod_msm_builtins.set(screen_names))
        for key in list(my_mod_msm_runtime["originals"]):
            if key[0] not in names:
                continue
            original = my_mod_msm_runtime["originals"].pop(key)
            applied = my_mod_msm_runtime["applied"].pop(key)
            if renpy.display.screen.screens.get(key, my_mod_msm_missing) is applied:
                my_mod_msm_set_screen(key, original)
        my_mod_msm_runtime["active"].difference_update(names)
        if not my_mod_msm_runtime["active"]:
            my_mod_msm_restore_config()

    def my_mod_msm_normalize_screens(screen_names):
        names = my_mod_msm_builtins.set(screen_names)
        # Даже при частичной замене должен оставаться путь выхода из мода.
        if names:
            names.add("game_menu_selector")
        return names

    def my_mod_msm_activate_runtime(screen_names):
        if not my_mod_msm_check_compatibility() or not my_mod_msm_validate_configuration():
            return False
        names = my_mod_msm_normalize_screens(screen_names)
        replacements = {}
        for name in names:
            variants = my_mod_msm_screen_variants(
                "{}_{}".format(my_mod_msm_config["MOD_ID"], name)
            )
            if variants:
                replacements[name] = variants
            else:
                my_mod_msm_log(30, u"Кастомный экран '{}' отсутствует.".format(name))
        if names and "game_menu_selector" not in replacements:
            my_mod_msm_log(40, u"Без кастомного game_menu_selector активация отменена.")
            return False

        my_mod_msm_reset_runtime(my_mod_msm_runtime["active"] - set(replacements))
        try:
            for name, variants in replacements.items():
                if name in my_mod_msm_runtime["active"]:
                    continue
                originals = my_mod_msm_screen_variants(name)
                my_mod_msm_runtime["active"].add(name)
                for variant in set(originals) | set(variants):
                    replacement = variants.get(variant, variants.get(None, my_mod_msm_missing))
                    # Если есть только специфичный вариант, сохраняем остальные.
                    if replacement is my_mod_msm_missing:
                        continue
                    key = (name, variant)
                    my_mod_msm_runtime["originals"][key] = originals.get(variant, my_mod_msm_missing)
                    my_mod_msm_runtime["applied"][key] = replacement
                    my_mod_msm_set_screen(key, replacement)
            if my_mod_msm_runtime["active"]:
                my_mod_msm_apply_config()
            return bool(my_mod_msm_runtime["active"])
        except Exception as error:
            my_mod_msm_log(40, u"Ошибка активации: {}".format(error))
            my_mod_msm_reset_runtime()
            return False

    def my_mod_msm_peer_hooks():
        # метка на callback
        # каждая копия по-прежнему работает без остальных.
        return [callback.es_msm_independent_hooks
                for callback in config.after_load_callbacks
                if hasattr(callback, "es_msm_independent_hooks")]

    def my_mod_msm_activate_screens(screen_names=None, partial=False):
        global my_mod_msm_saved_screens
        if not my_mod_msm_check_compatibility() or not my_mod_msm_validate_configuration():
            return False
        names = my_mod_msm_normalize_screens(
            my_mod_msm_config["DEFAULT_SCREENS"] if screen_names is None else screen_names
        )
        if partial:
            names.update(my_mod_msm_runtime["active"])
        if not names:
            return my_mod_msm_deactivate_screens()
        if not my_mod_msm_screen_variants(my_mod_msm_config["MOD_ID"] + "_game_menu_selector"):
            my_mod_msm_log(40, u"Кастомный game_menu_selector не найден.")
            return False
        for reset, load, deactivate, synchronize in my_mod_msm_peer_hooks():
            if reset is not my_mod_msm_reset_runtime:
                deactivate()
        result = my_mod_msm_activate_runtime(names)
        my_mod_msm_saved_screens = sorted(my_mod_msm_runtime["active"])
        return result

    def my_mod_msm_deactivate_screens(screen_names=None):
        global my_mod_msm_saved_screens
        names = (my_mod_msm_builtins.set(my_mod_msm_runtime["active"])
                if screen_names is None else my_mod_msm_builtins.set(screen_names))
        if "game_menu_selector" in names and my_mod_msm_runtime["active"] - names:
            names.discard("game_menu_selector")
        my_mod_msm_reset_runtime(names)
        my_mod_msm_saved_screens = sorted(my_mod_msm_runtime["active"])
        return True

    def my_mod_msm_toggle_screen(screen_name):
        if screen_name in my_mod_msm_runtime["active"]:
            my_mod_msm_deactivate_screens([screen_name])
        else:
            my_mod_msm_activate_screens([screen_name], partial=True)
        return screen_name in my_mod_msm_runtime["active"]

    def my_mod_msm_get_status():
        return {
            "is_active": bool(my_mod_msm_runtime["active"]),
            "active_screens": sorted(my_mod_msm_runtime["active"]),
            "total_screens": len(my_mod_msm_config["DEFAULT_SCREENS"]),
        }

    def my_mod_msm_load_state(allow_legacy=True):
        global my_mod_msm_saved_screens
        if my_mod_msm_saved_screens is None:
            # Поддержка сейвов, сделанных до установки мсм.
            save_title = getattr(renpy.store, "save_name", u"") or u""
            identifiers = (my_mod_msm_config["MOD_SAVE_IDENTIFIER"], my_mod_msm_config["MOD_NAME"])
            names = (my_mod_msm_config["DEFAULT_SCREENS"]
                    if allow_legacy and any(identifier and identifier in save_title for identifier in identifiers)
                    else [])
        else:
            names = my_mod_msm_saved_screens
        if names:
            my_mod_msm_activate_runtime(names)
        my_mod_msm_saved_screens = sorted(my_mod_msm_runtime["active"])

    def my_mod_msm_after_load_callback():
        hooks = my_mod_msm_peer_hooks()
        if hooks and hooks[0][0] is my_mod_msm_reset_runtime:
            # сначала возвращаем общий исходный интерфейс для ВСЕХ копий
            # затем включаем интерфейс загруженного мода.
            for reset, load, deactivate, synchronize in hooks:
                reset()
            # сохраняемый маркер точнее совпадения общего названия мода.
            allow_legacy = not any(synchronize()[0] is not None
                                    for reset, load, deactivate, synchronize in hooks)
            for reset, load, deactivate, synchronize in hooks:
                load(allow_legacy)

    def my_mod_msm_synchronize_state(apply=False):
        names = my_mod_msm_normalize_screens(my_mod_msm_saved_screens or [])
        if apply and names:
            my_mod_msm_activate_runtime(names)
        return my_mod_msm_saved_screens, my_mod_msm_builtins.set(my_mod_msm_runtime["active"])

    def my_mod_msm_interact_callback():
        # две фазы нужны также при rollback между интерфейсами разных модов
        # None означает, что этот мод ещё не включали в текущем прохождении.
        hooks = my_mod_msm_peer_hooks()
        if hooks and hooks[0][0] is my_mod_msm_reset_runtime:
            states = [synchronize() for reset, load, deactivate, synchronize in hooks]
            if any(my_mod_msm_normalize_screens(saved or []) != active for saved, active in states):
                for reset, load, deactivate, synchronize in hooks:
                    reset()
                for reset, load, deactivate, synchronize in hooks:
                    synchronize(True)

    my_mod_msm_after_load_callback.es_msm_independent_hooks = (
        my_mod_msm_reset_runtime, my_mod_msm_load_state,
        my_mod_msm_deactivate_screens, my_mod_msm_synchronize_state
    )

    if my_mod_msm_after_load_callback not in config.after_load_callbacks:
        config.after_load_callbacks.append(my_mod_msm_after_load_callback)
    if my_mod_msm_reset_runtime not in config.start_callbacks:
        config.start_callbacks.append(my_mod_msm_reset_runtime)
    if my_mod_msm_interact_callback not in config.interact_callbacks:
        config.interact_callbacks.append(my_mod_msm_interact_callback)

init 999 python:
    if my_mod_msm_config["MOD_CURSOR_PATH"]:
        if config.mouse is None:
            config.mouse = {}
        config.mouse[my_mod_msm_cursor_name] = [
            (my_mod_msm_config["MOD_CURSOR_PATH"], 0, 0)
        ]
