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
    'QPaintEngineState',
    'QPixelFormat',
    'QRgba64',
    'QSurface',
    'QTextBlockUserData',
    'QTextItem',
    'QTextLength',
    'QTextOption',
    'QCloseEvent',
    'QDragLeaveEvent',
    'QFocusEvent',
    'QHelpEvent',
    'QHideEvent',
    'QMoveEvent',
    'QShowEvent',
    'QTextBlock',
    'QWindowStateChangeEvent',
    'QResizeEvent',
    'QColor',
    'QColorSpace',
    'QInputMethodEvent',
    'QKeySequence',
    'QPageSize',
    'QPolygon',
    'QStatusTipEvent',
    'QUndoCommand',
    'QColorTransform',
    'QGradient',
    'QPageLayout',
    'QPolygonF',
    'QSurfaceFormat',
    'QLinearGradient',
    'QRadialGradient',
    'QTransform',
    'QFont',
    'QRegion',
    'QFontInfo',
    'QFontDatabase',
    'QPainterPath',
    'QRawFont',
    'QStaticText',
    'QBrush',
    'QPen',
    'QImageIOHandler',
    'QImageReader',
    'QPaintDevice',
    'QImage',
    'QPixmap',
    'QBitmap',
    'QPainter',
    'QPicture',
    'QDesktopServices',
    'QInputDevice',
    'QScreen',
    'QSessionManager',
    'QShortcut',
    'QStyleHints',
    'QUndoStack',
    'QValidator',
    'QClipboard',
    'QCursor',
    'QDoubleValidator',
    'QDrag',
    'QDropEvent',
    'QExposeEvent',
    'QFontMetrics',
    'QImageWriter',
    'QInputEvent',
    'QIntValidator',
    'QVector4D',
    'QVector3D',
    'QQuaternion',
    'QMatrix4x4',
    'QVector2D',
    'QMovie',
    'QOffscreenSurface',
    'QOpenGLContext',
    'QPagedPaintDevice',
    'QPaintEngine',
    'QPaintEvent',
    'QPainterPathStroker',
    'QPalette',
    'QPixmapCache',
    'QRegularExpressionValidator',
    'QTextFormat',
    'QTextLayout',
    'QUndoGroup',
    'QContextMenuEvent',
    'QDragMoveEvent',
    'QEventPoint',
    'QPointerEvent',
    'QPointingDevice',
    'QFileOpenEvent',
    'QFontMetricsF',
    'QKeyEvent',
    'QPdfWriter',
    'QTextBlockFormat',
    'QTextCharFormat',
    'QTextFrameFormat',
    'QTextLine',
    'QTextListFormat',
    'QDragEnterEvent',
    'QSinglePointEvent',
    'QTextImageFormat',
    'QTextTableCellFormat',
    'QTextTableFormat',
    'QAbstractFileIconProvider',
    'QTextDocument',
    'QTextDocumentFragment',
    'QTextObject',
    'QTextFrame',
    'QAbstractTextDocumentLayout',
    'QTextCursor',
    'QEnterEvent',
    'QHoverEvent',
    'QMouseEvent',
    'QNativeGestureEvent',
    'QTabletEvent',
    'QWheelEvent',
    'QFileSystemModel',
    'QIcon',
    'QIconEngine',
    'QWindow',
    'QSyntaxHighlighter',
    'QTextDocumentWriter',
    'QAction',
    'QActionGroup',
    'QBackingStore',
    'QGuiApplication',
    'QStandardItem',
    'QStandardItemModel',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_paint_engine_state import QPaintEngineState
  from ._q_pixel_format import QPixelFormat
  from ._q_rgba64 import QRgba64
  from ._q_surface import QSurface
  from ._q_text_block_user_data import QTextBlockUserData
  from ._q_text_item import QTextItem
  from ._q_text_length import QTextLength
  from ._q_text_option import QTextOption
  from ._q_close_event import QCloseEvent
  from ._q_drag_leave_event import QDragLeaveEvent
  from ._q_focus_event import QFocusEvent
  from ._q_help_event import QHelpEvent
  from ._q_hide_event import QHideEvent
  from ._q_move_event import QMoveEvent
  from ._q_show_event import QShowEvent
  from ._q_text_block import QTextBlock
  from ._q_window_state_change_event import QWindowStateChangeEvent
  from ._q_resize_event import QResizeEvent
  from ._q_color import QColor
  from ._q_color_space import QColorSpace
  from ._q_input_method_event import QInputMethodEvent
  from ._q_key_sequence import QKeySequence
  from ._q_page_size import QPageSize
  from ._q_polygon import QPolygon
  from ._q_status_tip_event import QStatusTipEvent
  from ._q_undo_command import QUndoCommand
  from ._q_color_transform import QColorTransform
  from ._q_gradient import QGradient
  from ._q_page_layout import QPageLayout
  from ._q_polygon_f import QPolygonF
  from ._q_surface_format import QSurfaceFormat
  from ._q_linear_gradient import QLinearGradient
  from ._q_radial_gradient import QRadialGradient
  from ._q_transform import QTransform
  from ._q_font import QFont
  from ._q_region import QRegion
  from ._q_font_info import QFontInfo
  from ._q_font_database import QFontDatabase
  from ._q_painter_path import QPainterPath
  from ._q_raw_font import QRawFont
  from ._q_static_text import QStaticText
  from ._q_brush import QBrush
  from ._q_pen import QPen
  from ._q_image_i_o_handler import QImageIOHandler
  from ._q_image_reader import QImageReader
  from ._q_paint_device import QPaintDevice
  from ._q_image import QImage
  from ._q_pixmap import QPixmap
  from ._q_bitmap import QBitmap
  from ._q_painter import QPainter
  from ._q_picture import QPicture
  from ._q_desktop_services import QDesktopServices
  from ._q_input_device import QInputDevice
  from ._q_screen import QScreen
  from ._q_session_manager import QSessionManager
  from ._q_shortcut import QShortcut
  from ._q_style_hints import QStyleHints
  from ._q_undo_stack import QUndoStack
  from ._q_validator import QValidator
  from ._q_clipboard import QClipboard
  from ._q_cursor import QCursor
  from ._q_double_validator import QDoubleValidator
  from ._q_drag import QDrag
  from ._q_drop_event import QDropEvent
  from ._q_expose_event import QExposeEvent
  from ._q_font_metrics import QFontMetrics
  from ._q_image_writer import QImageWriter
  from ._q_input_event import QInputEvent
  from ._q_int_validator import QIntValidator
  from ._q_vector4_d import QVector4D
  from ._q_vector3_d import QVector3D
  from ._q_quaternion import QQuaternion
  from ._q_matrix4x4 import QMatrix4x4
  from ._q_vector2_d import QVector2D
  from ._q_movie import QMovie
  from ._q_offscreen_surface import QOffscreenSurface
  from ._q_open_g_l_context import QOpenGLContext
  from ._q_paged_paint_device import QPagedPaintDevice
  from ._q_paint_engine import QPaintEngine
  from ._q_paint_event import QPaintEvent
  from ._q_painter_path_stroker import QPainterPathStroker
  from ._q_palette import QPalette
  from ._q_pixmap_cache import QPixmapCache
  from ._q_regular_expression_validator import QRegularExpressionValidator
  from ._q_text_format import QTextFormat
  from ._q_text_layout import QTextLayout
  from ._q_undo_group import QUndoGroup
  from ._q_context_menu_event import QContextMenuEvent
  from ._q_drag_move_event import QDragMoveEvent
  from ._q_event_point import QEventPoint
  from ._q_pointer_event import QPointerEvent
  from ._q_pointing_device import QPointingDevice
  from ._q_file_open_event import QFileOpenEvent
  from ._q_font_metrics_f import QFontMetricsF
  from ._q_key_event import QKeyEvent
  from ._q_pdf_writer import QPdfWriter
  from ._q_text_block_format import QTextBlockFormat
  from ._q_text_char_format import QTextCharFormat
  from ._q_text_frame_format import QTextFrameFormat
  from ._q_text_line import QTextLine
  from ._q_text_list_format import QTextListFormat
  from ._q_drag_enter_event import QDragEnterEvent
  from ._q_single_point_event import QSinglePointEvent
  from ._q_text_image_format import QTextImageFormat
  from ._q_text_table_cell_format import QTextTableCellFormat
  from ._q_text_table_format import QTextTableFormat
  from ._q_abstract_file_icon_provider import QAbstractFileIconProvider
  from ._q_text_document import QTextDocument
  from ._q_text_document_fragment import QTextDocumentFragment
  from ._q_text_object import QTextObject
  from ._q_text_frame import QTextFrame
  from ._q_abstract_text_document_layout import QAbstractTextDocumentLayout
  from ._q_text_cursor import QTextCursor
  from ._q_enter_event import QEnterEvent
  from ._q_hover_event import QHoverEvent
  from ._q_mouse_event import QMouseEvent
  from ._q_native_gesture_event import QNativeGestureEvent
  from ._q_tablet_event import QTabletEvent
  from ._q_wheel_event import QWheelEvent
  from ._q_file_system_model import QFileSystemModel
  from ._q_icon import QIcon
  from ._q_icon_engine import QIconEngine
  from ._q_window import QWindow
  from ._q_syntax_highlighter import QSyntaxHighlighter
  from ._q_text_document_writer import QTextDocumentWriter
  from ._q_action import QAction
  from ._q_action_group import QActionGroup
  from ._q_backing_store import QBackingStore
  from ._q_gui_application import QGuiApplication
  from ._q_standard_item import QStandardItem
  from ._q_standard_item_model import QStandardItemModel
  from ._q_abstract_file_icon_provider_icon_type import (
      IconType as QAbstractFileIconProviderIconType)
  from ._q_abstract_file_icon_provider_option import (
      Option as QAbstractFileIconProviderOption)
  from ._q_action_action_event import ActionEvent as QActionActionEvent
  from ._q_action_group_exclusion_policy import (
      ExclusionPolicy as QActionGroupExclusionPolicy)
  from ._q_action_menu_role import MenuRole as QActionMenuRole
  from ._q_action_priority import Priority as QActionPriority
  from ._q_clipboard_mode import Mode as QClipboardMode
  from ._q_color_name_format import NameFormat as QColorNameFormat
  from ._q_color_space_color_model import ColorModel as QColorSpaceColorModel
  from ._q_color_space_named_color_space import (
      NamedColorSpace as QColorSpaceNamedColorSpace)
  from ._q_color_space_primaries import Primaries as QColorSpacePrimaries
  from ._q_color_space__primary_points import (
      PrimaryPoints as QColorSpacePrimaryPoints)
  from ._q_color_space_transfer_function import (
      TransferFunction as QColorSpaceTransferFunction)
  from ._q_color_space_transform_model import (
      TransformModel as QColorSpaceTransformModel)
  from ._q_color_spec import Spec as QColorSpec
  from ._q_context_menu_event_reason import Reason as QContextMenuEventReason
  from ._q_double_validator_notation import (
      Notation as QDoubleValidatorNotation)
  from ._q_event_point_state import State as QEventPointState
  from ._q_file_system_model_option import Option as QFileSystemModelOption
  from ._q_file_system_model_roles import Roles as QFileSystemModelRoles
  from ._q_font_capitalization import Capitalization as QFontCapitalization
  from ._q_font_database_system_font import (
      SystemFont as QFontDatabaseSystemFont)
  from ._q_font_database_writing_system import (
      WritingSystem as QFontDatabaseWritingSystem)
  from ._q_font_hinting_preference import (
      HintingPreference as QFontHintingPreference)
  from ._q_font_resolve_properties import (
      ResolveProperties as QFontResolveProperties)
  from ._q_font_spacing_type import SpacingType as QFontSpacingType
  from ._q_font_stretch import Stretch as QFontStretch
  from ._q_font_style import Style as QFontStyle
  from ._q_font_style_hint import StyleHint as QFontStyleHint
  from ._q_font_style_strategy import StyleStrategy as QFontStyleStrategy
  from ._q_font__tag import Tag as QFontTag
  from ._q_font_weight import Weight as QFontWeight
  from ._q_gradient_coordinate_mode import (
      CoordinateMode as QGradientCoordinateMode)
  from ._q_gradient_interpolation_mode import (
      InterpolationMode as QGradientInterpolationMode)
  from ._q_gradient_preset import Preset as QGradientPreset
  from ._q_gradient_spread import Spread as QGradientSpread
  from ._q_gradient_type import Type as QGradientType
  from ._q_icon_engine_icon_engine_hook import (
      IconEngineHook as QIconEngineIconEngineHook)
  from ._q_icon_mode import Mode as QIconMode
  from ._q_icon_state import State as QIconState
  from ._q_icon_theme_icon import ThemeIcon as QIconThemeIcon
  from ._q_image_format import Format as QImageFormat
  from ._q_image_i_o_handler_image_option import (
      ImageOption as QImageIOHandlerImageOption)
  from ._q_image_i_o_handler_transformation import (
      Transformation as QImageIOHandlerTransformation)
  from ._q_image_invert_mode import InvertMode as QImageInvertMode
  from ._q_image_reader_image_reader_error import (
      ImageReaderError as QImageReaderImageReaderError)
  from ._q_image_writer_image_writer_error import (
      ImageWriterError as QImageWriterImageWriterError)
  from ._q_input_device_capability import (
      Capability as QInputDeviceCapability)
  from ._q_input_device_device_type import (
      DeviceType as QInputDeviceDeviceType)
  from ._q_input_method_event_attribute_type import (
      AttributeType as QInputMethodEventAttributeType)
  from ._q_key_sequence_sequence_format import (
      SequenceFormat as QKeySequenceSequenceFormat)
  from ._q_key_sequence_sequence_match import (
      SequenceMatch as QKeySequenceSequenceMatch)
  from ._q_key_sequence_standard_key import (
      StandardKey as QKeySequenceStandardKey)
  from ._q_matrix4x4_flag import Flag as QMatrix4x4Flag
  from ._q_movie_cache_mode import CacheMode as QMovieCacheMode
  from ._q_movie_movie_state import MovieState as QMovieMovieState
  from ._q_open_g_l_context_open_g_l_module_type import (
      OpenGLModuleType as QOpenGLContextOpenGLModuleType)
  from ._q_page_layout_mode import Mode as QPageLayoutMode
  from ._q_page_layout_orientation import (
      Orientation as QPageLayoutOrientation)
  from ._q_page_layout_out_of_bounds_policy import (
      OutOfBoundsPolicy as QPageLayoutOutOfBoundsPolicy)
  from ._q_page_layout_unit import Unit as QPageLayoutUnit
  from ._q_page_size_page_size_id import PageSizeId as QPageSizePageSizeId
  from ._q_page_size_size_match_policy import (
      SizeMatchPolicy as QPageSizeSizeMatchPolicy)
  from ._q_page_size_unit import Unit as QPageSizeUnit
  from ._q_paged_paint_device_pdf_version import (
      PdfVersion as QPagedPaintDevicePdfVersion)
  from ._q_paint_device_paint_device_metric import (
      PaintDeviceMetric as QPaintDevicePaintDeviceMetric)
  from ._q_paint_engine_dirty_flag import DirtyFlag as QPaintEngineDirtyFlag
  from ._q_paint_engine_paint_engine_feature import (
      PaintEngineFeature as QPaintEnginePaintEngineFeature)
  from ._q_paint_engine_polygon_draw_mode import (
      PolygonDrawMode as QPaintEnginePolygonDrawMode)
  from ._q_paint_engine_type import Type as QPaintEngineType
  from ._q_painter_composition_mode import (
      CompositionMode as QPainterCompositionMode)
  from ._q_painter_path_element_type import (
      ElementType as QPainterPathElementType)
  from ._q_painter_pixmap_fragment_hint import (
      PixmapFragmentHint as QPainterPixmapFragmentHint)
  from ._q_painter_render_hint import RenderHint as QPainterRenderHint
  from ._q_palette_color_group import ColorGroup as QPaletteColorGroup
  from ._q_palette_color_role import ColorRole as QPaletteColorRole
  from ._q_pdf_writer_color_model import ColorModel as QPdfWriterColorModel
  from ._q_pixel_format_alpha_position import (
      AlphaPosition as QPixelFormatAlphaPosition)
  from ._q_pixel_format_alpha_premultiplied import (
      AlphaPremultiplied as QPixelFormatAlphaPremultiplied)
  from ._q_pixel_format_alpha_usage import (
      AlphaUsage as QPixelFormatAlphaUsage)
  from ._q_pixel_format_byte_order import ByteOrder as QPixelFormatByteOrder
  from ._q_pixel_format_color_model import (
      ColorModel as QPixelFormatColorModel)
  from ._q_pixel_format_type_interpretation import (
      TypeInterpretation as QPixelFormatTypeInterpretation)
  from ._q_pixel_format_y_u_v_layout import (
      YUVLayout as QPixelFormatYUVLayout)
  from ._q_pointing_device_grab_transition import (
      GrabTransition as QPointingDeviceGrabTransition)
  from ._q_pointing_device_pointer_type import (
      PointerType as QPointingDevicePointerType)
  from ._q_raw_font_antialiasing_type import (
      AntialiasingType as QRawFontAntialiasingType)
  from ._q_raw_font_layout_flag import LayoutFlag as QRawFontLayoutFlag
  from ._q_region_region_type import RegionType as QRegionRegionType
  from ._q_session_manager_restart_hint import (
      RestartHint as QSessionManagerRestartHint)
  from ._q_standard_item_item_type import ItemType as QStandardItemItemType
  from ._q_static_text_performance_hint import (
      PerformanceHint as QStaticTextPerformanceHint)
  from ._q_surface_format_color_space import (
      ColorSpace as QSurfaceFormatColorSpace)
  from ._q_surface_format_format_option import (
      FormatOption as QSurfaceFormatFormatOption)
  from ._q_surface_format_open_g_l_context_profile import (
      OpenGLContextProfile as QSurfaceFormatOpenGLContextProfile)
  from ._q_surface_format_renderable_type import (
      RenderableType as QSurfaceFormatRenderableType)
  from ._q_surface_format_swap_behavior import (
      SwapBehavior as QSurfaceFormatSwapBehavior)
  from ._q_surface_surface_class import SurfaceClass as QSurfaceSurfaceClass
  from ._q_surface_surface_type import SurfaceType as QSurfaceSurfaceType
  from ._q_text_block_format_line_height_types import (
      LineHeightTypes as QTextBlockFormatLineHeightTypes)
  from ._q_text_block_format_marker_type import (
      MarkerType as QTextBlockFormatMarkerType)
  from ._q_text_char_format_font_properties_inheritance_behavior import (
      FontPropertiesInheritanceBehavior as
      QTextCharFormatFontPropertiesInheritanceBehavior)
  from ._q_text_char_format_underline_style import (
      UnderlineStyle as QTextCharFormatUnderlineStyle)
  from ._q_text_char_format_vertical_alignment import (
      VerticalAlignment as QTextCharFormatVerticalAlignment)
  from ._q_text_cursor_move_mode import MoveMode as QTextCursorMoveMode
  from ._q_text_cursor_move_operation import (
      MoveOperation as QTextCursorMoveOperation)
  from ._q_text_cursor_selection_type import (
      SelectionType as QTextCursorSelectionType)
  from ._q_text_document_find_flag import FindFlag as QTextDocumentFindFlag
  from ._q_text_document_markdown_feature import (
      MarkdownFeature as QTextDocumentMarkdownFeature)
  from ._q_text_document_meta_information import (
      MetaInformation as QTextDocumentMetaInformation)
  from ._q_text_document_resource_type import (
      ResourceType as QTextDocumentResourceType)
  from ._q_text_document_stacks import Stacks as QTextDocumentStacks
  from ._q_text_format_format_type import FormatType as QTextFormatFormatType
  from ._q_text_format_object_types import (
      ObjectTypes as QTextFormatObjectTypes)
  from ._q_text_format_page_break_flag import (
      PageBreakFlag as QTextFormatPageBreakFlag)
  from ._q_text_format_property import Property as QTextFormatProperty
  from ._q_text_frame_format_border_style import (
      BorderStyle as QTextFrameFormatBorderStyle)
  from ._q_text_frame_format_position import (
      Position as QTextFrameFormatPosition)
  from ._q_text_item_render_flag import RenderFlag as QTextItemRenderFlag
  from ._q_text_layout_cursor_mode import CursorMode as QTextLayoutCursorMode
  from ._q_text_layout_glyph_run_retrieval_flag import (
      GlyphRunRetrievalFlag as QTextLayoutGlyphRunRetrievalFlag)
  from ._q_text_length_type import Type as QTextLengthType
  from ._q_text_line_cursor_position import (
      CursorPosition as QTextLineCursorPosition)
  from ._q_text_line_edge import Edge as QTextLineEdge
  from ._q_text_list_format_style import Style as QTextListFormatStyle
  from ._q_text_option_flag import Flag as QTextOptionFlag
  from ._q_text_option_tab_type import TabType as QTextOptionTabType
  from ._q_text_option_wrap_mode import WrapMode as QTextOptionWrapMode
  from ._q_transform_transformation_type import (
      TransformationType as QTransformTransformationType)
  from ._q_validator_state import State as QValidatorState
  from ._q_window_ancestor_mode import AncestorMode as QWindowAncestorMode
  from ._q_window_visibility import Visibility as QWindowVisibility
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QPaintEngineState': '_q_paint_engine_state',
      'QPixelFormat': '_q_pixel_format',
      'QRgba64': '_q_rgba64',
      'QSurface': '_q_surface',
      'QTextBlockUserData': '_q_text_block_user_data',
      'QTextItem': '_q_text_item',
      'QTextLength': '_q_text_length',
      'QTextOption': '_q_text_option',
      'QCloseEvent': '_q_close_event',
      'QDragLeaveEvent': '_q_drag_leave_event',
      'QFocusEvent': '_q_focus_event',
      'QHelpEvent': '_q_help_event',
      'QHideEvent': '_q_hide_event',
      'QMoveEvent': '_q_move_event',
      'QShowEvent': '_q_show_event',
      'QTextBlock': '_q_text_block',
      'QWindowStateChangeEvent': '_q_window_state_change_event',
      'QResizeEvent': '_q_resize_event',
      'QColor': '_q_color',
      'QColorSpace': '_q_color_space',
      'QInputMethodEvent': '_q_input_method_event',
      'QKeySequence': '_q_key_sequence',
      'QPageSize': '_q_page_size',
      'QPolygon': '_q_polygon',
      'QStatusTipEvent': '_q_status_tip_event',
      'QUndoCommand': '_q_undo_command',
      'QColorTransform': '_q_color_transform',
      'QGradient': '_q_gradient',
      'QPageLayout': '_q_page_layout',
      'QPolygonF': '_q_polygon_f',
      'QSurfaceFormat': '_q_surface_format',
      'QLinearGradient': '_q_linear_gradient',
      'QRadialGradient': '_q_radial_gradient',
      'QTransform': '_q_transform',
      'QFont': '_q_font',
      'QRegion': '_q_region',
      'QFontInfo': '_q_font_info',
      'QFontDatabase': '_q_font_database',
      'QPainterPath': '_q_painter_path',
      'QRawFont': '_q_raw_font',
      'QStaticText': '_q_static_text',
      'QBrush': '_q_brush',
      'QPen': '_q_pen',
      'QImageIOHandler': '_q_image_i_o_handler',
      'QImageReader': '_q_image_reader',
      'QPaintDevice': '_q_paint_device',
      'QImage': '_q_image',
      'QPixmap': '_q_pixmap',
      'QBitmap': '_q_bitmap',
      'QPainter': '_q_painter',
      'QPicture': '_q_picture',
      'QDesktopServices': '_q_desktop_services',
      'QInputDevice': '_q_input_device',
      'QScreen': '_q_screen',
      'QSessionManager': '_q_session_manager',
      'QShortcut': '_q_shortcut',
      'QStyleHints': '_q_style_hints',
      'QUndoStack': '_q_undo_stack',
      'QValidator': '_q_validator',
      'QClipboard': '_q_clipboard',
      'QCursor': '_q_cursor',
      'QDoubleValidator': '_q_double_validator',
      'QDrag': '_q_drag',
      'QDropEvent': '_q_drop_event',
      'QExposeEvent': '_q_expose_event',
      'QFontMetrics': '_q_font_metrics',
      'QImageWriter': '_q_image_writer',
      'QInputEvent': '_q_input_event',
      'QIntValidator': '_q_int_validator',
      'QVector4D': '_q_vector4_d',
      'QVector3D': '_q_vector3_d',
      'QQuaternion': '_q_quaternion',
      'QMatrix4x4': '_q_matrix4x4',
      'QVector2D': '_q_vector2_d',
      'QMovie': '_q_movie',
      'QOffscreenSurface': '_q_offscreen_surface',
      'QOpenGLContext': '_q_open_g_l_context',
      'QPagedPaintDevice': '_q_paged_paint_device',
      'QPaintEngine': '_q_paint_engine',
      'QPaintEvent': '_q_paint_event',
      'QPainterPathStroker': '_q_painter_path_stroker',
      'QPalette': '_q_palette',
      'QPixmapCache': '_q_pixmap_cache',
      'QRegularExpressionValidator': '_q_regular_expression_validator',
      'QTextFormat': '_q_text_format',
      'QTextLayout': '_q_text_layout',
      'QUndoGroup': '_q_undo_group',
      'QContextMenuEvent': '_q_context_menu_event',
      'QDragMoveEvent': '_q_drag_move_event',
      'QEventPoint': '_q_event_point',
      'QPointerEvent': '_q_pointer_event',
      'QPointingDevice': '_q_pointing_device',
      'QFileOpenEvent': '_q_file_open_event',
      'QFontMetricsF': '_q_font_metrics_f',
      'QKeyEvent': '_q_key_event',
      'QPdfWriter': '_q_pdf_writer',
      'QTextBlockFormat': '_q_text_block_format',
      'QTextCharFormat': '_q_text_char_format',
      'QTextFrameFormat': '_q_text_frame_format',
      'QTextLine': '_q_text_line',
      'QTextListFormat': '_q_text_list_format',
      'QDragEnterEvent': '_q_drag_enter_event',
      'QSinglePointEvent': '_q_single_point_event',
      'QTextImageFormat': '_q_text_image_format',
      'QTextTableCellFormat': '_q_text_table_cell_format',
      'QTextTableFormat': '_q_text_table_format',
      'QAbstractFileIconProvider': '_q_abstract_file_icon_provider',
      'QTextDocument': '_q_text_document',
      'QTextDocumentFragment': '_q_text_document_fragment',
      'QTextObject': '_q_text_object',
      'QTextFrame': '_q_text_frame',
      'QAbstractTextDocumentLayout': '_q_abstract_text_document_layout',
      'QTextCursor': '_q_text_cursor',
      'QEnterEvent': '_q_enter_event',
      'QHoverEvent': '_q_hover_event',
      'QMouseEvent': '_q_mouse_event',
      'QNativeGestureEvent': '_q_native_gesture_event',
      'QTabletEvent': '_q_tablet_event',
      'QWheelEvent': '_q_wheel_event',
      'QFileSystemModel': '_q_file_system_model',
      'QIcon': '_q_icon',
      'QIconEngine': '_q_icon_engine',
      'QWindow': '_q_window',
      'QSyntaxHighlighter': '_q_syntax_highlighter',
      'QTextDocumentWriter': '_q_text_document_writer',
      'QAction': '_q_action',
      'QActionGroup': '_q_action_group',
      'QBackingStore': '_q_backing_store',
      'QGuiApplication': '_q_gui_application',
      'QStandardItem': '_q_standard_item',
      'QStandardItemModel': '_q_standard_item_model',
  }

  #  Where each enum is, and each class Qt writes inside another: the
  #  file, and the name it has there. The package gives each by what
  #  Qt writes it inside and its own name in one, so that the file of
  #  a class can ask for it as it asks for a class. None of them is
  #  in '__all__': a program reaches an enum through its class, as
  #  Qt writes it.
  __inner_files__ = {
      'QAbstractFileIconProviderIconType': (
          '_q_abstract_file_icon_provider_icon_type', 'IconType'),
      'QAbstractFileIconProviderOption': (
          '_q_abstract_file_icon_provider_option', 'Option'),
      'QActionActionEvent': ('_q_action_action_event', 'ActionEvent'),
      'QActionGroupExclusionPolicy': (
          '_q_action_group_exclusion_policy', 'ExclusionPolicy'),
      'QActionMenuRole': ('_q_action_menu_role', 'MenuRole'),
      'QActionPriority': ('_q_action_priority', 'Priority'),
      'QClipboardMode': ('_q_clipboard_mode', 'Mode'),
      'QColorNameFormat': ('_q_color_name_format', 'NameFormat'),
      'QColorSpaceColorModel': ('_q_color_space_color_model', 'ColorModel'),
      'QColorSpaceNamedColorSpace': (
          '_q_color_space_named_color_space', 'NamedColorSpace'),
      'QColorSpacePrimaries': ('_q_color_space_primaries', 'Primaries'),
      'QColorSpacePrimaryPoints': (
          '_q_color_space__primary_points', 'PrimaryPoints'),
      'QColorSpaceTransferFunction': (
          '_q_color_space_transfer_function', 'TransferFunction'),
      'QColorSpaceTransformModel': (
          '_q_color_space_transform_model', 'TransformModel'),
      'QColorSpec': ('_q_color_spec', 'Spec'),
      'QContextMenuEventReason': ('_q_context_menu_event_reason', 'Reason'),
      'QDoubleValidatorNotation': (
          '_q_double_validator_notation', 'Notation'),
      'QEventPointState': ('_q_event_point_state', 'State'),
      'QFileSystemModelOption': ('_q_file_system_model_option', 'Option'),
      'QFileSystemModelRoles': ('_q_file_system_model_roles', 'Roles'),
      'QFontCapitalization': ('_q_font_capitalization', 'Capitalization'),
      'QFontDatabaseSystemFont': (
          '_q_font_database_system_font', 'SystemFont'),
      'QFontDatabaseWritingSystem': (
          '_q_font_database_writing_system', 'WritingSystem'),
      'QFontHintingPreference': (
          '_q_font_hinting_preference', 'HintingPreference'),
      'QFontResolveProperties': (
          '_q_font_resolve_properties', 'ResolveProperties'),
      'QFontSpacingType': ('_q_font_spacing_type', 'SpacingType'),
      'QFontStretch': ('_q_font_stretch', 'Stretch'),
      'QFontStyle': ('_q_font_style', 'Style'),
      'QFontStyleHint': ('_q_font_style_hint', 'StyleHint'),
      'QFontStyleStrategy': ('_q_font_style_strategy', 'StyleStrategy'),
      'QFontTag': ('_q_font__tag', 'Tag'),
      'QFontWeight': ('_q_font_weight', 'Weight'),
      'QGradientCoordinateMode': (
          '_q_gradient_coordinate_mode', 'CoordinateMode'),
      'QGradientInterpolationMode': (
          '_q_gradient_interpolation_mode', 'InterpolationMode'),
      'QGradientPreset': ('_q_gradient_preset', 'Preset'),
      'QGradientSpread': ('_q_gradient_spread', 'Spread'),
      'QGradientType': ('_q_gradient_type', 'Type'),
      'QIconEngineIconEngineHook': (
          '_q_icon_engine_icon_engine_hook', 'IconEngineHook'),
      'QIconMode': ('_q_icon_mode', 'Mode'),
      'QIconState': ('_q_icon_state', 'State'),
      'QIconThemeIcon': ('_q_icon_theme_icon', 'ThemeIcon'),
      'QImageFormat': ('_q_image_format', 'Format'),
      'QImageIOHandlerImageOption': (
          '_q_image_i_o_handler_image_option', 'ImageOption'),
      'QImageIOHandlerTransformation': (
          '_q_image_i_o_handler_transformation', 'Transformation'),
      'QImageInvertMode': ('_q_image_invert_mode', 'InvertMode'),
      'QImageReaderImageReaderError': (
          '_q_image_reader_image_reader_error', 'ImageReaderError'),
      'QImageWriterImageWriterError': (
          '_q_image_writer_image_writer_error', 'ImageWriterError'),
      'QInputDeviceCapability': ('_q_input_device_capability', 'Capability'),
      'QInputDeviceDeviceType': (
          '_q_input_device_device_type', 'DeviceType'),
      'QInputMethodEventAttributeType': (
          '_q_input_method_event_attribute_type', 'AttributeType'),
      'QKeySequenceSequenceFormat': (
          '_q_key_sequence_sequence_format', 'SequenceFormat'),
      'QKeySequenceSequenceMatch': (
          '_q_key_sequence_sequence_match', 'SequenceMatch'),
      'QKeySequenceStandardKey': (
          '_q_key_sequence_standard_key', 'StandardKey'),
      'QMatrix4x4Flag': ('_q_matrix4x4_flag', 'Flag'),
      'QMovieCacheMode': ('_q_movie_cache_mode', 'CacheMode'),
      'QMovieMovieState': ('_q_movie_movie_state', 'MovieState'),
      'QOpenGLContextOpenGLModuleType': (
          '_q_open_g_l_context_open_g_l_module_type', 'OpenGLModuleType'),
      'QPageLayoutMode': ('_q_page_layout_mode', 'Mode'),
      'QPageLayoutOrientation': (
          '_q_page_layout_orientation', 'Orientation'),
      'QPageLayoutOutOfBoundsPolicy': (
          '_q_page_layout_out_of_bounds_policy', 'OutOfBoundsPolicy'),
      'QPageLayoutUnit': ('_q_page_layout_unit', 'Unit'),
      'QPageSizePageSizeId': ('_q_page_size_page_size_id', 'PageSizeId'),
      'QPageSizeSizeMatchPolicy': (
          '_q_page_size_size_match_policy', 'SizeMatchPolicy'),
      'QPageSizeUnit': ('_q_page_size_unit', 'Unit'),
      'QPagedPaintDevicePdfVersion': (
          '_q_paged_paint_device_pdf_version', 'PdfVersion'),
      'QPaintDevicePaintDeviceMetric': (
          '_q_paint_device_paint_device_metric', 'PaintDeviceMetric'),
      'QPaintEngineDirtyFlag': ('_q_paint_engine_dirty_flag', 'DirtyFlag'),
      'QPaintEnginePaintEngineFeature': (
          '_q_paint_engine_paint_engine_feature', 'PaintEngineFeature'),
      'QPaintEnginePolygonDrawMode': (
          '_q_paint_engine_polygon_draw_mode', 'PolygonDrawMode'),
      'QPaintEngineType': ('_q_paint_engine_type', 'Type'),
      'QPainterCompositionMode': (
          '_q_painter_composition_mode', 'CompositionMode'),
      'QPainterPathElementType': (
          '_q_painter_path_element_type', 'ElementType'),
      'QPainterPixmapFragmentHint': (
          '_q_painter_pixmap_fragment_hint', 'PixmapFragmentHint'),
      'QPainterRenderHint': ('_q_painter_render_hint', 'RenderHint'),
      'QPaletteColorGroup': ('_q_palette_color_group', 'ColorGroup'),
      'QPaletteColorRole': ('_q_palette_color_role', 'ColorRole'),
      'QPdfWriterColorModel': ('_q_pdf_writer_color_model', 'ColorModel'),
      'QPixelFormatAlphaPosition': (
          '_q_pixel_format_alpha_position', 'AlphaPosition'),
      'QPixelFormatAlphaPremultiplied': (
          '_q_pixel_format_alpha_premultiplied', 'AlphaPremultiplied'),
      'QPixelFormatAlphaUsage': (
          '_q_pixel_format_alpha_usage', 'AlphaUsage'),
      'QPixelFormatByteOrder': ('_q_pixel_format_byte_order', 'ByteOrder'),
      'QPixelFormatColorModel': (
          '_q_pixel_format_color_model', 'ColorModel'),
      'QPixelFormatTypeInterpretation': (
          '_q_pixel_format_type_interpretation', 'TypeInterpretation'),
      'QPixelFormatYUVLayout': ('_q_pixel_format_y_u_v_layout', 'YUVLayout'),
      'QPointingDeviceGrabTransition': (
          '_q_pointing_device_grab_transition', 'GrabTransition'),
      'QPointingDevicePointerType': (
          '_q_pointing_device_pointer_type', 'PointerType'),
      'QRawFontAntialiasingType': (
          '_q_raw_font_antialiasing_type', 'AntialiasingType'),
      'QRawFontLayoutFlag': ('_q_raw_font_layout_flag', 'LayoutFlag'),
      'QRegionRegionType': ('_q_region_region_type', 'RegionType'),
      'QSessionManagerRestartHint': (
          '_q_session_manager_restart_hint', 'RestartHint'),
      'QStandardItemItemType': ('_q_standard_item_item_type', 'ItemType'),
      'QStaticTextPerformanceHint': (
          '_q_static_text_performance_hint', 'PerformanceHint'),
      'QSurfaceFormatColorSpace': (
          '_q_surface_format_color_space', 'ColorSpace'),
      'QSurfaceFormatFormatOption': (
          '_q_surface_format_format_option', 'FormatOption'),
      'QSurfaceFormatOpenGLContextProfile': (
          '_q_surface_format_open_g_l_context_profile',
          'OpenGLContextProfile'),
      'QSurfaceFormatRenderableType': (
          '_q_surface_format_renderable_type', 'RenderableType'),
      'QSurfaceFormatSwapBehavior': (
          '_q_surface_format_swap_behavior', 'SwapBehavior'),
      'QSurfaceSurfaceClass': ('_q_surface_surface_class', 'SurfaceClass'),
      'QSurfaceSurfaceType': ('_q_surface_surface_type', 'SurfaceType'),
      'QTextBlockFormatLineHeightTypes': (
          '_q_text_block_format_line_height_types', 'LineHeightTypes'),
      'QTextBlockFormatMarkerType': (
          '_q_text_block_format_marker_type', 'MarkerType'),
      'QTextCharFormatFontPropertiesInheritanceBehavior': (
          '_q_text_char_format_font_properties_inheritance_behavior',
          'FontPropertiesInheritanceBehavior'),
      'QTextCharFormatUnderlineStyle': (
          '_q_text_char_format_underline_style', 'UnderlineStyle'),
      'QTextCharFormatVerticalAlignment': (
          '_q_text_char_format_vertical_alignment', 'VerticalAlignment'),
      'QTextCursorMoveMode': ('_q_text_cursor_move_mode', 'MoveMode'),
      'QTextCursorMoveOperation': (
          '_q_text_cursor_move_operation', 'MoveOperation'),
      'QTextCursorSelectionType': (
          '_q_text_cursor_selection_type', 'SelectionType'),
      'QTextDocumentFindFlag': ('_q_text_document_find_flag', 'FindFlag'),
      'QTextDocumentMarkdownFeature': (
          '_q_text_document_markdown_feature', 'MarkdownFeature'),
      'QTextDocumentMetaInformation': (
          '_q_text_document_meta_information', 'MetaInformation'),
      'QTextDocumentResourceType': (
          '_q_text_document_resource_type', 'ResourceType'),
      'QTextDocumentStacks': ('_q_text_document_stacks', 'Stacks'),
      'QTextFormatFormatType': ('_q_text_format_format_type', 'FormatType'),
      'QTextFormatObjectTypes': (
          '_q_text_format_object_types', 'ObjectTypes'),
      'QTextFormatPageBreakFlag': (
          '_q_text_format_page_break_flag', 'PageBreakFlag'),
      'QTextFormatProperty': ('_q_text_format_property', 'Property'),
      'QTextFrameFormatBorderStyle': (
          '_q_text_frame_format_border_style', 'BorderStyle'),
      'QTextFrameFormatPosition': (
          '_q_text_frame_format_position', 'Position'),
      'QTextItemRenderFlag': ('_q_text_item_render_flag', 'RenderFlag'),
      'QTextLayoutCursorMode': ('_q_text_layout_cursor_mode', 'CursorMode'),
      'QTextLayoutGlyphRunRetrievalFlag': (
          '_q_text_layout_glyph_run_retrieval_flag',
          'GlyphRunRetrievalFlag'),
      'QTextLengthType': ('_q_text_length_type', 'Type'),
      'QTextLineCursorPosition': (
          '_q_text_line_cursor_position', 'CursorPosition'),
      'QTextLineEdge': ('_q_text_line_edge', 'Edge'),
      'QTextListFormatStyle': ('_q_text_list_format_style', 'Style'),
      'QTextOptionFlag': ('_q_text_option_flag', 'Flag'),
      'QTextOptionTabType': ('_q_text_option_tab_type', 'TabType'),
      'QTextOptionWrapMode': ('_q_text_option_wrap_mode', 'WrapMode'),
      'QTransformTransformationType': (
          '_q_transform_transformation_type', 'TransformationType'),
      'QValidatorState': ('_q_validator_state', 'State'),
      'QWindowAncestorMode': ('_q_window_ancestor_mode', 'AncestorMode'),
      'QWindowVisibility': ('_q_window_visibility', 'Visibility'),
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtGui import QStandardItemModel'. Python calls
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
