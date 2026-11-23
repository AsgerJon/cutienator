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
    'QBindingStatus',
    'QByteArrayView',
    'QCameraPermission',
    'QCborParserError',
    'QChar',
    'QContiguousCacheData',
    'QDeadlineTimer',
    'QElapsedTimer',
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
    'QMargins',
    'QMessageLogContext',
    'QMetaClassInfo',
    'QMetaMethodArgument',
    'QMetaMethodReturnArgument',
    'QMethodRawArguments',
    'QMicrophonePermission',
    'QModelRoleData',
    'QObjectData',
    'QOperatingSystemVersionBase',
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
    'QBasicMutex',
    'QBindingStorage',
    'QBitArray',
    'QByteArray',
    'QGenericReturnArgument',
    'QLine',
    'QMarginsF',
    'QMetaContainer',
    'QModelRoleDataSpan',
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
    'QBasicReadWriteLock',
    'QBitRef',
    'QByteArrayMatcher',
    'QCollatorSortKey',
    'QLineF',
    'QMetaAssociation',
    'QMetaSequence',
    'QMutex',
    'QOperatingSystemVersion',
    'QRect',
    'QSemaphoreReleaser',
    'QSizeF',
    'QAssociativeConstIterator',
    'QAssociativeIterator',
    'QCommandLineOption',
    'QLatin1String',
    'QLatin1StringMatcher',
    'QLockFile',
    'QLoggingCategory',
    'QProcessEnvironment',
    'QPropertyBindingError',
    'QReadWriteLock',
    'QRectF',
    'QSequentialConstIterator',
    'QSequentialIterator',
    'QStringConverter',
    'QStringMatcher',
    'QTemporaryDir',
    'QTextBoundaryFinder',
    'QTime',
    'QUrl',
    'QUrlQuery',
    'QUuid',
    'QVersionNumber',
    'QXmlStreamAttribute',
    'QXmlStreamAttributes',
    'QXmlStreamEntityResolver',
    'QXmlStreamNamespaceDeclaration',
    'QMetaObject',
    'QObject',
    'QDataStream',
    'QDateTime',
    'QLocale',
    'QModelIndex',
    'QEvent',
    'QIODevice',
    'QJsonArray',
    'QJsonObject',
    'QCborStreamWriter',
    'QDebug',
    'QMetaType',
    'QPersistentModelIndex',
    'QVariant',
    'QTimeZone',
    'QBasicTimer',
    'QCborStreamReader',
    'QCborValue',
    'QCollator',
    'QDate',
    'QEventLoop',
    'QMetaMethod',
    'QMetaProperty',
    'QMimeData',
    'QSocketNotifier',
    'QTextStream',
    'QThread',
    'QAbstractEventDispatcher',
    'QAbstractItemModel',
    'QCalendar',
    'QCborArray',
    'QCborError',
    'QCborMap',
    'QCborValueConstRef',
    'QChildEvent',
    'QEasingCurve',
    'QJsonDocument',
    'QJsonValue',
    'QTextStreamManipulator',
    'QTimerEvent',
    'QMessageLogger',
    'QReadLocker',
    'QStringDecoder',
    'QStringEncoder',
    'QWaitCondition',
    'QWriteLocker',
    'QAbstractAnimation',
    'QAbstractAnimationTimer',
    'QAbstractEventDispatcherV2',
    'QAbstractListModel',
    'QAbstractTableModel',
    'QAdoptedThread',
    'QAssociativeIterable',
    'QBluetoothPermission',
    'QBuffer',
    'QCalendarPermission',
    'QCborValueRef',
    'QChronoTimer',
    'QConcatenateTablesProxyModel',
    'QContactsPermission',
    'QCryptographicHash',
    'QDaemonThread',
    'QDebugStateSaver',
    'QDirListing',
    'QDynamicPropertyChangeEvent',
    'QEventLoopLocker',
    'QFileDevice',
    'QFileSelector',
    'QFileSystemWatcher',
    'QFileSystemWatcherEngine',
    'QFutureWatcherBase',
    'QIOOperation',
    'QItemSelectionRange',
    'QJsonValueConstRef',
    'QLibrary',
    'QLibraryInfo',
    'QLocationPermission',
    'QMetaEnum',
    'QMimeType',
    'QNativeIpcKey',
    'QNoDebug',
    'QNonContiguousByteDevice',
    'QObjectCleanupHandler',
    'QPermission',
    'QProcess',
    'QRandomAccessAsyncFile',
    'QResource',
    'QSequentialIterable',
    'QSettings',
    'QSignalBlocker',
    'QSignalMapper',
    'QSingleShotTimer',
    'QStandardPaths',
    'QThreadPool',
    'QTimeLine',
    'QTimer',
    'QTranslator',
    'QUntypedPropertyBinding',
    'QVariantConstPointer',
    'QXmlStreamReader',
    'QAnimationDriver',
    'QAnimationTimer',
    'QByteDeviceWrappingIoDevice',
    'QFile',
    'QFutureInterfaceBase',
    'QIOReadWriteOperationBase',
    'QItemSelection',
    'QItemSelectionModel',
    'QJsonValueRef',
    'QMessageAuthenticationCode',
    'QNonContiguousByteDeviceByteArrayImpl',
    'QNonContiguousByteDeviceIoDeviceImpl',
    'QNonContiguousByteDeviceRingBufferImpl',
    'QPauseAnimation',
    'QPermissionPlugin',
    'QPluginLoader',
    'QPollingFileSystemWatcherEngine',
    'QPropertyObserver',
    'QRangeModel',
    'QRangeModelImplBase',
    'QSaveFile',
    'QSharedMemory',
    'QStringListModel',
    'QSystemSemaphore',
    'QVariantAnimation',
    'QXmlStreamWriter',
    'QAbstractProxyModel',
    'QAnimationGroup',
    'QDir',
    'QIOReadOperation',
    'QIOVectoredReadOperation',
    'QIOVectoredWriteOperation',
    'QIOWriteOperation',
    'QPropertyAnimation',
    'QPropertyNotifier',
    'QTemporaryFile',
    'QUnifiedTimer',
    'QUntypedBindable',
    'QCoreApplication',
    'QDefaultAnimationDriver',
    'QDirIterator',
    'QIdentityProxyModel',
    'QParallelAnimationGroup',
    'QSequentialAnimationGroup',
    'QSortFilterProxyModel',
    'QStorageInfo',
    'QTransposeProxyModel',
    'QCommandLineParser',
    'QFileInfo',
    'QMimeDatabase',
    'QXmlStreamEntityDeclarations',
    'QXmlStreamNotationDeclarations',
    'QByteArrayList',
    'QXmlStreamNamespaceDeclarations',
    'QObjectList',
    'QModelIndexList',
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
  from ._q_binding_status import QBindingStatus
  from ._q_byte_array_view import QByteArrayView
  from ._q_camera_permission import QCameraPermission
  from ._q_cbor_parser_error import QCborParserError
  from ._q_char import QChar
  from ._q_contiguous_cache_data import QContiguousCacheData
  from ._q_deadline_timer import QDeadlineTimer
  from ._q_elapsed_timer import QElapsedTimer
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
  from ._q_margins import QMargins
  from ._q_message_log_context import QMessageLogContext
  from ._q_meta_class_info import QMetaClassInfo
  from ._q_meta_method_argument import QMetaMethodArgument
  from ._q_meta_method_return_argument import QMetaMethodReturnArgument
  from ._q_method_raw_arguments import QMethodRawArguments
  from ._q_microphone_permission import QMicrophonePermission
  from ._q_model_role_data import QModelRoleData
  from ._q_object_data import QObjectData
  from ._q_operating_system_version_base import QOperatingSystemVersionBase
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
  from ._q_basic_mutex import QBasicMutex
  from ._q_binding_storage import QBindingStorage
  from ._q_bit_array import QBitArray
  from ._q_byte_array import QByteArray
  from ._q_generic_return_argument import QGenericReturnArgument
  from ._q_line import QLine
  from ._q_margins_f import QMarginsF
  from ._q_meta_container import QMetaContainer
  from ._q_model_role_data_span import QModelRoleDataSpan
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
  from ._q_basic_read_write_lock import QBasicReadWriteLock
  from ._q_bit_ref import QBitRef
  from ._q_byte_array_matcher import QByteArrayMatcher
  from ._q_collator_sort_key import QCollatorSortKey
  from ._q_line_f import QLineF
  from ._q_meta_association import QMetaAssociation
  from ._q_meta_sequence import QMetaSequence
  from ._q_mutex import QMutex
  from ._q_operating_system_version import QOperatingSystemVersion
  from ._q_rect import QRect
  from ._q_semaphore_releaser import QSemaphoreReleaser
  from ._q_size_f import QSizeF
  from ._q_associative_const_iterator import QAssociativeConstIterator
  from ._q_associative_iterator import QAssociativeIterator
  from ._q_command_line_option import QCommandLineOption
  from ._q_latin1_string import QLatin1String
  from ._q_latin1_string_matcher import QLatin1StringMatcher
  from ._q_lock_file import QLockFile
  from ._q_logging_category import QLoggingCategory
  from ._q_process_environment import QProcessEnvironment
  from ._q_property_binding_error import QPropertyBindingError
  from ._q_read_write_lock import QReadWriteLock
  from ._q_rect_f import QRectF
  from ._q_sequential_const_iterator import QSequentialConstIterator
  from ._q_sequential_iterator import QSequentialIterator
  from ._q_string_converter import QStringConverter
  from ._q_string_matcher import QStringMatcher
  from ._q_temporary_dir import QTemporaryDir
  from ._q_text_boundary_finder import QTextBoundaryFinder
  from ._q_time import QTime
  from ._q_url import QUrl
  from ._q_url_query import QUrlQuery
  from ._q_uuid import QUuid
  from ._q_version_number import QVersionNumber
  from ._q_xml_stream_attribute import QXmlStreamAttribute
  from ._q_xml_stream_attributes import QXmlStreamAttributes
  from ._q_xml_stream_entity_resolver import QXmlStreamEntityResolver
  from ._q_xml_stream_namespace_declaration import QXmlStreamNamespaceDeclaration
  from ._q_meta_object import QMetaObject
  from ._q_object import QObject
  from ._q_data_stream import QDataStream
  from ._q_date_time import QDateTime
  from ._q_locale import QLocale
  from ._q_model_index import QModelIndex
  from ._q_event import QEvent
  from ._q_i_o_device import QIODevice
  from ._q_json_array import QJsonArray
  from ._q_json_object import QJsonObject
  from ._q_cbor_stream_writer import QCborStreamWriter
  from ._q_debug import QDebug
  from ._q_meta_type import QMetaType
  from ._q_persistent_model_index import QPersistentModelIndex
  from ._q_variant import QVariant
  from ._q_time_zone import QTimeZone
  from ._q_basic_timer import QBasicTimer
  from ._q_cbor_stream_reader import QCborStreamReader
  from ._q_cbor_value import QCborValue
  from ._q_collator import QCollator
  from ._q_date import QDate
  from ._q_event_loop import QEventLoop
  from ._q_meta_method import QMetaMethod
  from ._q_meta_property import QMetaProperty
  from ._q_mime_data import QMimeData
  from ._q_socket_notifier import QSocketNotifier
  from ._q_text_stream import QTextStream
  from ._q_thread import QThread
  from ._q_abstract_event_dispatcher import QAbstractEventDispatcher
  from ._q_abstract_item_model import QAbstractItemModel
  from ._q_calendar import QCalendar
  from ._q_cbor_array import QCborArray
  from ._q_cbor_error import QCborError
  from ._q_cbor_map import QCborMap
  from ._q_cbor_value_const_ref import QCborValueConstRef
  from ._q_child_event import QChildEvent
  from ._q_easing_curve import QEasingCurve
  from ._q_json_document import QJsonDocument
  from ._q_json_value import QJsonValue
  from ._q_text_stream_manipulator import QTextStreamManipulator
  from ._q_timer_event import QTimerEvent
  from ._q_message_logger import QMessageLogger
  from ._q_read_locker import QReadLocker
  from ._q_string_decoder import QStringDecoder
  from ._q_string_encoder import QStringEncoder
  from ._q_wait_condition import QWaitCondition
  from ._q_write_locker import QWriteLocker
  from ._q_abstract_animation import QAbstractAnimation
  from ._q_abstract_animation_timer import QAbstractAnimationTimer
  from ._q_abstract_event_dispatcher_v2 import QAbstractEventDispatcherV2
  from ._q_abstract_list_model import QAbstractListModel
  from ._q_abstract_table_model import QAbstractTableModel
  from ._q_adopted_thread import QAdoptedThread
  from ._q_associative_iterable import QAssociativeIterable
  from ._q_bluetooth_permission import QBluetoothPermission
  from ._q_buffer import QBuffer
  from ._q_calendar_permission import QCalendarPermission
  from ._q_cbor_value_ref import QCborValueRef
  from ._q_chrono_timer import QChronoTimer
  from ._q_concatenate_tables_proxy_model import QConcatenateTablesProxyModel
  from ._q_contacts_permission import QContactsPermission
  from ._q_cryptographic_hash import QCryptographicHash
  from ._q_daemon_thread import QDaemonThread
  from ._q_debug_state_saver import QDebugStateSaver
  from ._q_dir_listing import QDirListing
  from ._q_dynamic_property_change_event import QDynamicPropertyChangeEvent
  from ._q_event_loop_locker import QEventLoopLocker
  from ._q_file_device import QFileDevice
  from ._q_file_selector import QFileSelector
  from ._q_file_system_watcher import QFileSystemWatcher
  from ._q_file_system_watcher_engine import QFileSystemWatcherEngine
  from ._q_future_watcher_base import QFutureWatcherBase
  from ._q_i_o_operation import QIOOperation
  from ._q_item_selection_range import QItemSelectionRange
  from ._q_json_value_const_ref import QJsonValueConstRef
  from ._q_library import QLibrary
  from ._q_library_info import QLibraryInfo
  from ._q_location_permission import QLocationPermission
  from ._q_meta_enum import QMetaEnum
  from ._q_mime_type import QMimeType
  from ._q_native_ipc_key import QNativeIpcKey
  from ._q_no_debug import QNoDebug
  from ._q_non_contiguous_byte_device import QNonContiguousByteDevice
  from ._q_object_cleanup_handler import QObjectCleanupHandler
  from ._q_permission import QPermission
  from ._q_process import QProcess
  from ._q_random_access_async_file import QRandomAccessAsyncFile
  from ._q_resource import QResource
  from ._q_sequential_iterable import QSequentialIterable
  from ._q_settings import QSettings
  from ._q_signal_blocker import QSignalBlocker
  from ._q_signal_mapper import QSignalMapper
  from ._q_single_shot_timer import QSingleShotTimer
  from ._q_standard_paths import QStandardPaths
  from ._q_thread_pool import QThreadPool
  from ._q_time_line import QTimeLine
  from ._q_timer import QTimer
  from ._q_translator import QTranslator
  from ._q_untyped_property_binding import QUntypedPropertyBinding
  from ._q_variant_const_pointer import QVariantConstPointer
  from ._q_xml_stream_reader import QXmlStreamReader
  from ._q_animation_driver import QAnimationDriver
  from ._q_animation_timer import QAnimationTimer
  from ._q_byte_device_wrapping_io_device import QByteDeviceWrappingIoDevice
  from ._q_file import QFile
  from ._q_future_interface_base import QFutureInterfaceBase
  from ._q_i_o_read_write_operation_base import QIOReadWriteOperationBase
  from ._q_item_selection import QItemSelection
  from ._q_item_selection_model import QItemSelectionModel
  from ._q_json_value_ref import QJsonValueRef
  from ._q_message_authentication_code import QMessageAuthenticationCode
  from ._q_non_contiguous_byte_device_byte_array_impl import QNonContiguousByteDeviceByteArrayImpl
  from ._q_non_contiguous_byte_device_io_device_impl import QNonContiguousByteDeviceIoDeviceImpl
  from ._q_non_contiguous_byte_device_ring_buffer_impl import QNonContiguousByteDeviceRingBufferImpl
  from ._q_pause_animation import QPauseAnimation
  from ._q_permission_plugin import QPermissionPlugin
  from ._q_plugin_loader import QPluginLoader
  from ._q_polling_file_system_watcher_engine import QPollingFileSystemWatcherEngine
  from ._q_property_observer import QPropertyObserver
  from ._q_range_model import QRangeModel
  from ._q_range_model_impl_base import QRangeModelImplBase
  from ._q_save_file import QSaveFile
  from ._q_shared_memory import QSharedMemory
  from ._q_string_list_model import QStringListModel
  from ._q_system_semaphore import QSystemSemaphore
  from ._q_variant_animation import QVariantAnimation
  from ._q_xml_stream_writer import QXmlStreamWriter
  from ._q_abstract_proxy_model import QAbstractProxyModel
  from ._q_animation_group import QAnimationGroup
  from ._q_dir import QDir
  from ._q_i_o_read_operation import QIOReadOperation
  from ._q_i_o_vectored_read_operation import QIOVectoredReadOperation
  from ._q_i_o_vectored_write_operation import QIOVectoredWriteOperation
  from ._q_i_o_write_operation import QIOWriteOperation
  from ._q_property_animation import QPropertyAnimation
  from ._q_property_notifier import QPropertyNotifier
  from ._q_temporary_file import QTemporaryFile
  from ._q_unified_timer import QUnifiedTimer
  from ._q_untyped_bindable import QUntypedBindable
  from ._q_core_application import QCoreApplication
  from ._q_default_animation_driver import QDefaultAnimationDriver
  from ._q_dir_iterator import QDirIterator
  from ._q_identity_proxy_model import QIdentityProxyModel
  from ._q_parallel_animation_group import QParallelAnimationGroup
  from ._q_sequential_animation_group import QSequentialAnimationGroup
  from ._q_sort_filter_proxy_model import QSortFilterProxyModel
  from ._q_storage_info import QStorageInfo
  from ._q_transpose_proxy_model import QTransposeProxyModel
  from ._q_command_line_parser import QCommandLineParser
  from ._q_file_info import QFileInfo
  from ._q_mime_database import QMimeDatabase
  from ._q_xml_stream_entity_declaration import QXmlStreamEntityDeclarations
  from ._q_xml_stream_notation_declaration import QXmlStreamNotationDeclarations
  from ._q_byte_array import QByteArrayList
  from ._q_xml_stream_namespace_declaration import QXmlStreamNamespaceDeclarations
  from ._q_object import QObjectList
  from ._q_model_index import QModelIndexList
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
      'QBindingStatus': '_q_binding_status',
      'QByteArrayView': '_q_byte_array_view',
      'QCameraPermission': '_q_camera_permission',
      'QCborParserError': '_q_cbor_parser_error',
      'QChar': '_q_char',
      'QContiguousCacheData': '_q_contiguous_cache_data',
      'QDeadlineTimer': '_q_deadline_timer',
      'QElapsedTimer': '_q_elapsed_timer',
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
      'QMargins': '_q_margins',
      'QMessageLogContext': '_q_message_log_context',
      'QMetaClassInfo': '_q_meta_class_info',
      'QMetaMethodArgument': '_q_meta_method_argument',
      'QMetaMethodReturnArgument': '_q_meta_method_return_argument',
      'QMethodRawArguments': '_q_method_raw_arguments',
      'QMicrophonePermission': '_q_microphone_permission',
      'QModelRoleData': '_q_model_role_data',
      'QObjectData': '_q_object_data',
      'QOperatingSystemVersionBase': '_q_operating_system_version_base',
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
      'QBasicMutex': '_q_basic_mutex',
      'QBindingStorage': '_q_binding_storage',
      'QBitArray': '_q_bit_array',
      'QByteArray': '_q_byte_array',
      'QGenericReturnArgument': '_q_generic_return_argument',
      'QLine': '_q_line',
      'QMarginsF': '_q_margins_f',
      'QMetaContainer': '_q_meta_container',
      'QModelRoleDataSpan': '_q_model_role_data_span',
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
      'QBasicReadWriteLock': '_q_basic_read_write_lock',
      'QBitRef': '_q_bit_ref',
      'QByteArrayMatcher': '_q_byte_array_matcher',
      'QCollatorSortKey': '_q_collator_sort_key',
      'QLineF': '_q_line_f',
      'QMetaAssociation': '_q_meta_association',
      'QMetaSequence': '_q_meta_sequence',
      'QMutex': '_q_mutex',
      'QOperatingSystemVersion': '_q_operating_system_version',
      'QRect': '_q_rect',
      'QSemaphoreReleaser': '_q_semaphore_releaser',
      'QSizeF': '_q_size_f',
      'QAssociativeConstIterator': '_q_associative_const_iterator',
      'QAssociativeIterator': '_q_associative_iterator',
      'QCommandLineOption': '_q_command_line_option',
      'QLatin1String': '_q_latin1_string',
      'QLatin1StringMatcher': '_q_latin1_string_matcher',
      'QLockFile': '_q_lock_file',
      'QLoggingCategory': '_q_logging_category',
      'QProcessEnvironment': '_q_process_environment',
      'QPropertyBindingError': '_q_property_binding_error',
      'QReadWriteLock': '_q_read_write_lock',
      'QRectF': '_q_rect_f',
      'QSequentialConstIterator': '_q_sequential_const_iterator',
      'QSequentialIterator': '_q_sequential_iterator',
      'QStringConverter': '_q_string_converter',
      'QStringMatcher': '_q_string_matcher',
      'QTemporaryDir': '_q_temporary_dir',
      'QTextBoundaryFinder': '_q_text_boundary_finder',
      'QTime': '_q_time',
      'QUrl': '_q_url',
      'QUrlQuery': '_q_url_query',
      'QUuid': '_q_uuid',
      'QVersionNumber': '_q_version_number',
      'QXmlStreamAttribute': '_q_xml_stream_attribute',
      'QXmlStreamAttributes': '_q_xml_stream_attributes',
      'QXmlStreamEntityResolver': '_q_xml_stream_entity_resolver',
      'QXmlStreamNamespaceDeclaration': '_q_xml_stream_namespace_declaration',
      'QMetaObject': '_q_meta_object',
      'QObject': '_q_object',
      'QDataStream': '_q_data_stream',
      'QDateTime': '_q_date_time',
      'QLocale': '_q_locale',
      'QModelIndex': '_q_model_index',
      'QEvent': '_q_event',
      'QIODevice': '_q_i_o_device',
      'QJsonArray': '_q_json_array',
      'QJsonObject': '_q_json_object',
      'QCborStreamWriter': '_q_cbor_stream_writer',
      'QDebug': '_q_debug',
      'QMetaType': '_q_meta_type',
      'QPersistentModelIndex': '_q_persistent_model_index',
      'QVariant': '_q_variant',
      'QTimeZone': '_q_time_zone',
      'QBasicTimer': '_q_basic_timer',
      'QCborStreamReader': '_q_cbor_stream_reader',
      'QCborValue': '_q_cbor_value',
      'QCollator': '_q_collator',
      'QDate': '_q_date',
      'QEventLoop': '_q_event_loop',
      'QMetaMethod': '_q_meta_method',
      'QMetaProperty': '_q_meta_property',
      'QMimeData': '_q_mime_data',
      'QSocketNotifier': '_q_socket_notifier',
      'QTextStream': '_q_text_stream',
      'QThread': '_q_thread',
      'QAbstractEventDispatcher': '_q_abstract_event_dispatcher',
      'QAbstractItemModel': '_q_abstract_item_model',
      'QCalendar': '_q_calendar',
      'QCborArray': '_q_cbor_array',
      'QCborError': '_q_cbor_error',
      'QCborMap': '_q_cbor_map',
      'QCborValueConstRef': '_q_cbor_value_const_ref',
      'QChildEvent': '_q_child_event',
      'QEasingCurve': '_q_easing_curve',
      'QJsonDocument': '_q_json_document',
      'QJsonValue': '_q_json_value',
      'QTextStreamManipulator': '_q_text_stream_manipulator',
      'QTimerEvent': '_q_timer_event',
      'QMessageLogger': '_q_message_logger',
      'QReadLocker': '_q_read_locker',
      'QStringDecoder': '_q_string_decoder',
      'QStringEncoder': '_q_string_encoder',
      'QWaitCondition': '_q_wait_condition',
      'QWriteLocker': '_q_write_locker',
      'QAbstractAnimation': '_q_abstract_animation',
      'QAbstractAnimationTimer': '_q_abstract_animation_timer',
      'QAbstractEventDispatcherV2': '_q_abstract_event_dispatcher_v2',
      'QAbstractListModel': '_q_abstract_list_model',
      'QAbstractTableModel': '_q_abstract_table_model',
      'QAdoptedThread': '_q_adopted_thread',
      'QAssociativeIterable': '_q_associative_iterable',
      'QBluetoothPermission': '_q_bluetooth_permission',
      'QBuffer': '_q_buffer',
      'QCalendarPermission': '_q_calendar_permission',
      'QCborValueRef': '_q_cbor_value_ref',
      'QChronoTimer': '_q_chrono_timer',
      'QConcatenateTablesProxyModel': '_q_concatenate_tables_proxy_model',
      'QContactsPermission': '_q_contacts_permission',
      'QCryptographicHash': '_q_cryptographic_hash',
      'QDaemonThread': '_q_daemon_thread',
      'QDebugStateSaver': '_q_debug_state_saver',
      'QDirListing': '_q_dir_listing',
      'QDynamicPropertyChangeEvent': '_q_dynamic_property_change_event',
      'QEventLoopLocker': '_q_event_loop_locker',
      'QFileDevice': '_q_file_device',
      'QFileSelector': '_q_file_selector',
      'QFileSystemWatcher': '_q_file_system_watcher',
      'QFileSystemWatcherEngine': '_q_file_system_watcher_engine',
      'QFutureWatcherBase': '_q_future_watcher_base',
      'QIOOperation': '_q_i_o_operation',
      'QItemSelectionRange': '_q_item_selection_range',
      'QJsonValueConstRef': '_q_json_value_const_ref',
      'QLibrary': '_q_library',
      'QLibraryInfo': '_q_library_info',
      'QLocationPermission': '_q_location_permission',
      'QMetaEnum': '_q_meta_enum',
      'QMimeType': '_q_mime_type',
      'QNativeIpcKey': '_q_native_ipc_key',
      'QNoDebug': '_q_no_debug',
      'QNonContiguousByteDevice': '_q_non_contiguous_byte_device',
      'QObjectCleanupHandler': '_q_object_cleanup_handler',
      'QPermission': '_q_permission',
      'QProcess': '_q_process',
      'QRandomAccessAsyncFile': '_q_random_access_async_file',
      'QResource': '_q_resource',
      'QSequentialIterable': '_q_sequential_iterable',
      'QSettings': '_q_settings',
      'QSignalBlocker': '_q_signal_blocker',
      'QSignalMapper': '_q_signal_mapper',
      'QSingleShotTimer': '_q_single_shot_timer',
      'QStandardPaths': '_q_standard_paths',
      'QThreadPool': '_q_thread_pool',
      'QTimeLine': '_q_time_line',
      'QTimer': '_q_timer',
      'QTranslator': '_q_translator',
      'QUntypedPropertyBinding': '_q_untyped_property_binding',
      'QVariantConstPointer': '_q_variant_const_pointer',
      'QXmlStreamReader': '_q_xml_stream_reader',
      'QAnimationDriver': '_q_animation_driver',
      'QAnimationTimer': '_q_animation_timer',
      'QByteDeviceWrappingIoDevice': '_q_byte_device_wrapping_io_device',
      'QFile': '_q_file',
      'QFutureInterfaceBase': '_q_future_interface_base',
      'QIOReadWriteOperationBase': '_q_i_o_read_write_operation_base',
      'QItemSelection': '_q_item_selection',
      'QItemSelectionModel': '_q_item_selection_model',
      'QJsonValueRef': '_q_json_value_ref',
      'QMessageAuthenticationCode': '_q_message_authentication_code',
      'QNonContiguousByteDeviceByteArrayImpl': '_q_non_contiguous_byte_device_byte_array_impl',
      'QNonContiguousByteDeviceIoDeviceImpl': '_q_non_contiguous_byte_device_io_device_impl',
      'QNonContiguousByteDeviceRingBufferImpl': '_q_non_contiguous_byte_device_ring_buffer_impl',
      'QPauseAnimation': '_q_pause_animation',
      'QPermissionPlugin': '_q_permission_plugin',
      'QPluginLoader': '_q_plugin_loader',
      'QPollingFileSystemWatcherEngine': '_q_polling_file_system_watcher_engine',
      'QPropertyObserver': '_q_property_observer',
      'QRangeModel': '_q_range_model',
      'QRangeModelImplBase': '_q_range_model_impl_base',
      'QSaveFile': '_q_save_file',
      'QSharedMemory': '_q_shared_memory',
      'QStringListModel': '_q_string_list_model',
      'QSystemSemaphore': '_q_system_semaphore',
      'QVariantAnimation': '_q_variant_animation',
      'QXmlStreamWriter': '_q_xml_stream_writer',
      'QAbstractProxyModel': '_q_abstract_proxy_model',
      'QAnimationGroup': '_q_animation_group',
      'QDir': '_q_dir',
      'QIOReadOperation': '_q_i_o_read_operation',
      'QIOVectoredReadOperation': '_q_i_o_vectored_read_operation',
      'QIOVectoredWriteOperation': '_q_i_o_vectored_write_operation',
      'QIOWriteOperation': '_q_i_o_write_operation',
      'QPropertyAnimation': '_q_property_animation',
      'QPropertyNotifier': '_q_property_notifier',
      'QTemporaryFile': '_q_temporary_file',
      'QUnifiedTimer': '_q_unified_timer',
      'QUntypedBindable': '_q_untyped_bindable',
      'QCoreApplication': '_q_core_application',
      'QDefaultAnimationDriver': '_q_default_animation_driver',
      'QDirIterator': '_q_dir_iterator',
      'QIdentityProxyModel': '_q_identity_proxy_model',
      'QParallelAnimationGroup': '_q_parallel_animation_group',
      'QSequentialAnimationGroup': '_q_sequential_animation_group',
      'QSortFilterProxyModel': '_q_sort_filter_proxy_model',
      'QStorageInfo': '_q_storage_info',
      'QTransposeProxyModel': '_q_transpose_proxy_model',
      'QCommandLineParser': '_q_command_line_parser',
      'QFileInfo': '_q_file_info',
      'QMimeDatabase': '_q_mime_database',
      'QXmlStreamEntityDeclarations': '_q_xml_stream_entity_declaration',
      'QXmlStreamNotationDeclarations': '_q_xml_stream_notation_declaration',
      'QByteArrayList': '_q_byte_array',
      'QXmlStreamNamespaceDeclarations': '_q_xml_stream_namespace_declaration',
      'QObjectList': '_q_object',
      'QModelIndexList': '_q_model_index',
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
