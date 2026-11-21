"""
The 'cutienator.QtWidgets' package provides the cute classes of the part
of Qt named QtWidgets, under the name PySide6 has for it.

  from cutienator.QtWidgets import QApplication, QWidget, QPushButton

A class is brought in the first time it is asked for, with the files
it needs and no others. So bringing in the package costs nothing, and a
program pays for the classes it uses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QSizePolicy',
    'QTableWidgetSelectionRange',
    'QLayoutItem',
    'QStyleFactory',
    'QSpacerItem',
    'QGesture',
    'QGraphicsEffect',
    'QPanGesture',
    'QPinchGesture',
    'QScroller',
    'QGraphicsBlurEffect',
    'QGraphicsColorizeEffect',
    'QGraphicsDropShadowEffect',
    'QGraphicsOpacityEffect',
    'QGraphicsTransform',
    'QGraphicsScale',
    'QFileIconProvider',
    'QPlainTextDocumentLayout',
    'QTableWidgetItem',
    'QWidget',
    'QStyleOption',
    'QStyleOptionComplex',
    'QApplication',
    'QLayout',
    'QStyle',
    'QAbstractButton',
    'QAbstractSlider',
    'QBoxLayout',
    'QCalendarWidget',
    'QCommonStyle',
    'QDialog',
    'QFocusFrame',
    'QFormLayout',
    'QGestureEvent',
    'QGraphicsSceneEvent',
    'QGridLayout',
    'QKeySequenceEdit',
    'QSizeGrip',
    'QSplashScreen',
    'QStackedLayout',
    'QStatusBar',
    'QStyleOptionButton',
    'QStyleOptionComboBox',
    'QStyleOptionFocusRect',
    'QStyleOptionFrame',
    'QStyleOptionGraphicsItem',
    'QStyleOptionGroupBox',
    'QStyleOptionHeader',
    'QStyleOptionMenuItem',
    'QStyleOptionProgressBar',
    'QStyleOptionSlider',
    'QStyleOptionSpinBox',
    'QStyleOptionTab',
    'QStyleOptionTabBarBase',
    'QStyleOptionToolBar',
    'QStyleOptionToolButton',
    'QStyleOptionViewItem',
    'QStylePainter',
    'QToolTip',
    'QWhatsThis',
    'QWidgetAction',
    'QWidgetItem',
    'QButtonGroup',
    'QCheckBox',
    'QColorDialog',
    'QDial',
    'QDialogButtonBox',
    'QDockWidget',
    'QErrorMessage',
    'QFontDialog',
    'QFrame',
    'QGraphicsSceneContextMenuEvent',
    'QGraphicsSceneHelpEvent',
    'QGraphicsSceneHoverEvent',
    'QGraphicsSceneMouseEvent',
    'QGraphicsSceneResizeEvent',
    'QGroupBox',
    'QHBoxLayout',
    'QItemEditorFactory',
    'QMenu',
    'QProgressBar',
    'QProxyStyle',
    'QRadioButton',
    'QRubberBand',
    'QScrollBar',
    'QSlider',
    'QTabBar',
    'QToolBar',
    'QVBoxLayout',
    'QWizard',
    'QWizardPage',
    'QAbstractScrollArea',
    'QGraphicsItem',
    'QGraphicsItemGroup',
    'QLCDNumber',
    'QLabel',
    'QMdiSubWindow',
    'QMenuBar',
    'QPushButton',
    'QSplitter',
    'QStackedWidget',
    'QSystemTrayIcon',
    'QTabWidget',
    'QToolBox',
    'QToolButton',
    'QAbstractGraphicsShapeItem',
    'QAbstractItemDelegate',
    'QAbstractItemView',
    'QCommandLinkButton',
    'QGraphicsLayoutItem',
    'QGraphicsLineItem',
    'QGraphicsObject',
    'QGraphicsPixmapItem',
    'QMainWindow',
    'QMdiArea',
    'QMessageBox',
    'QPlainTextEdit',
    'QProgressDialog',
    'QScrollArea',
    'QSplitterHandle',
    'QTextEdit',
    'QCompleter',
    'QDataWidgetMapper',
    'QFileDialog',
    'QGraphicsEllipseItem',
    'QGraphicsLayout',
    'QGraphicsPathItem',
    'QGraphicsPolygonItem',
    'QGraphicsRectItem',
    'QGraphicsSimpleTextItem',
    'QGraphicsTextItem',
    'QHeaderView',
    'QItemDelegate',
    'QListView',
    'QStyledItemDelegate',
    'QTextBrowser',
    'QGraphicsGridLayout',
    'QGraphicsLinearLayout',
    'QGraphicsWidget',
    'QLineEdit',
    'QListWidget',
    'QListWidgetItem',
    'QTableView',
    'QTreeView',
    'QAbstractSpinBox',
    'QComboBox',
    'QGraphicsProxyWidget',
    'QGraphicsScene',
    'QInputDialog',
    'QTableWidget',
    'QTreeWidget',
    'QTreeWidgetItem',
    'QDateTimeEdit',
    'QDoubleSpinBox',
    'QFontComboBox',
    'QGraphicsView',
    'QSpinBox',
    'QTreeWidgetItemIterator',
    'QDateEdit',
    'QTimeEdit',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_size_policy import QSizePolicy
  from ._q_table_widget_selection_range import QTableWidgetSelectionRange
  from ._q_layout_item import QLayoutItem
  from ._q_style_factory import QStyleFactory
  from ._q_spacer_item import QSpacerItem
  from ._q_gesture import QGesture
  from ._q_graphics_effect import QGraphicsEffect
  from ._q_pan_gesture import QPanGesture
  from ._q_pinch_gesture import QPinchGesture
  from ._q_scroller import QScroller
  from ._q_graphics_blur_effect import QGraphicsBlurEffect
  from ._q_graphics_colorize_effect import QGraphicsColorizeEffect
  from ._q_graphics_drop_shadow_effect import QGraphicsDropShadowEffect
  from ._q_graphics_opacity_effect import QGraphicsOpacityEffect
  from ._q_graphics_transform import QGraphicsTransform
  from ._q_graphics_scale import QGraphicsScale
  from ._q_file_icon_provider import QFileIconProvider
  from ._q_plain_text_document_layout import QPlainTextDocumentLayout
  from ._q_table_widget_item import QTableWidgetItem
  from ._q_widget import QWidget
  from ._q_style_option import QStyleOption
  from ._q_style_option_complex import QStyleOptionComplex
  from ._q_application import QApplication
  from ._q_layout import QLayout
  from ._q_style import QStyle
  from ._q_abstract_button import QAbstractButton
  from ._q_abstract_slider import QAbstractSlider
  from ._q_box_layout import QBoxLayout
  from ._q_calendar_widget import QCalendarWidget
  from ._q_common_style import QCommonStyle
  from ._q_dialog import QDialog
  from ._q_focus_frame import QFocusFrame
  from ._q_form_layout import QFormLayout
  from ._q_gesture_event import QGestureEvent
  from ._q_graphics_scene_event import QGraphicsSceneEvent
  from ._q_grid_layout import QGridLayout
  from ._q_key_sequence_edit import QKeySequenceEdit
  from ._q_size_grip import QSizeGrip
  from ._q_splash_screen import QSplashScreen
  from ._q_stacked_layout import QStackedLayout
  from ._q_status_bar import QStatusBar
  from ._q_style_option_button import QStyleOptionButton
  from ._q_style_option_combo_box import QStyleOptionComboBox
  from ._q_style_option_focus_rect import QStyleOptionFocusRect
  from ._q_style_option_frame import QStyleOptionFrame
  from ._q_style_option_graphics_item import QStyleOptionGraphicsItem
  from ._q_style_option_group_box import QStyleOptionGroupBox
  from ._q_style_option_header import QStyleOptionHeader
  from ._q_style_option_menu_item import QStyleOptionMenuItem
  from ._q_style_option_progress_bar import QStyleOptionProgressBar
  from ._q_style_option_slider import QStyleOptionSlider
  from ._q_style_option_spin_box import QStyleOptionSpinBox
  from ._q_style_option_tab import QStyleOptionTab
  from ._q_style_option_tab_bar_base import QStyleOptionTabBarBase
  from ._q_style_option_tool_bar import QStyleOptionToolBar
  from ._q_style_option_tool_button import QStyleOptionToolButton
  from ._q_style_option_view_item import QStyleOptionViewItem
  from ._q_style_painter import QStylePainter
  from ._q_tool_tip import QToolTip
  from ._q_whats_this import QWhatsThis
  from ._q_widget_action import QWidgetAction
  from ._q_widget_item import QWidgetItem
  from ._q_button_group import QButtonGroup
  from ._q_check_box import QCheckBox
  from ._q_color_dialog import QColorDialog
  from ._q_dial import QDial
  from ._q_dialog_button_box import QDialogButtonBox
  from ._q_dock_widget import QDockWidget
  from ._q_error_message import QErrorMessage
  from ._q_font_dialog import QFontDialog
  from ._q_frame import QFrame
  from ._q_graphics_scene_context_menu_event import QGraphicsSceneContextMenuEvent
  from ._q_graphics_scene_help_event import QGraphicsSceneHelpEvent
  from ._q_graphics_scene_hover_event import QGraphicsSceneHoverEvent
  from ._q_graphics_scene_mouse_event import QGraphicsSceneMouseEvent
  from ._q_graphics_scene_resize_event import QGraphicsSceneResizeEvent
  from ._q_group_box import QGroupBox
  from ._q_h_box_layout import QHBoxLayout
  from ._q_item_editor_factory import QItemEditorFactory
  from ._q_menu import QMenu
  from ._q_progress_bar import QProgressBar
  from ._q_proxy_style import QProxyStyle
  from ._q_radio_button import QRadioButton
  from ._q_rubber_band import QRubberBand
  from ._q_scroll_bar import QScrollBar
  from ._q_slider import QSlider
  from ._q_tab_bar import QTabBar
  from ._q_tool_bar import QToolBar
  from ._q_v_box_layout import QVBoxLayout
  from ._q_wizard import QWizard
  from ._q_wizard_page import QWizardPage
  from ._q_abstract_scroll_area import QAbstractScrollArea
  from ._q_graphics_item import QGraphicsItem
  from ._q_graphics_item_group import QGraphicsItemGroup
  from ._q_l_c_d_number import QLCDNumber
  from ._q_label import QLabel
  from ._q_mdi_sub_window import QMdiSubWindow
  from ._q_menu_bar import QMenuBar
  from ._q_push_button import QPushButton
  from ._q_splitter import QSplitter
  from ._q_stacked_widget import QStackedWidget
  from ._q_system_tray_icon import QSystemTrayIcon
  from ._q_tab_widget import QTabWidget
  from ._q_tool_box import QToolBox
  from ._q_tool_button import QToolButton
  from ._q_abstract_graphics_shape_item import QAbstractGraphicsShapeItem
  from ._q_abstract_item_delegate import QAbstractItemDelegate
  from ._q_abstract_item_view import QAbstractItemView
  from ._q_command_link_button import QCommandLinkButton
  from ._q_graphics_layout_item import QGraphicsLayoutItem
  from ._q_graphics_line_item import QGraphicsLineItem
  from ._q_graphics_object import QGraphicsObject
  from ._q_graphics_pixmap_item import QGraphicsPixmapItem
  from ._q_main_window import QMainWindow
  from ._q_mdi_area import QMdiArea
  from ._q_message_box import QMessageBox
  from ._q_plain_text_edit import QPlainTextEdit
  from ._q_progress_dialog import QProgressDialog
  from ._q_scroll_area import QScrollArea
  from ._q_splitter_handle import QSplitterHandle
  from ._q_text_edit import QTextEdit
  from ._q_completer import QCompleter
  from ._q_data_widget_mapper import QDataWidgetMapper
  from ._q_file_dialog import QFileDialog
  from ._q_graphics_ellipse_item import QGraphicsEllipseItem
  from ._q_graphics_layout import QGraphicsLayout
  from ._q_graphics_path_item import QGraphicsPathItem
  from ._q_graphics_polygon_item import QGraphicsPolygonItem
  from ._q_graphics_rect_item import QGraphicsRectItem
  from ._q_graphics_simple_text_item import QGraphicsSimpleTextItem
  from ._q_graphics_text_item import QGraphicsTextItem
  from ._q_header_view import QHeaderView
  from ._q_item_delegate import QItemDelegate
  from ._q_list_view import QListView
  from ._q_styled_item_delegate import QStyledItemDelegate
  from ._q_text_browser import QTextBrowser
  from ._q_graphics_grid_layout import QGraphicsGridLayout
  from ._q_graphics_linear_layout import QGraphicsLinearLayout
  from ._q_graphics_widget import QGraphicsWidget
  from ._q_line_edit import QLineEdit
  from ._q_list_widget import QListWidget
  from ._q_list_widget_item import QListWidgetItem
  from ._q_table_view import QTableView
  from ._q_tree_view import QTreeView
  from ._q_abstract_spin_box import QAbstractSpinBox
  from ._q_combo_box import QComboBox
  from ._q_graphics_proxy_widget import QGraphicsProxyWidget
  from ._q_graphics_scene import QGraphicsScene
  from ._q_input_dialog import QInputDialog
  from ._q_table_widget import QTableWidget
  from ._q_tree_widget import QTreeWidget
  from ._q_tree_widget_item import QTreeWidgetItem
  from ._q_date_time_edit import QDateTimeEdit
  from ._q_double_spin_box import QDoubleSpinBox
  from ._q_font_combo_box import QFontComboBox
  from ._q_graphics_view import QGraphicsView
  from ._q_spin_box import QSpinBox
  from ._q_tree_widget_item_iterator import QTreeWidgetItemIterator
  from ._q_date_edit import QDateEdit
  from ._q_time_edit import QTimeEdit
  from ._q_abstract_item_delegate_end_edit_hint import (
      EndEditHint as QAbstractItemDelegateEndEditHint)
  from ._q_abstract_item_view_drag_drop_mode import (
      DragDropMode as QAbstractItemViewDragDropMode)
  from ._q_abstract_item_view_edit_trigger import (
      EditTrigger as QAbstractItemViewEditTrigger)
  from ._q_abstract_item_view_scroll_hint import (
      ScrollHint as QAbstractItemViewScrollHint)
  from ._q_abstract_item_view_scroll_mode import (
      ScrollMode as QAbstractItemViewScrollMode)
  from ._q_abstract_item_view_selection_behavior import (
      SelectionBehavior as QAbstractItemViewSelectionBehavior)
  from ._q_abstract_item_view_selection_mode import (
      SelectionMode as QAbstractItemViewSelectionMode)
  from ._q_abstract_scroll_area_size_adjust_policy import (
      SizeAdjustPolicy as QAbstractScrollAreaSizeAdjustPolicy)
  from ._q_abstract_slider_slider_action import (
      SliderAction as QAbstractSliderSliderAction)
  from ._q_abstract_spin_box_button_symbols import (
      ButtonSymbols as QAbstractSpinBoxButtonSymbols)
  from ._q_abstract_spin_box_correction_mode import (
      CorrectionMode as QAbstractSpinBoxCorrectionMode)
  from ._q_abstract_spin_box_step_enabled_flag import (
      StepEnabledFlag as QAbstractSpinBoxStepEnabledFlag)
  from ._q_abstract_spin_box_step_type import (
      StepType as QAbstractSpinBoxStepType)
  from ._q_box_layout_direction import Direction as QBoxLayoutDirection
  from ._q_calendar_widget_horizontal_header_format import (
      HorizontalHeaderFormat as QCalendarWidgetHorizontalHeaderFormat)
  from ._q_calendar_widget_selection_mode import (
      SelectionMode as QCalendarWidgetSelectionMode)
  from ._q_calendar_widget_vertical_header_format import (
      VerticalHeaderFormat as QCalendarWidgetVerticalHeaderFormat)
  from ._q_color_dialog_color_dialog_option import (
      ColorDialogOption as QColorDialogColorDialogOption)
  from ._q_combo_box_insert_policy import (
      InsertPolicy as QComboBoxInsertPolicy)
  from ._q_combo_box_label_drawing_mode import (
      LabelDrawingMode as QComboBoxLabelDrawingMode)
  from ._q_combo_box_size_adjust_policy import (
      SizeAdjustPolicy as QComboBoxSizeAdjustPolicy)
  from ._q_completer_completion_mode import (
      CompletionMode as QCompleterCompletionMode)
  from ._q_completer_model_sorting import (
      ModelSorting as QCompleterModelSorting)
  from ._q_data_widget_mapper_submit_policy import (
      SubmitPolicy as QDataWidgetMapperSubmitPolicy)
  from ._q_date_time_edit_section import Section as QDateTimeEditSection
  from ._q_dialog_button_box_button_layout import (
      ButtonLayout as QDialogButtonBoxButtonLayout)
  from ._q_dialog_button_box_button_role import (
      ButtonRole as QDialogButtonBoxButtonRole)
  from ._q_dialog_button_box_standard_button import (
      StandardButton as QDialogButtonBoxStandardButton)
  from ._q_dialog_dialog_code import DialogCode as QDialogDialogCode
  from ._q_dock_widget_dock_widget_feature import (
      DockWidgetFeature as QDockWidgetDockWidgetFeature)
  from ._q_file_dialog_accept_mode import AcceptMode as QFileDialogAcceptMode
  from ._q_file_dialog_dialog_label import (
      DialogLabel as QFileDialogDialogLabel)
  from ._q_file_dialog_file_mode import FileMode as QFileDialogFileMode
  from ._q_file_dialog_option import Option as QFileDialogOption
  from ._q_file_dialog_view_mode import ViewMode as QFileDialogViewMode
  from ._q_font_combo_box_font_filter import (
      FontFilter as QFontComboBoxFontFilter)
  from ._q_font_dialog_font_dialog_option import (
      FontDialogOption as QFontDialogFontDialogOption)
  from ._q_form_layout_field_growth_policy import (
      FieldGrowthPolicy as QFormLayoutFieldGrowthPolicy)
  from ._q_form_layout_item_role import ItemRole as QFormLayoutItemRole
  from ._q_form_layout_row_wrap_policy import (
      RowWrapPolicy as QFormLayoutRowWrapPolicy)
  from ._q_form_layout__take_row_result import (
      TakeRowResult as QFormLayoutTakeRowResult)
  from ._q_frame_shadow import Shadow as QFrameShadow
  from ._q_frame_shape import Shape as QFrameShape
  from ._q_frame_style_mask import StyleMask as QFrameStyleMask
  from ._q_gesture_gesture_cancel_policy import (
      GestureCancelPolicy as QGestureGestureCancelPolicy)
  from ._q_graphics_blur_effect_blur_hint import (
      BlurHint as QGraphicsBlurEffectBlurHint)
  from ._q_graphics_effect_change_flag import (
      ChangeFlag as QGraphicsEffectChangeFlag)
  from ._q_graphics_effect_pixmap_pad_mode import (
      PixmapPadMode as QGraphicsEffectPixmapPadMode)
  from ._q_graphics_item_cache_mode import (
      CacheMode as QGraphicsItemCacheMode)
  from ._q_graphics_item_graphics_item_change import (
      GraphicsItemChange as QGraphicsItemGraphicsItemChange)
  from ._q_graphics_item_graphics_item_flag import (
      GraphicsItemFlag as QGraphicsItemGraphicsItemFlag)
  from ._q_graphics_item_panel_modality import (
      PanelModality as QGraphicsItemPanelModality)
  from ._q_graphics_pixmap_item_shape_mode import (
      ShapeMode as QGraphicsPixmapItemShapeMode)
  from ._q_graphics_scene_context_menu_event_reason import (
      Reason as QGraphicsSceneContextMenuEventReason)
  from ._q_graphics_scene_item_index_method import (
      ItemIndexMethod as QGraphicsSceneItemIndexMethod)
  from ._q_graphics_scene_scene_layer import (
      SceneLayer as QGraphicsSceneSceneLayer)
  from ._q_graphics_view_cache_mode_flag import (
      CacheModeFlag as QGraphicsViewCacheModeFlag)
  from ._q_graphics_view_drag_mode import DragMode as QGraphicsViewDragMode
  from ._q_graphics_view_optimization_flag import (
      OptimizationFlag as QGraphicsViewOptimizationFlag)
  from ._q_graphics_view_viewport_anchor import (
      ViewportAnchor as QGraphicsViewViewportAnchor)
  from ._q_graphics_view_viewport_update_mode import (
      ViewportUpdateMode as QGraphicsViewViewportUpdateMode)
  from ._q_header_view_resize_mode import ResizeMode as QHeaderViewResizeMode
  from ._q_input_dialog_input_dialog_option import (
      InputDialogOption as QInputDialogInputDialogOption)
  from ._q_input_dialog_input_mode import InputMode as QInputDialogInputMode
  from ._q_l_c_d_number_mode import Mode as QLCDNumberMode
  from ._q_l_c_d_number_segment_style import (
      SegmentStyle as QLCDNumberSegmentStyle)
  from ._q_layout_size_constraint import (
      SizeConstraint as QLayoutSizeConstraint)
  from ._q_line_edit_action_position import (
      ActionPosition as QLineEditActionPosition)
  from ._q_line_edit_echo_mode import EchoMode as QLineEditEchoMode
  from ._q_list_view_flow import Flow as QListViewFlow
  from ._q_list_view_layout_mode import LayoutMode as QListViewLayoutMode
  from ._q_list_view_movement import Movement as QListViewMovement
  from ._q_list_view_resize_mode import ResizeMode as QListViewResizeMode
  from ._q_list_view_view_mode import ViewMode as QListViewViewMode
  from ._q_list_widget_item_item_type import (
      ItemType as QListWidgetItemItemType)
  from ._q_main_window_dock_option import DockOption as QMainWindowDockOption
  from ._q_mdi_area_area_option import AreaOption as QMdiAreaAreaOption
  from ._q_mdi_area_view_mode import ViewMode as QMdiAreaViewMode
  from ._q_mdi_area_window_order import WindowOrder as QMdiAreaWindowOrder
  from ._q_mdi_sub_window_sub_window_option import (
      SubWindowOption as QMdiSubWindowSubWindowOption)
  from ._q_message_box_button_role import ButtonRole as QMessageBoxButtonRole
  from ._q_message_box_icon import Icon as QMessageBoxIcon
  from ._q_message_box_option import Option as QMessageBoxOption
  from ._q_message_box_standard_button import (
      StandardButton as QMessageBoxStandardButton)
  from ._q_pinch_gesture_change_flag import (
      ChangeFlag as QPinchGestureChangeFlag)
  from ._q_plain_text_edit_line_wrap_mode import (
      LineWrapMode as QPlainTextEditLineWrapMode)
  from ._q_progress_bar_direction import Direction as QProgressBarDirection
  from ._q_rubber_band_shape import Shape as QRubberBandShape
  from ._q_scroller_input import Input as QScrollerInput
  from ._q_scroller_scroller_gesture_type import (
      ScrollerGestureType as QScrollerScrollerGestureType)
  from ._q_scroller_state import State as QScrollerState
  from ._q_size_policy_control_type import (
      ControlType as QSizePolicyControlType)
  from ._q_size_policy_policy import Policy as QSizePolicyPolicy
  from ._q_size_policy_policy_flag import PolicyFlag as QSizePolicyPolicyFlag
  from ._q_slider_tick_position import TickPosition as QSliderTickPosition
  from ._q_stacked_layout_stacking_mode import (
      StackingMode as QStackedLayoutStackingMode)
  from ._q_style_complex_control import (
      ComplexControl as QStyleComplexControl)
  from ._q_style_contents_type import ContentsType as QStyleContentsType
  from ._q_style_control_element import (
      ControlElement as QStyleControlElement)
  from ._q_style_option_button_button_feature import (
      ButtonFeature as QStyleOptionButtonButtonFeature)
  from ._q_style_option_button_style_option_type import (
      StyleOptionType as QStyleOptionButtonStyleOptionType)
  from ._q_style_option_button_style_option_version import (
      StyleOptionVersion as QStyleOptionButtonStyleOptionVersion)
  from ._q_style_option_combo_box_style_option_type import (
      StyleOptionType as QStyleOptionComboBoxStyleOptionType)
  from ._q_style_option_combo_box_style_option_version import (
      StyleOptionVersion as QStyleOptionComboBoxStyleOptionVersion)
  from ._q_style_option_complex_style_option_type import (
      StyleOptionType as QStyleOptionComplexStyleOptionType)
  from ._q_style_option_complex_style_option_version import (
      StyleOptionVersion as QStyleOptionComplexStyleOptionVersion)
  from ._q_style_option_focus_rect_style_option_type import (
      StyleOptionType as QStyleOptionFocusRectStyleOptionType)
  from ._q_style_option_focus_rect_style_option_version import (
      StyleOptionVersion as QStyleOptionFocusRectStyleOptionVersion)
  from ._q_style_option_frame_frame_feature import (
      FrameFeature as QStyleOptionFrameFrameFeature)
  from ._q_style_option_frame_style_option_type import (
      StyleOptionType as QStyleOptionFrameStyleOptionType)
  from ._q_style_option_frame_style_option_version import (
      StyleOptionVersion as QStyleOptionFrameStyleOptionVersion)
  from ._q_style_option_graphics_item_style_option_type import (
      StyleOptionType as QStyleOptionGraphicsItemStyleOptionType)
  from ._q_style_option_graphics_item_style_option_version import (
      StyleOptionVersion as QStyleOptionGraphicsItemStyleOptionVersion)
  from ._q_style_option_group_box_style_option_type import (
      StyleOptionType as QStyleOptionGroupBoxStyleOptionType)
  from ._q_style_option_group_box_style_option_version import (
      StyleOptionVersion as QStyleOptionGroupBoxStyleOptionVersion)
  from ._q_style_option_header_section_position import (
      SectionPosition as QStyleOptionHeaderSectionPosition)
  from ._q_style_option_header_selected_position import (
      SelectedPosition as QStyleOptionHeaderSelectedPosition)
  from ._q_style_option_header_sort_indicator import (
      SortIndicator as QStyleOptionHeaderSortIndicator)
  from ._q_style_option_header_style_option_type import (
      StyleOptionType as QStyleOptionHeaderStyleOptionType)
  from ._q_style_option_header_style_option_version import (
      StyleOptionVersion as QStyleOptionHeaderStyleOptionVersion)
  from ._q_style_option_menu_item_check_type import (
      CheckType as QStyleOptionMenuItemCheckType)
  from ._q_style_option_menu_item_menu_item_type import (
      MenuItemType as QStyleOptionMenuItemMenuItemType)
  from ._q_style_option_menu_item_style_option_type import (
      StyleOptionType as QStyleOptionMenuItemStyleOptionType)
  from ._q_style_option_menu_item_style_option_version import (
      StyleOptionVersion as QStyleOptionMenuItemStyleOptionVersion)
  from ._q_style_option_option_type import (
      OptionType as QStyleOptionOptionType)
  from ._q_style_option_progress_bar_style_option_type import (
      StyleOptionType as QStyleOptionProgressBarStyleOptionType)
  from ._q_style_option_progress_bar_style_option_version import (
      StyleOptionVersion as QStyleOptionProgressBarStyleOptionVersion)
  from ._q_style_option_slider_style_option_type import (
      StyleOptionType as QStyleOptionSliderStyleOptionType)
  from ._q_style_option_slider_style_option_version import (
      StyleOptionVersion as QStyleOptionSliderStyleOptionVersion)
  from ._q_style_option_spin_box_style_option_type import (
      StyleOptionType as QStyleOptionSpinBoxStyleOptionType)
  from ._q_style_option_spin_box_style_option_version import (
      StyleOptionVersion as QStyleOptionSpinBoxStyleOptionVersion)
  from ._q_style_option_style_option_type import (
      StyleOptionType as QStyleOptionStyleOptionType)
  from ._q_style_option_style_option_version import (
      StyleOptionVersion as QStyleOptionStyleOptionVersion)
  from ._q_style_option_tab_bar_base_style_option_type import (
      StyleOptionType as QStyleOptionTabBarBaseStyleOptionType)
  from ._q_style_option_tab_bar_base_style_option_version import (
      StyleOptionVersion as QStyleOptionTabBarBaseStyleOptionVersion)
  from ._q_style_option_tab_corner_widget import (
      CornerWidget as QStyleOptionTabCornerWidget)
  from ._q_style_option_tab_selected_position import (
      SelectedPosition as QStyleOptionTabSelectedPosition)
  from ._q_style_option_tab_style_option_type import (
      StyleOptionType as QStyleOptionTabStyleOptionType)
  from ._q_style_option_tab_style_option_version import (
      StyleOptionVersion as QStyleOptionTabStyleOptionVersion)
  from ._q_style_option_tab_tab_feature import (
      TabFeature as QStyleOptionTabTabFeature)
  from ._q_style_option_tab_tab_position import (
      TabPosition as QStyleOptionTabTabPosition)
  from ._q_style_option_tool_bar_style_option_type import (
      StyleOptionType as QStyleOptionToolBarStyleOptionType)
  from ._q_style_option_tool_bar_style_option_version import (
      StyleOptionVersion as QStyleOptionToolBarStyleOptionVersion)
  from ._q_style_option_tool_bar_tool_bar_feature import (
      ToolBarFeature as QStyleOptionToolBarToolBarFeature)
  from ._q_style_option_tool_bar_tool_bar_position import (
      ToolBarPosition as QStyleOptionToolBarToolBarPosition)
  from ._q_style_option_tool_button_style_option_type import (
      StyleOptionType as QStyleOptionToolButtonStyleOptionType)
  from ._q_style_option_tool_button_style_option_version import (
      StyleOptionVersion as QStyleOptionToolButtonStyleOptionVersion)
  from ._q_style_option_tool_button_tool_button_feature import (
      ToolButtonFeature as QStyleOptionToolButtonToolButtonFeature)
  from ._q_style_option_view_item_position import (
      Position as QStyleOptionViewItemPosition)
  from ._q_style_option_view_item_style_option_type import (
      StyleOptionType as QStyleOptionViewItemStyleOptionType)
  from ._q_style_option_view_item_style_option_version import (
      StyleOptionVersion as QStyleOptionViewItemStyleOptionVersion)
  from ._q_style_option_view_item_view_item_feature import (
      ViewItemFeature as QStyleOptionViewItemViewItemFeature)
  from ._q_style_option_view_item_view_item_position import (
      ViewItemPosition as QStyleOptionViewItemViewItemPosition)
  from ._q_style_pixel_metric import PixelMetric as QStylePixelMetric
  from ._q_style_primitive_element import (
      PrimitiveElement as QStylePrimitiveElement)
  from ._q_style_request_software_input_panel import (
      RequestSoftwareInputPanel as QStyleRequestSoftwareInputPanel)
  from ._q_style_standard_pixmap import (
      StandardPixmap as QStyleStandardPixmap)
  from ._q_style_state_flag import StateFlag as QStyleStateFlag
  from ._q_style_style_hint import StyleHint as QStyleStyleHint
  from ._q_style_sub_control import SubControl as QStyleSubControl
  from ._q_style_sub_element import SubElement as QStyleSubElement
  from ._q_system_tray_icon_activation_reason import (
      ActivationReason as QSystemTrayIconActivationReason)
  from ._q_system_tray_icon_message_icon import (
      MessageIcon as QSystemTrayIconMessageIcon)
  from ._q_tab_bar_button_position import (
      ButtonPosition as QTabBarButtonPosition)
  from ._q_tab_bar_selection_behavior import (
      SelectionBehavior as QTabBarSelectionBehavior)
  from ._q_tab_bar_shape import Shape as QTabBarShape
  from ._q_tab_widget_tab_position import (
      TabPosition as QTabWidgetTabPosition)
  from ._q_tab_widget_tab_shape import TabShape as QTabWidgetTabShape
  from ._q_table_widget_item_item_type import (
      ItemType as QTableWidgetItemItemType)
  from ._q_text_edit_auto_formatting_flag import (
      AutoFormattingFlag as QTextEditAutoFormattingFlag)
  from ._q_text_edit_line_wrap_mode import (
      LineWrapMode as QTextEditLineWrapMode)
  from ._q_tool_button_tool_button_popup_mode import (
      ToolButtonPopupMode as QToolButtonToolButtonPopupMode)
  from ._q_tree_widget_item_child_indicator_policy import (
      ChildIndicatorPolicy as QTreeWidgetItemChildIndicatorPolicy)
  from ._q_tree_widget_item_item_type import (
      ItemType as QTreeWidgetItemItemType)
  from ._q_tree_widget_item_iterator_iterator_flag import (
      IteratorFlag as QTreeWidgetItemIteratorIteratorFlag)
  from ._q_widget_render_flag import RenderFlag as QWidgetRenderFlag
  from ._q_wizard_wizard_button import WizardButton as QWizardWizardButton
  from ._q_wizard_wizard_option import WizardOption as QWizardWizardOption
  from ._q_wizard_wizard_pixmap import WizardPixmap as QWizardWizardPixmap
  from ._q_wizard_wizard_style import WizardStyle as QWizardWizardStyle
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QSizePolicy': '_q_size_policy',
      'QTableWidgetSelectionRange': '_q_table_widget_selection_range',
      'QLayoutItem': '_q_layout_item',
      'QStyleFactory': '_q_style_factory',
      'QSpacerItem': '_q_spacer_item',
      'QGesture': '_q_gesture',
      'QGraphicsEffect': '_q_graphics_effect',
      'QPanGesture': '_q_pan_gesture',
      'QPinchGesture': '_q_pinch_gesture',
      'QScroller': '_q_scroller',
      'QGraphicsBlurEffect': '_q_graphics_blur_effect',
      'QGraphicsColorizeEffect': '_q_graphics_colorize_effect',
      'QGraphicsDropShadowEffect': '_q_graphics_drop_shadow_effect',
      'QGraphicsOpacityEffect': '_q_graphics_opacity_effect',
      'QGraphicsTransform': '_q_graphics_transform',
      'QGraphicsScale': '_q_graphics_scale',
      'QFileIconProvider': '_q_file_icon_provider',
      'QPlainTextDocumentLayout': '_q_plain_text_document_layout',
      'QTableWidgetItem': '_q_table_widget_item',
      'QWidget': '_q_widget',
      'QStyleOption': '_q_style_option',
      'QStyleOptionComplex': '_q_style_option_complex',
      'QApplication': '_q_application',
      'QLayout': '_q_layout',
      'QStyle': '_q_style',
      'QAbstractButton': '_q_abstract_button',
      'QAbstractSlider': '_q_abstract_slider',
      'QBoxLayout': '_q_box_layout',
      'QCalendarWidget': '_q_calendar_widget',
      'QCommonStyle': '_q_common_style',
      'QDialog': '_q_dialog',
      'QFocusFrame': '_q_focus_frame',
      'QFormLayout': '_q_form_layout',
      'QGestureEvent': '_q_gesture_event',
      'QGraphicsSceneEvent': '_q_graphics_scene_event',
      'QGridLayout': '_q_grid_layout',
      'QKeySequenceEdit': '_q_key_sequence_edit',
      'QSizeGrip': '_q_size_grip',
      'QSplashScreen': '_q_splash_screen',
      'QStackedLayout': '_q_stacked_layout',
      'QStatusBar': '_q_status_bar',
      'QStyleOptionButton': '_q_style_option_button',
      'QStyleOptionComboBox': '_q_style_option_combo_box',
      'QStyleOptionFocusRect': '_q_style_option_focus_rect',
      'QStyleOptionFrame': '_q_style_option_frame',
      'QStyleOptionGraphicsItem': '_q_style_option_graphics_item',
      'QStyleOptionGroupBox': '_q_style_option_group_box',
      'QStyleOptionHeader': '_q_style_option_header',
      'QStyleOptionMenuItem': '_q_style_option_menu_item',
      'QStyleOptionProgressBar': '_q_style_option_progress_bar',
      'QStyleOptionSlider': '_q_style_option_slider',
      'QStyleOptionSpinBox': '_q_style_option_spin_box',
      'QStyleOptionTab': '_q_style_option_tab',
      'QStyleOptionTabBarBase': '_q_style_option_tab_bar_base',
      'QStyleOptionToolBar': '_q_style_option_tool_bar',
      'QStyleOptionToolButton': '_q_style_option_tool_button',
      'QStyleOptionViewItem': '_q_style_option_view_item',
      'QStylePainter': '_q_style_painter',
      'QToolTip': '_q_tool_tip',
      'QWhatsThis': '_q_whats_this',
      'QWidgetAction': '_q_widget_action',
      'QWidgetItem': '_q_widget_item',
      'QButtonGroup': '_q_button_group',
      'QCheckBox': '_q_check_box',
      'QColorDialog': '_q_color_dialog',
      'QDial': '_q_dial',
      'QDialogButtonBox': '_q_dialog_button_box',
      'QDockWidget': '_q_dock_widget',
      'QErrorMessage': '_q_error_message',
      'QFontDialog': '_q_font_dialog',
      'QFrame': '_q_frame',
      'QGraphicsSceneContextMenuEvent': '_q_graphics_scene_context_menu_event',
      'QGraphicsSceneHelpEvent': '_q_graphics_scene_help_event',
      'QGraphicsSceneHoverEvent': '_q_graphics_scene_hover_event',
      'QGraphicsSceneMouseEvent': '_q_graphics_scene_mouse_event',
      'QGraphicsSceneResizeEvent': '_q_graphics_scene_resize_event',
      'QGroupBox': '_q_group_box',
      'QHBoxLayout': '_q_h_box_layout',
      'QItemEditorFactory': '_q_item_editor_factory',
      'QMenu': '_q_menu',
      'QProgressBar': '_q_progress_bar',
      'QProxyStyle': '_q_proxy_style',
      'QRadioButton': '_q_radio_button',
      'QRubberBand': '_q_rubber_band',
      'QScrollBar': '_q_scroll_bar',
      'QSlider': '_q_slider',
      'QTabBar': '_q_tab_bar',
      'QToolBar': '_q_tool_bar',
      'QVBoxLayout': '_q_v_box_layout',
      'QWizard': '_q_wizard',
      'QWizardPage': '_q_wizard_page',
      'QAbstractScrollArea': '_q_abstract_scroll_area',
      'QGraphicsItem': '_q_graphics_item',
      'QGraphicsItemGroup': '_q_graphics_item_group',
      'QLCDNumber': '_q_l_c_d_number',
      'QLabel': '_q_label',
      'QMdiSubWindow': '_q_mdi_sub_window',
      'QMenuBar': '_q_menu_bar',
      'QPushButton': '_q_push_button',
      'QSplitter': '_q_splitter',
      'QStackedWidget': '_q_stacked_widget',
      'QSystemTrayIcon': '_q_system_tray_icon',
      'QTabWidget': '_q_tab_widget',
      'QToolBox': '_q_tool_box',
      'QToolButton': '_q_tool_button',
      'QAbstractGraphicsShapeItem': '_q_abstract_graphics_shape_item',
      'QAbstractItemDelegate': '_q_abstract_item_delegate',
      'QAbstractItemView': '_q_abstract_item_view',
      'QCommandLinkButton': '_q_command_link_button',
      'QGraphicsLayoutItem': '_q_graphics_layout_item',
      'QGraphicsLineItem': '_q_graphics_line_item',
      'QGraphicsObject': '_q_graphics_object',
      'QGraphicsPixmapItem': '_q_graphics_pixmap_item',
      'QMainWindow': '_q_main_window',
      'QMdiArea': '_q_mdi_area',
      'QMessageBox': '_q_message_box',
      'QPlainTextEdit': '_q_plain_text_edit',
      'QProgressDialog': '_q_progress_dialog',
      'QScrollArea': '_q_scroll_area',
      'QSplitterHandle': '_q_splitter_handle',
      'QTextEdit': '_q_text_edit',
      'QCompleter': '_q_completer',
      'QDataWidgetMapper': '_q_data_widget_mapper',
      'QFileDialog': '_q_file_dialog',
      'QGraphicsEllipseItem': '_q_graphics_ellipse_item',
      'QGraphicsLayout': '_q_graphics_layout',
      'QGraphicsPathItem': '_q_graphics_path_item',
      'QGraphicsPolygonItem': '_q_graphics_polygon_item',
      'QGraphicsRectItem': '_q_graphics_rect_item',
      'QGraphicsSimpleTextItem': '_q_graphics_simple_text_item',
      'QGraphicsTextItem': '_q_graphics_text_item',
      'QHeaderView': '_q_header_view',
      'QItemDelegate': '_q_item_delegate',
      'QListView': '_q_list_view',
      'QStyledItemDelegate': '_q_styled_item_delegate',
      'QTextBrowser': '_q_text_browser',
      'QGraphicsGridLayout': '_q_graphics_grid_layout',
      'QGraphicsLinearLayout': '_q_graphics_linear_layout',
      'QGraphicsWidget': '_q_graphics_widget',
      'QLineEdit': '_q_line_edit',
      'QListWidget': '_q_list_widget',
      'QListWidgetItem': '_q_list_widget_item',
      'QTableView': '_q_table_view',
      'QTreeView': '_q_tree_view',
      'QAbstractSpinBox': '_q_abstract_spin_box',
      'QComboBox': '_q_combo_box',
      'QGraphicsProxyWidget': '_q_graphics_proxy_widget',
      'QGraphicsScene': '_q_graphics_scene',
      'QInputDialog': '_q_input_dialog',
      'QTableWidget': '_q_table_widget',
      'QTreeWidget': '_q_tree_widget',
      'QTreeWidgetItem': '_q_tree_widget_item',
      'QDateTimeEdit': '_q_date_time_edit',
      'QDoubleSpinBox': '_q_double_spin_box',
      'QFontComboBox': '_q_font_combo_box',
      'QGraphicsView': '_q_graphics_view',
      'QSpinBox': '_q_spin_box',
      'QTreeWidgetItemIterator': '_q_tree_widget_item_iterator',
      'QDateEdit': '_q_date_edit',
      'QTimeEdit': '_q_time_edit',
  }

  #  Where each enum is, and each class Qt writes inside another: the
  #  file, and the name it has there. The package gives each by what
  #  Qt writes it inside and its own name in one, so that the file of
  #  a class can ask for it as it asks for a class. None of them is
  #  in '__all__': a program reaches an enum through its class, as
  #  Qt writes it.
  __inner_files__ = {
      'QAbstractItemDelegateEndEditHint': (
          '_q_abstract_item_delegate_end_edit_hint', 'EndEditHint'),
      'QAbstractItemViewDragDropMode': (
          '_q_abstract_item_view_drag_drop_mode', 'DragDropMode'),
      'QAbstractItemViewEditTrigger': (
          '_q_abstract_item_view_edit_trigger', 'EditTrigger'),
      'QAbstractItemViewScrollHint': (
          '_q_abstract_item_view_scroll_hint', 'ScrollHint'),
      'QAbstractItemViewScrollMode': (
          '_q_abstract_item_view_scroll_mode', 'ScrollMode'),
      'QAbstractItemViewSelectionBehavior': (
          '_q_abstract_item_view_selection_behavior', 'SelectionBehavior'),
      'QAbstractItemViewSelectionMode': (
          '_q_abstract_item_view_selection_mode', 'SelectionMode'),
      'QAbstractScrollAreaSizeAdjustPolicy': (
          '_q_abstract_scroll_area_size_adjust_policy', 'SizeAdjustPolicy'),
      'QAbstractSliderSliderAction': (
          '_q_abstract_slider_slider_action', 'SliderAction'),
      'QAbstractSpinBoxButtonSymbols': (
          '_q_abstract_spin_box_button_symbols', 'ButtonSymbols'),
      'QAbstractSpinBoxCorrectionMode': (
          '_q_abstract_spin_box_correction_mode', 'CorrectionMode'),
      'QAbstractSpinBoxStepEnabledFlag': (
          '_q_abstract_spin_box_step_enabled_flag', 'StepEnabledFlag'),
      'QAbstractSpinBoxStepType': (
          '_q_abstract_spin_box_step_type', 'StepType'),
      'QBoxLayoutDirection': ('_q_box_layout_direction', 'Direction'),
      'QCalendarWidgetHorizontalHeaderFormat': (
          '_q_calendar_widget_horizontal_header_format',
          'HorizontalHeaderFormat'),
      'QCalendarWidgetSelectionMode': (
          '_q_calendar_widget_selection_mode', 'SelectionMode'),
      'QCalendarWidgetVerticalHeaderFormat': (
          '_q_calendar_widget_vertical_header_format',
          'VerticalHeaderFormat'),
      'QColorDialogColorDialogOption': (
          '_q_color_dialog_color_dialog_option', 'ColorDialogOption'),
      'QComboBoxInsertPolicy': (
          '_q_combo_box_insert_policy', 'InsertPolicy'),
      'QComboBoxLabelDrawingMode': (
          '_q_combo_box_label_drawing_mode', 'LabelDrawingMode'),
      'QComboBoxSizeAdjustPolicy': (
          '_q_combo_box_size_adjust_policy', 'SizeAdjustPolicy'),
      'QCompleterCompletionMode': (
          '_q_completer_completion_mode', 'CompletionMode'),
      'QCompleterModelSorting': (
          '_q_completer_model_sorting', 'ModelSorting'),
      'QDataWidgetMapperSubmitPolicy': (
          '_q_data_widget_mapper_submit_policy', 'SubmitPolicy'),
      'QDateTimeEditSection': ('_q_date_time_edit_section', 'Section'),
      'QDialogButtonBoxButtonLayout': (
          '_q_dialog_button_box_button_layout', 'ButtonLayout'),
      'QDialogButtonBoxButtonRole': (
          '_q_dialog_button_box_button_role', 'ButtonRole'),
      'QDialogButtonBoxStandardButton': (
          '_q_dialog_button_box_standard_button', 'StandardButton'),
      'QDialogDialogCode': ('_q_dialog_dialog_code', 'DialogCode'),
      'QDockWidgetDockWidgetFeature': (
          '_q_dock_widget_dock_widget_feature', 'DockWidgetFeature'),
      'QFileDialogAcceptMode': ('_q_file_dialog_accept_mode', 'AcceptMode'),
      'QFileDialogDialogLabel': (
          '_q_file_dialog_dialog_label', 'DialogLabel'),
      'QFileDialogFileMode': ('_q_file_dialog_file_mode', 'FileMode'),
      'QFileDialogOption': ('_q_file_dialog_option', 'Option'),
      'QFileDialogViewMode': ('_q_file_dialog_view_mode', 'ViewMode'),
      'QFontComboBoxFontFilter': (
          '_q_font_combo_box_font_filter', 'FontFilter'),
      'QFontDialogFontDialogOption': (
          '_q_font_dialog_font_dialog_option', 'FontDialogOption'),
      'QFormLayoutFieldGrowthPolicy': (
          '_q_form_layout_field_growth_policy', 'FieldGrowthPolicy'),
      'QFormLayoutItemRole': ('_q_form_layout_item_role', 'ItemRole'),
      'QFormLayoutRowWrapPolicy': (
          '_q_form_layout_row_wrap_policy', 'RowWrapPolicy'),
      'QFormLayoutTakeRowResult': (
          '_q_form_layout__take_row_result', 'TakeRowResult'),
      'QFrameShadow': ('_q_frame_shadow', 'Shadow'),
      'QFrameShape': ('_q_frame_shape', 'Shape'),
      'QFrameStyleMask': ('_q_frame_style_mask', 'StyleMask'),
      'QGestureGestureCancelPolicy': (
          '_q_gesture_gesture_cancel_policy', 'GestureCancelPolicy'),
      'QGraphicsBlurEffectBlurHint': (
          '_q_graphics_blur_effect_blur_hint', 'BlurHint'),
      'QGraphicsEffectChangeFlag': (
          '_q_graphics_effect_change_flag', 'ChangeFlag'),
      'QGraphicsEffectPixmapPadMode': (
          '_q_graphics_effect_pixmap_pad_mode', 'PixmapPadMode'),
      'QGraphicsItemCacheMode': ('_q_graphics_item_cache_mode', 'CacheMode'),
      'QGraphicsItemGraphicsItemChange': (
          '_q_graphics_item_graphics_item_change', 'GraphicsItemChange'),
      'QGraphicsItemGraphicsItemFlag': (
          '_q_graphics_item_graphics_item_flag', 'GraphicsItemFlag'),
      'QGraphicsItemPanelModality': (
          '_q_graphics_item_panel_modality', 'PanelModality'),
      'QGraphicsPixmapItemShapeMode': (
          '_q_graphics_pixmap_item_shape_mode', 'ShapeMode'),
      'QGraphicsSceneContextMenuEventReason': (
          '_q_graphics_scene_context_menu_event_reason', 'Reason'),
      'QGraphicsSceneItemIndexMethod': (
          '_q_graphics_scene_item_index_method', 'ItemIndexMethod'),
      'QGraphicsSceneSceneLayer': (
          '_q_graphics_scene_scene_layer', 'SceneLayer'),
      'QGraphicsViewCacheModeFlag': (
          '_q_graphics_view_cache_mode_flag', 'CacheModeFlag'),
      'QGraphicsViewDragMode': ('_q_graphics_view_drag_mode', 'DragMode'),
      'QGraphicsViewOptimizationFlag': (
          '_q_graphics_view_optimization_flag', 'OptimizationFlag'),
      'QGraphicsViewViewportAnchor': (
          '_q_graphics_view_viewport_anchor', 'ViewportAnchor'),
      'QGraphicsViewViewportUpdateMode': (
          '_q_graphics_view_viewport_update_mode', 'ViewportUpdateMode'),
      'QHeaderViewResizeMode': ('_q_header_view_resize_mode', 'ResizeMode'),
      'QInputDialogInputDialogOption': (
          '_q_input_dialog_input_dialog_option', 'InputDialogOption'),
      'QInputDialogInputMode': ('_q_input_dialog_input_mode', 'InputMode'),
      'QLCDNumberMode': ('_q_l_c_d_number_mode', 'Mode'),
      'QLCDNumberSegmentStyle': (
          '_q_l_c_d_number_segment_style', 'SegmentStyle'),
      'QLayoutSizeConstraint': (
          '_q_layout_size_constraint', 'SizeConstraint'),
      'QLineEditActionPosition': (
          '_q_line_edit_action_position', 'ActionPosition'),
      'QLineEditEchoMode': ('_q_line_edit_echo_mode', 'EchoMode'),
      'QListViewFlow': ('_q_list_view_flow', 'Flow'),
      'QListViewLayoutMode': ('_q_list_view_layout_mode', 'LayoutMode'),
      'QListViewMovement': ('_q_list_view_movement', 'Movement'),
      'QListViewResizeMode': ('_q_list_view_resize_mode', 'ResizeMode'),
      'QListViewViewMode': ('_q_list_view_view_mode', 'ViewMode'),
      'QListWidgetItemItemType': (
          '_q_list_widget_item_item_type', 'ItemType'),
      'QMainWindowDockOption': ('_q_main_window_dock_option', 'DockOption'),
      'QMdiAreaAreaOption': ('_q_mdi_area_area_option', 'AreaOption'),
      'QMdiAreaViewMode': ('_q_mdi_area_view_mode', 'ViewMode'),
      'QMdiAreaWindowOrder': ('_q_mdi_area_window_order', 'WindowOrder'),
      'QMdiSubWindowSubWindowOption': (
          '_q_mdi_sub_window_sub_window_option', 'SubWindowOption'),
      'QMessageBoxButtonRole': ('_q_message_box_button_role', 'ButtonRole'),
      'QMessageBoxIcon': ('_q_message_box_icon', 'Icon'),
      'QMessageBoxOption': ('_q_message_box_option', 'Option'),
      'QMessageBoxStandardButton': (
          '_q_message_box_standard_button', 'StandardButton'),
      'QPinchGestureChangeFlag': (
          '_q_pinch_gesture_change_flag', 'ChangeFlag'),
      'QPlainTextEditLineWrapMode': (
          '_q_plain_text_edit_line_wrap_mode', 'LineWrapMode'),
      'QProgressBarDirection': ('_q_progress_bar_direction', 'Direction'),
      'QRubberBandShape': ('_q_rubber_band_shape', 'Shape'),
      'QScrollerInput': ('_q_scroller_input', 'Input'),
      'QScrollerScrollerGestureType': (
          '_q_scroller_scroller_gesture_type', 'ScrollerGestureType'),
      'QScrollerState': ('_q_scroller_state', 'State'),
      'QSizePolicyControlType': (
          '_q_size_policy_control_type', 'ControlType'),
      'QSizePolicyPolicy': ('_q_size_policy_policy', 'Policy'),
      'QSizePolicyPolicyFlag': ('_q_size_policy_policy_flag', 'PolicyFlag'),
      'QSliderTickPosition': ('_q_slider_tick_position', 'TickPosition'),
      'QStackedLayoutStackingMode': (
          '_q_stacked_layout_stacking_mode', 'StackingMode'),
      'QStyleComplexControl': ('_q_style_complex_control', 'ComplexControl'),
      'QStyleContentsType': ('_q_style_contents_type', 'ContentsType'),
      'QStyleControlElement': ('_q_style_control_element', 'ControlElement'),
      'QStyleOptionButtonButtonFeature': (
          '_q_style_option_button_button_feature', 'ButtonFeature'),
      'QStyleOptionButtonStyleOptionType': (
          '_q_style_option_button_style_option_type', 'StyleOptionType'),
      'QStyleOptionButtonStyleOptionVersion': (
          '_q_style_option_button_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionComboBoxStyleOptionType': (
          '_q_style_option_combo_box_style_option_type', 'StyleOptionType'),
      'QStyleOptionComboBoxStyleOptionVersion': (
          '_q_style_option_combo_box_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionComplexStyleOptionType': (
          '_q_style_option_complex_style_option_type', 'StyleOptionType'),
      'QStyleOptionComplexStyleOptionVersion': (
          '_q_style_option_complex_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionFocusRectStyleOptionType': (
          '_q_style_option_focus_rect_style_option_type', 'StyleOptionType'),
      'QStyleOptionFocusRectStyleOptionVersion': (
          '_q_style_option_focus_rect_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionFrameFrameFeature': (
          '_q_style_option_frame_frame_feature', 'FrameFeature'),
      'QStyleOptionFrameStyleOptionType': (
          '_q_style_option_frame_style_option_type', 'StyleOptionType'),
      'QStyleOptionFrameStyleOptionVersion': (
          '_q_style_option_frame_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionGraphicsItemStyleOptionType': (
          '_q_style_option_graphics_item_style_option_type',
          'StyleOptionType'),
      'QStyleOptionGraphicsItemStyleOptionVersion': (
          '_q_style_option_graphics_item_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionGroupBoxStyleOptionType': (
          '_q_style_option_group_box_style_option_type', 'StyleOptionType'),
      'QStyleOptionGroupBoxStyleOptionVersion': (
          '_q_style_option_group_box_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionHeaderSectionPosition': (
          '_q_style_option_header_section_position', 'SectionPosition'),
      'QStyleOptionHeaderSelectedPosition': (
          '_q_style_option_header_selected_position', 'SelectedPosition'),
      'QStyleOptionHeaderSortIndicator': (
          '_q_style_option_header_sort_indicator', 'SortIndicator'),
      'QStyleOptionHeaderStyleOptionType': (
          '_q_style_option_header_style_option_type', 'StyleOptionType'),
      'QStyleOptionHeaderStyleOptionVersion': (
          '_q_style_option_header_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionMenuItemCheckType': (
          '_q_style_option_menu_item_check_type', 'CheckType'),
      'QStyleOptionMenuItemMenuItemType': (
          '_q_style_option_menu_item_menu_item_type', 'MenuItemType'),
      'QStyleOptionMenuItemStyleOptionType': (
          '_q_style_option_menu_item_style_option_type', 'StyleOptionType'),
      'QStyleOptionMenuItemStyleOptionVersion': (
          '_q_style_option_menu_item_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionOptionType': (
          '_q_style_option_option_type', 'OptionType'),
      'QStyleOptionProgressBarStyleOptionType': (
          '_q_style_option_progress_bar_style_option_type',
          'StyleOptionType'),
      'QStyleOptionProgressBarStyleOptionVersion': (
          '_q_style_option_progress_bar_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionSliderStyleOptionType': (
          '_q_style_option_slider_style_option_type', 'StyleOptionType'),
      'QStyleOptionSliderStyleOptionVersion': (
          '_q_style_option_slider_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionSpinBoxStyleOptionType': (
          '_q_style_option_spin_box_style_option_type', 'StyleOptionType'),
      'QStyleOptionSpinBoxStyleOptionVersion': (
          '_q_style_option_spin_box_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionStyleOptionType': (
          '_q_style_option_style_option_type', 'StyleOptionType'),
      'QStyleOptionStyleOptionVersion': (
          '_q_style_option_style_option_version', 'StyleOptionVersion'),
      'QStyleOptionTabBarBaseStyleOptionType': (
          '_q_style_option_tab_bar_base_style_option_type',
          'StyleOptionType'),
      'QStyleOptionTabBarBaseStyleOptionVersion': (
          '_q_style_option_tab_bar_base_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionTabCornerWidget': (
          '_q_style_option_tab_corner_widget', 'CornerWidget'),
      'QStyleOptionTabSelectedPosition': (
          '_q_style_option_tab_selected_position', 'SelectedPosition'),
      'QStyleOptionTabStyleOptionType': (
          '_q_style_option_tab_style_option_type', 'StyleOptionType'),
      'QStyleOptionTabStyleOptionVersion': (
          '_q_style_option_tab_style_option_version', 'StyleOptionVersion'),
      'QStyleOptionTabTabFeature': (
          '_q_style_option_tab_tab_feature', 'TabFeature'),
      'QStyleOptionTabTabPosition': (
          '_q_style_option_tab_tab_position', 'TabPosition'),
      'QStyleOptionToolBarStyleOptionType': (
          '_q_style_option_tool_bar_style_option_type', 'StyleOptionType'),
      'QStyleOptionToolBarStyleOptionVersion': (
          '_q_style_option_tool_bar_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionToolBarToolBarFeature': (
          '_q_style_option_tool_bar_tool_bar_feature', 'ToolBarFeature'),
      'QStyleOptionToolBarToolBarPosition': (
          '_q_style_option_tool_bar_tool_bar_position', 'ToolBarPosition'),
      'QStyleOptionToolButtonStyleOptionType': (
          '_q_style_option_tool_button_style_option_type',
          'StyleOptionType'),
      'QStyleOptionToolButtonStyleOptionVersion': (
          '_q_style_option_tool_button_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionToolButtonToolButtonFeature': (
          '_q_style_option_tool_button_tool_button_feature',
          'ToolButtonFeature'),
      'QStyleOptionViewItemPosition': (
          '_q_style_option_view_item_position', 'Position'),
      'QStyleOptionViewItemStyleOptionType': (
          '_q_style_option_view_item_style_option_type', 'StyleOptionType'),
      'QStyleOptionViewItemStyleOptionVersion': (
          '_q_style_option_view_item_style_option_version',
          'StyleOptionVersion'),
      'QStyleOptionViewItemViewItemFeature': (
          '_q_style_option_view_item_view_item_feature', 'ViewItemFeature'),
      'QStyleOptionViewItemViewItemPosition': (
          '_q_style_option_view_item_view_item_position',
          'ViewItemPosition'),
      'QStylePixelMetric': ('_q_style_pixel_metric', 'PixelMetric'),
      'QStylePrimitiveElement': (
          '_q_style_primitive_element', 'PrimitiveElement'),
      'QStyleRequestSoftwareInputPanel': (
          '_q_style_request_software_input_panel',
          'RequestSoftwareInputPanel'),
      'QStyleStandardPixmap': ('_q_style_standard_pixmap', 'StandardPixmap'),
      'QStyleStateFlag': ('_q_style_state_flag', 'StateFlag'),
      'QStyleStyleHint': ('_q_style_style_hint', 'StyleHint'),
      'QStyleSubControl': ('_q_style_sub_control', 'SubControl'),
      'QStyleSubElement': ('_q_style_sub_element', 'SubElement'),
      'QSystemTrayIconActivationReason': (
          '_q_system_tray_icon_activation_reason', 'ActivationReason'),
      'QSystemTrayIconMessageIcon': (
          '_q_system_tray_icon_message_icon', 'MessageIcon'),
      'QTabBarButtonPosition': (
          '_q_tab_bar_button_position', 'ButtonPosition'),
      'QTabBarSelectionBehavior': (
          '_q_tab_bar_selection_behavior', 'SelectionBehavior'),
      'QTabBarShape': ('_q_tab_bar_shape', 'Shape'),
      'QTabWidgetTabPosition': ('_q_tab_widget_tab_position', 'TabPosition'),
      'QTabWidgetTabShape': ('_q_tab_widget_tab_shape', 'TabShape'),
      'QTableWidgetItemItemType': (
          '_q_table_widget_item_item_type', 'ItemType'),
      'QTextEditAutoFormattingFlag': (
          '_q_text_edit_auto_formatting_flag', 'AutoFormattingFlag'),
      'QTextEditLineWrapMode': (
          '_q_text_edit_line_wrap_mode', 'LineWrapMode'),
      'QToolButtonToolButtonPopupMode': (
          '_q_tool_button_tool_button_popup_mode', 'ToolButtonPopupMode'),
      'QTreeWidgetItemChildIndicatorPolicy': (
          '_q_tree_widget_item_child_indicator_policy',
          'ChildIndicatorPolicy'),
      'QTreeWidgetItemItemType': (
          '_q_tree_widget_item_item_type', 'ItemType'),
      'QTreeWidgetItemIteratorIteratorFlag': (
          '_q_tree_widget_item_iterator_iterator_flag', 'IteratorFlag'),
      'QWidgetRenderFlag': ('_q_widget_render_flag', 'RenderFlag'),
      'QWizardWizardButton': ('_q_wizard_wizard_button', 'WizardButton'),
      'QWizardWizardOption': ('_q_wizard_wizard_option', 'WizardOption'),
      'QWizardWizardPixmap': ('_q_wizard_wizard_pixmap', 'WizardPixmap'),
      'QWizardWizardStyle': ('_q_wizard_wizard_style', 'WizardStyle'),
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtWidgets import QTimeEdit'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time. An
    enum, or a class Qt writes inside another, is brought in the
    same way, by the name '__inner_files__' has for it.

    Raises
    ------

    AttributeError
      The part has nothing of that name.
    """
    if name in __class_files__:
      fileName, heldName = __class_files__[name], name
    elif name in __inner_files__:
      fileName, heldName = __inner_files__[name]
    else:
      infoSpec = """module '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (__name__, name))
    module = importlib.import_module('.%s' % fileName, __name__)
    value = getattr(module, heldName)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names every class of the part, brought in or not."""
    return [*__all__]
