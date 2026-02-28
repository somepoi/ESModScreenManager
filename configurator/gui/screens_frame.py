"""фрейм выбора экранов"""

import customtkinter as ctk
from typing import Callable
from .widgets.tooltip import Tooltip, TooltipCheckBox
from ..core.config_data import SCREENS, SCREEN_DESCRIPTIONS, DEFAULT_SCREENS


class ScreensFrame(ctk.CTkFrame):
    """фрейм с чекбоксами выбора экранов"""
    
    def __init__(self, parent, on_change: Callable = None, **kwargs):
        """
        инициализация фрейма выбора экранов
        
        Args:
            parent: родительский виджет
            on_change: колбэк при изменении
            **kwargs: доп. аргументы для CTkFrame
        """
        super().__init__(parent, **kwargs)
        
        self.on_change = on_change
        self.screen_checkboxes = {}
        
        self._create_widgets()
    
    def _create_widgets(self):
        """создать все виджеты для выбора экранов"""
        
        # заголовок
        title = ctk.CTkLabel(
            self,
            text="Выбор экранов для замены",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        title.pack(anchor="w", padx=20, pady=(20, 10))
        
        # описание
        desc = ctk.CTkLabel(
            self,
            text="Выберите экраны которые вы хотите заменить на кастомные.\n"
                 "Внутриигровое меню должно быть обязательно выбрано!",
            font=ctk.CTkFont(size=12),
            text_color="#888888",
            justify="left"
        )
        desc.pack(anchor="w", padx=20, pady=(0, 15))
        
        # сетка чекбоксов
        grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        grid_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # две колонки
        left_col = []
        right_col = []
        
        # делим экраны на две колонки
        screens_list = list(SCREENS.items())
        mid = (len(screens_list) + 1) // 2
        
        for i, (code, name) in enumerate(screens_list):
            checkbox = TooltipCheckBox(
                grid_frame,
                screen_code=code,
                screen_name=name,
                screen_description=SCREEN_DESCRIPTIONS.get(code, ""),
                font=ctk.CTkFont(size=13)
            )
            
            # выбираем по умолчанию если в DEFAULT_SCREENS
            if code in DEFAULT_SCREENS:
                checkbox.select()
            
            checkbox.configure(command=self._on_checkbox_change)
            
            if i < mid:
                left_col.append(checkbox)
            else:
                right_col.append(checkbox)
            
            self.screen_checkboxes[code] = checkbox
        
        # левая колонка
        left_frame = ctk.CTkFrame(grid_frame, fg_color="transparent")
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        for cb in left_col:
            cb.pack(anchor="w", pady=4)
        
        # правая колонка
        right_frame = ctk.CTkFrame(grid_frame, fg_color="transparent")
        right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))
        
        for cb in right_col:
            cb.pack(anchor="w", pady=4)
    
    def _on_checkbox_change(self):
        """обработка изменения чекбокса"""
        if self.on_change:
            self.on_change()
    
    def get_selected_screens(self) -> list:
        """
        получить список выбранных экранов
        
        Returns:
            список кодовых имен экранов
        """
        selected = []
        for code, checkbox in self.screen_checkboxes.items():
            if checkbox.get() == 1:
                selected.append(code)
        return selected
    
    def set_selected_screens(self, screens: list):
        """
        установить выбранные экраны
        
        Args:
            screens: список кодовых имен для выбора
        """
        for code, checkbox in self.screen_checkboxes.items():
            if code in screens:
                checkbox.select()
            else:
                checkbox.deselect()
    
    def set_enabled(self, enabled: bool):
        """включить/выключить все чекбоксы"""
        state = "normal" if enabled else "disabled"
        
        for checkbox in self.screen_checkboxes.values():
            checkbox.configure(state=state)
    
    def validate(self) -> tuple[bool, str]:
        """
        валидировать выбор экранов
        
        Returns:
            (валиден, сообщение об ошибке)
        """
        selected = self.get_selected_screens()
        
        if not selected:
            return False, "Выберите хотя бы один экран"
        
        if 'game_menu_selector' not in selected:
            return False, 'Экран "Внутриигровое меню" должен быть выбран'
        
        return True, ""
