"""
The 'cutienator.QtCore' package provides the cute classes of the part of
Qt named QtCore, under the name PySide6 has for it.

  from cutienator.QtCore import QObject, QSize, Qt

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
    'Qt',
    'QBasicMutex',
    'QBluetoothPermission',
    'QByteArrayView',
    'QCameraPermission',
    'QChar',
    'QCollatorSortKey',
    'QDeadlineTimer',
    'QElapsedTimer',
    'QEvent',
    'QGenericArgument',
    'QIODeviceBase',
    'QKeyCombination',
    'QMargins',
    'QMessageLogContext',
    'QMetaEnum',
    'QPermission',
    'QPoint',
    'QRegularExpressionMatchIterator',
    'QRunnable',
    'QSysInfo',
    'QUntypedPropertyData',
    'QBasicReadWriteLock',
    'QBindingStorage',
    'QBitArray',
    'QByteArray',
    'QGenericReturnArgument',
    'QLine',
    'QMarginsF',
    'QModelRoleDataSpan',
    'QMutex',
    'QPointF',
    'QRecursiveMutex',
    'QSemaphore',
    'QSize',
    'QAbstractNativeEventFilter',
    'QRegularExpressionMatch',
    'QRegularExpression',
    'QDynamicPropertyChangeEvent',
    'QEasingCurve',
    'QLineF',
    'QModelIndex',
    'QReadWriteLock',
    'QRect',
    'QSizeF',
    'QCommandLineOption',
    'QItemSelectionRange',
    'QLibraryInfo',
    'QLockFile',
    'QLoggingCategory',
    'QMimeType',
    'QPersistentModelIndex',
    'QProcessEnvironment',
    'QRectF',
    'QStandardPaths',
    'QTextBoundaryFinder',
    'QTime',
    'QUrl',
    'QUrlQuery',
    'QUuid',
    'QVersionNumber',
    'QWaitCondition',
    'QDate',
    'QDateTime',
    'QLocale',
    'QCalendar',
    'QTimeZone',
    'QSystemSemaphore',
    'QMetaObject',
    'QObject',
    'QIODevice',
    'QDataStream',
    'QJsonArray',
    'QJsonObject',
    'QBasicTimer',
    'QEventLoop',
    'QSocketNotifier',
    'QTextStream',
    'QMetaType',
    'QAbstractEventDispatcher',
    'QJsonValue',
    'QMetaMethod',
    'QThread',
    'QTimerEvent',
    'QVariant',
    'QCollator',
    'QResource',
    'QAbstractAnimation',
    'QBuffer',
    'QFileDevice',
    'QFileSystemWatcher',
    'QLibrary',
    'QMetaProperty',
    'QMimeData',
    'QProcess',
    'QSettings',
    'QSharedMemory',
    'QSignalBlocker',
    'QSignalMapper',
    'QThreadPool',
    'QTimeLine',
    'QTimer',
    'QTranslator',
    'QXmlStreamReader',
    'QAbstractItemModel',
    'QAnimationGroup',
    'QCoreApplication',
    'QFile',
    'QSaveFile',
    'QVariantAnimation',
    'QAbstractListModel',
    'QAbstractTableModel',
    'QCommandLineParser',
    'QDir',
    'QItemSelection',
    'QItemSelectionModel',
    'QParallelAnimationGroup',
    'QPropertyAnimation',
    'QTemporaryFile',
    'QAbstractProxyModel',
    'QDirIterator',
    'QFileInfo',
    'QStorageInfo',
    'QStringListModel',
    'QIdentityProxyModel',
    'QMimeDatabase',
    'QSortFilterProxyModel',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._qt import Qt
  from ._q_basic_mutex import QBasicMutex
  from ._q_bluetooth_permission import QBluetoothPermission
  from ._q_byte_array_view import QByteArrayView
  from ._q_camera_permission import QCameraPermission
  from ._q_char import QChar
  from ._q_collator_sort_key import QCollatorSortKey
  from ._q_deadline_timer import QDeadlineTimer
  from ._q_elapsed_timer import QElapsedTimer
  from ._q_event import QEvent
  from ._q_generic_argument import QGenericArgument
  from ._q_i_o_device_base import QIODeviceBase
  from ._q_key_combination import QKeyCombination
  from ._q_margins import QMargins
  from ._q_message_log_context import QMessageLogContext
  from ._q_meta_enum import QMetaEnum
  from ._q_permission import QPermission
  from ._q_point import QPoint
  from ._q_regular_expression_match_iterator import QRegularExpressionMatchIterator
  from ._q_runnable import QRunnable
  from ._q_sys_info import QSysInfo
  from ._q_untyped_property_data import QUntypedPropertyData
  from ._q_basic_read_write_lock import QBasicReadWriteLock
  from ._q_binding_storage import QBindingStorage
  from ._q_bit_array import QBitArray
  from ._q_byte_array import QByteArray
  from ._q_generic_return_argument import QGenericReturnArgument
  from ._q_line import QLine
  from ._q_margins_f import QMarginsF
  from ._q_model_role_data_span import QModelRoleDataSpan
  from ._q_mutex import QMutex
  from ._q_point_f import QPointF
  from ._q_recursive_mutex import QRecursiveMutex
  from ._q_semaphore import QSemaphore
  from ._q_size import QSize
  from ._q_abstract_native_event_filter import QAbstractNativeEventFilter
  from ._q_regular_expression_match import QRegularExpressionMatch
  from ._q_regular_expression import QRegularExpression
  from ._q_dynamic_property_change_event import QDynamicPropertyChangeEvent
  from ._q_easing_curve import QEasingCurve
  from ._q_line_f import QLineF
  from ._q_model_index import QModelIndex
  from ._q_read_write_lock import QReadWriteLock
  from ._q_rect import QRect
  from ._q_size_f import QSizeF
  from ._q_command_line_option import QCommandLineOption
  from ._q_item_selection_range import QItemSelectionRange
  from ._q_library_info import QLibraryInfo
  from ._q_lock_file import QLockFile
  from ._q_logging_category import QLoggingCategory
  from ._q_mime_type import QMimeType
  from ._q_persistent_model_index import QPersistentModelIndex
  from ._q_process_environment import QProcessEnvironment
  from ._q_rect_f import QRectF
  from ._q_standard_paths import QStandardPaths
  from ._q_text_boundary_finder import QTextBoundaryFinder
  from ._q_time import QTime
  from ._q_url import QUrl
  from ._q_url_query import QUrlQuery
  from ._q_uuid import QUuid
  from ._q_version_number import QVersionNumber
  from ._q_wait_condition import QWaitCondition
  from ._q_date import QDate
  from ._q_date_time import QDateTime
  from ._q_locale import QLocale
  from ._q_calendar import QCalendar
  from ._q_time_zone import QTimeZone
  from ._q_system_semaphore import QSystemSemaphore
  from ._q_meta_object import QMetaObject
  from ._q_object import QObject
  from ._q_i_o_device import QIODevice
  from ._q_data_stream import QDataStream
  from ._q_json_array import QJsonArray
  from ._q_json_object import QJsonObject
  from ._q_basic_timer import QBasicTimer
  from ._q_event_loop import QEventLoop
  from ._q_socket_notifier import QSocketNotifier
  from ._q_text_stream import QTextStream
  from ._q_meta_type import QMetaType
  from ._q_abstract_event_dispatcher import QAbstractEventDispatcher
  from ._q_json_value import QJsonValue
  from ._q_meta_method import QMetaMethod
  from ._q_thread import QThread
  from ._q_timer_event import QTimerEvent
  from ._q_variant import QVariant
  from ._q_collator import QCollator
  from ._q_resource import QResource
  from ._q_abstract_animation import QAbstractAnimation
  from ._q_buffer import QBuffer
  from ._q_file_device import QFileDevice
  from ._q_file_system_watcher import QFileSystemWatcher
  from ._q_library import QLibrary
  from ._q_meta_property import QMetaProperty
  from ._q_mime_data import QMimeData
  from ._q_process import QProcess
  from ._q_settings import QSettings
  from ._q_shared_memory import QSharedMemory
  from ._q_signal_blocker import QSignalBlocker
  from ._q_signal_mapper import QSignalMapper
  from ._q_thread_pool import QThreadPool
  from ._q_time_line import QTimeLine
  from ._q_timer import QTimer
  from ._q_translator import QTranslator
  from ._q_xml_stream_reader import QXmlStreamReader
  from ._q_abstract_item_model import QAbstractItemModel
  from ._q_animation_group import QAnimationGroup
  from ._q_core_application import QCoreApplication
  from ._q_file import QFile
  from ._q_save_file import QSaveFile
  from ._q_variant_animation import QVariantAnimation
  from ._q_abstract_list_model import QAbstractListModel
  from ._q_abstract_table_model import QAbstractTableModel
  from ._q_command_line_parser import QCommandLineParser
  from ._q_dir import QDir
  from ._q_item_selection import QItemSelection
  from ._q_item_selection_model import QItemSelectionModel
  from ._q_parallel_animation_group import QParallelAnimationGroup
  from ._q_property_animation import QPropertyAnimation
  from ._q_temporary_file import QTemporaryFile
  from ._q_abstract_proxy_model import QAbstractProxyModel
  from ._q_dir_iterator import QDirIterator
  from ._q_file_info import QFileInfo
  from ._q_storage_info import QStorageInfo
  from ._q_string_list_model import QStringListModel
  from ._q_identity_proxy_model import QIdentityProxyModel
  from ._q_mime_database import QMimeDatabase
  from ._q_sort_filter_proxy_model import QSortFilterProxyModel
  from ._q_abstract_animation_deletion_policy import (
      DeletionPolicy as QAbstractAnimationDeletionPolicy)
  from ._q_abstract_animation_direction import (
      Direction as QAbstractAnimationDirection)
  from ._q_abstract_animation_state import State as QAbstractAnimationState
  from ._q_abstract_item_model_check_index_option import (
      CheckIndexOption as QAbstractItemModelCheckIndexOption)
  from ._q_abstract_item_model_layout_change_hint import (
      LayoutChangeHint as QAbstractItemModelLayoutChangeHint)
  from ._q_bluetooth_permission_communication_mode import (
      CommunicationMode as QBluetoothPermissionCommunicationMode)
  from ._q_byte_array_base64_decoding_status import (
      Base64DecodingStatus as QByteArrayBase64DecodingStatus)
  from ._q_byte_array_base64_option import (
      Base64Option as QByteArrayBase64Option)
  from ._q_calendar_system import System as QCalendarSystem
  from ._q_char_category import Category as QCharCategory
  from ._q_char_combining_class import CombiningClass as QCharCombiningClass
  from ._q_char_decomposition import Decomposition as QCharDecomposition
  from ._q_char_direction import Direction as QCharDirection
  from ._q_char_joining_type import JoiningType as QCharJoiningType
  from ._q_char_script import Script as QCharScript
  from ._q_char_special_character import (
      SpecialCharacter as QCharSpecialCharacter)
  from ._q_char_unicode_version import UnicodeVersion as QCharUnicodeVersion
  from ._q_command_line_option_flag import Flag as QCommandLineOptionFlag
  from ._q_command_line_parser_message_type import (
      MessageType as QCommandLineParserMessageType)
  from ._q_command_line_parser_options_after_positional_arguments_mode import (
      OptionsAfterPositionalArgumentsMode as
      QCommandLineParserOptionsAfterPositionalArgumentsMode)
  from ._q_command_line_parser_single_dash_word_option_mode import (
      SingleDashWordOptionMode as QCommandLineParserSingleDashWordOptionMode)
  from ._q_data_stream_byte_order import ByteOrder as QDataStreamByteOrder
  from ._q_data_stream_floating_point_precision import (
      FloatingPointPrecision as QDataStreamFloatingPointPrecision)
  from ._q_data_stream_status import Status as QDataStreamStatus
  from ._q_data_stream_version import Version as QDataStreamVersion
  from ._q_date_time_transition_resolution import (
      TransitionResolution as QDateTimeTransitionResolution)
  from ._q_date_time_year_range import YearRange as QDateTimeYearRange
  from ._q_deadline_timer_forever_constant import (
      ForeverConstant as QDeadlineTimerForeverConstant)
  from ._q_dir_filter import Filter as QDirFilter
  from ._q_dir_iterator_iterator_flag import (
      IteratorFlag as QDirIteratorIteratorFlag)
  from ._q_dir_sort_flag import SortFlag as QDirSortFlag
  from ._q_easing_curve_type import Type as QEasingCurveType
  from ._q_elapsed_timer_clock_type import (
      ClockType as QElapsedTimerClockType)
  from ._q_event_loop_process_events_flag import (
      ProcessEventsFlag as QEventLoopProcessEventsFlag)
  from ._q_event_type import Type as QEventType
  from ._q_file_device_file_error import FileError as QFileDeviceFileError
  from ._q_file_device_file_handle_flag import (
      FileHandleFlag as QFileDeviceFileHandleFlag)
  from ._q_file_device_file_time import FileTime as QFileDeviceFileTime
  from ._q_file_device_memory_map_flag import (
      MemoryMapFlag as QFileDeviceMemoryMapFlag)
  from ._q_file_device_permission import Permission as QFileDevicePermission
  from ._q_i_o_device_base_open_mode_flag import (
      OpenModeFlag as QIODeviceBaseOpenModeFlag)
  from ._q_item_selection_model_selection_flag import (
      SelectionFlag as QItemSelectionModelSelectionFlag)
  from ._q_json_value_type import Type as QJsonValueType
  from ._q_library_info_library_path import (
      LibraryPath as QLibraryInfoLibraryPath)
  from ._q_library_load_hint import LoadHint as QLibraryLoadHint
  from ._q_line_f_intersection_type import (
      IntersectionType as QLineFIntersectionType)
  from ._q_locale_country import Country as QLocaleCountry
  from ._q_locale_currency_symbol_format import (
      CurrencySymbolFormat as QLocaleCurrencySymbolFormat)
  from ._q_locale_data_size_format import (
      DataSizeFormat as QLocaleDataSizeFormat)
  from ._q_locale_floating_point_precision_option import (
      FloatingPointPrecisionOption as QLocaleFloatingPointPrecisionOption)
  from ._q_locale_format_type import FormatType as QLocaleFormatType
  from ._q_locale_language import Language as QLocaleLanguage
  from ._q_locale_language_code_type import (
      LanguageCodeType as QLocaleLanguageCodeType)
  from ._q_locale_measurement_system import (
      MeasurementSystem as QLocaleMeasurementSystem)
  from ._q_locale_number_option import NumberOption as QLocaleNumberOption
  from ._q_locale_quotation_style import (
      QuotationStyle as QLocaleQuotationStyle)
  from ._q_locale_script import Script as QLocaleScript
  from ._q_locale_tag_separator import TagSeparator as QLocaleTagSeparator
  from ._q_lock_file_lock_error import LockError as QLockFileLockError
  from ._q_meta_method_access import Access as QMetaMethodAccess
  from ._q_meta_method_attributes import Attributes as QMetaMethodAttributes
  from ._q_meta_method_method_type import MethodType as QMetaMethodMethodType
  from ._q_meta_object_call import Call as QMetaObjectCall
  from ._q_meta_object__connection import Connection as QMetaObjectConnection
  from ._q_meta_type_type import Type as QMetaTypeType
  from ._q_meta_type_type_flag import TypeFlag as QMetaTypeTypeFlag
  from ._q_mime_database_match_mode import (
      MatchMode as QMimeDatabaseMatchMode)
  from ._q_process_environment_initialization import (
      Initialization as QProcessEnvironmentInitialization)
  from ._q_process_exit_status import ExitStatus as QProcessExitStatus
  from ._q_process_input_channel_mode import (
      InputChannelMode as QProcessInputChannelMode)
  from ._q_process_process_channel import (
      ProcessChannel as QProcessProcessChannel)
  from ._q_process_process_channel_mode import (
      ProcessChannelMode as QProcessProcessChannelMode)
  from ._q_process_process_error import ProcessError as QProcessProcessError
  from ._q_process_process_state import ProcessState as QProcessProcessState
  from ._q_process_unix_process_flag import (
      UnixProcessFlag as QProcessUnixProcessFlag)
  from ._q_read_write_lock_recursion_mode import (
      RecursionMode as QReadWriteLockRecursionMode)
  from ._q_regular_expression_match_option import (
      MatchOption as QRegularExpressionMatchOption)
  from ._q_regular_expression_match_type import (
      MatchType as QRegularExpressionMatchType)
  from ._q_regular_expression_pattern_option import (
      PatternOption as QRegularExpressionPatternOption)
  from ._q_regular_expression_wildcard_conversion_option import (
      WildcardConversionOption as QRegularExpressionWildcardConversionOption)
  from ._q_resource_compression import Compression as QResourceCompression
  from ._q_settings_format import Format as QSettingsFormat
  from ._q_settings_scope import Scope as QSettingsScope
  from ._q_settings_status import Status as QSettingsStatus
  from ._q_shared_memory_access_mode import (
      AccessMode as QSharedMemoryAccessMode)
  from ._q_shared_memory_shared_memory_error import (
      SharedMemoryError as QSharedMemorySharedMemoryError)
  from ._q_socket_notifier_type import Type as QSocketNotifierType
  from ._q_sort_filter_proxy_model_data_change_relevance_flag import (
      DataChangeRelevanceFlag as
      QSortFilterProxyModelDataChangeRelevanceFlag)
  from ._q_sort_filter_proxy_model_direction import (
      Direction as QSortFilterProxyModelDirection)
  from ._q_standard_paths_locate_option import (
      LocateOption as QStandardPathsLocateOption)
  from ._q_standard_paths_standard_location import (
      StandardLocation as QStandardPathsStandardLocation)
  from ._q_sys_info_endian import Endian as QSysInfoEndian
  from ._q_sys_info_sizes import Sizes as QSysInfoSizes
  from ._q_system_semaphore_access_mode import (
      AccessMode as QSystemSemaphoreAccessMode)
  from ._q_system_semaphore_system_semaphore_error import (
      SystemSemaphoreError as QSystemSemaphoreSystemSemaphoreError)
  from ._q_text_boundary_finder_boundary_reason import (
      BoundaryReason as QTextBoundaryFinderBoundaryReason)
  from ._q_text_boundary_finder_boundary_type import (
      BoundaryType as QTextBoundaryFinderBoundaryType)
  from ._q_text_stream_field_alignment import (
      FieldAlignment as QTextStreamFieldAlignment)
  from ._q_text_stream_number_flag import NumberFlag as QTextStreamNumberFlag
  from ._q_text_stream_real_number_notation import (
      RealNumberNotation as QTextStreamRealNumberNotation)
  from ._q_text_stream_status import Status as QTextStreamStatus
  from ._q_thread_priority import Priority as QThreadPriority
  from ._q_thread_quality_of_service import (
      QualityOfService as QThreadQualityOfService)
  from ._q_time_line_direction import Direction as QTimeLineDirection
  from ._q_time_line_state import State as QTimeLineState
  from ._q_time_zone_initialization import (
      Initialization as QTimeZoneInitialization)
  from ._q_time_zone_name_type import NameType as QTimeZoneNameType
  from ._q_time_zone_time_type import TimeType as QTimeZoneTimeType
  from ._q_url_ace_processing_option import (
      AceProcessingOption as QUrlAceProcessingOption)
  from ._q_url_component_formatting_option import (
      ComponentFormattingOption as QUrlComponentFormattingOption)
  from ._q_url_parsing_mode import ParsingMode as QUrlParsingMode
  from ._q_url_url_formatting_option import (
      UrlFormattingOption as QUrlUrlFormattingOption)
  from ._q_url_user_input_resolution_option import (
      UserInputResolutionOption as QUrlUserInputResolutionOption)
  from ._q_uuid_string_format import StringFormat as QUuidStringFormat
  from ._q_uuid_variant import Variant as QUuidVariant
  from ._q_uuid_version import Version as QUuidVersion
  from ._q_variant_type import Type as QVariantType
  from ._q_xml_stream_reader_error import Error as QXmlStreamReaderError
  from ._q_xml_stream_reader_read_element_text_behaviour import (
      ReadElementTextBehaviour as QXmlStreamReaderReadElementTextBehaviour)
  from ._q_xml_stream_reader_token_type import (
      TokenType as QXmlStreamReaderTokenType)
  from ._qt_alignment_flag import AlignmentFlag as QtAlignmentFlag
  from ._qt_anchor_point import AnchorPoint as QtAnchorPoint
  from ._qt_application_attribute import (
      ApplicationAttribute as QtApplicationAttribute)
  from ._qt_application_state import ApplicationState as QtApplicationState
  from ._qt_arrow_type import ArrowType as QtArrowType
  from ._qt_aspect_ratio_mode import AspectRatioMode as QtAspectRatioMode
  from ._qt_axis import Axis as QtAxis
  from ._qt_b_g_mode import BGMode as QtBGMode
  from ._qt_brush_style import BrushStyle as QtBrushStyle
  from ._qt_case_sensitivity import CaseSensitivity as QtCaseSensitivity
  from ._qt_check_state import CheckState as QtCheckState
  from ._qt_checksum_type import ChecksumType as QtChecksumType
  from ._qt_clip_operation import ClipOperation as QtClipOperation
  from ._qt_color_scheme import ColorScheme as QtColorScheme
  from ._qt_connection_type import ConnectionType as QtConnectionType
  from ._qt_context_menu_policy import (
      ContextMenuPolicy as QtContextMenuPolicy)
  from ._qt_context_menu_trigger import (
      ContextMenuTrigger as QtContextMenuTrigger)
  from ._qt_contrast_preference import (
      ContrastPreference as QtContrastPreference)
  from ._qt_coordinate_system import CoordinateSystem as QtCoordinateSystem
  from ._qt_corner import Corner as QtCorner
  from ._qt_cursor_move_style import CursorMoveStyle as QtCursorMoveStyle
  from ._qt_cursor_shape import CursorShape as QtCursorShape
  from ._qt_date_format import DateFormat as QtDateFormat
  from ._qt_day_of_week import DayOfWeek as QtDayOfWeek
  from ._qt_dock_widget_area import DockWidgetArea as QtDockWidgetArea
  from ._qt_dock_widget_area_sizes import (
      DockWidgetAreaSizes as QtDockWidgetAreaSizes)
  from ._qt_drop_action import DropAction as QtDropAction
  from ._qt_edge import Edge as QtEdge
  from ._qt_enter_key_type import EnterKeyType as QtEnterKeyType
  from ._qt_event_priority import EventPriority as QtEventPriority
  from ._qt_fill_rule import FillRule as QtFillRule
  from ._qt_find_child_option import FindChildOption as QtFindChildOption
  from ._qt_focus_policy import FocusPolicy as QtFocusPolicy
  from ._qt_focus_reason import FocusReason as QtFocusReason
  from ._qt_gesture_flag import GestureFlag as QtGestureFlag
  from ._qt_gesture_state import GestureState as QtGestureState
  from ._qt_gesture_type import GestureType as QtGestureType
  from ._qt_global_color import GlobalColor as QtGlobalColor
  from ._qt_high_dpi_scale_factor_rounding_policy import (
      HighDpiScaleFactorRoundingPolicy as QtHighDpiScaleFactorRoundingPolicy)
  from ._qt_hit_test_accuracy import HitTestAccuracy as QtHitTestAccuracy
  from ._qt_image_conversion_flag import (
      ImageConversionFlag as QtImageConversionFlag)
  from ._qt_initialization import Initialization as QtInitialization
  from ._qt_input_method_hint import InputMethodHint as QtInputMethodHint
  from ._qt_input_method_query import InputMethodQuery as QtInputMethodQuery
  from ._qt_item_data_role import ItemDataRole as QtItemDataRole
  from ._qt_item_flag import ItemFlag as QtItemFlag
  from ._qt_item_selection_mode import (
      ItemSelectionMode as QtItemSelectionMode)
  from ._qt_item_selection_operation import (
      ItemSelectionOperation as QtItemSelectionOperation)
  from ._qt_key import Key as QtKey
  from ._qt_keyboard_modifier import KeyboardModifier as QtKeyboardModifier
  from ._qt_layout_direction import LayoutDirection as QtLayoutDirection
  from ._qt_mask_mode import MaskMode as QtMaskMode
  from ._qt_match_flag import MatchFlag as QtMatchFlag
  from ._qt_modifier import Modifier as QtModifier
  from ._qt_motion_preference import MotionPreference as QtMotionPreference
  from ._qt_mouse_button import MouseButton as QtMouseButton
  from ._qt_mouse_event_flag import MouseEventFlag as QtMouseEventFlag
  from ._qt_mouse_event_source import MouseEventSource as QtMouseEventSource
  from ._qt_native_gesture_type import (
      NativeGestureType as QtNativeGestureType)
  from ._qt_navigation_mode import NavigationMode as QtNavigationMode
  from ._qt_orientation import Orientation as QtOrientation
  from ._qt_pen_cap_style import PenCapStyle as QtPenCapStyle
  from ._qt_pen_join_style import PenJoinStyle as QtPenJoinStyle
  from ._qt_pen_style import PenStyle as QtPenStyle
  from ._qt_permission_status import PermissionStatus as QtPermissionStatus
  from ._qt_return_by_value_constant import (
      ReturnByValueConstant as QtReturnByValueConstant)
  from ._qt_screen_orientation import (
      ScreenOrientation as QtScreenOrientation)
  from ._qt_scroll_bar_policy import ScrollBarPolicy as QtScrollBarPolicy
  from ._qt_scroll_phase import ScrollPhase as QtScrollPhase
  from ._qt_shortcut_context import ShortcutContext as QtShortcutContext
  from ._qt_size_hint import SizeHint as QtSizeHint
  from ._qt_size_mode import SizeMode as QtSizeMode
  from ._qt_sort_order import SortOrder as QtSortOrder
  from ._qt_split_behavior_flags import (
      SplitBehaviorFlags as QtSplitBehaviorFlags)
  from ._qt_tab_focus_behavior import TabFocusBehavior as QtTabFocusBehavior
  from ._qt_text_elide_mode import TextElideMode as QtTextElideMode
  from ._qt_text_flag import TextFlag as QtTextFlag
  from ._qt_text_format import TextFormat as QtTextFormat
  from ._qt_text_interaction_flag import (
      TextInteractionFlag as QtTextInteractionFlag)
  from ._qt_tile_rule import TileRule as QtTileRule
  from ._qt_time_spec import TimeSpec as QtTimeSpec
  from ._qt_timer_id import TimerId as QtTimerId
  from ._qt_timer_type import TimerType as QtTimerType
  from ._qt_tool_bar_area import ToolBarArea as QtToolBarArea
  from ._qt_tool_bar_area_sizes import ToolBarAreaSizes as QtToolBarAreaSizes
  from ._qt_tool_button_style import ToolButtonStyle as QtToolButtonStyle
  from ._qt_touch_point_state import TouchPointState as QtTouchPointState
  from ._qt_transformation_mode import (
      TransformationMode as QtTransformationMode)
  from ._qt_u_i_effect import UIEffect as QtUIEffect
  from ._qt_white_space_mode import WhiteSpaceMode as QtWhiteSpaceMode
  from ._qt_widget_attribute import WidgetAttribute as QtWidgetAttribute
  from ._qt_window_frame_section import (
      WindowFrameSection as QtWindowFrameSection)
  from ._qt_window_modality import WindowModality as QtWindowModality
  from ._qt_window_state import WindowState as QtWindowState
  from ._qt_window_type import WindowType as QtWindowType
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'Qt': '_qt',
      'QBasicMutex': '_q_basic_mutex',
      'QBluetoothPermission': '_q_bluetooth_permission',
      'QByteArrayView': '_q_byte_array_view',
      'QCameraPermission': '_q_camera_permission',
      'QChar': '_q_char',
      'QCollatorSortKey': '_q_collator_sort_key',
      'QDeadlineTimer': '_q_deadline_timer',
      'QElapsedTimer': '_q_elapsed_timer',
      'QEvent': '_q_event',
      'QGenericArgument': '_q_generic_argument',
      'QIODeviceBase': '_q_i_o_device_base',
      'QKeyCombination': '_q_key_combination',
      'QMargins': '_q_margins',
      'QMessageLogContext': '_q_message_log_context',
      'QMetaEnum': '_q_meta_enum',
      'QPermission': '_q_permission',
      'QPoint': '_q_point',
      'QRegularExpressionMatchIterator': '_q_regular_expression_match_iterator',
      'QRunnable': '_q_runnable',
      'QSysInfo': '_q_sys_info',
      'QUntypedPropertyData': '_q_untyped_property_data',
      'QBasicReadWriteLock': '_q_basic_read_write_lock',
      'QBindingStorage': '_q_binding_storage',
      'QBitArray': '_q_bit_array',
      'QByteArray': '_q_byte_array',
      'QGenericReturnArgument': '_q_generic_return_argument',
      'QLine': '_q_line',
      'QMarginsF': '_q_margins_f',
      'QModelRoleDataSpan': '_q_model_role_data_span',
      'QMutex': '_q_mutex',
      'QPointF': '_q_point_f',
      'QRecursiveMutex': '_q_recursive_mutex',
      'QSemaphore': '_q_semaphore',
      'QSize': '_q_size',
      'QAbstractNativeEventFilter': '_q_abstract_native_event_filter',
      'QRegularExpressionMatch': '_q_regular_expression_match',
      'QRegularExpression': '_q_regular_expression',
      'QDynamicPropertyChangeEvent': '_q_dynamic_property_change_event',
      'QEasingCurve': '_q_easing_curve',
      'QLineF': '_q_line_f',
      'QModelIndex': '_q_model_index',
      'QReadWriteLock': '_q_read_write_lock',
      'QRect': '_q_rect',
      'QSizeF': '_q_size_f',
      'QCommandLineOption': '_q_command_line_option',
      'QItemSelectionRange': '_q_item_selection_range',
      'QLibraryInfo': '_q_library_info',
      'QLockFile': '_q_lock_file',
      'QLoggingCategory': '_q_logging_category',
      'QMimeType': '_q_mime_type',
      'QPersistentModelIndex': '_q_persistent_model_index',
      'QProcessEnvironment': '_q_process_environment',
      'QRectF': '_q_rect_f',
      'QStandardPaths': '_q_standard_paths',
      'QTextBoundaryFinder': '_q_text_boundary_finder',
      'QTime': '_q_time',
      'QUrl': '_q_url',
      'QUrlQuery': '_q_url_query',
      'QUuid': '_q_uuid',
      'QVersionNumber': '_q_version_number',
      'QWaitCondition': '_q_wait_condition',
      'QDate': '_q_date',
      'QDateTime': '_q_date_time',
      'QLocale': '_q_locale',
      'QCalendar': '_q_calendar',
      'QTimeZone': '_q_time_zone',
      'QSystemSemaphore': '_q_system_semaphore',
      'QMetaObject': '_q_meta_object',
      'QObject': '_q_object',
      'QIODevice': '_q_i_o_device',
      'QDataStream': '_q_data_stream',
      'QJsonArray': '_q_json_array',
      'QJsonObject': '_q_json_object',
      'QBasicTimer': '_q_basic_timer',
      'QEventLoop': '_q_event_loop',
      'QSocketNotifier': '_q_socket_notifier',
      'QTextStream': '_q_text_stream',
      'QMetaType': '_q_meta_type',
      'QAbstractEventDispatcher': '_q_abstract_event_dispatcher',
      'QJsonValue': '_q_json_value',
      'QMetaMethod': '_q_meta_method',
      'QThread': '_q_thread',
      'QTimerEvent': '_q_timer_event',
      'QVariant': '_q_variant',
      'QCollator': '_q_collator',
      'QResource': '_q_resource',
      'QAbstractAnimation': '_q_abstract_animation',
      'QBuffer': '_q_buffer',
      'QFileDevice': '_q_file_device',
      'QFileSystemWatcher': '_q_file_system_watcher',
      'QLibrary': '_q_library',
      'QMetaProperty': '_q_meta_property',
      'QMimeData': '_q_mime_data',
      'QProcess': '_q_process',
      'QSettings': '_q_settings',
      'QSharedMemory': '_q_shared_memory',
      'QSignalBlocker': '_q_signal_blocker',
      'QSignalMapper': '_q_signal_mapper',
      'QThreadPool': '_q_thread_pool',
      'QTimeLine': '_q_time_line',
      'QTimer': '_q_timer',
      'QTranslator': '_q_translator',
      'QXmlStreamReader': '_q_xml_stream_reader',
      'QAbstractItemModel': '_q_abstract_item_model',
      'QAnimationGroup': '_q_animation_group',
      'QCoreApplication': '_q_core_application',
      'QFile': '_q_file',
      'QSaveFile': '_q_save_file',
      'QVariantAnimation': '_q_variant_animation',
      'QAbstractListModel': '_q_abstract_list_model',
      'QAbstractTableModel': '_q_abstract_table_model',
      'QCommandLineParser': '_q_command_line_parser',
      'QDir': '_q_dir',
      'QItemSelection': '_q_item_selection',
      'QItemSelectionModel': '_q_item_selection_model',
      'QParallelAnimationGroup': '_q_parallel_animation_group',
      'QPropertyAnimation': '_q_property_animation',
      'QTemporaryFile': '_q_temporary_file',
      'QAbstractProxyModel': '_q_abstract_proxy_model',
      'QDirIterator': '_q_dir_iterator',
      'QFileInfo': '_q_file_info',
      'QStorageInfo': '_q_storage_info',
      'QStringListModel': '_q_string_list_model',
      'QIdentityProxyModel': '_q_identity_proxy_model',
      'QMimeDatabase': '_q_mime_database',
      'QSortFilterProxyModel': '_q_sort_filter_proxy_model',
  }

  #  Where each enum is, and each class Qt writes inside another: the
  #  file, and the name it has there. The package gives each by what
  #  Qt writes it inside and its own name in one, so that the file of
  #  a class can ask for it as it asks for a class. None of them is
  #  in '__all__': a program reaches an enum through its class, as
  #  Qt writes it.
  __inner_files__ = {
      'QAbstractAnimationDeletionPolicy': (
          '_q_abstract_animation_deletion_policy', 'DeletionPolicy'),
      'QAbstractAnimationDirection': (
          '_q_abstract_animation_direction', 'Direction'),
      'QAbstractAnimationState': ('_q_abstract_animation_state', 'State'),
      'QAbstractItemModelCheckIndexOption': (
          '_q_abstract_item_model_check_index_option', 'CheckIndexOption'),
      'QAbstractItemModelLayoutChangeHint': (
          '_q_abstract_item_model_layout_change_hint', 'LayoutChangeHint'),
      'QBluetoothPermissionCommunicationMode': (
          '_q_bluetooth_permission_communication_mode', 'CommunicationMode'),
      'QByteArrayBase64DecodingStatus': (
          '_q_byte_array_base64_decoding_status', 'Base64DecodingStatus'),
      'QByteArrayBase64Option': (
          '_q_byte_array_base64_option', 'Base64Option'),
      'QCalendarSystem': ('_q_calendar_system', 'System'),
      'QCharCategory': ('_q_char_category', 'Category'),
      'QCharCombiningClass': ('_q_char_combining_class', 'CombiningClass'),
      'QCharDecomposition': ('_q_char_decomposition', 'Decomposition'),
      'QCharDirection': ('_q_char_direction', 'Direction'),
      'QCharJoiningType': ('_q_char_joining_type', 'JoiningType'),
      'QCharScript': ('_q_char_script', 'Script'),
      'QCharSpecialCharacter': (
          '_q_char_special_character', 'SpecialCharacter'),
      'QCharUnicodeVersion': ('_q_char_unicode_version', 'UnicodeVersion'),
      'QCommandLineOptionFlag': ('_q_command_line_option_flag', 'Flag'),
      'QCommandLineParserMessageType': (
          '_q_command_line_parser_message_type', 'MessageType'),
      'QCommandLineParserOptionsAfterPositionalArgumentsMode': (
          '_q_command_line_parser_options_after_positional_arguments_mode',
          'OptionsAfterPositionalArgumentsMode'),
      'QCommandLineParserSingleDashWordOptionMode': (
          '_q_command_line_parser_single_dash_word_option_mode',
          'SingleDashWordOptionMode'),
      'QDataStreamByteOrder': ('_q_data_stream_byte_order', 'ByteOrder'),
      'QDataStreamFloatingPointPrecision': (
          '_q_data_stream_floating_point_precision',
          'FloatingPointPrecision'),
      'QDataStreamStatus': ('_q_data_stream_status', 'Status'),
      'QDataStreamVersion': ('_q_data_stream_version', 'Version'),
      'QDateTimeTransitionResolution': (
          '_q_date_time_transition_resolution', 'TransitionResolution'),
      'QDateTimeYearRange': ('_q_date_time_year_range', 'YearRange'),
      'QDeadlineTimerForeverConstant': (
          '_q_deadline_timer_forever_constant', 'ForeverConstant'),
      'QDirFilter': ('_q_dir_filter', 'Filter'),
      'QDirIteratorIteratorFlag': (
          '_q_dir_iterator_iterator_flag', 'IteratorFlag'),
      'QDirSortFlag': ('_q_dir_sort_flag', 'SortFlag'),
      'QEasingCurveType': ('_q_easing_curve_type', 'Type'),
      'QElapsedTimerClockType': ('_q_elapsed_timer_clock_type', 'ClockType'),
      'QEventLoopProcessEventsFlag': (
          '_q_event_loop_process_events_flag', 'ProcessEventsFlag'),
      'QEventType': ('_q_event_type', 'Type'),
      'QFileDeviceFileError': ('_q_file_device_file_error', 'FileError'),
      'QFileDeviceFileHandleFlag': (
          '_q_file_device_file_handle_flag', 'FileHandleFlag'),
      'QFileDeviceFileTime': ('_q_file_device_file_time', 'FileTime'),
      'QFileDeviceMemoryMapFlag': (
          '_q_file_device_memory_map_flag', 'MemoryMapFlag'),
      'QFileDevicePermission': ('_q_file_device_permission', 'Permission'),
      'QIODeviceBaseOpenModeFlag': (
          '_q_i_o_device_base_open_mode_flag', 'OpenModeFlag'),
      'QItemSelectionModelSelectionFlag': (
          '_q_item_selection_model_selection_flag', 'SelectionFlag'),
      'QJsonValueType': ('_q_json_value_type', 'Type'),
      'QLibraryInfoLibraryPath': (
          '_q_library_info_library_path', 'LibraryPath'),
      'QLibraryLoadHint': ('_q_library_load_hint', 'LoadHint'),
      'QLineFIntersectionType': (
          '_q_line_f_intersection_type', 'IntersectionType'),
      'QLocaleCountry': ('_q_locale_country', 'Country'),
      'QLocaleCurrencySymbolFormat': (
          '_q_locale_currency_symbol_format', 'CurrencySymbolFormat'),
      'QLocaleDataSizeFormat': (
          '_q_locale_data_size_format', 'DataSizeFormat'),
      'QLocaleFloatingPointPrecisionOption': (
          '_q_locale_floating_point_precision_option',
          'FloatingPointPrecisionOption'),
      'QLocaleFormatType': ('_q_locale_format_type', 'FormatType'),
      'QLocaleLanguage': ('_q_locale_language', 'Language'),
      'QLocaleLanguageCodeType': (
          '_q_locale_language_code_type', 'LanguageCodeType'),
      'QLocaleMeasurementSystem': (
          '_q_locale_measurement_system', 'MeasurementSystem'),
      'QLocaleNumberOption': ('_q_locale_number_option', 'NumberOption'),
      'QLocaleQuotationStyle': (
          '_q_locale_quotation_style', 'QuotationStyle'),
      'QLocaleScript': ('_q_locale_script', 'Script'),
      'QLocaleTagSeparator': ('_q_locale_tag_separator', 'TagSeparator'),
      'QLockFileLockError': ('_q_lock_file_lock_error', 'LockError'),
      'QMetaMethodAccess': ('_q_meta_method_access', 'Access'),
      'QMetaMethodAttributes': ('_q_meta_method_attributes', 'Attributes'),
      'QMetaMethodMethodType': ('_q_meta_method_method_type', 'MethodType'),
      'QMetaObjectCall': ('_q_meta_object_call', 'Call'),
      'QMetaObjectConnection': ('_q_meta_object__connection', 'Connection'),
      'QMetaTypeType': ('_q_meta_type_type', 'Type'),
      'QMetaTypeTypeFlag': ('_q_meta_type_type_flag', 'TypeFlag'),
      'QMimeDatabaseMatchMode': ('_q_mime_database_match_mode', 'MatchMode'),
      'QProcessEnvironmentInitialization': (
          '_q_process_environment_initialization', 'Initialization'),
      'QProcessExitStatus': ('_q_process_exit_status', 'ExitStatus'),
      'QProcessInputChannelMode': (
          '_q_process_input_channel_mode', 'InputChannelMode'),
      'QProcessProcessChannel': (
          '_q_process_process_channel', 'ProcessChannel'),
      'QProcessProcessChannelMode': (
          '_q_process_process_channel_mode', 'ProcessChannelMode'),
      'QProcessProcessError': ('_q_process_process_error', 'ProcessError'),
      'QProcessProcessState': ('_q_process_process_state', 'ProcessState'),
      'QProcessUnixProcessFlag': (
          '_q_process_unix_process_flag', 'UnixProcessFlag'),
      'QReadWriteLockRecursionMode': (
          '_q_read_write_lock_recursion_mode', 'RecursionMode'),
      'QRegularExpressionMatchOption': (
          '_q_regular_expression_match_option', 'MatchOption'),
      'QRegularExpressionMatchType': (
          '_q_regular_expression_match_type', 'MatchType'),
      'QRegularExpressionPatternOption': (
          '_q_regular_expression_pattern_option', 'PatternOption'),
      'QRegularExpressionWildcardConversionOption': (
          '_q_regular_expression_wildcard_conversion_option',
          'WildcardConversionOption'),
      'QResourceCompression': ('_q_resource_compression', 'Compression'),
      'QSettingsFormat': ('_q_settings_format', 'Format'),
      'QSettingsScope': ('_q_settings_scope', 'Scope'),
      'QSettingsStatus': ('_q_settings_status', 'Status'),
      'QSharedMemoryAccessMode': (
          '_q_shared_memory_access_mode', 'AccessMode'),
      'QSharedMemorySharedMemoryError': (
          '_q_shared_memory_shared_memory_error', 'SharedMemoryError'),
      'QSocketNotifierType': ('_q_socket_notifier_type', 'Type'),
      'QSortFilterProxyModelDataChangeRelevanceFlag': (
          '_q_sort_filter_proxy_model_data_change_relevance_flag',
          'DataChangeRelevanceFlag'),
      'QSortFilterProxyModelDirection': (
          '_q_sort_filter_proxy_model_direction', 'Direction'),
      'QStandardPathsLocateOption': (
          '_q_standard_paths_locate_option', 'LocateOption'),
      'QStandardPathsStandardLocation': (
          '_q_standard_paths_standard_location', 'StandardLocation'),
      'QSysInfoEndian': ('_q_sys_info_endian', 'Endian'),
      'QSysInfoSizes': ('_q_sys_info_sizes', 'Sizes'),
      'QSystemSemaphoreAccessMode': (
          '_q_system_semaphore_access_mode', 'AccessMode'),
      'QSystemSemaphoreSystemSemaphoreError': (
          '_q_system_semaphore_system_semaphore_error',
          'SystemSemaphoreError'),
      'QTextBoundaryFinderBoundaryReason': (
          '_q_text_boundary_finder_boundary_reason', 'BoundaryReason'),
      'QTextBoundaryFinderBoundaryType': (
          '_q_text_boundary_finder_boundary_type', 'BoundaryType'),
      'QTextStreamFieldAlignment': (
          '_q_text_stream_field_alignment', 'FieldAlignment'),
      'QTextStreamNumberFlag': ('_q_text_stream_number_flag', 'NumberFlag'),
      'QTextStreamRealNumberNotation': (
          '_q_text_stream_real_number_notation', 'RealNumberNotation'),
      'QTextStreamStatus': ('_q_text_stream_status', 'Status'),
      'QThreadPriority': ('_q_thread_priority', 'Priority'),
      'QThreadQualityOfService': (
          '_q_thread_quality_of_service', 'QualityOfService'),
      'QTimeLineDirection': ('_q_time_line_direction', 'Direction'),
      'QTimeLineState': ('_q_time_line_state', 'State'),
      'QTimeZoneInitialization': (
          '_q_time_zone_initialization', 'Initialization'),
      'QTimeZoneNameType': ('_q_time_zone_name_type', 'NameType'),
      'QTimeZoneTimeType': ('_q_time_zone_time_type', 'TimeType'),
      'QUrlAceProcessingOption': (
          '_q_url_ace_processing_option', 'AceProcessingOption'),
      'QUrlComponentFormattingOption': (
          '_q_url_component_formatting_option', 'ComponentFormattingOption'),
      'QUrlParsingMode': ('_q_url_parsing_mode', 'ParsingMode'),
      'QUrlUrlFormattingOption': (
          '_q_url_url_formatting_option', 'UrlFormattingOption'),
      'QUrlUserInputResolutionOption': (
          '_q_url_user_input_resolution_option',
          'UserInputResolutionOption'),
      'QUuidStringFormat': ('_q_uuid_string_format', 'StringFormat'),
      'QUuidVariant': ('_q_uuid_variant', 'Variant'),
      'QUuidVersion': ('_q_uuid_version', 'Version'),
      'QVariantType': ('_q_variant_type', 'Type'),
      'QXmlStreamReaderError': ('_q_xml_stream_reader_error', 'Error'),
      'QXmlStreamReaderReadElementTextBehaviour': (
          '_q_xml_stream_reader_read_element_text_behaviour',
          'ReadElementTextBehaviour'),
      'QXmlStreamReaderTokenType': (
          '_q_xml_stream_reader_token_type', 'TokenType'),
      'QtAlignmentFlag': ('_qt_alignment_flag', 'AlignmentFlag'),
      'QtAnchorPoint': ('_qt_anchor_point', 'AnchorPoint'),
      'QtApplicationAttribute': (
          '_qt_application_attribute', 'ApplicationAttribute'),
      'QtApplicationState': ('_qt_application_state', 'ApplicationState'),
      'QtArrowType': ('_qt_arrow_type', 'ArrowType'),
      'QtAspectRatioMode': ('_qt_aspect_ratio_mode', 'AspectRatioMode'),
      'QtAxis': ('_qt_axis', 'Axis'),
      'QtBGMode': ('_qt_b_g_mode', 'BGMode'),
      'QtBrushStyle': ('_qt_brush_style', 'BrushStyle'),
      'QtCaseSensitivity': ('_qt_case_sensitivity', 'CaseSensitivity'),
      'QtCheckState': ('_qt_check_state', 'CheckState'),
      'QtChecksumType': ('_qt_checksum_type', 'ChecksumType'),
      'QtClipOperation': ('_qt_clip_operation', 'ClipOperation'),
      'QtColorScheme': ('_qt_color_scheme', 'ColorScheme'),
      'QtConnectionType': ('_qt_connection_type', 'ConnectionType'),
      'QtContextMenuPolicy': (
          '_qt_context_menu_policy', 'ContextMenuPolicy'),
      'QtContextMenuTrigger': (
          '_qt_context_menu_trigger', 'ContextMenuTrigger'),
      'QtContrastPreference': (
          '_qt_contrast_preference', 'ContrastPreference'),
      'QtCoordinateSystem': ('_qt_coordinate_system', 'CoordinateSystem'),
      'QtCorner': ('_qt_corner', 'Corner'),
      'QtCursorMoveStyle': ('_qt_cursor_move_style', 'CursorMoveStyle'),
      'QtCursorShape': ('_qt_cursor_shape', 'CursorShape'),
      'QtDateFormat': ('_qt_date_format', 'DateFormat'),
      'QtDayOfWeek': ('_qt_day_of_week', 'DayOfWeek'),
      'QtDockWidgetArea': ('_qt_dock_widget_area', 'DockWidgetArea'),
      'QtDockWidgetAreaSizes': (
          '_qt_dock_widget_area_sizes', 'DockWidgetAreaSizes'),
      'QtDropAction': ('_qt_drop_action', 'DropAction'),
      'QtEdge': ('_qt_edge', 'Edge'),
      'QtEnterKeyType': ('_qt_enter_key_type', 'EnterKeyType'),
      'QtEventPriority': ('_qt_event_priority', 'EventPriority'),
      'QtFillRule': ('_qt_fill_rule', 'FillRule'),
      'QtFindChildOption': ('_qt_find_child_option', 'FindChildOption'),
      'QtFocusPolicy': ('_qt_focus_policy', 'FocusPolicy'),
      'QtFocusReason': ('_qt_focus_reason', 'FocusReason'),
      'QtGestureFlag': ('_qt_gesture_flag', 'GestureFlag'),
      'QtGestureState': ('_qt_gesture_state', 'GestureState'),
      'QtGestureType': ('_qt_gesture_type', 'GestureType'),
      'QtGlobalColor': ('_qt_global_color', 'GlobalColor'),
      'QtHighDpiScaleFactorRoundingPolicy': (
          '_qt_high_dpi_scale_factor_rounding_policy',
          'HighDpiScaleFactorRoundingPolicy'),
      'QtHitTestAccuracy': ('_qt_hit_test_accuracy', 'HitTestAccuracy'),
      'QtImageConversionFlag': (
          '_qt_image_conversion_flag', 'ImageConversionFlag'),
      'QtInitialization': ('_qt_initialization', 'Initialization'),
      'QtInputMethodHint': ('_qt_input_method_hint', 'InputMethodHint'),
      'QtInputMethodQuery': ('_qt_input_method_query', 'InputMethodQuery'),
      'QtItemDataRole': ('_qt_item_data_role', 'ItemDataRole'),
      'QtItemFlag': ('_qt_item_flag', 'ItemFlag'),
      'QtItemSelectionMode': (
          '_qt_item_selection_mode', 'ItemSelectionMode'),
      'QtItemSelectionOperation': (
          '_qt_item_selection_operation', 'ItemSelectionOperation'),
      'QtKey': ('_qt_key', 'Key'),
      'QtKeyboardModifier': ('_qt_keyboard_modifier', 'KeyboardModifier'),
      'QtLayoutDirection': ('_qt_layout_direction', 'LayoutDirection'),
      'QtMaskMode': ('_qt_mask_mode', 'MaskMode'),
      'QtMatchFlag': ('_qt_match_flag', 'MatchFlag'),
      'QtModifier': ('_qt_modifier', 'Modifier'),
      'QtMotionPreference': ('_qt_motion_preference', 'MotionPreference'),
      'QtMouseButton': ('_qt_mouse_button', 'MouseButton'),
      'QtMouseEventFlag': ('_qt_mouse_event_flag', 'MouseEventFlag'),
      'QtMouseEventSource': ('_qt_mouse_event_source', 'MouseEventSource'),
      'QtNativeGestureType': (
          '_qt_native_gesture_type', 'NativeGestureType'),
      'QtNavigationMode': ('_qt_navigation_mode', 'NavigationMode'),
      'QtOrientation': ('_qt_orientation', 'Orientation'),
      'QtPenCapStyle': ('_qt_pen_cap_style', 'PenCapStyle'),
      'QtPenJoinStyle': ('_qt_pen_join_style', 'PenJoinStyle'),
      'QtPenStyle': ('_qt_pen_style', 'PenStyle'),
      'QtPermissionStatus': ('_qt_permission_status', 'PermissionStatus'),
      'QtReturnByValueConstant': (
          '_qt_return_by_value_constant', 'ReturnByValueConstant'),
      'QtScreenOrientation': ('_qt_screen_orientation', 'ScreenOrientation'),
      'QtScrollBarPolicy': ('_qt_scroll_bar_policy', 'ScrollBarPolicy'),
      'QtScrollPhase': ('_qt_scroll_phase', 'ScrollPhase'),
      'QtShortcutContext': ('_qt_shortcut_context', 'ShortcutContext'),
      'QtSizeHint': ('_qt_size_hint', 'SizeHint'),
      'QtSizeMode': ('_qt_size_mode', 'SizeMode'),
      'QtSortOrder': ('_qt_sort_order', 'SortOrder'),
      'QtSplitBehaviorFlags': (
          '_qt_split_behavior_flags', 'SplitBehaviorFlags'),
      'QtTabFocusBehavior': ('_qt_tab_focus_behavior', 'TabFocusBehavior'),
      'QtTextElideMode': ('_qt_text_elide_mode', 'TextElideMode'),
      'QtTextFlag': ('_qt_text_flag', 'TextFlag'),
      'QtTextFormat': ('_qt_text_format', 'TextFormat'),
      'QtTextInteractionFlag': (
          '_qt_text_interaction_flag', 'TextInteractionFlag'),
      'QtTileRule': ('_qt_tile_rule', 'TileRule'),
      'QtTimeSpec': ('_qt_time_spec', 'TimeSpec'),
      'QtTimerId': ('_qt_timer_id', 'TimerId'),
      'QtTimerType': ('_qt_timer_type', 'TimerType'),
      'QtToolBarArea': ('_qt_tool_bar_area', 'ToolBarArea'),
      'QtToolBarAreaSizes': ('_qt_tool_bar_area_sizes', 'ToolBarAreaSizes'),
      'QtToolButtonStyle': ('_qt_tool_button_style', 'ToolButtonStyle'),
      'QtTouchPointState': ('_qt_touch_point_state', 'TouchPointState'),
      'QtTransformationMode': (
          '_qt_transformation_mode', 'TransformationMode'),
      'QtUIEffect': ('_qt_u_i_effect', 'UIEffect'),
      'QtWhiteSpaceMode': ('_qt_white_space_mode', 'WhiteSpaceMode'),
      'QtWidgetAttribute': ('_qt_widget_attribute', 'WidgetAttribute'),
      'QtWindowFrameSection': (
          '_qt_window_frame_section', 'WindowFrameSection'),
      'QtWindowModality': ('_qt_window_modality', 'WindowModality'),
      'QtWindowState': ('_qt_window_state', 'WindowState'),
      'QtWindowType': ('_qt_window_type', 'WindowType'),
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtCore import QSortFilterProxyModel'. Python calls
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
