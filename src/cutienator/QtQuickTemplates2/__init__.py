"""
The 'cutienator.QtQuickTemplates2' package provides the cute classes of
the part of Qt named QtQuickTemplates2, under the name PySide6 has for
it.

  from cutienator.QtQuickTemplates2 import QQuickUntypedDeferredPointer, QQuickVelocityCalculator

A class is brought in the first time it is asked for, with the files it
needs and no others. So bringing in the package costs nothing, and a
program pays for the classes it uses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QQuickUntypedDeferredPointer',
    'QQuickVelocityCalculator',
    'QColorDialogOptionsForeign',
    'QFileDialogOptionsForeign',
    'QFontDialogOptionsForeign',
    'QHeaderDataProxyModel',
    'QQuickApplicationWindowAttached',
    'QQuickCalendar',
    'QQuickIcon',
    'QQuickNativeIcon',
    'QQuickShortcutContext',
    'QQuickSplitHandleAttached',
    'QQuickSplitViewAttached',
    'QQuickStackViewAttached',
    'QQuickSwipeDelegateAttached',
    'QQuickSwipeViewAttached',
    'QQuickTabBarAttached',
    'QQuickTumblerAttached',
    'QQuickAction',
    'QQuickCalendarModel',
    'QQuickDayOfWeekModel',
    'QQuickIconPrivate',
    'QQuickMonthModel',
    'QQuickWeekNumberModel',
    'QQuickActionGroup',
    'QQuickActionGroupAttached',
    'QQuickTheme',
    'QQuickThemePrivate',
    'QQuickDialogButtonBoxAttached',
    'QQuickOverlayAttached',
    'QQuickNativeIconLoader',
    'QQuickContentItem',
    'QQuickControl',
    'QQuickControlPrivate',
    'QQuickIndicatorButton',
    'QQuickOverlay',
    'QQuickPressHandler',
    'QQuickStackViewArg',
    'QQuickStackViewAttachedPrivate',
    'QQuickTumblerAttachedPrivate',
    'QAccessibleQuickControl',
    'QQuickAbstractButton',
    'QQuickAbstractButtonPrivate',
    'QQuickBusyIndicator',
    'QQuickContainer',
    'QQuickContainerPrivate',
    'QQuickDayOfWeekRow',
    'QQuickDial',
    'QQuickDoubleSpinBox',
    'QQuickIndicatorButtonPrivate',
    'QQuickMenuSeparator',
    'QQuickMonthGrid',
    'QQuickPageIndicator',
    'QQuickPanePrivate',
    'QQuickPopup',
    'QQuickPopupPrivate',
    'QQuickProgressBar',
    'QQuickRangeSlider',
    'QQuickRangeSliderNode',
    'QQuickScrollBar',
    'QQuickScrollIndicator',
    'QQuickSelectionRectangle',
    'QQuickSelectionRectanglePrivate',
    'QQuickSlider',
    'QQuickSpinBox',
    'QQuickStackView',
    'QQuickToolSeparator',
    'QQuickTumbler',
    'QQuickWeekNumberColumn',
    'QAccessibleQuickScrollBar',
    'QAccessibleQuickSlider',
    'QQuickApplicationWindow',
    'QQuickButtonGroup',
    'QQuickButtonPrivate',
    'QQuickCheckBox',
    'QQuickComboBox',
    'QQuickDelayButton',
    'QQuickDialog',
    'QQuickDialogPrivate',
    'QQuickDialogButtonBox',
    'QQuickDrawer',
    'QQuickFramePrivate',
    'QQuickItemDelegatePrivate',
    'QQuickMenu',
    'QQuickMenuItem',
    'QQuickOverlayPrivate',
    'QQuickPagePrivate',
    'QQuickPane',
    'QQuickPopupAnchors',
    'QQuickPopupPositioner',
    'QQuickPopupTransitionManager',
    'QQuickPopupWindow',
    'QQuickRadioButton',
    'QQuickScrollBarAttached',
    'QQuickScrollBarPrivate',
    'QQuickScrollIndicatorAttached',
    'QQuickSearchField',
    'QQuickSelectionRectangleAttached',
    'QQuickSplitView',
    'QQuickStackElement',
    'QQuickSwipeView',
    'QQuickSwitch',
    'QQuickTabBar',
    'QQuickTabButton',
    'QQuickToolTip',
    'QQuickTumblerPrivate',
    'QAccessibleQuickApplicationWindow',
    'QQuickApplicationWindowPrivate',
    'QQuickButton',
    'QQuickButtonGroupAttached',
    'QQuickContextMenu',
    'QQuickDialogButtonBoxAttachedPrivate',
    'QQuickDialogButtonBoxPrivate',
    'QQuickDrawerPrivate',
    'QQuickFrame',
    'QQuickItemDelegate',
    'QQuickLabel',
    'QQuickMenuBar',
    'QQuickMenuBarItem',
    'QQuickMenuItemPrivate',
    'QQuickMenuPrivate',
    'QQuickNativeMenuItem',
    'QQuickPage',
    'QQuickPopupAnchorsPrivate',
    'QQuickScrollBarAttachedPrivate',
    'QQuickScrollView',
    'QQuickStackTransition',
    'QQuickTableViewDelegatePrivate',
    'QQuickTextField',
    'QQuickToolBar',
    'QQuickToolTipAttached',
    'QAccessibleQuickPage',
    'QQuickCheckDelegate',
    'QQuickGroupBox',
    'QQuickHeaderViewBase',
    'QQuickHeaderViewBasePrivate',
    'QQuickLabelPrivate',
    'QQuickMenuBarItemPrivate',
    'QQuickMenuBarPrivate',
    'QQuickPopupItem',
    'QQuickRadioDelegate',
    'QQuickRoundButton',
    'QQuickStackViewPrivate',
    'QQuickSwipeDelegate',
    'QQuickSwitchDelegate',
    'QQuickTableViewDelegate',
    'QQuickTextFieldPrivate',
    'QQuickToolButton',
    'QQuickToolTipAttachedPrivate',
    'QAccessibleQuickPopupItem',
    'QQuickHeaderViewDelegate',
    'QQuickHorizontalHeaderViewPrivate',
    'QQuickPopupItemPrivate',
    'QQuickSwipe',
    'QQuickSwipeDelegatePrivate',
    'QQuickTreeViewDelegate',
    'QQuickVerticalHeaderViewPrivate',
    'QQuickHorizontalHeaderView',
    'QQuickVerticalHeaderView',
    'QQuickTextArea',
    'QQuickTextAreaAttached',
    'QQuickTextAreaPrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick_untyped_deferred_pointer import QQuickUntypedDeferredPointer
  from ._q_quick_velocity_calculator import QQuickVelocityCalculator
  from ._q_color_dialog_options_foreign import QColorDialogOptionsForeign
  from ._q_file_dialog_options_foreign import QFileDialogOptionsForeign
  from ._q_font_dialog_options_foreign import QFontDialogOptionsForeign
  from ._q_header_data_proxy_model import QHeaderDataProxyModel
  from ._q_quick_application_window_attached import QQuickApplicationWindowAttached
  from ._q_quick_calendar import QQuickCalendar
  from ._q_quick_icon import QQuickIcon
  from ._q_quick_native_icon import QQuickNativeIcon
  from ._q_quick_shortcut_context import QQuickShortcutContext
  from ._q_quick_split_handle_attached import QQuickSplitHandleAttached
  from ._q_quick_split_view_attached import QQuickSplitViewAttached
  from ._q_quick_stack_view_attached import QQuickStackViewAttached
  from ._q_quick_swipe_delegate_attached import QQuickSwipeDelegateAttached
  from ._q_quick_swipe_view_attached import QQuickSwipeViewAttached
  from ._q_quick_tab_bar_attached import QQuickTabBarAttached
  from ._q_quick_tumbler_attached import QQuickTumblerAttached
  from ._q_quick_action import QQuickAction
  from ._q_quick_calendar_model import QQuickCalendarModel
  from ._q_quick_day_of_week_model import QQuickDayOfWeekModel
  from ._q_quick_icon_private import QQuickIconPrivate
  from ._q_quick_month_model import QQuickMonthModel
  from ._q_quick_week_number_model import QQuickWeekNumberModel
  from ._q_quick_action_group import QQuickActionGroup
  from ._q_quick_action_group_attached import QQuickActionGroupAttached
  from ._q_quick_theme import QQuickTheme
  from ._q_quick_theme_private import QQuickThemePrivate
  from ._q_quick_dialog_button_box_attached import QQuickDialogButtonBoxAttached
  from ._q_quick_overlay_attached import QQuickOverlayAttached
  from ._q_quick_native_icon_loader import QQuickNativeIconLoader
  from ._q_quick_content_item import QQuickContentItem
  from ._q_quick_control import QQuickControl
  from ._q_quick_control_private import QQuickControlPrivate
  from ._q_quick_indicator_button import QQuickIndicatorButton
  from ._q_quick_overlay import QQuickOverlay
  from ._q_quick_press_handler import QQuickPressHandler
  from ._q_quick_stack_view_arg import QQuickStackViewArg
  from ._q_quick_stack_view_attached_private import QQuickStackViewAttachedPrivate
  from ._q_quick_tumbler_attached_private import QQuickTumblerAttachedPrivate
  from ._q_accessible_quick_control import QAccessibleQuickControl
  from ._q_quick_abstract_button import QQuickAbstractButton
  from ._q_quick_abstract_button_private import QQuickAbstractButtonPrivate
  from ._q_quick_busy_indicator import QQuickBusyIndicator
  from ._q_quick_container import QQuickContainer
  from ._q_quick_container_private import QQuickContainerPrivate
  from ._q_quick_day_of_week_row import QQuickDayOfWeekRow
  from ._q_quick_dial import QQuickDial
  from ._q_quick_double_spin_box import QQuickDoubleSpinBox
  from ._q_quick_indicator_button_private import QQuickIndicatorButtonPrivate
  from ._q_quick_menu_separator import QQuickMenuSeparator
  from ._q_quick_month_grid import QQuickMonthGrid
  from ._q_quick_page_indicator import QQuickPageIndicator
  from ._q_quick_pane_private import QQuickPanePrivate
  from ._q_quick_popup import QQuickPopup
  from ._q_quick_popup_private import QQuickPopupPrivate
  from ._q_quick_progress_bar import QQuickProgressBar
  from ._q_quick_range_slider import QQuickRangeSlider
  from ._q_quick_range_slider_node import QQuickRangeSliderNode
  from ._q_quick_scroll_bar import QQuickScrollBar
  from ._q_quick_scroll_indicator import QQuickScrollIndicator
  from ._q_quick_selection_rectangle import QQuickSelectionRectangle
  from ._q_quick_selection_rectangle_private import QQuickSelectionRectanglePrivate
  from ._q_quick_slider import QQuickSlider
  from ._q_quick_spin_box import QQuickSpinBox
  from ._q_quick_stack_view import QQuickStackView
  from ._q_quick_tool_separator import QQuickToolSeparator
  from ._q_quick_tumbler import QQuickTumbler
  from ._q_quick_week_number_column import QQuickWeekNumberColumn
  from ._q_accessible_quick_scroll_bar import QAccessibleQuickScrollBar
  from ._q_accessible_quick_slider import QAccessibleQuickSlider
  from ._q_quick_application_window import QQuickApplicationWindow
  from ._q_quick_button_group import QQuickButtonGroup
  from ._q_quick_button_private import QQuickButtonPrivate
  from ._q_quick_check_box import QQuickCheckBox
  from ._q_quick_combo_box import QQuickComboBox
  from ._q_quick_delay_button import QQuickDelayButton
  from ._q_quick_dialog import QQuickDialog
  from ._q_quick_dialog_private import QQuickDialogPrivate
  from ._q_quick_dialog_button_box import QQuickDialogButtonBox
  from ._q_quick_drawer import QQuickDrawer
  from ._q_quick_frame_private import QQuickFramePrivate
  from ._q_quick_item_delegate_private import QQuickItemDelegatePrivate
  from ._q_quick_menu import QQuickMenu
  from ._q_quick_menu_item import QQuickMenuItem
  from ._q_quick_overlay_private import QQuickOverlayPrivate
  from ._q_quick_page_private import QQuickPagePrivate
  from ._q_quick_pane import QQuickPane
  from ._q_quick_popup_anchors import QQuickPopupAnchors
  from ._q_quick_popup_positioner import QQuickPopupPositioner
  from ._q_quick_popup_transition_manager import QQuickPopupTransitionManager
  from ._q_quick_popup_window import QQuickPopupWindow
  from ._q_quick_radio_button import QQuickRadioButton
  from ._q_quick_scroll_bar_attached import QQuickScrollBarAttached
  from ._q_quick_scroll_bar_private import QQuickScrollBarPrivate
  from ._q_quick_scroll_indicator_attached import QQuickScrollIndicatorAttached
  from ._q_quick_search_field import QQuickSearchField
  from ._q_quick_selection_rectangle_attached import QQuickSelectionRectangleAttached
  from ._q_quick_split_view import QQuickSplitView
  from ._q_quick_stack_element import QQuickStackElement
  from ._q_quick_swipe_view import QQuickSwipeView
  from ._q_quick_switch import QQuickSwitch
  from ._q_quick_tab_bar import QQuickTabBar
  from ._q_quick_tab_button import QQuickTabButton
  from ._q_quick_tool_tip import QQuickToolTip
  from ._q_quick_tumbler_private import QQuickTumblerPrivate
  from ._q_accessible_quick_application_window import QAccessibleQuickApplicationWindow
  from ._q_quick_application_window_private import QQuickApplicationWindowPrivate
  from ._q_quick_button import QQuickButton
  from ._q_quick_button_group_attached import QQuickButtonGroupAttached
  from ._q_quick_context_menu import QQuickContextMenu
  from ._q_quick_dialog_button_box_attached_private import QQuickDialogButtonBoxAttachedPrivate
  from ._q_quick_dialog_button_box_private import QQuickDialogButtonBoxPrivate
  from ._q_quick_drawer_private import QQuickDrawerPrivate
  from ._q_quick_frame import QQuickFrame
  from ._q_quick_item_delegate import QQuickItemDelegate
  from ._q_quick_label import QQuickLabel
  from ._q_quick_menu_bar import QQuickMenuBar
  from ._q_quick_menu_bar_item import QQuickMenuBarItem
  from ._q_quick_menu_item_private import QQuickMenuItemPrivate
  from ._q_quick_menu_private import QQuickMenuPrivate
  from ._q_quick_native_menu_item import QQuickNativeMenuItem
  from ._q_quick_page import QQuickPage
  from ._q_quick_popup_anchors_private import QQuickPopupAnchorsPrivate
  from ._q_quick_scroll_bar_attached_private import QQuickScrollBarAttachedPrivate
  from ._q_quick_scroll_view import QQuickScrollView
  from ._q_quick_stack_transition import QQuickStackTransition
  from ._q_quick_table_view_delegate_private import QQuickTableViewDelegatePrivate
  from ._q_quick_text_field import QQuickTextField
  from ._q_quick_tool_bar import QQuickToolBar
  from ._q_quick_tool_tip_attached import QQuickToolTipAttached
  from ._q_accessible_quick_page import QAccessibleQuickPage
  from ._q_quick_check_delegate import QQuickCheckDelegate
  from ._q_quick_group_box import QQuickGroupBox
  from ._q_quick_header_view_base import QQuickHeaderViewBase
  from ._q_quick_header_view_base_private import QQuickHeaderViewBasePrivate
  from ._q_quick_label_private import QQuickLabelPrivate
  from ._q_quick_menu_bar_item_private import QQuickMenuBarItemPrivate
  from ._q_quick_menu_bar_private import QQuickMenuBarPrivate
  from ._q_quick_popup_item import QQuickPopupItem
  from ._q_quick_radio_delegate import QQuickRadioDelegate
  from ._q_quick_round_button import QQuickRoundButton
  from ._q_quick_stack_view_private import QQuickStackViewPrivate
  from ._q_quick_swipe_delegate import QQuickSwipeDelegate
  from ._q_quick_switch_delegate import QQuickSwitchDelegate
  from ._q_quick_table_view_delegate import QQuickTableViewDelegate
  from ._q_quick_text_field_private import QQuickTextFieldPrivate
  from ._q_quick_tool_button import QQuickToolButton
  from ._q_quick_tool_tip_attached_private import QQuickToolTipAttachedPrivate
  from ._q_accessible_quick_popup_item import QAccessibleQuickPopupItem
  from ._q_quick_header_view_delegate import QQuickHeaderViewDelegate
  from ._q_quick_horizontal_header_view_private import QQuickHorizontalHeaderViewPrivate
  from ._q_quick_popup_item_private import QQuickPopupItemPrivate
  from ._q_quick_swipe import QQuickSwipe
  from ._q_quick_swipe_delegate_private import QQuickSwipeDelegatePrivate
  from ._q_quick_tree_view_delegate import QQuickTreeViewDelegate
  from ._q_quick_vertical_header_view_private import QQuickVerticalHeaderViewPrivate
  from ._q_quick_horizontal_header_view import QQuickHorizontalHeaderView
  from ._q_quick_vertical_header_view import QQuickVerticalHeaderView
  from ._q_quick_text_area import QQuickTextArea
  from ._q_quick_text_area_attached import QQuickTextAreaAttached
  from ._q_quick_text_area_private import QQuickTextAreaPrivate
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuickUntypedDeferredPointer': '_q_quick_untyped_deferred_pointer',
      'QQuickVelocityCalculator': '_q_quick_velocity_calculator',
      'QColorDialogOptionsForeign': '_q_color_dialog_options_foreign',
      'QFileDialogOptionsForeign': '_q_file_dialog_options_foreign',
      'QFontDialogOptionsForeign': '_q_font_dialog_options_foreign',
      'QHeaderDataProxyModel': '_q_header_data_proxy_model',
      'QQuickApplicationWindowAttached': '_q_quick_application_window_attached',
      'QQuickCalendar': '_q_quick_calendar',
      'QQuickIcon': '_q_quick_icon',
      'QQuickNativeIcon': '_q_quick_native_icon',
      'QQuickShortcutContext': '_q_quick_shortcut_context',
      'QQuickSplitHandleAttached': '_q_quick_split_handle_attached',
      'QQuickSplitViewAttached': '_q_quick_split_view_attached',
      'QQuickStackViewAttached': '_q_quick_stack_view_attached',
      'QQuickSwipeDelegateAttached': '_q_quick_swipe_delegate_attached',
      'QQuickSwipeViewAttached': '_q_quick_swipe_view_attached',
      'QQuickTabBarAttached': '_q_quick_tab_bar_attached',
      'QQuickTumblerAttached': '_q_quick_tumbler_attached',
      'QQuickAction': '_q_quick_action',
      'QQuickCalendarModel': '_q_quick_calendar_model',
      'QQuickDayOfWeekModel': '_q_quick_day_of_week_model',
      'QQuickIconPrivate': '_q_quick_icon_private',
      'QQuickMonthModel': '_q_quick_month_model',
      'QQuickWeekNumberModel': '_q_quick_week_number_model',
      'QQuickActionGroup': '_q_quick_action_group',
      'QQuickActionGroupAttached': '_q_quick_action_group_attached',
      'QQuickTheme': '_q_quick_theme',
      'QQuickThemePrivate': '_q_quick_theme_private',
      'QQuickDialogButtonBoxAttached': '_q_quick_dialog_button_box_attached',
      'QQuickOverlayAttached': '_q_quick_overlay_attached',
      'QQuickNativeIconLoader': '_q_quick_native_icon_loader',
      'QQuickContentItem': '_q_quick_content_item',
      'QQuickControl': '_q_quick_control',
      'QQuickControlPrivate': '_q_quick_control_private',
      'QQuickIndicatorButton': '_q_quick_indicator_button',
      'QQuickOverlay': '_q_quick_overlay',
      'QQuickPressHandler': '_q_quick_press_handler',
      'QQuickStackViewArg': '_q_quick_stack_view_arg',
      'QQuickStackViewAttachedPrivate': '_q_quick_stack_view_attached_private',
      'QQuickTumblerAttachedPrivate': '_q_quick_tumbler_attached_private',
      'QAccessibleQuickControl': '_q_accessible_quick_control',
      'QQuickAbstractButton': '_q_quick_abstract_button',
      'QQuickAbstractButtonPrivate': '_q_quick_abstract_button_private',
      'QQuickBusyIndicator': '_q_quick_busy_indicator',
      'QQuickContainer': '_q_quick_container',
      'QQuickContainerPrivate': '_q_quick_container_private',
      'QQuickDayOfWeekRow': '_q_quick_day_of_week_row',
      'QQuickDial': '_q_quick_dial',
      'QQuickDoubleSpinBox': '_q_quick_double_spin_box',
      'QQuickIndicatorButtonPrivate': '_q_quick_indicator_button_private',
      'QQuickMenuSeparator': '_q_quick_menu_separator',
      'QQuickMonthGrid': '_q_quick_month_grid',
      'QQuickPageIndicator': '_q_quick_page_indicator',
      'QQuickPanePrivate': '_q_quick_pane_private',
      'QQuickPopup': '_q_quick_popup',
      'QQuickPopupPrivate': '_q_quick_popup_private',
      'QQuickProgressBar': '_q_quick_progress_bar',
      'QQuickRangeSlider': '_q_quick_range_slider',
      'QQuickRangeSliderNode': '_q_quick_range_slider_node',
      'QQuickScrollBar': '_q_quick_scroll_bar',
      'QQuickScrollIndicator': '_q_quick_scroll_indicator',
      'QQuickSelectionRectangle': '_q_quick_selection_rectangle',
      'QQuickSelectionRectanglePrivate': '_q_quick_selection_rectangle_private',
      'QQuickSlider': '_q_quick_slider',
      'QQuickSpinBox': '_q_quick_spin_box',
      'QQuickStackView': '_q_quick_stack_view',
      'QQuickToolSeparator': '_q_quick_tool_separator',
      'QQuickTumbler': '_q_quick_tumbler',
      'QQuickWeekNumberColumn': '_q_quick_week_number_column',
      'QAccessibleQuickScrollBar': '_q_accessible_quick_scroll_bar',
      'QAccessibleQuickSlider': '_q_accessible_quick_slider',
      'QQuickApplicationWindow': '_q_quick_application_window',
      'QQuickButtonGroup': '_q_quick_button_group',
      'QQuickButtonPrivate': '_q_quick_button_private',
      'QQuickCheckBox': '_q_quick_check_box',
      'QQuickComboBox': '_q_quick_combo_box',
      'QQuickDelayButton': '_q_quick_delay_button',
      'QQuickDialog': '_q_quick_dialog',
      'QQuickDialogPrivate': '_q_quick_dialog_private',
      'QQuickDialogButtonBox': '_q_quick_dialog_button_box',
      'QQuickDrawer': '_q_quick_drawer',
      'QQuickFramePrivate': '_q_quick_frame_private',
      'QQuickItemDelegatePrivate': '_q_quick_item_delegate_private',
      'QQuickMenu': '_q_quick_menu',
      'QQuickMenuItem': '_q_quick_menu_item',
      'QQuickOverlayPrivate': '_q_quick_overlay_private',
      'QQuickPagePrivate': '_q_quick_page_private',
      'QQuickPane': '_q_quick_pane',
      'QQuickPopupAnchors': '_q_quick_popup_anchors',
      'QQuickPopupPositioner': '_q_quick_popup_positioner',
      'QQuickPopupTransitionManager': '_q_quick_popup_transition_manager',
      'QQuickPopupWindow': '_q_quick_popup_window',
      'QQuickRadioButton': '_q_quick_radio_button',
      'QQuickScrollBarAttached': '_q_quick_scroll_bar_attached',
      'QQuickScrollBarPrivate': '_q_quick_scroll_bar_private',
      'QQuickScrollIndicatorAttached': '_q_quick_scroll_indicator_attached',
      'QQuickSearchField': '_q_quick_search_field',
      'QQuickSelectionRectangleAttached': '_q_quick_selection_rectangle_attached',
      'QQuickSplitView': '_q_quick_split_view',
      'QQuickStackElement': '_q_quick_stack_element',
      'QQuickSwipeView': '_q_quick_swipe_view',
      'QQuickSwitch': '_q_quick_switch',
      'QQuickTabBar': '_q_quick_tab_bar',
      'QQuickTabButton': '_q_quick_tab_button',
      'QQuickToolTip': '_q_quick_tool_tip',
      'QQuickTumblerPrivate': '_q_quick_tumbler_private',
      'QAccessibleQuickApplicationWindow': '_q_accessible_quick_application_window',
      'QQuickApplicationWindowPrivate': '_q_quick_application_window_private',
      'QQuickButton': '_q_quick_button',
      'QQuickButtonGroupAttached': '_q_quick_button_group_attached',
      'QQuickContextMenu': '_q_quick_context_menu',
      'QQuickDialogButtonBoxAttachedPrivate': '_q_quick_dialog_button_box_attached_private',
      'QQuickDialogButtonBoxPrivate': '_q_quick_dialog_button_box_private',
      'QQuickDrawerPrivate': '_q_quick_drawer_private',
      'QQuickFrame': '_q_quick_frame',
      'QQuickItemDelegate': '_q_quick_item_delegate',
      'QQuickLabel': '_q_quick_label',
      'QQuickMenuBar': '_q_quick_menu_bar',
      'QQuickMenuBarItem': '_q_quick_menu_bar_item',
      'QQuickMenuItemPrivate': '_q_quick_menu_item_private',
      'QQuickMenuPrivate': '_q_quick_menu_private',
      'QQuickNativeMenuItem': '_q_quick_native_menu_item',
      'QQuickPage': '_q_quick_page',
      'QQuickPopupAnchorsPrivate': '_q_quick_popup_anchors_private',
      'QQuickScrollBarAttachedPrivate': '_q_quick_scroll_bar_attached_private',
      'QQuickScrollView': '_q_quick_scroll_view',
      'QQuickStackTransition': '_q_quick_stack_transition',
      'QQuickTableViewDelegatePrivate': '_q_quick_table_view_delegate_private',
      'QQuickTextField': '_q_quick_text_field',
      'QQuickToolBar': '_q_quick_tool_bar',
      'QQuickToolTipAttached': '_q_quick_tool_tip_attached',
      'QAccessibleQuickPage': '_q_accessible_quick_page',
      'QQuickCheckDelegate': '_q_quick_check_delegate',
      'QQuickGroupBox': '_q_quick_group_box',
      'QQuickHeaderViewBase': '_q_quick_header_view_base',
      'QQuickHeaderViewBasePrivate': '_q_quick_header_view_base_private',
      'QQuickLabelPrivate': '_q_quick_label_private',
      'QQuickMenuBarItemPrivate': '_q_quick_menu_bar_item_private',
      'QQuickMenuBarPrivate': '_q_quick_menu_bar_private',
      'QQuickPopupItem': '_q_quick_popup_item',
      'QQuickRadioDelegate': '_q_quick_radio_delegate',
      'QQuickRoundButton': '_q_quick_round_button',
      'QQuickStackViewPrivate': '_q_quick_stack_view_private',
      'QQuickSwipeDelegate': '_q_quick_swipe_delegate',
      'QQuickSwitchDelegate': '_q_quick_switch_delegate',
      'QQuickTableViewDelegate': '_q_quick_table_view_delegate',
      'QQuickTextFieldPrivate': '_q_quick_text_field_private',
      'QQuickToolButton': '_q_quick_tool_button',
      'QQuickToolTipAttachedPrivate': '_q_quick_tool_tip_attached_private',
      'QAccessibleQuickPopupItem': '_q_accessible_quick_popup_item',
      'QQuickHeaderViewDelegate': '_q_quick_header_view_delegate',
      'QQuickHorizontalHeaderViewPrivate': '_q_quick_horizontal_header_view_private',
      'QQuickPopupItemPrivate': '_q_quick_popup_item_private',
      'QQuickSwipe': '_q_quick_swipe',
      'QQuickSwipeDelegatePrivate': '_q_quick_swipe_delegate_private',
      'QQuickTreeViewDelegate': '_q_quick_tree_view_delegate',
      'QQuickVerticalHeaderViewPrivate': '_q_quick_vertical_header_view_private',
      'QQuickHorizontalHeaderView': '_q_quick_horizontal_header_view',
      'QQuickVerticalHeaderView': '_q_quick_vertical_header_view',
      'QQuickTextArea': '_q_quick_text_area',
      'QQuickTextAreaAttached': '_q_quick_text_area_attached',
      'QQuickTextAreaPrivate': '_q_quick_text_area_private',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuickTemplates2 import QQuickTextAreaPrivate'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    try:
      fileName = __class_files__[name]
    except KeyError:
      infoSpec = """module '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (__name__, name)) from None
    module = importlib.import_module('.%s' % fileName, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names every class of the part, brought in or not."""
    return [*__all__]
