"""
The 'cutienator.QtGui' package provides the cute classes of the part of
Qt named QtGui, under the name PySide6 has for it.

  from cutienator.QtGui import QColor, QFont

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
    'QAbstractUndoItem',
    'QAccessibleHyperlinkInterface',
    'QAccessibleImageInterface',
    'QAccessibleTableCellInterface',
    'QBrushData',
    'QPaintEngineState',
    'QRgba64',
    'QTextBlockUserData',
    'QTextFrameLayoutData',
    'QTextItem',
    'QTextLength',
    'QTextOption',
    'QBrushDataPointerDeleter',
    'QAccessibleViewportInterface',
    'QAccessibleActionInterface',
    'QAccessibleEditableTextInterface',
    'QColor',
    'QGenericPluginFactory',
    'QPageRanges',
    'QPageSize',
    'QPolygon',
    'QUndoCommand',
    'QColorTransform',
    'QPageLayout',
    'QPolygonF',
    'QAccessibilityHints',
    'QAccessibleBridgePlugin',
    'QAccessiblePlugin',
    'QAccessibleValueInterface',
    'QApplicationStateChangeEvent',
    'QCloseEvent',
    'QColorSpace',
    'QDesktopServices',
    'QDragLeaveEvent',
    'QDropEvent',
    'QFocusEvent',
    'QFontVariableAxis',
    'QGenericPlugin',
    'QGradient',
    'QHelpEvent',
    'QHideEvent',
    'QIconDragEvent',
    'QIconEnginePlugin',
    'QImageIOPlugin',
    'QInputDevice',
    'QInputDeviceManager',
    'QInputMethodEvent',
    'QInputMethodQueryEvent',
    'QInternalMimeData',
    'QKeySequence',
    'QMoveEvent',
    'QOpenGLContextGroup',
    'QPixelFormat',
    'QPlatformSurfaceEvent',
    'QPointingDeviceUniqueId',
    'QResizeEvent',
    'QScreen',
    'QScrollEvent',
    'QScrollPrepareEvent',
    'QShowEvent',
    'QStatusTipEvent',
    'QStyleHints',
    'QSurface',
    'QToolBarChangeEvent',
    'QUndoStack',
    'QValidator',
    'QWhatsThisClickedEvent',
    'QWindowStateChangeEvent',
    'QTransform',
    'QFont',
    'QRegion',
    'QFontInfo',
    'QFontDatabase',
    'QImageIOHandler',
    'QPainterPath',
    'QRawFont',
    'QGlyphRun',
    'QStaticText',
    'QBrush',
    'QPen',
    'QImageReader',
    'QImageWriter',
    'QPaintDevice',
    'QImage',
    'QPixmap',
    'QBitmap',
    'QPainter',
    'QPicture',
    'QConicalGradient',
    'QDoubleValidator',
    'QDragMoveEvent',
    'QInputEvent',
    'QIntValidator',
    'QLinearGradient',
    'QPdfOutputIntent',
    'QRadialGradient',
    'QRegularExpressionValidator',
    'QScreenOrientationChangeEvent',
    'QShortcut',
    'QSurfaceFormat',
    'QUndoGroup',
    'QClipboard',
    'QContextMenuEvent',
    'QCursor',
    'QDrag',
    'QDragEnterEvent',
    'QEventPoint',
    'QPointerEvent',
    'QPointingDevice',
    'QTouchEvent',
    'QExposeEvent',
    'QFileOpenEvent',
    'QFontMetrics',
    'QInputMethod',
    'QKeyEvent',
    'QVector4D',
    'QVector3D',
    'QQuaternion',
    'QMatrix4x4',
    'QVector2D',
    'QMovie',
    'QOffscreenSurface',
    'QOpenGLContext',
    'QPagedPaintDevice',
    'QPaintEvent',
    'QPainterPathStroker',
    'QPainterStateGuard',
    'QPalette',
    'QPixmapCache',
    'QShortcutEvent',
    'QTextFormat',
    'QBasicDrag',
    'QDragManager',
    'QFontMetricsF',
    'QInputControl',
    'QKeyMapper',
    'QOpenGLFunctionsPrivate',
    'QPdfWriter',
    'QSinglePointEvent',
    'QTextBlockFormat',
    'QTextCharFormat',
    'QTextFrameFormat',
    'QTextListFormat',
    'QEnterEvent',
    'QFontCache',
    'QHoverEvent',
    'QMouseEvent',
    'QNativeGestureEvent',
    'QOpenGLExtraFunctionsPrivate',
    'QOpenGLFunctions',
    'QSimpleDrag',
    'QTabletEvent',
    'QTextImageFormat',
    'QTextTableCellFormat',
    'QTextTableFormat',
    'QWheelEvent',
    'QAbstractFileIconProvider',
    'QTextDocument',
    'QTextBlock',
    'QTextInlineObject',
    'QTextLayout',
    'QTextObject',
    'QTextFrame',
    'QAbstractTextDocumentLayout',
    'QTextCursor',
    'QTextTable',
    'QTextDocumentFragment',
    'QIcon',
    'QIconEngine',
    'QWindow',
    'QOpenGLExtraFunctions',
    'QPaintEngine',
    'QAccessibleInterface',
    'QAccessible',
    'QAccessibleEvent',
    'QAction',
    'QActionGroup',
    'QBackingStore',
    'QChildWindowEvent',
    'QFileInfoGatherer',
    'QFileSystemModel',
    'QStandardItem',
    'QStandardItemModel',
    'QSyntaxHighlighter',
    'QTextDocumentWriter',
    'QTextFragment',
    'QTextLine',
    'QTextObjectInterface',
    'QTextTableCell',
    'QAccessibleAnnouncementEvent',
    'QAccessibleAttributesInterface',
    'QAccessibleBridge',
    'QAccessibleCache',
    'QAccessibleObject',
    'QAccessibleSelectionInterface',
    'QAccessibleStateChangeEvent',
    'QAccessibleTableModelChangeEvent',
    'QAccessibleTextCursorEvent',
    'QAccessibleTextInterface',
    'QAccessibleValueChangeEvent',
    'QActionEvent',
    'QBackingStoreRhiSupportWindowWatcher',
    'QGuiApplication',
    'QSessionManager',
    'QPaintDeviceWindow',
    'QTextBlockGroup',
    'QTextDocumentLayout',
    'QTextImageHandler',
    'QAccessibleApplication',
    'QAccessibleTableInterface',
    'QAccessibleTextInsertEvent',
    'QAccessibleTextRemoveEvent',
    'QAccessibleTextSelectionEvent',
    'QAccessibleTextUpdateEvent',
    'QRasterWindow',
    'QTextList',
    'QShapedPixmapWindow',
    'QWindowList',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_abstract_undo_item import QAbstractUndoItem
  from ._q_accessible_hyperlink_interface import QAccessibleHyperlinkInterface
  from ._q_accessible_image_interface import QAccessibleImageInterface
  from ._q_accessible_table_cell_interface import QAccessibleTableCellInterface
  from ._q_brush_data import QBrushData
  from ._q_paint_engine_state import QPaintEngineState
  from ._q_rgba64 import QRgba64
  from ._q_text_block_user_data import QTextBlockUserData
  from ._q_text_frame_layout_data import QTextFrameLayoutData
  from ._q_text_item import QTextItem
  from ._q_text_length import QTextLength
  from ._q_text_option import QTextOption
  from ._q_brush_data_pointer_deleter import QBrushDataPointerDeleter
  from ._q_accessible_viewport_interface import QAccessibleViewportInterface
  from ._q_accessible_action_interface import QAccessibleActionInterface
  from ._q_accessible_editable_text_interface import QAccessibleEditableTextInterface
  from ._q_color import QColor
  from ._q_generic_plugin_factory import QGenericPluginFactory
  from ._q_page_ranges import QPageRanges
  from ._q_page_size import QPageSize
  from ._q_polygon import QPolygon
  from ._q_undo_command import QUndoCommand
  from ._q_color_transform import QColorTransform
  from ._q_page_layout import QPageLayout
  from ._q_polygon_f import QPolygonF
  from ._q_accessibility_hints import QAccessibilityHints
  from ._q_accessible_bridge_plugin import QAccessibleBridgePlugin
  from ._q_accessible_plugin import QAccessiblePlugin
  from ._q_accessible_value_interface import QAccessibleValueInterface
  from ._q_application_state_change_event import QApplicationStateChangeEvent
  from ._q_close_event import QCloseEvent
  from ._q_color_space import QColorSpace
  from ._q_desktop_services import QDesktopServices
  from ._q_drag_leave_event import QDragLeaveEvent
  from ._q_drop_event import QDropEvent
  from ._q_focus_event import QFocusEvent
  from ._q_font_variable_axis import QFontVariableAxis
  from ._q_generic_plugin import QGenericPlugin
  from ._q_gradient import QGradient
  from ._q_help_event import QHelpEvent
  from ._q_hide_event import QHideEvent
  from ._q_icon_drag_event import QIconDragEvent
  from ._q_icon_engine_plugin import QIconEnginePlugin
  from ._q_image_i_o_plugin import QImageIOPlugin
  from ._q_input_device import QInputDevice
  from ._q_input_device_manager import QInputDeviceManager
  from ._q_input_method_event import QInputMethodEvent
  from ._q_input_method_query_event import QInputMethodQueryEvent
  from ._q_internal_mime_data import QInternalMimeData
  from ._q_key_sequence import QKeySequence
  from ._q_move_event import QMoveEvent
  from ._q_open_g_l_context_group import QOpenGLContextGroup
  from ._q_pixel_format import QPixelFormat
  from ._q_platform_surface_event import QPlatformSurfaceEvent
  from ._q_pointing_device_unique_id import QPointingDeviceUniqueId
  from ._q_resize_event import QResizeEvent
  from ._q_screen import QScreen
  from ._q_scroll_event import QScrollEvent
  from ._q_scroll_prepare_event import QScrollPrepareEvent
  from ._q_show_event import QShowEvent
  from ._q_status_tip_event import QStatusTipEvent
  from ._q_style_hints import QStyleHints
  from ._q_surface import QSurface
  from ._q_tool_bar_change_event import QToolBarChangeEvent
  from ._q_undo_stack import QUndoStack
  from ._q_validator import QValidator
  from ._q_whats_this_clicked_event import QWhatsThisClickedEvent
  from ._q_window_state_change_event import QWindowStateChangeEvent
  from ._q_transform import QTransform
  from ._q_font import QFont
  from ._q_region import QRegion
  from ._q_font_info import QFontInfo
  from ._q_font_database import QFontDatabase
  from ._q_image_i_o_handler import QImageIOHandler
  from ._q_painter_path import QPainterPath
  from ._q_raw_font import QRawFont
  from ._q_glyph_run import QGlyphRun
  from ._q_static_text import QStaticText
  from ._q_brush import QBrush
  from ._q_pen import QPen
  from ._q_image_reader import QImageReader
  from ._q_image_writer import QImageWriter
  from ._q_paint_device import QPaintDevice
  from ._q_image import QImage
  from ._q_pixmap import QPixmap
  from ._q_bitmap import QBitmap
  from ._q_painter import QPainter
  from ._q_picture import QPicture
  from ._q_conical_gradient import QConicalGradient
  from ._q_double_validator import QDoubleValidator
  from ._q_drag_move_event import QDragMoveEvent
  from ._q_input_event import QInputEvent
  from ._q_int_validator import QIntValidator
  from ._q_linear_gradient import QLinearGradient
  from ._q_pdf_output_intent import QPdfOutputIntent
  from ._q_radial_gradient import QRadialGradient
  from ._q_regular_expression_validator import QRegularExpressionValidator
  from ._q_screen_orientation_change_event import QScreenOrientationChangeEvent
  from ._q_shortcut import QShortcut
  from ._q_surface_format import QSurfaceFormat
  from ._q_undo_group import QUndoGroup
  from ._q_clipboard import QClipboard
  from ._q_context_menu_event import QContextMenuEvent
  from ._q_cursor import QCursor
  from ._q_drag import QDrag
  from ._q_drag_enter_event import QDragEnterEvent
  from ._q_event_point import QEventPoint
  from ._q_pointer_event import QPointerEvent
  from ._q_pointing_device import QPointingDevice
  from ._q_touch_event import QTouchEvent
  from ._q_expose_event import QExposeEvent
  from ._q_file_open_event import QFileOpenEvent
  from ._q_font_metrics import QFontMetrics
  from ._q_input_method import QInputMethod
  from ._q_key_event import QKeyEvent
  from ._q_vector4_d import QVector4D
  from ._q_vector3_d import QVector3D
  from ._q_quaternion import QQuaternion
  from ._q_matrix4x4 import QMatrix4x4
  from ._q_vector2_d import QVector2D
  from ._q_movie import QMovie
  from ._q_offscreen_surface import QOffscreenSurface
  from ._q_open_g_l_context import QOpenGLContext
  from ._q_paged_paint_device import QPagedPaintDevice
  from ._q_paint_event import QPaintEvent
  from ._q_painter_path_stroker import QPainterPathStroker
  from ._q_painter_state_guard import QPainterStateGuard
  from ._q_palette import QPalette
  from ._q_pixmap_cache import QPixmapCache
  from ._q_shortcut_event import QShortcutEvent
  from ._q_text_format import QTextFormat
  from ._q_basic_drag import QBasicDrag
  from ._q_drag_manager import QDragManager
  from ._q_font_metrics_f import QFontMetricsF
  from ._q_input_control import QInputControl
  from ._q_key_mapper import QKeyMapper
  from ._q_open_g_l_functions_private import QOpenGLFunctionsPrivate
  from ._q_pdf_writer import QPdfWriter
  from ._q_single_point_event import QSinglePointEvent
  from ._q_text_block_format import QTextBlockFormat
  from ._q_text_char_format import QTextCharFormat
  from ._q_text_frame_format import QTextFrameFormat
  from ._q_text_list_format import QTextListFormat
  from ._q_enter_event import QEnterEvent
  from ._q_font_cache import QFontCache
  from ._q_hover_event import QHoverEvent
  from ._q_mouse_event import QMouseEvent
  from ._q_native_gesture_event import QNativeGestureEvent
  from ._q_open_g_l_extra_functions_private import QOpenGLExtraFunctionsPrivate
  from ._q_open_g_l_functions import QOpenGLFunctions
  from ._q_simple_drag import QSimpleDrag
  from ._q_tablet_event import QTabletEvent
  from ._q_text_image_format import QTextImageFormat
  from ._q_text_table_cell_format import QTextTableCellFormat
  from ._q_text_table_format import QTextTableFormat
  from ._q_wheel_event import QWheelEvent
  from ._q_abstract_file_icon_provider import QAbstractFileIconProvider
  from ._q_text_document import QTextDocument
  from ._q_text_block import QTextBlock
  from ._q_text_inline_object import QTextInlineObject
  from ._q_text_layout import QTextLayout
  from ._q_text_object import QTextObject
  from ._q_text_frame import QTextFrame
  from ._q_abstract_text_document_layout import QAbstractTextDocumentLayout
  from ._q_text_cursor import QTextCursor
  from ._q_text_table import QTextTable
  from ._q_text_document_fragment import QTextDocumentFragment
  from ._q_icon import QIcon
  from ._q_icon_engine import QIconEngine
  from ._q_window import QWindow
  from ._q_open_g_l_extra_functions import QOpenGLExtraFunctions
  from ._q_paint_engine import QPaintEngine
  from ._q_accessible_interface import QAccessibleInterface
  from ._q_accessible import QAccessible
  from ._q_accessible_event import QAccessibleEvent
  from ._q_action import QAction
  from ._q_action_group import QActionGroup
  from ._q_backing_store import QBackingStore
  from ._q_child_window_event import QChildWindowEvent
  from ._q_file_info_gatherer import QFileInfoGatherer
  from ._q_file_system_model import QFileSystemModel
  from ._q_standard_item import QStandardItem
  from ._q_standard_item_model import QStandardItemModel
  from ._q_syntax_highlighter import QSyntaxHighlighter
  from ._q_text_document_writer import QTextDocumentWriter
  from ._q_text_fragment import QTextFragment
  from ._q_text_line import QTextLine
  from ._q_text_object_interface import QTextObjectInterface
  from ._q_text_table_cell import QTextTableCell
  from ._q_accessible_announcement_event import QAccessibleAnnouncementEvent
  from ._q_accessible_attributes_interface import QAccessibleAttributesInterface
  from ._q_accessible_bridge import QAccessibleBridge
  from ._q_accessible_cache import QAccessibleCache
  from ._q_accessible_object import QAccessibleObject
  from ._q_accessible_selection_interface import QAccessibleSelectionInterface
  from ._q_accessible_state_change_event import QAccessibleStateChangeEvent
  from ._q_accessible_table_model_change_event import QAccessibleTableModelChangeEvent
  from ._q_accessible_text_cursor_event import QAccessibleTextCursorEvent
  from ._q_accessible_text_interface import QAccessibleTextInterface
  from ._q_accessible_value_change_event import QAccessibleValueChangeEvent
  from ._q_action_event import QActionEvent
  from ._q_backing_store_rhi_support_window_watcher import QBackingStoreRhiSupportWindowWatcher
  from ._q_gui_application import QGuiApplication
  from ._q_session_manager import QSessionManager
  from ._q_paint_device_window import QPaintDeviceWindow
  from ._q_text_block_group import QTextBlockGroup
  from ._q_text_document_layout import QTextDocumentLayout
  from ._q_text_image_handler import QTextImageHandler
  from ._q_accessible_application import QAccessibleApplication
  from ._q_accessible_table_interface import QAccessibleTableInterface
  from ._q_accessible_text_insert_event import QAccessibleTextInsertEvent
  from ._q_accessible_text_remove_event import QAccessibleTextRemoveEvent
  from ._q_accessible_text_selection_event import QAccessibleTextSelectionEvent
  from ._q_accessible_text_update_event import QAccessibleTextUpdateEvent
  from ._q_raster_window import QRasterWindow
  from ._q_text_list import QTextList
  from ._q_shaped_pixmap_window import QShapedPixmapWindow
  from ._q_window import QWindowList
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QAbstractUndoItem': '_q_abstract_undo_item',
      'QAccessibleHyperlinkInterface': '_q_accessible_hyperlink_interface',
      'QAccessibleImageInterface': '_q_accessible_image_interface',
      'QAccessibleTableCellInterface': '_q_accessible_table_cell_interface',
      'QBrushData': '_q_brush_data',
      'QPaintEngineState': '_q_paint_engine_state',
      'QRgba64': '_q_rgba64',
      'QTextBlockUserData': '_q_text_block_user_data',
      'QTextFrameLayoutData': '_q_text_frame_layout_data',
      'QTextItem': '_q_text_item',
      'QTextLength': '_q_text_length',
      'QTextOption': '_q_text_option',
      'QBrushDataPointerDeleter': '_q_brush_data_pointer_deleter',
      'QAccessibleViewportInterface': '_q_accessible_viewport_interface',
      'QAccessibleActionInterface': '_q_accessible_action_interface',
      'QAccessibleEditableTextInterface': '_q_accessible_editable_text_interface',
      'QColor': '_q_color',
      'QGenericPluginFactory': '_q_generic_plugin_factory',
      'QPageRanges': '_q_page_ranges',
      'QPageSize': '_q_page_size',
      'QPolygon': '_q_polygon',
      'QUndoCommand': '_q_undo_command',
      'QColorTransform': '_q_color_transform',
      'QPageLayout': '_q_page_layout',
      'QPolygonF': '_q_polygon_f',
      'QAccessibilityHints': '_q_accessibility_hints',
      'QAccessibleBridgePlugin': '_q_accessible_bridge_plugin',
      'QAccessiblePlugin': '_q_accessible_plugin',
      'QAccessibleValueInterface': '_q_accessible_value_interface',
      'QApplicationStateChangeEvent': '_q_application_state_change_event',
      'QCloseEvent': '_q_close_event',
      'QColorSpace': '_q_color_space',
      'QDesktopServices': '_q_desktop_services',
      'QDragLeaveEvent': '_q_drag_leave_event',
      'QDropEvent': '_q_drop_event',
      'QFocusEvent': '_q_focus_event',
      'QFontVariableAxis': '_q_font_variable_axis',
      'QGenericPlugin': '_q_generic_plugin',
      'QGradient': '_q_gradient',
      'QHelpEvent': '_q_help_event',
      'QHideEvent': '_q_hide_event',
      'QIconDragEvent': '_q_icon_drag_event',
      'QIconEnginePlugin': '_q_icon_engine_plugin',
      'QImageIOPlugin': '_q_image_i_o_plugin',
      'QInputDevice': '_q_input_device',
      'QInputDeviceManager': '_q_input_device_manager',
      'QInputMethodEvent': '_q_input_method_event',
      'QInputMethodQueryEvent': '_q_input_method_query_event',
      'QInternalMimeData': '_q_internal_mime_data',
      'QKeySequence': '_q_key_sequence',
      'QMoveEvent': '_q_move_event',
      'QOpenGLContextGroup': '_q_open_g_l_context_group',
      'QPixelFormat': '_q_pixel_format',
      'QPlatformSurfaceEvent': '_q_platform_surface_event',
      'QPointingDeviceUniqueId': '_q_pointing_device_unique_id',
      'QResizeEvent': '_q_resize_event',
      'QScreen': '_q_screen',
      'QScrollEvent': '_q_scroll_event',
      'QScrollPrepareEvent': '_q_scroll_prepare_event',
      'QShowEvent': '_q_show_event',
      'QStatusTipEvent': '_q_status_tip_event',
      'QStyleHints': '_q_style_hints',
      'QSurface': '_q_surface',
      'QToolBarChangeEvent': '_q_tool_bar_change_event',
      'QUndoStack': '_q_undo_stack',
      'QValidator': '_q_validator',
      'QWhatsThisClickedEvent': '_q_whats_this_clicked_event',
      'QWindowStateChangeEvent': '_q_window_state_change_event',
      'QTransform': '_q_transform',
      'QFont': '_q_font',
      'QRegion': '_q_region',
      'QFontInfo': '_q_font_info',
      'QFontDatabase': '_q_font_database',
      'QImageIOHandler': '_q_image_i_o_handler',
      'QPainterPath': '_q_painter_path',
      'QRawFont': '_q_raw_font',
      'QGlyphRun': '_q_glyph_run',
      'QStaticText': '_q_static_text',
      'QBrush': '_q_brush',
      'QPen': '_q_pen',
      'QImageReader': '_q_image_reader',
      'QImageWriter': '_q_image_writer',
      'QPaintDevice': '_q_paint_device',
      'QImage': '_q_image',
      'QPixmap': '_q_pixmap',
      'QBitmap': '_q_bitmap',
      'QPainter': '_q_painter',
      'QPicture': '_q_picture',
      'QConicalGradient': '_q_conical_gradient',
      'QDoubleValidator': '_q_double_validator',
      'QDragMoveEvent': '_q_drag_move_event',
      'QInputEvent': '_q_input_event',
      'QIntValidator': '_q_int_validator',
      'QLinearGradient': '_q_linear_gradient',
      'QPdfOutputIntent': '_q_pdf_output_intent',
      'QRadialGradient': '_q_radial_gradient',
      'QRegularExpressionValidator': '_q_regular_expression_validator',
      'QScreenOrientationChangeEvent': '_q_screen_orientation_change_event',
      'QShortcut': '_q_shortcut',
      'QSurfaceFormat': '_q_surface_format',
      'QUndoGroup': '_q_undo_group',
      'QClipboard': '_q_clipboard',
      'QContextMenuEvent': '_q_context_menu_event',
      'QCursor': '_q_cursor',
      'QDrag': '_q_drag',
      'QDragEnterEvent': '_q_drag_enter_event',
      'QEventPoint': '_q_event_point',
      'QPointerEvent': '_q_pointer_event',
      'QPointingDevice': '_q_pointing_device',
      'QTouchEvent': '_q_touch_event',
      'QExposeEvent': '_q_expose_event',
      'QFileOpenEvent': '_q_file_open_event',
      'QFontMetrics': '_q_font_metrics',
      'QInputMethod': '_q_input_method',
      'QKeyEvent': '_q_key_event',
      'QVector4D': '_q_vector4_d',
      'QVector3D': '_q_vector3_d',
      'QQuaternion': '_q_quaternion',
      'QMatrix4x4': '_q_matrix4x4',
      'QVector2D': '_q_vector2_d',
      'QMovie': '_q_movie',
      'QOffscreenSurface': '_q_offscreen_surface',
      'QOpenGLContext': '_q_open_g_l_context',
      'QPagedPaintDevice': '_q_paged_paint_device',
      'QPaintEvent': '_q_paint_event',
      'QPainterPathStroker': '_q_painter_path_stroker',
      'QPainterStateGuard': '_q_painter_state_guard',
      'QPalette': '_q_palette',
      'QPixmapCache': '_q_pixmap_cache',
      'QShortcutEvent': '_q_shortcut_event',
      'QTextFormat': '_q_text_format',
      'QBasicDrag': '_q_basic_drag',
      'QDragManager': '_q_drag_manager',
      'QFontMetricsF': '_q_font_metrics_f',
      'QInputControl': '_q_input_control',
      'QKeyMapper': '_q_key_mapper',
      'QOpenGLFunctionsPrivate': '_q_open_g_l_functions_private',
      'QPdfWriter': '_q_pdf_writer',
      'QSinglePointEvent': '_q_single_point_event',
      'QTextBlockFormat': '_q_text_block_format',
      'QTextCharFormat': '_q_text_char_format',
      'QTextFrameFormat': '_q_text_frame_format',
      'QTextListFormat': '_q_text_list_format',
      'QEnterEvent': '_q_enter_event',
      'QFontCache': '_q_font_cache',
      'QHoverEvent': '_q_hover_event',
      'QMouseEvent': '_q_mouse_event',
      'QNativeGestureEvent': '_q_native_gesture_event',
      'QOpenGLExtraFunctionsPrivate': '_q_open_g_l_extra_functions_private',
      'QOpenGLFunctions': '_q_open_g_l_functions',
      'QSimpleDrag': '_q_simple_drag',
      'QTabletEvent': '_q_tablet_event',
      'QTextImageFormat': '_q_text_image_format',
      'QTextTableCellFormat': '_q_text_table_cell_format',
      'QTextTableFormat': '_q_text_table_format',
      'QWheelEvent': '_q_wheel_event',
      'QAbstractFileIconProvider': '_q_abstract_file_icon_provider',
      'QTextDocument': '_q_text_document',
      'QTextBlock': '_q_text_block',
      'QTextInlineObject': '_q_text_inline_object',
      'QTextLayout': '_q_text_layout',
      'QTextObject': '_q_text_object',
      'QTextFrame': '_q_text_frame',
      'QAbstractTextDocumentLayout': '_q_abstract_text_document_layout',
      'QTextCursor': '_q_text_cursor',
      'QTextTable': '_q_text_table',
      'QTextDocumentFragment': '_q_text_document_fragment',
      'QIcon': '_q_icon',
      'QIconEngine': '_q_icon_engine',
      'QWindow': '_q_window',
      'QOpenGLExtraFunctions': '_q_open_g_l_extra_functions',
      'QPaintEngine': '_q_paint_engine',
      'QAccessibleInterface': '_q_accessible_interface',
      'QAccessible': '_q_accessible',
      'QAccessibleEvent': '_q_accessible_event',
      'QAction': '_q_action',
      'QActionGroup': '_q_action_group',
      'QBackingStore': '_q_backing_store',
      'QChildWindowEvent': '_q_child_window_event',
      'QFileInfoGatherer': '_q_file_info_gatherer',
      'QFileSystemModel': '_q_file_system_model',
      'QStandardItem': '_q_standard_item',
      'QStandardItemModel': '_q_standard_item_model',
      'QSyntaxHighlighter': '_q_syntax_highlighter',
      'QTextDocumentWriter': '_q_text_document_writer',
      'QTextFragment': '_q_text_fragment',
      'QTextLine': '_q_text_line',
      'QTextObjectInterface': '_q_text_object_interface',
      'QTextTableCell': '_q_text_table_cell',
      'QAccessibleAnnouncementEvent': '_q_accessible_announcement_event',
      'QAccessibleAttributesInterface': '_q_accessible_attributes_interface',
      'QAccessibleBridge': '_q_accessible_bridge',
      'QAccessibleCache': '_q_accessible_cache',
      'QAccessibleObject': '_q_accessible_object',
      'QAccessibleSelectionInterface': '_q_accessible_selection_interface',
      'QAccessibleStateChangeEvent': '_q_accessible_state_change_event',
      'QAccessibleTableModelChangeEvent': '_q_accessible_table_model_change_event',
      'QAccessibleTextCursorEvent': '_q_accessible_text_cursor_event',
      'QAccessibleTextInterface': '_q_accessible_text_interface',
      'QAccessibleValueChangeEvent': '_q_accessible_value_change_event',
      'QActionEvent': '_q_action_event',
      'QBackingStoreRhiSupportWindowWatcher': '_q_backing_store_rhi_support_window_watcher',
      'QGuiApplication': '_q_gui_application',
      'QSessionManager': '_q_session_manager',
      'QPaintDeviceWindow': '_q_paint_device_window',
      'QTextBlockGroup': '_q_text_block_group',
      'QTextDocumentLayout': '_q_text_document_layout',
      'QTextImageHandler': '_q_text_image_handler',
      'QAccessibleApplication': '_q_accessible_application',
      'QAccessibleTableInterface': '_q_accessible_table_interface',
      'QAccessibleTextInsertEvent': '_q_accessible_text_insert_event',
      'QAccessibleTextRemoveEvent': '_q_accessible_text_remove_event',
      'QAccessibleTextSelectionEvent': '_q_accessible_text_selection_event',
      'QAccessibleTextUpdateEvent': '_q_accessible_text_update_event',
      'QRasterWindow': '_q_raster_window',
      'QTextList': '_q_text_list',
      'QShapedPixmapWindow': '_q_shaped_pixmap_window',
      'QWindowList': '_q_window',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtGui import QWindowList'. Python calls
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
