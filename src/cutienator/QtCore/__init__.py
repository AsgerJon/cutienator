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
    'QList',
    'QStringList',
    'QMap',
    'QHash',
    'QAdoptSharedDataTag',
    'QArrayData',
    'QAtomicInt',
    'QBasicMutex',
    'QBindingStatus',
    'QBitRef',
    'QBluetoothPermission',
    'QByteArrayView',
    'QCalendarPermission',
    'QCameraPermission',
    'QCborError',
    'QCborParserError',
    'QChar',
    'QCollatorSortKey',
    'QContactsPermission',
    'QContiguousCacheData',
    'QDeadlineTimer',
    'QElapsedTimer',
    'QEvent',
    'QException',
    'QFactoryInterface',
    'QFlag',
    'QGenericArgument',
    'QHashDummyValue',
    'QHashSeed',
    'QIODeviceBase',
    'QIncompatibleFlag',
    'QInternal',
    'QJsonParseError',
    'QKeyCombination',
    'QLatin1Char',
    'QLocationPermission',
    'QMargins',
    'QMessageLogContext',
    'QMetaClassInfo',
    'QMetaEnum',
    'QMetaMethodArgument',
    'QMetaMethodReturnArgument',
    'QMethodRawArguments',
    'QMicrophonePermission',
    'QModelRoleData',
    'QObjectData',
    'QOperatingSystemVersionBase',
    'QPermission',
    'QPluginMetaData',
    'QPoint',
    'QPropertyBindingPrivatePtr',
    'QPropertyBindingSourceLocation',
    'QPropertyObserverBase',
    'QPropertyProxyBindingData',
    'QRandomGenerator',
    'QRegularExpressionMatchIterator',
    'QRunnable',
    'QScopedPointerPodDeleter',
    'QScopedPropertyUpdateGroup',
    'QSharedData',
    'QSocketDescriptor',
    'QStaticByteArrayMatcherBase',
    'QStaticPlugin',
    'QStringConverterBase',
    'QStringTokenizerBaseBase',
    'QSysInfo',
    'QThreadStorageData',
    'QTypeRevision',
    'QUntypedPropertyData',
    'QVLABaseBase',
    'QXmlStreamEntityDeclaration',
    'QXmlStreamNotationDeclaration',
    'qfloat16',
    'QAbstractConcatenable',
    'QBasicReadWriteLock',
    'QBindingStorage',
    'QBitArray',
    'QByteArray',
    'QGenericReturnArgument',
    'QLine',
    'QMarginsF',
    'QMetaContainer',
    'QModelRoleDataSpan',
    'QMutex',
    'QOperatingSystemVersionUnexported',
    'QPartialOrdering',
    'QPointF',
    'QRandomGenerator64',
    'QRecursiveMutex',
    'QSemaphore',
    'QSize',
    'QUnhandledException',
    'QAbstractNativeEventFilter',
    'QRegularExpressionMatch',
    'QRegularExpression',
    'QByteArrayMatcher',
    'QDynamicPropertyChangeEvent',
    'QEasingCurve',
    'QLineF',
    'QMetaAssociation',
    'QMetaSequence',
    'QModelIndex',
    'QOperatingSystemVersion',
    'QReadWriteLock',
    'QRect',
    'QSemaphoreReleaser',
    'QSizeF',
    'QAssociativeConstIterator',
    'QAssociativeIterator',
    'QCommandLineOption',
    'QDirListing',
    'QItemSelectionRange',
    'QLatin1String',
    'QLatin1StringMatcher',
    'QLibraryInfo',
    'QLockFile',
    'QLoggingCategory',
    'QMimeType',
    'QNativeIpcKey',
    'QPersistentModelIndex',
    'QProcessEnvironment',
    'QPropertyBindingError',
    'QReadLocker',
    'QRectF',
    'QSequentialConstIterator',
    'QSequentialIterator',
    'QStandardPaths',
    'QStringConverter',
    'QStringMatcher',
    'QTemporaryDir',
    'QTextBoundaryFinder',
    'QTime',
    'QUrl',
    'QUrlQuery',
    'QUuid',
    'QVersionNumber',
    'QWaitCondition',
    'QWriteLocker',
    'QXmlStreamAttribute',
    'QXmlStreamAttributes',
    'QXmlStreamEntityResolver',
    'QXmlStreamNamespaceDeclaration',
    'QDate',
    'QDateTime',
    'QLocale',
    'QCalendar',
    'QTimeZone',
    'QMessageLogger',
    'QStringDecoder',
    'QStringEncoder',
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
    'QTextStreamManipulator',
    'QDebug',
    'QMetaType',
    'QAbstractEventDispatcher',
    'QChildEvent',
    'QJsonDocument',
    'QJsonValue',
    'QMetaMethod',
    'QThread',
    'QTimerEvent',
    'QVariant',
    'QCollator',
    'QResource',
    'QAbstractAnimation',
    'QAbstractEventDispatcherV2',
    'QAnimationDriver',
    'QAssociativeIterable',
    'QBuffer',
    'QCborStreamReader',
    'QCborStreamWriter',
    'QChronoTimer',
    'QCryptographicHash',
    'QDebugStateSaver',
    'QEventLoopLocker',
    'QFileDevice',
    'QFileSelector',
    'QFileSystemWatcher',
    'QFutureWatcherBase',
    'QJsonValueConstRef',
    'QLibrary',
    'QMetaProperty',
    'QMimeData',
    'QNoDebug',
    'QObjectCleanupHandler',
    'QProcess',
    'QSequentialIterable',
    'QSettings',
    'QSharedMemory',
    'QSignalBlocker',
    'QSignalMapper',
    'QThreadPool',
    'QTimeLine',
    'QTimer',
    'QTranslator',
    'QUntypedPropertyBinding',
    'QVariantConstPointer',
    'QXmlStreamReader',
    'QAbstractItemModel',
    'QAnimationGroup',
    'QCborArray',
    'QCborMap',
    'QCborValue',
    'QCoreApplication',
    'QFile',
    'QFutureInterfaceBase',
    'QJsonValueRef',
    'QMessageAuthenticationCode',
    'QPauseAnimation',
    'QPluginLoader',
    'QSaveFile',
    'QVariantAnimation',
    'QXmlStreamWriter',
    'QAbstractListModel',
    'QAbstractTableModel',
    'QCborValueConstRef',
    'QCommandLineParser',
    'QConcatenateTablesProxyModel',
    'QDir',
    'QItemSelection',
    'QItemSelectionModel',
    'QParallelAnimationGroup',
    'QPropertyAnimation',
    'QPropertyObserver',
    'QRangeModel',
    'QSequentialAnimationGroup',
    'QTemporaryFile',
    'QAbstractProxyModel',
    'QCborValueRef',
    'QDirIterator',
    'QFileInfo',
    'QPropertyNotifier',
    'QRangeModelImplBase',
    'QStorageInfo',
    'QStringListModel',
    'QUntypedBindable',
    'QIdentityProxyModel',
    'QMimeDatabase',
    'QSortFilterProxyModel',
    'QTransposeProxyModel',
    'QXmlStreamEntityDeclarations',
    'QXmlStreamNotationDeclarations',
    'QByteArrayList',
    'QModelIndexList',
    'QXmlStreamNamespaceDeclarations',
    'QObjectList',
    'QVariantList',
    'QVariantMap',
    'QVariantHash',
    'QFileInfoList',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._qt import Qt
  from ._q_list import QList
  from ._q_string_list import QStringList
  from ._q_map import QMap
  from ._q_hash import QHash
  from ._q_adopt_shared_data_tag import QAdoptSharedDataTag
  from ._q_array_data import QArrayData
  from ._q_atomic_int import QAtomicInt
  from ._q_basic_mutex import QBasicMutex
  from ._q_binding_status import QBindingStatus
  from ._q_bit_ref import QBitRef
  from ._q_bluetooth_permission import QBluetoothPermission
  from ._q_byte_array_view import QByteArrayView
  from ._q_calendar_permission import QCalendarPermission
  from ._q_camera_permission import QCameraPermission
  from ._q_cbor_error import QCborError
  from ._q_cbor_parser_error import QCborParserError
  from ._q_char import QChar
  from ._q_collator_sort_key import QCollatorSortKey
  from ._q_contacts_permission import QContactsPermission
  from ._q_contiguous_cache_data import QContiguousCacheData
  from ._q_deadline_timer import QDeadlineTimer
  from ._q_elapsed_timer import QElapsedTimer
  from ._q_event import QEvent
  from ._q_exception import QException
  from ._q_factory_interface import QFactoryInterface
  from ._q_flag import QFlag
  from ._q_generic_argument import QGenericArgument
  from ._q_hash_dummy_value import QHashDummyValue
  from ._q_hash_seed import QHashSeed
  from ._q_i_o_device_base import QIODeviceBase
  from ._q_incompatible_flag import QIncompatibleFlag
  from ._q_internal import QInternal
  from ._q_json_parse_error import QJsonParseError
  from ._q_key_combination import QKeyCombination
  from ._q_latin1_char import QLatin1Char
  from ._q_location_permission import QLocationPermission
  from ._q_margins import QMargins
  from ._q_message_log_context import QMessageLogContext
  from ._q_meta_class_info import QMetaClassInfo
  from ._q_meta_enum import QMetaEnum
  from ._q_meta_method_argument import QMetaMethodArgument
  from ._q_meta_method_return_argument import QMetaMethodReturnArgument
  from ._q_method_raw_arguments import QMethodRawArguments
  from ._q_microphone_permission import QMicrophonePermission
  from ._q_model_role_data import QModelRoleData
  from ._q_object_data import QObjectData
  from ._q_operating_system_version_base import QOperatingSystemVersionBase
  from ._q_permission import QPermission
  from ._q_plugin_meta_data import QPluginMetaData
  from ._q_point import QPoint
  from ._q_property_binding_private_ptr import QPropertyBindingPrivatePtr
  from ._q_property_binding_source_location import QPropertyBindingSourceLocation
  from ._q_property_observer_base import QPropertyObserverBase
  from ._q_property_proxy_binding_data import QPropertyProxyBindingData
  from ._q_random_generator import QRandomGenerator
  from ._q_regular_expression_match_iterator import QRegularExpressionMatchIterator
  from ._q_runnable import QRunnable
  from ._q_scoped_pointer_pod_deleter import QScopedPointerPodDeleter
  from ._q_scoped_property_update_group import QScopedPropertyUpdateGroup
  from ._q_shared_data import QSharedData
  from ._q_socket_descriptor import QSocketDescriptor
  from ._q_static_byte_array_matcher_base import QStaticByteArrayMatcherBase
  from ._q_static_plugin import QStaticPlugin
  from ._q_string_converter_base import QStringConverterBase
  from ._q_string_tokenizer_base_base import QStringTokenizerBaseBase
  from ._q_sys_info import QSysInfo
  from ._q_thread_storage_data import QThreadStorageData
  from ._q_type_revision import QTypeRevision
  from ._q_untyped_property_data import QUntypedPropertyData
  from ._q_v_l_a_base_base import QVLABaseBase
  from ._q_xml_stream_entity_declaration import QXmlStreamEntityDeclaration
  from ._q_xml_stream_notation_declaration import QXmlStreamNotationDeclaration
  from ._qfloat16 import qfloat16
  from ._q_abstract_concatenable import QAbstractConcatenable
  from ._q_basic_read_write_lock import QBasicReadWriteLock
  from ._q_binding_storage import QBindingStorage
  from ._q_bit_array import QBitArray
  from ._q_byte_array import QByteArray
  from ._q_generic_return_argument import QGenericReturnArgument
  from ._q_line import QLine
  from ._q_margins_f import QMarginsF
  from ._q_meta_container import QMetaContainer
  from ._q_model_role_data_span import QModelRoleDataSpan
  from ._q_mutex import QMutex
  from ._q_operating_system_version_unexported import QOperatingSystemVersionUnexported
  from ._q_partial_ordering import QPartialOrdering
  from ._q_point_f import QPointF
  from ._q_random_generator64 import QRandomGenerator64
  from ._q_recursive_mutex import QRecursiveMutex
  from ._q_semaphore import QSemaphore
  from ._q_size import QSize
  from ._q_unhandled_exception import QUnhandledException
  from ._q_abstract_native_event_filter import QAbstractNativeEventFilter
  from ._q_regular_expression_match import QRegularExpressionMatch
  from ._q_regular_expression import QRegularExpression
  from ._q_byte_array_matcher import QByteArrayMatcher
  from ._q_dynamic_property_change_event import QDynamicPropertyChangeEvent
  from ._q_easing_curve import QEasingCurve
  from ._q_line_f import QLineF
  from ._q_meta_association import QMetaAssociation
  from ._q_meta_sequence import QMetaSequence
  from ._q_model_index import QModelIndex
  from ._q_operating_system_version import QOperatingSystemVersion
  from ._q_read_write_lock import QReadWriteLock
  from ._q_rect import QRect
  from ._q_semaphore_releaser import QSemaphoreReleaser
  from ._q_size_f import QSizeF
  from ._q_associative_const_iterator import QAssociativeConstIterator
  from ._q_associative_iterator import QAssociativeIterator
  from ._q_command_line_option import QCommandLineOption
  from ._q_dir_listing import QDirListing
  from ._q_item_selection_range import QItemSelectionRange
  from ._q_latin1_string import QLatin1String
  from ._q_latin1_string_matcher import QLatin1StringMatcher
  from ._q_library_info import QLibraryInfo
  from ._q_lock_file import QLockFile
  from ._q_logging_category import QLoggingCategory
  from ._q_mime_type import QMimeType
  from ._q_native_ipc_key import QNativeIpcKey
  from ._q_persistent_model_index import QPersistentModelIndex
  from ._q_process_environment import QProcessEnvironment
  from ._q_property_binding_error import QPropertyBindingError
  from ._q_read_locker import QReadLocker
  from ._q_rect_f import QRectF
  from ._q_sequential_const_iterator import QSequentialConstIterator
  from ._q_sequential_iterator import QSequentialIterator
  from ._q_standard_paths import QStandardPaths
  from ._q_string_converter import QStringConverter
  from ._q_string_matcher import QStringMatcher
  from ._q_temporary_dir import QTemporaryDir
  from ._q_text_boundary_finder import QTextBoundaryFinder
  from ._q_time import QTime
  from ._q_url import QUrl
  from ._q_url_query import QUrlQuery
  from ._q_uuid import QUuid
  from ._q_version_number import QVersionNumber
  from ._q_wait_condition import QWaitCondition
  from ._q_write_locker import QWriteLocker
  from ._q_xml_stream_attribute import QXmlStreamAttribute
  from ._q_xml_stream_attributes import QXmlStreamAttributes
  from ._q_xml_stream_entity_resolver import QXmlStreamEntityResolver
  from ._q_xml_stream_namespace_declaration import QXmlStreamNamespaceDeclaration
  from ._q_date import QDate
  from ._q_date_time import QDateTime
  from ._q_locale import QLocale
  from ._q_calendar import QCalendar
  from ._q_time_zone import QTimeZone
  from ._q_message_logger import QMessageLogger
  from ._q_string_decoder import QStringDecoder
  from ._q_string_encoder import QStringEncoder
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
  from ._q_text_stream_manipulator import QTextStreamManipulator
  from ._q_debug import QDebug
  from ._q_meta_type import QMetaType
  from ._q_abstract_event_dispatcher import QAbstractEventDispatcher
  from ._q_child_event import QChildEvent
  from ._q_json_document import QJsonDocument
  from ._q_json_value import QJsonValue
  from ._q_meta_method import QMetaMethod
  from ._q_thread import QThread
  from ._q_timer_event import QTimerEvent
  from ._q_variant import QVariant
  from ._q_collator import QCollator
  from ._q_resource import QResource
  from ._q_abstract_animation import QAbstractAnimation
  from ._q_abstract_event_dispatcher_v2 import QAbstractEventDispatcherV2
  from ._q_animation_driver import QAnimationDriver
  from ._q_associative_iterable import QAssociativeIterable
  from ._q_buffer import QBuffer
  from ._q_cbor_stream_reader import QCborStreamReader
  from ._q_cbor_stream_writer import QCborStreamWriter
  from ._q_chrono_timer import QChronoTimer
  from ._q_cryptographic_hash import QCryptographicHash
  from ._q_debug_state_saver import QDebugStateSaver
  from ._q_event_loop_locker import QEventLoopLocker
  from ._q_file_device import QFileDevice
  from ._q_file_selector import QFileSelector
  from ._q_file_system_watcher import QFileSystemWatcher
  from ._q_future_watcher_base import QFutureWatcherBase
  from ._q_json_value_const_ref import QJsonValueConstRef
  from ._q_library import QLibrary
  from ._q_meta_property import QMetaProperty
  from ._q_mime_data import QMimeData
  from ._q_no_debug import QNoDebug
  from ._q_object_cleanup_handler import QObjectCleanupHandler
  from ._q_process import QProcess
  from ._q_sequential_iterable import QSequentialIterable
  from ._q_settings import QSettings
  from ._q_shared_memory import QSharedMemory
  from ._q_signal_blocker import QSignalBlocker
  from ._q_signal_mapper import QSignalMapper
  from ._q_thread_pool import QThreadPool
  from ._q_time_line import QTimeLine
  from ._q_timer import QTimer
  from ._q_translator import QTranslator
  from ._q_untyped_property_binding import QUntypedPropertyBinding
  from ._q_variant_const_pointer import QVariantConstPointer
  from ._q_xml_stream_reader import QXmlStreamReader
  from ._q_abstract_item_model import QAbstractItemModel
  from ._q_animation_group import QAnimationGroup
  from ._q_cbor_array import QCborArray
  from ._q_cbor_map import QCborMap
  from ._q_cbor_value import QCborValue
  from ._q_core_application import QCoreApplication
  from ._q_file import QFile
  from ._q_future_interface_base import QFutureInterfaceBase
  from ._q_json_value_ref import QJsonValueRef
  from ._q_message_authentication_code import QMessageAuthenticationCode
  from ._q_pause_animation import QPauseAnimation
  from ._q_plugin_loader import QPluginLoader
  from ._q_save_file import QSaveFile
  from ._q_variant_animation import QVariantAnimation
  from ._q_xml_stream_writer import QXmlStreamWriter
  from ._q_abstract_list_model import QAbstractListModel
  from ._q_abstract_table_model import QAbstractTableModel
  from ._q_cbor_value_const_ref import QCborValueConstRef
  from ._q_command_line_parser import QCommandLineParser
  from ._q_concatenate_tables_proxy_model import QConcatenateTablesProxyModel
  from ._q_dir import QDir
  from ._q_item_selection import QItemSelection
  from ._q_item_selection_model import QItemSelectionModel
  from ._q_parallel_animation_group import QParallelAnimationGroup
  from ._q_property_animation import QPropertyAnimation
  from ._q_property_observer import QPropertyObserver
  from ._q_range_model import QRangeModel
  from ._q_sequential_animation_group import QSequentialAnimationGroup
  from ._q_temporary_file import QTemporaryFile
  from ._q_abstract_proxy_model import QAbstractProxyModel
  from ._q_cbor_value_ref import QCborValueRef
  from ._q_dir_iterator import QDirIterator
  from ._q_file_info import QFileInfo
  from ._q_property_notifier import QPropertyNotifier
  from ._q_range_model_impl_base import QRangeModelImplBase
  from ._q_storage_info import QStorageInfo
  from ._q_string_list_model import QStringListModel
  from ._q_untyped_bindable import QUntypedBindable
  from ._q_identity_proxy_model import QIdentityProxyModel
  from ._q_mime_database import QMimeDatabase
  from ._q_sort_filter_proxy_model import QSortFilterProxyModel
  from ._q_transpose_proxy_model import QTransposeProxyModel
  from ._q_xml_stream_entity_declaration import QXmlStreamEntityDeclarations
  from ._q_xml_stream_notation_declaration import QXmlStreamNotationDeclarations
  from ._q_byte_array import QByteArrayList
  from ._q_model_index import QModelIndexList
  from ._q_xml_stream_namespace_declaration import QXmlStreamNamespaceDeclarations
  from ._q_object import QObjectList
  from ._q_variant import QVariantList
  from ._q_variant import QVariantMap
  from ._q_variant import QVariantHash
  from ._q_file_info import QFileInfoList
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'Qt': '_qt',
      'QList': '_q_list',
      'QStringList': '_q_string_list',
      'QMap': '_q_map',
      'QHash': '_q_hash',
      'QAdoptSharedDataTag': '_q_adopt_shared_data_tag',
      'QArrayData': '_q_array_data',
      'QAtomicInt': '_q_atomic_int',
      'QBasicMutex': '_q_basic_mutex',
      'QBindingStatus': '_q_binding_status',
      'QBitRef': '_q_bit_ref',
      'QBluetoothPermission': '_q_bluetooth_permission',
      'QByteArrayView': '_q_byte_array_view',
      'QCalendarPermission': '_q_calendar_permission',
      'QCameraPermission': '_q_camera_permission',
      'QCborError': '_q_cbor_error',
      'QCborParserError': '_q_cbor_parser_error',
      'QChar': '_q_char',
      'QCollatorSortKey': '_q_collator_sort_key',
      'QContactsPermission': '_q_contacts_permission',
      'QContiguousCacheData': '_q_contiguous_cache_data',
      'QDeadlineTimer': '_q_deadline_timer',
      'QElapsedTimer': '_q_elapsed_timer',
      'QEvent': '_q_event',
      'QException': '_q_exception',
      'QFactoryInterface': '_q_factory_interface',
      'QFlag': '_q_flag',
      'QGenericArgument': '_q_generic_argument',
      'QHashDummyValue': '_q_hash_dummy_value',
      'QHashSeed': '_q_hash_seed',
      'QIODeviceBase': '_q_i_o_device_base',
      'QIncompatibleFlag': '_q_incompatible_flag',
      'QInternal': '_q_internal',
      'QJsonParseError': '_q_json_parse_error',
      'QKeyCombination': '_q_key_combination',
      'QLatin1Char': '_q_latin1_char',
      'QLocationPermission': '_q_location_permission',
      'QMargins': '_q_margins',
      'QMessageLogContext': '_q_message_log_context',
      'QMetaClassInfo': '_q_meta_class_info',
      'QMetaEnum': '_q_meta_enum',
      'QMetaMethodArgument': '_q_meta_method_argument',
      'QMetaMethodReturnArgument': '_q_meta_method_return_argument',
      'QMethodRawArguments': '_q_method_raw_arguments',
      'QMicrophonePermission': '_q_microphone_permission',
      'QModelRoleData': '_q_model_role_data',
      'QObjectData': '_q_object_data',
      'QOperatingSystemVersionBase': '_q_operating_system_version_base',
      'QPermission': '_q_permission',
      'QPluginMetaData': '_q_plugin_meta_data',
      'QPoint': '_q_point',
      'QPropertyBindingPrivatePtr': '_q_property_binding_private_ptr',
      'QPropertyBindingSourceLocation': '_q_property_binding_source_location',
      'QPropertyObserverBase': '_q_property_observer_base',
      'QPropertyProxyBindingData': '_q_property_proxy_binding_data',
      'QRandomGenerator': '_q_random_generator',
      'QRegularExpressionMatchIterator': '_q_regular_expression_match_iterator',
      'QRunnable': '_q_runnable',
      'QScopedPointerPodDeleter': '_q_scoped_pointer_pod_deleter',
      'QScopedPropertyUpdateGroup': '_q_scoped_property_update_group',
      'QSharedData': '_q_shared_data',
      'QSocketDescriptor': '_q_socket_descriptor',
      'QStaticByteArrayMatcherBase': '_q_static_byte_array_matcher_base',
      'QStaticPlugin': '_q_static_plugin',
      'QStringConverterBase': '_q_string_converter_base',
      'QStringTokenizerBaseBase': '_q_string_tokenizer_base_base',
      'QSysInfo': '_q_sys_info',
      'QThreadStorageData': '_q_thread_storage_data',
      'QTypeRevision': '_q_type_revision',
      'QUntypedPropertyData': '_q_untyped_property_data',
      'QVLABaseBase': '_q_v_l_a_base_base',
      'QXmlStreamEntityDeclaration': '_q_xml_stream_entity_declaration',
      'QXmlStreamNotationDeclaration': '_q_xml_stream_notation_declaration',
      'qfloat16': '_qfloat16',
      'QAbstractConcatenable': '_q_abstract_concatenable',
      'QBasicReadWriteLock': '_q_basic_read_write_lock',
      'QBindingStorage': '_q_binding_storage',
      'QBitArray': '_q_bit_array',
      'QByteArray': '_q_byte_array',
      'QGenericReturnArgument': '_q_generic_return_argument',
      'QLine': '_q_line',
      'QMarginsF': '_q_margins_f',
      'QMetaContainer': '_q_meta_container',
      'QModelRoleDataSpan': '_q_model_role_data_span',
      'QMutex': '_q_mutex',
      'QOperatingSystemVersionUnexported': '_q_operating_system_version_unexported',
      'QPartialOrdering': '_q_partial_ordering',
      'QPointF': '_q_point_f',
      'QRandomGenerator64': '_q_random_generator64',
      'QRecursiveMutex': '_q_recursive_mutex',
      'QSemaphore': '_q_semaphore',
      'QSize': '_q_size',
      'QUnhandledException': '_q_unhandled_exception',
      'QAbstractNativeEventFilter': '_q_abstract_native_event_filter',
      'QRegularExpressionMatch': '_q_regular_expression_match',
      'QRegularExpression': '_q_regular_expression',
      'QByteArrayMatcher': '_q_byte_array_matcher',
      'QDynamicPropertyChangeEvent': '_q_dynamic_property_change_event',
      'QEasingCurve': '_q_easing_curve',
      'QLineF': '_q_line_f',
      'QMetaAssociation': '_q_meta_association',
      'QMetaSequence': '_q_meta_sequence',
      'QModelIndex': '_q_model_index',
      'QOperatingSystemVersion': '_q_operating_system_version',
      'QReadWriteLock': '_q_read_write_lock',
      'QRect': '_q_rect',
      'QSemaphoreReleaser': '_q_semaphore_releaser',
      'QSizeF': '_q_size_f',
      'QAssociativeConstIterator': '_q_associative_const_iterator',
      'QAssociativeIterator': '_q_associative_iterator',
      'QCommandLineOption': '_q_command_line_option',
      'QDirListing': '_q_dir_listing',
      'QItemSelectionRange': '_q_item_selection_range',
      'QLatin1String': '_q_latin1_string',
      'QLatin1StringMatcher': '_q_latin1_string_matcher',
      'QLibraryInfo': '_q_library_info',
      'QLockFile': '_q_lock_file',
      'QLoggingCategory': '_q_logging_category',
      'QMimeType': '_q_mime_type',
      'QNativeIpcKey': '_q_native_ipc_key',
      'QPersistentModelIndex': '_q_persistent_model_index',
      'QProcessEnvironment': '_q_process_environment',
      'QPropertyBindingError': '_q_property_binding_error',
      'QReadLocker': '_q_read_locker',
      'QRectF': '_q_rect_f',
      'QSequentialConstIterator': '_q_sequential_const_iterator',
      'QSequentialIterator': '_q_sequential_iterator',
      'QStandardPaths': '_q_standard_paths',
      'QStringConverter': '_q_string_converter',
      'QStringMatcher': '_q_string_matcher',
      'QTemporaryDir': '_q_temporary_dir',
      'QTextBoundaryFinder': '_q_text_boundary_finder',
      'QTime': '_q_time',
      'QUrl': '_q_url',
      'QUrlQuery': '_q_url_query',
      'QUuid': '_q_uuid',
      'QVersionNumber': '_q_version_number',
      'QWaitCondition': '_q_wait_condition',
      'QWriteLocker': '_q_write_locker',
      'QXmlStreamAttribute': '_q_xml_stream_attribute',
      'QXmlStreamAttributes': '_q_xml_stream_attributes',
      'QXmlStreamEntityResolver': '_q_xml_stream_entity_resolver',
      'QXmlStreamNamespaceDeclaration': '_q_xml_stream_namespace_declaration',
      'QDate': '_q_date',
      'QDateTime': '_q_date_time',
      'QLocale': '_q_locale',
      'QCalendar': '_q_calendar',
      'QTimeZone': '_q_time_zone',
      'QMessageLogger': '_q_message_logger',
      'QStringDecoder': '_q_string_decoder',
      'QStringEncoder': '_q_string_encoder',
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
      'QTextStreamManipulator': '_q_text_stream_manipulator',
      'QDebug': '_q_debug',
      'QMetaType': '_q_meta_type',
      'QAbstractEventDispatcher': '_q_abstract_event_dispatcher',
      'QChildEvent': '_q_child_event',
      'QJsonDocument': '_q_json_document',
      'QJsonValue': '_q_json_value',
      'QMetaMethod': '_q_meta_method',
      'QThread': '_q_thread',
      'QTimerEvent': '_q_timer_event',
      'QVariant': '_q_variant',
      'QCollator': '_q_collator',
      'QResource': '_q_resource',
      'QAbstractAnimation': '_q_abstract_animation',
      'QAbstractEventDispatcherV2': '_q_abstract_event_dispatcher_v2',
      'QAnimationDriver': '_q_animation_driver',
      'QAssociativeIterable': '_q_associative_iterable',
      'QBuffer': '_q_buffer',
      'QCborStreamReader': '_q_cbor_stream_reader',
      'QCborStreamWriter': '_q_cbor_stream_writer',
      'QChronoTimer': '_q_chrono_timer',
      'QCryptographicHash': '_q_cryptographic_hash',
      'QDebugStateSaver': '_q_debug_state_saver',
      'QEventLoopLocker': '_q_event_loop_locker',
      'QFileDevice': '_q_file_device',
      'QFileSelector': '_q_file_selector',
      'QFileSystemWatcher': '_q_file_system_watcher',
      'QFutureWatcherBase': '_q_future_watcher_base',
      'QJsonValueConstRef': '_q_json_value_const_ref',
      'QLibrary': '_q_library',
      'QMetaProperty': '_q_meta_property',
      'QMimeData': '_q_mime_data',
      'QNoDebug': '_q_no_debug',
      'QObjectCleanupHandler': '_q_object_cleanup_handler',
      'QProcess': '_q_process',
      'QSequentialIterable': '_q_sequential_iterable',
      'QSettings': '_q_settings',
      'QSharedMemory': '_q_shared_memory',
      'QSignalBlocker': '_q_signal_blocker',
      'QSignalMapper': '_q_signal_mapper',
      'QThreadPool': '_q_thread_pool',
      'QTimeLine': '_q_time_line',
      'QTimer': '_q_timer',
      'QTranslator': '_q_translator',
      'QUntypedPropertyBinding': '_q_untyped_property_binding',
      'QVariantConstPointer': '_q_variant_const_pointer',
      'QXmlStreamReader': '_q_xml_stream_reader',
      'QAbstractItemModel': '_q_abstract_item_model',
      'QAnimationGroup': '_q_animation_group',
      'QCborArray': '_q_cbor_array',
      'QCborMap': '_q_cbor_map',
      'QCborValue': '_q_cbor_value',
      'QCoreApplication': '_q_core_application',
      'QFile': '_q_file',
      'QFutureInterfaceBase': '_q_future_interface_base',
      'QJsonValueRef': '_q_json_value_ref',
      'QMessageAuthenticationCode': '_q_message_authentication_code',
      'QPauseAnimation': '_q_pause_animation',
      'QPluginLoader': '_q_plugin_loader',
      'QSaveFile': '_q_save_file',
      'QVariantAnimation': '_q_variant_animation',
      'QXmlStreamWriter': '_q_xml_stream_writer',
      'QAbstractListModel': '_q_abstract_list_model',
      'QAbstractTableModel': '_q_abstract_table_model',
      'QCborValueConstRef': '_q_cbor_value_const_ref',
      'QCommandLineParser': '_q_command_line_parser',
      'QConcatenateTablesProxyModel': '_q_concatenate_tables_proxy_model',
      'QDir': '_q_dir',
      'QItemSelection': '_q_item_selection',
      'QItemSelectionModel': '_q_item_selection_model',
      'QParallelAnimationGroup': '_q_parallel_animation_group',
      'QPropertyAnimation': '_q_property_animation',
      'QPropertyObserver': '_q_property_observer',
      'QRangeModel': '_q_range_model',
      'QSequentialAnimationGroup': '_q_sequential_animation_group',
      'QTemporaryFile': '_q_temporary_file',
      'QAbstractProxyModel': '_q_abstract_proxy_model',
      'QCborValueRef': '_q_cbor_value_ref',
      'QDirIterator': '_q_dir_iterator',
      'QFileInfo': '_q_file_info',
      'QPropertyNotifier': '_q_property_notifier',
      'QRangeModelImplBase': '_q_range_model_impl_base',
      'QStorageInfo': '_q_storage_info',
      'QStringListModel': '_q_string_list_model',
      'QUntypedBindable': '_q_untyped_bindable',
      'QIdentityProxyModel': '_q_identity_proxy_model',
      'QMimeDatabase': '_q_mime_database',
      'QSortFilterProxyModel': '_q_sort_filter_proxy_model',
      'QTransposeProxyModel': '_q_transpose_proxy_model',
      'QXmlStreamEntityDeclarations': '_q_xml_stream_entity_declaration',
      'QXmlStreamNotationDeclarations': '_q_xml_stream_notation_declaration',
      'QByteArrayList': '_q_byte_array',
      'QModelIndexList': '_q_model_index',
      'QXmlStreamNamespaceDeclarations': '_q_xml_stream_namespace_declaration',
      'QObjectList': '_q_object',
      'QVariantList': '_q_variant',
      'QVariantMap': '_q_variant',
      'QVariantHash': '_q_variant',
      'QFileInfoList': '_q_file_info',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtCore import QFileInfoList'. Python calls
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
