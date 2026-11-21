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
    'QStyleHintReturn',
    'QTableWidgetSelectionRange',
    'QTileRules',
    'QWidgetData',
    'QStyleHintReturnMask',
    'QStyleHintReturnVariant',
    'QLayoutItem',
    'QStyleFactory',
    'QColormap',
    'QSpacerItem',
    'QGesture',
    'QGraphicsAnchor',
    'QScrollerProperties',
    'QStylePlugin',
    'QGestureRecognizer',
    'QGraphicsEffect',
    'QPanGesture',
    'QPinchGesture',
    'QScroller',
    'QSwipeGesture',
    'QTapAndHoldGesture',
    'QTapGesture',
    'QGraphicsBlurEffect',
    'QGraphicsColorizeEffect',
    'QGraphicsDropShadowEffect',
    'QGraphicsOpacityEffect',
    'QGraphicsTransform',
    'QGraphicsRotation',
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
    'QAccessibleWidget',
    'QBoxLayout',
    'QCalendarWidget',
    'QCommonStyle',
    'QDialog',
    'QFocusFrame',
    'QFormLayout',
    'QGestureEvent',
    'QGraphicsSceneEvent',
    'QGridLayout',
    'QItemEditorCreatorBase',
    'QKeySequenceEdit',
    'QRhiWidget',
    'QSizeGrip',
    'QSplashScreen',
    'QStackedLayout',
    'QStatusBar',
    'QStyleOptionButton',
    'QStyleOptionComboBox',
    'QStyleOptionDockWidget',
    'QStyleOptionFocusRect',
    'QStyleOptionFrame',
    'QStyleOptionGraphicsItem',
    'QStyleOptionGroupBox',
    'QStyleOptionHeader',
    'QStyleOptionMenuItem',
    'QStyleOptionProgressBar',
    'QStyleOptionRubberBand',
    'QStyleOptionSizeGrip',
    'QStyleOptionSlider',
    'QStyleOptionSpinBox',
    'QStyleOptionTab',
    'QStyleOptionTabBarBase',
    'QStyleOptionTabWidgetFrame',
    'QStyleOptionTitleBar',
    'QStyleOptionToolBar',
    'QStyleOptionToolBox',
    'QStyleOptionToolButton',
    'QStyleOptionViewItem',
    'QStylePainter',
    'QToolTip',
    'QWhatsThis',
    'QWidgetAction',
    'QWidgetItem',
    'QAccessibleWidgetV2',
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
    'QGraphicsSceneDragDropEvent',
    'QGraphicsSceneHelpEvent',
    'QGraphicsSceneHoverEvent',
    'QGraphicsSceneMouseEvent',
    'QGraphicsSceneMoveEvent',
    'QGraphicsSceneResizeEvent',
    'QGraphicsSceneWheelEvent',
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
    'QStyleOptionHeaderV2',
    'QStyleOptionMenuItemV2',
    'QTabBar',
    'QToolBar',
    'QVBoxLayout',
    'QWidgetItemV2',
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
    'QGraphicsItemAnimation',
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
    'QColumnView',
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
    'QGraphicsAnchorLayout',
    'QGraphicsGridLayout',
    'QGraphicsLinearLayout',
    'QGraphicsWidget',
    'QLineEdit',
    'QListWidget',
    'QListWidgetItem',
    'QTableView',
    'QTreeView',
    'QUndoView',
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
  from ._q_style_hint_return import QStyleHintReturn
  from ._q_table_widget_selection_range import QTableWidgetSelectionRange
  from ._q_tile_rules import QTileRules
  from ._q_widget_data import QWidgetData
  from ._q_style_hint_return_mask import QStyleHintReturnMask
  from ._q_style_hint_return_variant import QStyleHintReturnVariant
  from ._q_layout_item import QLayoutItem
  from ._q_style_factory import QStyleFactory
  from ._q_colormap import QColormap
  from ._q_spacer_item import QSpacerItem
  from ._q_gesture import QGesture
  from ._q_graphics_anchor import QGraphicsAnchor
  from ._q_scroller_properties import QScrollerProperties
  from ._q_style_plugin import QStylePlugin
  from ._q_gesture_recognizer import QGestureRecognizer
  from ._q_graphics_effect import QGraphicsEffect
  from ._q_pan_gesture import QPanGesture
  from ._q_pinch_gesture import QPinchGesture
  from ._q_scroller import QScroller
  from ._q_swipe_gesture import QSwipeGesture
  from ._q_tap_and_hold_gesture import QTapAndHoldGesture
  from ._q_tap_gesture import QTapGesture
  from ._q_graphics_blur_effect import QGraphicsBlurEffect
  from ._q_graphics_colorize_effect import QGraphicsColorizeEffect
  from ._q_graphics_drop_shadow_effect import QGraphicsDropShadowEffect
  from ._q_graphics_opacity_effect import QGraphicsOpacityEffect
  from ._q_graphics_transform import QGraphicsTransform
  from ._q_graphics_rotation import QGraphicsRotation
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
  from ._q_accessible_widget import QAccessibleWidget
  from ._q_box_layout import QBoxLayout
  from ._q_calendar_widget import QCalendarWidget
  from ._q_common_style import QCommonStyle
  from ._q_dialog import QDialog
  from ._q_focus_frame import QFocusFrame
  from ._q_form_layout import QFormLayout
  from ._q_gesture_event import QGestureEvent
  from ._q_graphics_scene_event import QGraphicsSceneEvent
  from ._q_grid_layout import QGridLayout
  from ._q_item_editor_creator_base import QItemEditorCreatorBase
  from ._q_key_sequence_edit import QKeySequenceEdit
  from ._q_rhi_widget import QRhiWidget
  from ._q_size_grip import QSizeGrip
  from ._q_splash_screen import QSplashScreen
  from ._q_stacked_layout import QStackedLayout
  from ._q_status_bar import QStatusBar
  from ._q_style_option_button import QStyleOptionButton
  from ._q_style_option_combo_box import QStyleOptionComboBox
  from ._q_style_option_dock_widget import QStyleOptionDockWidget
  from ._q_style_option_focus_rect import QStyleOptionFocusRect
  from ._q_style_option_frame import QStyleOptionFrame
  from ._q_style_option_graphics_item import QStyleOptionGraphicsItem
  from ._q_style_option_group_box import QStyleOptionGroupBox
  from ._q_style_option_header import QStyleOptionHeader
  from ._q_style_option_menu_item import QStyleOptionMenuItem
  from ._q_style_option_progress_bar import QStyleOptionProgressBar
  from ._q_style_option_rubber_band import QStyleOptionRubberBand
  from ._q_style_option_size_grip import QStyleOptionSizeGrip
  from ._q_style_option_slider import QStyleOptionSlider
  from ._q_style_option_spin_box import QStyleOptionSpinBox
  from ._q_style_option_tab import QStyleOptionTab
  from ._q_style_option_tab_bar_base import QStyleOptionTabBarBase
  from ._q_style_option_tab_widget_frame import QStyleOptionTabWidgetFrame
  from ._q_style_option_title_bar import QStyleOptionTitleBar
  from ._q_style_option_tool_bar import QStyleOptionToolBar
  from ._q_style_option_tool_box import QStyleOptionToolBox
  from ._q_style_option_tool_button import QStyleOptionToolButton
  from ._q_style_option_view_item import QStyleOptionViewItem
  from ._q_style_painter import QStylePainter
  from ._q_tool_tip import QToolTip
  from ._q_whats_this import QWhatsThis
  from ._q_widget_action import QWidgetAction
  from ._q_widget_item import QWidgetItem
  from ._q_accessible_widget_v2 import QAccessibleWidgetV2
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
  from ._q_graphics_scene_drag_drop_event import QGraphicsSceneDragDropEvent
  from ._q_graphics_scene_help_event import QGraphicsSceneHelpEvent
  from ._q_graphics_scene_hover_event import QGraphicsSceneHoverEvent
  from ._q_graphics_scene_mouse_event import QGraphicsSceneMouseEvent
  from ._q_graphics_scene_move_event import QGraphicsSceneMoveEvent
  from ._q_graphics_scene_resize_event import QGraphicsSceneResizeEvent
  from ._q_graphics_scene_wheel_event import QGraphicsSceneWheelEvent
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
  from ._q_style_option_header_v2 import QStyleOptionHeaderV2
  from ._q_style_option_menu_item_v2 import QStyleOptionMenuItemV2
  from ._q_tab_bar import QTabBar
  from ._q_tool_bar import QToolBar
  from ._q_v_box_layout import QVBoxLayout
  from ._q_widget_item_v2 import QWidgetItemV2
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
  from ._q_graphics_item_animation import QGraphicsItemAnimation
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
  from ._q_column_view import QColumnView
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
  from ._q_graphics_anchor_layout import QGraphicsAnchorLayout
  from ._q_graphics_grid_layout import QGraphicsGridLayout
  from ._q_graphics_linear_layout import QGraphicsLinearLayout
  from ._q_graphics_widget import QGraphicsWidget
  from ._q_line_edit import QLineEdit
  from ._q_list_widget import QListWidget
  from ._q_list_widget_item import QListWidgetItem
  from ._q_table_view import QTableView
  from ._q_tree_view import QTreeView
  from ._q_undo_view import QUndoView
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
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QSizePolicy': '_q_size_policy',
      'QStyleHintReturn': '_q_style_hint_return',
      'QTableWidgetSelectionRange': '_q_table_widget_selection_range',
      'QTileRules': '_q_tile_rules',
      'QWidgetData': '_q_widget_data',
      'QStyleHintReturnMask': '_q_style_hint_return_mask',
      'QStyleHintReturnVariant': '_q_style_hint_return_variant',
      'QLayoutItem': '_q_layout_item',
      'QStyleFactory': '_q_style_factory',
      'QColormap': '_q_colormap',
      'QSpacerItem': '_q_spacer_item',
      'QGesture': '_q_gesture',
      'QGraphicsAnchor': '_q_graphics_anchor',
      'QScrollerProperties': '_q_scroller_properties',
      'QStylePlugin': '_q_style_plugin',
      'QGestureRecognizer': '_q_gesture_recognizer',
      'QGraphicsEffect': '_q_graphics_effect',
      'QPanGesture': '_q_pan_gesture',
      'QPinchGesture': '_q_pinch_gesture',
      'QScroller': '_q_scroller',
      'QSwipeGesture': '_q_swipe_gesture',
      'QTapAndHoldGesture': '_q_tap_and_hold_gesture',
      'QTapGesture': '_q_tap_gesture',
      'QGraphicsBlurEffect': '_q_graphics_blur_effect',
      'QGraphicsColorizeEffect': '_q_graphics_colorize_effect',
      'QGraphicsDropShadowEffect': '_q_graphics_drop_shadow_effect',
      'QGraphicsOpacityEffect': '_q_graphics_opacity_effect',
      'QGraphicsTransform': '_q_graphics_transform',
      'QGraphicsRotation': '_q_graphics_rotation',
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
      'QAccessibleWidget': '_q_accessible_widget',
      'QBoxLayout': '_q_box_layout',
      'QCalendarWidget': '_q_calendar_widget',
      'QCommonStyle': '_q_common_style',
      'QDialog': '_q_dialog',
      'QFocusFrame': '_q_focus_frame',
      'QFormLayout': '_q_form_layout',
      'QGestureEvent': '_q_gesture_event',
      'QGraphicsSceneEvent': '_q_graphics_scene_event',
      'QGridLayout': '_q_grid_layout',
      'QItemEditorCreatorBase': '_q_item_editor_creator_base',
      'QKeySequenceEdit': '_q_key_sequence_edit',
      'QRhiWidget': '_q_rhi_widget',
      'QSizeGrip': '_q_size_grip',
      'QSplashScreen': '_q_splash_screen',
      'QStackedLayout': '_q_stacked_layout',
      'QStatusBar': '_q_status_bar',
      'QStyleOptionButton': '_q_style_option_button',
      'QStyleOptionComboBox': '_q_style_option_combo_box',
      'QStyleOptionDockWidget': '_q_style_option_dock_widget',
      'QStyleOptionFocusRect': '_q_style_option_focus_rect',
      'QStyleOptionFrame': '_q_style_option_frame',
      'QStyleOptionGraphicsItem': '_q_style_option_graphics_item',
      'QStyleOptionGroupBox': '_q_style_option_group_box',
      'QStyleOptionHeader': '_q_style_option_header',
      'QStyleOptionMenuItem': '_q_style_option_menu_item',
      'QStyleOptionProgressBar': '_q_style_option_progress_bar',
      'QStyleOptionRubberBand': '_q_style_option_rubber_band',
      'QStyleOptionSizeGrip': '_q_style_option_size_grip',
      'QStyleOptionSlider': '_q_style_option_slider',
      'QStyleOptionSpinBox': '_q_style_option_spin_box',
      'QStyleOptionTab': '_q_style_option_tab',
      'QStyleOptionTabBarBase': '_q_style_option_tab_bar_base',
      'QStyleOptionTabWidgetFrame': '_q_style_option_tab_widget_frame',
      'QStyleOptionTitleBar': '_q_style_option_title_bar',
      'QStyleOptionToolBar': '_q_style_option_tool_bar',
      'QStyleOptionToolBox': '_q_style_option_tool_box',
      'QStyleOptionToolButton': '_q_style_option_tool_button',
      'QStyleOptionViewItem': '_q_style_option_view_item',
      'QStylePainter': '_q_style_painter',
      'QToolTip': '_q_tool_tip',
      'QWhatsThis': '_q_whats_this',
      'QWidgetAction': '_q_widget_action',
      'QWidgetItem': '_q_widget_item',
      'QAccessibleWidgetV2': '_q_accessible_widget_v2',
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
      'QGraphicsSceneDragDropEvent': '_q_graphics_scene_drag_drop_event',
      'QGraphicsSceneHelpEvent': '_q_graphics_scene_help_event',
      'QGraphicsSceneHoverEvent': '_q_graphics_scene_hover_event',
      'QGraphicsSceneMouseEvent': '_q_graphics_scene_mouse_event',
      'QGraphicsSceneMoveEvent': '_q_graphics_scene_move_event',
      'QGraphicsSceneResizeEvent': '_q_graphics_scene_resize_event',
      'QGraphicsSceneWheelEvent': '_q_graphics_scene_wheel_event',
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
      'QStyleOptionHeaderV2': '_q_style_option_header_v2',
      'QStyleOptionMenuItemV2': '_q_style_option_menu_item_v2',
      'QTabBar': '_q_tab_bar',
      'QToolBar': '_q_tool_bar',
      'QVBoxLayout': '_q_v_box_layout',
      'QWidgetItemV2': '_q_widget_item_v2',
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
      'QGraphicsItemAnimation': '_q_graphics_item_animation',
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
      'QColumnView': '_q_column_view',
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
      'QGraphicsAnchorLayout': '_q_graphics_anchor_layout',
      'QGraphicsGridLayout': '_q_graphics_grid_layout',
      'QGraphicsLinearLayout': '_q_graphics_linear_layout',
      'QGraphicsWidget': '_q_graphics_widget',
      'QLineEdit': '_q_line_edit',
      'QListWidget': '_q_list_widget',
      'QListWidgetItem': '_q_list_widget_item',
      'QTableView': '_q_table_view',
      'QTreeView': '_q_tree_view',
      'QUndoView': '_q_undo_view',
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


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtWidgets import QTimeEdit'. Python calls
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
