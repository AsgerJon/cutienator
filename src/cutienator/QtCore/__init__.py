"""
The namespace '' of Qt, a package of 'cutienator.QtCore':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtCore import 
  .DecodedArchRequirements

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QList',
    'QStringList',
    'QMap',
    'QHash',
    'CalculateGrowingBlockSizeResult',
    'DecodedArchRequirements',
    'ProcessOpenModeResult',
    'QAbstractDeclarativeData',
    'QAdoptSharedDataTag',
    'QArrayData',
    'QAtomicInt',
    'QBindingStatus',
    'QByteArrayView',
    'QCameraPermission',
    'QCborParserError',
    'QChar',
    'QCharAttributes',
    'QContiguousCacheData',
    'QDeadlineTimer',
    'QElapsedTimer',
    'QException',
    'QFactoryInterface',
    'QFileSelectorSharedData',
    'QFlag',
    'QFreeListDefaultConstants',
    'QGenericArgument',
    'QHashDummyValue',
    'QHashSeed',
    'QIODeviceBase',
    'QIORingRequestEmptyBase',
    'QIncompatibleFlag',
    'QInternal',
    'QJsonParseError',
    'QKeyCombination',
    'QLatch',
    'QLatin1Char',
    'QLibraryScanResult',
    'QMargins',
    'QMessageLogContext',
    'QMetaClassInfo',
    'QMetaMethodArgument',
    'QMetaMethodReturnArgument',
    'QMetaTypeModuleHelper',
    'QMethodRawArguments',
    'QMicrophonePermission',
    'QMimeMagicResult',
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
    'QSignalSpyCallbackSet',
    'QSocketDescriptor',
    'QSocketNotifierSetUNIX',
    'QStaticByteArrayMatcherBase',
    'QStaticPlugin',
    'QStringConverterBase',
    'QStringTokenizerBaseBase',
    'QSysInfo',
    'QSystemError',
    'QThreadPipe',
    'QThreadStorageData',
    'QTypeRevision',
    'QUntypedPropertyData',
    'QUtf8BaseTraits',
    'QVLABaseBase',
    'QXmlStream',
    'QXmlStreamEntityDeclaration',
    'QXmlStreamGrammar',
    'QXmlStreamNotationDeclaration',
    'qfloat16',
    'qt_semun',
    'QAbstractConcatenable',
    'QBasicMutex',
    'QBindingStorage',
    'QBitArray',
    'QByteArray',
    'QCollatorSortKeyPrivate',
    'QGenericReturnArgument',
    'QIORingRequestOffsetFdBase',
    'QLine',
    'QMarginsF',
    'QMetaContainer',
    'QModelRoleDataSpan',
    'QMutexPrivate',
    'QOperatingSystemVersionUnexported',
    'QPartialOrdering',
    'QPointF',
    'QPropertyBindingErrorPrivate',
    'QRandomGenerator64',
    'QReadWriteLockPrivate',
    'QRecursiveMutex',
    'QSemaphore',
    'QSize',
    'QUnhandledException',
    'QUtf8BaseTraitsNoAscii',
    'QueuePage',
    'QAbstractNativeEventFilter',
    'QRegularExpressionMatch',
    'QStringView',
    'QAnyStringView',
    'QRegularExpression',
    'QString',
    'QBasicReadWriteLock',
    'QBitRef',
    'QByteArrayMatcher',
    'QCollatorSortKey',
    'QLineF',
    'QMetaAssociation',
    'QMetaSequence',
    'QMetaStringTable',
    'QMutex',
    'QOperatingSystemVersion',
    'QOrderedMutexLocker',
    'QRect',
    'QRingBuffer',
    'QRingChunk',
    'QSemaphoreReleaser',
    'QSizeF',
    'QAbstractFileEngineHandler',
    'QAssociativeConstIterator',
    'QAssociativeIterator',
    'QCommandLineOption',
    'QConfFile',
    'QCtfTracePointProvider',
    'QElfParser',
    'QFileSystemEntry',
    'QFileSystemWatcherPathKey',
    'QLatin1String',
    'QLatin1StringMatcher',
    'QLocaleId',
    'QLockFile',
    'QLoggingCategory',
    'QLoggingRule',
    'QLoggingSettingsParser',
    'QMimeGlobMatchResult',
    'QMimeGlobPattern',
    'QMimeMagicRule',
    'QMimeTypePrivate',
    'QMimeTypeXMLData',
    'QPluginParsedMetaData',
    'QProcEnvValue',
    'QProcessEnvironment',
    'QProcessEnvironmentPrivate',
    'QPropertyBindingError',
    'QReadWriteLock',
    'QRectF',
    'QSequentialConstIterator',
    'QSequentialIterator',
    'QSettingsGroup',
    'QSettingsKey',
    'QStorageInfoPrivate',
    'QStringConverter',
    'QStringIterator',
    'QStringMatcher',
    'QTemporaryDir',
    'QTemporaryFileName',
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
    'QXmlStreamPrivateTagStack',
    'QXmlUtils',
    'QMetaObject',
    'QObject',
    'QIODevice',
    'QDataStream',
    'QModelIndex',
    'QDateTime',
    'QLocale',
    'QEvent',
    'QCborContainerPrivate',
    'QJsonArray',
    'QJsonObject',
    'QCborStreamWriter',
    'QDebug',
    'QMetaType',
    'QPersistentModelIndex',
    'QVariant',
    'QBasicTimer',
    'QCborStreamReader',
    'QCborValue',
    'QCollator',
    'QEventLoop',
    'QLocaleData',
    'QMetaMethod',
    'QMetaProperty',
    'QMimeData',
    'QPersistentModelIndexData',
    'QSocketNotifier',
    'QTextStream',
    'QThread',
    'QThreadData',
    'QTimeZone',
    'QAbstractEventDispatcher',
    'QAbstractItemModel',
    'QCalendar',
    'QCborArray',
    'QCborError',
    'QCborMap',
    'QCborValueConstRef',
    'QChildEvent',
    'QDate',
    'QEasingCurve',
    'QJsonDocument',
    'QJsonValue',
    'QLocalePrivate',
    'QObjectPrivate',
    'QAbstractEventDispatcherPrivate',
    'QAbstractItemModelPrivate',
    'QIODevicePrivate',
    'QTextStreamManipulator',
    'QThreadPrivate',
    'QTimerEvent',
    'QCtfTraceMetadata',
    'QCtfTracePointEvent',
    'QInternalMessageLogContext',
    'QLatin1',
    'QLocal8Bit',
    'QLockFilePrivate',
    'QLoggingCategoryWithEnvironmentOverride',
    'QLoggingRegistry',
    'QMessageLogger',
    'QMimeAllGlobPatterns',
    'QMimeGlobPatternList',
    'QMimeMagicRuleMatcher',
    'QReadLocker',
    'QStringDecoder',
    'QStringEncoder',
    'QUtf16',
    'QUtf32',
    'QUtf8',
    'QWaitCondition',
    'QWriteLocker',
    'QAbstractAnimation',
    'QAbstractAnimationPrivate',
    'QAbstractAnimationTimer',
    'QAbstractEventDispatcherV2',
    'QAbstractListModel',
    'QAbstractMetaCallEvent',
    'QAbstractProxyModelPrivate',
    'QAbstractTableModel',
    'QAdoptedThread',
    'QAnimationDriverPrivate',
    'QArgumentType',
    'QAssociativeIterable',
    'QBluetoothPermission',
    'QBuffer',
    'QCalendarLocale',
    'QCalendarPermission',
    'QCborValueRef',
    'QChronoTimer',
    'QCollatorPrivate',
    'QConcatenateTablesProxyModel',
    'QContactsPermission',
    'QCryptographicHash',
    'QCtfLib',
    'QDaemonThread',
    'QDatePattern',
    'QDateTimePattern',
    'QDateTimePrivate',
    'QDebugStateSaver',
    'QDeferredDeleteEvent',
    'QDirListing',
    'QDynamicMetaObjectData',
    'QDynamicPropertyChangeEvent',
    'QEventDispatcherGlibPrivate',
    'QEventDispatcherUNIXPrivate',
    'QEventLoopLocker',
    'QEventLoopPrivate',
    'QFileDevice',
    'QFileDevicePrivate',
    'QFileSelector',
    'QFileSelectorPrivate',
    'QFileSystemWatcher',
    'QFileSystemWatcherEngine',
    'QFutureCallOutEvent',
    'QFutureWatcherBase',
    'QIOOperation',
    'QIOOperationPrivate',
    'QItemSelectionRange',
    'QJsonValueConstRef',
    'QLibrary',
    'QLibraryInfo',
    'QLocationPermission',
    'QMetaEnum',
    'QMetaMethodInvoker',
    'QMimeType',
    'QMimeTypeParserBase',
    'QNativeIpcKey',
    'QNoDebug',
    'QNonContiguousByteDevice',
    'QObjectCleanupHandler',
    'QPermission',
    'QPostEvent',
    'QProcess',
    'QRandomAccessAsyncFile',
    'QResource',
    'QScopedScopeLevelCounter',
    'QSequentialIterable',
    'QSettings',
    'QSignalBlocker',
    'QSignalMapper',
    'QSingleShotTimer',
    'QStandardPaths',
    'QSystemLocale',
    'QTextStreamPrivate',
    'QThreadPool',
    'QThreadPoolPrivate',
    'QTimeLine',
    'QTimePattern',
    'QTimer',
    'QTimerInfo',
    'QTranslator',
    'QUntypedPropertyBinding',
    'QVariantConstPointer',
    'QWindowsFileSystemWatcherEngineThread',
    'QXmlStreamReader',
    'QZipReader',
    'QAbstractDynamicMetaObject',
    'QAnimationDriver',
    'QAnimationGroupPrivate',
    'QAnimationTimer',
    'QByteDeviceWrappingIoDevice',
    'QCalendarBackend',
    'QEventDispatcherGlib',
    'QEventDispatcherUNIX',
    'QFactoryLoader',
    'QFile',
    'QFilePrivate',
    'QFileSystemWatcherPrivate',
    'QFutureCallOutInterface',
    'QIOReadWriteOperationBase',
    'QIORing',
    'QIdentityProxyModelPrivate',
    'QInotifyFileSystemWatcherEngine',
    'QItemSelection',
    'QItemSelectionModel',
    'QItemSelectionModelPrivate',
    'QJsonValueRef',
    'QKqueueFileSystemWatcherEngine',
    'QLibraryInfoPrivate',
    'QLibraryPrivate',
    'QMessageAuthenticationCode',
    'QMetaCallEvent',
    'QMetaObjectBuilder',
    'QMetaObjectPrivate',
    'QNativeIpcKeyPrivate',
    'QNonContiguousByteDeviceByteArrayImpl',
    'QNonContiguousByteDeviceFactory',
    'QNonContiguousByteDeviceIoDeviceImpl',
    'QNonContiguousByteDeviceRingBufferImpl',
    'QPauseAnimation',
    'QPermissionPlugin',
    'QPluginLoader',
    'QPollingFileSystemWatcherEngine',
    'QPostEventList',
    'QProcessPrivate',
    'QPropertyBindingPrivate',
    'QPropertyObserver',
    'QPropertyBindingDataPointer',
    'QPropertyObserverPointer',
    'QRandomAccessAsyncFileBackend',
    'QRandomAccessAsyncFilePrivate',
    'QRangeModel',
    'QRangeModelImplBase',
    'QSaveFile',
    'QSaveFilePrivate',
    'QSettingsPrivate',
    'QSharedMemory',
    'QStringListModel',
    'QSystemSemaphore',
    'QTimerInfoList',
    'QTimerPrivate',
    'QTransposeProxyModelPrivate',
    'QVariantAnimation',
    'QVariantAnimationPrivate',
    'QWindowsFileSystemWatcherEngine',
    'QXmlStreamReaderPrivate',
    'QXmlStreamWriter',
    'QAbstractFileEngine',
    'QAbstractFileEnginePrivate',
    'QAbstractProxyModel',
    'QAnimationGroup',
    'QBindingObserverPtr',
    'QConfFileSettingsPrivate',
    'QCoreApplicationPrivate',
    'QDir',
    'QDirPrivate',
    'QFutureWatcherBasePrivate',
    'QHijriCalendar',
    'QIOReadOperation',
    'QIOVectoredReadOperation',
    'QIOVectoredWriteOperation',
    'QIOWriteOperation',
    'QJalaliCalendar',
    'QMetaEnumBuilder',
    'QMetaMethodBuilder',
    'QParallelAnimationGroupPrivate',
    'QPropertyAnimation',
    'QPropertyAnimationPrivate',
    'QPropertyNotifier',
    'QPropertyObserverNodeProtector',
    'QQueuedMetaCallEvent',
    'QRandomAccessAsyncFileThreadPoolBackend',
    'QRomanCalendar',
    'QSequentialAnimationGroupPrivate',
    'QSharedMemoryLocker',
    'QSystemSemaphorePrivate',
    'QTemporaryFile',
    'QTemporaryFilePrivate',
    'QUnifiedTimer',
    'QUntypedBindable',
    'QZipWriter',
    'QAbstractFileEngineIterator',
    'QCoreApplication',
    'QDateTimeParser',
    'QDefaultAnimationDriver',
    'QDirIterator',
    'QFileSystemIterator',
    'QFileSystemMetaData',
    'QFutureInterfaceBase',
    'QGregorianCalendar',
    'QIdentityProxyModel',
    'QIslamicCivilCalendar',
    'QJulianCalendar',
    'QMetaPropertyBuilder',
    'QMilankovicCalendar',
    'QParallelAnimationGroup',
    'QResourceFileEngine',
    'QSequentialAnimationGroup',
    'QSharedMemoryPrivate',
    'QSortFilterProxyModel',
    'QStorageInfo',
    'QSystemSemaphorePosix',
    'QSystemSemaphoreSystemV',
    'QSystemSemaphoreWin32',
    'QTransposeProxyModel',
    'QUntypedBindablePrivate',
    'QWasmAnimationDriver',
    'QCommandLineParser',
    'QFSFileEngineIterator',
    'QFSFileEnginePrivate',
    'QFileInfo',
    'QFileInfoPrivate',
    'QFileSystemEngine',
    'QFutureInterfaceBasePrivate',
    'QResourceFileEngineIterator',
    'QSharedMemoryPosix',
    'QSharedMemorySystemV',
    'QSharedMemoryWin32',
    'QDirEntryInfo',
    'QFSFileEngine',
    'QMimeDatabase',
    'QMimeDatabasePrivate',
    'QTemporaryFileEngine',
    'QMimeProviderBase',
    'QMimeBinaryProvider',
    'QMimeXMLProvider',
    'QMimeTypeParser',
    'QSSGUserShaderFragmentOutputs',
    'QXmlStreamEntityDeclarations',
    'QXmlStreamNotationDeclarations',
    'QByteArrayList',
    'QIntHash',
    'QXmlStreamNamespaceDeclarations',
    'QObjectList',
    'QModelIndexList',
    'QVariantList',
    'QVariantHash',
    'QVariantMap',
    'QFileInfoList',
    'QHashPrivate',
    'QHooks',
    'QJsonPrivate',
    'QLocalTime',
    'QOhosAppContext',
    'QRangeModelDetails',
    'QTest',
    'QUnicodeTables',
    'QUnicodeTools',
    'Qt',
    'QtCbor',
    'QtFuture',
    'QtGlobalStatic',
    'QtIpcCommon',
    'QtMetaContainerPrivate',
    'QtMetaTypePrivate',
    'QtMocConstants',
    'QtMocHelpers',
    'QtOrderingPrivate',
    'QtParseCommon',
    'QtParseQtTemporalFormat',
    'QtParseTemporal',
    'QtParseTimeZone',
    'QtPrivate',
    'QtSharedPointer',
    'QtTemporalPattern',
    'QtUniqueHandleTraits',
    'q20',
    'q23',
    'qxp',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_list import QList
  from ._q_string_list import QStringList
  from ._q_map import QMap
  from ._q_hash import QHash
  from ._calculate_growing_block_size_result import CalculateGrowingBlockSizeResult
  from ._decoded_arch_requirements import DecodedArchRequirements
  from ._process_open_mode_result import ProcessOpenModeResult
  from ._q_abstract_declarative_data import QAbstractDeclarativeData
  from ._q_adopt_shared_data_tag import QAdoptSharedDataTag
  from ._q_array_data import QArrayData
  from ._q_atomic_int import QAtomicInt
  from ._q_binding_status import QBindingStatus
  from ._q_byte_array_view import QByteArrayView
  from ._q_camera_permission import QCameraPermission
  from ._q_cbor_parser_error import QCborParserError
  from ._q_char import QChar
  from ._q_char_attributes import QCharAttributes
  from ._q_contiguous_cache_data import QContiguousCacheData
  from ._q_deadline_timer import QDeadlineTimer
  from ._q_elapsed_timer import QElapsedTimer
  from ._q_exception import QException
  from ._q_factory_interface import QFactoryInterface
  from ._q_file_selector_shared_data import QFileSelectorSharedData
  from ._q_flag import QFlag
  from ._q_free_list_default_constants import QFreeListDefaultConstants
  from ._q_generic_argument import QGenericArgument
  from ._q_hash_dummy_value import QHashDummyValue
  from ._q_hash_seed import QHashSeed
  from ._q_i_o_device_base import QIODeviceBase
  from ._q_i_o_ring_request_empty_base import QIORingRequestEmptyBase
  from ._q_incompatible_flag import QIncompatibleFlag
  from ._q_internal import QInternal
  from ._q_json_parse_error import QJsonParseError
  from ._q_key_combination import QKeyCombination
  from ._q_latch import QLatch
  from ._q_latin1_char import QLatin1Char
  from ._q_library_scan_result import QLibraryScanResult
  from ._q_margins import QMargins
  from ._q_message_log_context import QMessageLogContext
  from ._q_meta_class_info import QMetaClassInfo
  from ._q_meta_method_argument import QMetaMethodArgument
  from ._q_meta_method_return_argument import QMetaMethodReturnArgument
  from ._q_meta_type_module_helper import QMetaTypeModuleHelper
  from ._q_method_raw_arguments import QMethodRawArguments
  from ._q_microphone_permission import QMicrophonePermission
  from ._q_mime_magic_result import QMimeMagicResult
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
  from ._q_signal_spy_callback_set import QSignalSpyCallbackSet
  from ._q_socket_descriptor import QSocketDescriptor
  from ._q_socket_notifier_set_u_n_i_x import QSocketNotifierSetUNIX
  from ._q_static_byte_array_matcher_base import QStaticByteArrayMatcherBase
  from ._q_static_plugin import QStaticPlugin
  from ._q_string_converter_base import QStringConverterBase
  from ._q_string_tokenizer_base_base import QStringTokenizerBaseBase
  from ._q_sys_info import QSysInfo
  from ._q_system_error import QSystemError
  from ._q_thread_pipe import QThreadPipe
  from ._q_thread_storage_data import QThreadStorageData
  from ._q_type_revision import QTypeRevision
  from ._q_untyped_property_data import QUntypedPropertyData
  from ._q_utf8_base_traits import QUtf8BaseTraits
  from ._q_v_l_a_base_base import QVLABaseBase
  from ._q_xml_stream import QXmlStream
  from ._q_xml_stream_entity_declaration import QXmlStreamEntityDeclaration
  from ._q_xml_stream_grammar import QXmlStreamGrammar
  from ._q_xml_stream_notation_declaration import QXmlStreamNotationDeclaration
  from ._qfloat16 import qfloat16
  from ._qt_semun import qt_semun
  from ._q_abstract_concatenable import QAbstractConcatenable
  from ._q_basic_mutex import QBasicMutex
  from ._q_binding_storage import QBindingStorage
  from ._q_bit_array import QBitArray
  from ._q_byte_array import QByteArray
  from ._q_collator_sort_key_private import QCollatorSortKeyPrivate
  from ._q_generic_return_argument import QGenericReturnArgument
  from ._q_i_o_ring_request_offset_fd_base import QIORingRequestOffsetFdBase
  from ._q_line import QLine
  from ._q_margins_f import QMarginsF
  from ._q_meta_container import QMetaContainer
  from ._q_model_role_data_span import QModelRoleDataSpan
  from ._q_mutex_private import QMutexPrivate
  from ._q_operating_system_version_unexported import QOperatingSystemVersionUnexported
  from ._q_partial_ordering import QPartialOrdering
  from ._q_point_f import QPointF
  from ._q_property_binding_error_private import QPropertyBindingErrorPrivate
  from ._q_random_generator64 import QRandomGenerator64
  from ._q_read_write_lock_private import QReadWriteLockPrivate
  from ._q_recursive_mutex import QRecursiveMutex
  from ._q_semaphore import QSemaphore
  from ._q_size import QSize
  from ._q_unhandled_exception import QUnhandledException
  from ._q_utf8_base_traits_no_ascii import QUtf8BaseTraitsNoAscii
  from ._queue_page import QueuePage
  from ._q_abstract_native_event_filter import QAbstractNativeEventFilter
  from ._q_regular_expression_match import QRegularExpressionMatch
  from ._q_string_view import QStringView
  from ._q_any_string_view import QAnyStringView
  from ._q_regular_expression import QRegularExpression
  from ._q_string import QString
  from ._q_basic_read_write_lock import QBasicReadWriteLock
  from ._q_bit_ref import QBitRef
  from ._q_byte_array_matcher import QByteArrayMatcher
  from ._q_collator_sort_key import QCollatorSortKey
  from ._q_line_f import QLineF
  from ._q_meta_association import QMetaAssociation
  from ._q_meta_sequence import QMetaSequence
  from ._q_meta_string_table import QMetaStringTable
  from ._q_mutex import QMutex
  from ._q_operating_system_version import QOperatingSystemVersion
  from ._q_ordered_mutex_locker import QOrderedMutexLocker
  from ._q_rect import QRect
  from ._q_ring_buffer import QRingBuffer
  from ._q_ring_chunk import QRingChunk
  from ._q_semaphore_releaser import QSemaphoreReleaser
  from ._q_size_f import QSizeF
  from ._q_abstract_file_engine_handler import QAbstractFileEngineHandler
  from ._q_associative_const_iterator import QAssociativeConstIterator
  from ._q_associative_iterator import QAssociativeIterator
  from ._q_command_line_option import QCommandLineOption
  from ._q_conf_file import QConfFile
  from ._q_ctf_trace_point_provider import QCtfTracePointProvider
  from ._q_elf_parser import QElfParser
  from ._q_file_system_entry import QFileSystemEntry
  from ._q_file_system_watcher_path_key import QFileSystemWatcherPathKey
  from ._q_latin1_string import QLatin1String
  from ._q_latin1_string_matcher import QLatin1StringMatcher
  from ._q_locale_id import QLocaleId
  from ._q_lock_file import QLockFile
  from ._q_logging_category import QLoggingCategory
  from ._q_logging_rule import QLoggingRule
  from ._q_logging_settings_parser import QLoggingSettingsParser
  from ._q_mime_glob_match_result import QMimeGlobMatchResult
  from ._q_mime_glob_pattern import QMimeGlobPattern
  from ._q_mime_magic_rule import QMimeMagicRule
  from ._q_mime_type_private import QMimeTypePrivate
  from ._q_mime_type_x_m_l_data import QMimeTypeXMLData
  from ._q_plugin_parsed_meta_data import QPluginParsedMetaData
  from ._q_proc_env_value import QProcEnvValue
  from ._q_process_environment import QProcessEnvironment
  from ._q_process_environment_private import QProcessEnvironmentPrivate
  from ._q_property_binding_error import QPropertyBindingError
  from ._q_read_write_lock import QReadWriteLock
  from ._q_rect_f import QRectF
  from ._q_sequential_const_iterator import QSequentialConstIterator
  from ._q_sequential_iterator import QSequentialIterator
  from ._q_settings_group import QSettingsGroup
  from ._q_settings_key import QSettingsKey
  from ._q_storage_info_private import QStorageInfoPrivate
  from ._q_string_converter import QStringConverter
  from ._q_string_iterator import QStringIterator
  from ._q_string_matcher import QStringMatcher
  from ._q_temporary_dir import QTemporaryDir
  from ._q_temporary_file_name import QTemporaryFileName
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
  from ._q_xml_stream_private_tag_stack import QXmlStreamPrivateTagStack
  from ._q_xml_utils import QXmlUtils
  from ._q_meta_object import QMetaObject
  from ._q_object import QObject
  from ._q_i_o_device import QIODevice
  from ._q_data_stream import QDataStream
  from ._q_model_index import QModelIndex
  from ._q_date_time import QDateTime
  from ._q_locale import QLocale
  from ._q_event import QEvent
  from ._q_cbor_container_private import QCborContainerPrivate
  from ._q_json_array import QJsonArray
  from ._q_json_object import QJsonObject
  from ._q_cbor_stream_writer import QCborStreamWriter
  from ._q_debug import QDebug
  from ._q_meta_type import QMetaType
  from ._q_persistent_model_index import QPersistentModelIndex
  from ._q_variant import QVariant
  from ._q_basic_timer import QBasicTimer
  from ._q_cbor_stream_reader import QCborStreamReader
  from ._q_cbor_value import QCborValue
  from ._q_collator import QCollator
  from ._q_event_loop import QEventLoop
  from ._q_locale_data import QLocaleData
  from ._q_meta_method import QMetaMethod
  from ._q_meta_property import QMetaProperty
  from ._q_mime_data import QMimeData
  from ._q_persistent_model_index_data import QPersistentModelIndexData
  from ._q_socket_notifier import QSocketNotifier
  from ._q_text_stream import QTextStream
  from ._q_thread import QThread
  from ._q_thread_data import QThreadData
  from ._q_time_zone import QTimeZone
  from ._q_abstract_event_dispatcher import QAbstractEventDispatcher
  from ._q_abstract_item_model import QAbstractItemModel
  from ._q_calendar import QCalendar
  from ._q_cbor_array import QCborArray
  from ._q_cbor_error import QCborError
  from ._q_cbor_map import QCborMap
  from ._q_cbor_value_const_ref import QCborValueConstRef
  from ._q_child_event import QChildEvent
  from ._q_date import QDate
  from ._q_easing_curve import QEasingCurve
  from ._q_json_document import QJsonDocument
  from ._q_json_value import QJsonValue
  from ._q_locale_private import QLocalePrivate
  from ._q_object_private import QObjectPrivate
  from ._q_abstract_event_dispatcher_private import QAbstractEventDispatcherPrivate
  from ._q_abstract_item_model_private import QAbstractItemModelPrivate
  from ._q_i_o_device_private import QIODevicePrivate
  from ._q_text_stream_manipulator import QTextStreamManipulator
  from ._q_thread_private import QThreadPrivate
  from ._q_timer_event import QTimerEvent
  from ._q_ctf_trace_metadata import QCtfTraceMetadata
  from ._q_ctf_trace_point_event import QCtfTracePointEvent
  from ._q_internal_message_log_context import QInternalMessageLogContext
  from ._q_latin1 import QLatin1
  from ._q_local8_bit import QLocal8Bit
  from ._q_lock_file_private import QLockFilePrivate
  from ._q_logging_category_with_environment_override import QLoggingCategoryWithEnvironmentOverride
  from ._q_logging_registry import QLoggingRegistry
  from ._q_message_logger import QMessageLogger
  from ._q_mime_all_glob_patterns import QMimeAllGlobPatterns
  from ._q_mime_glob_pattern_list import QMimeGlobPatternList
  from ._q_mime_magic_rule_matcher import QMimeMagicRuleMatcher
  from ._q_read_locker import QReadLocker
  from ._q_string_decoder import QStringDecoder
  from ._q_string_encoder import QStringEncoder
  from ._q_utf16 import QUtf16
  from ._q_utf32 import QUtf32
  from ._q_utf8 import QUtf8
  from ._q_wait_condition import QWaitCondition
  from ._q_write_locker import QWriteLocker
  from ._q_abstract_animation import QAbstractAnimation
  from ._q_abstract_animation_private import QAbstractAnimationPrivate
  from ._q_abstract_animation_timer import QAbstractAnimationTimer
  from ._q_abstract_event_dispatcher_v2 import QAbstractEventDispatcherV2
  from ._q_abstract_list_model import QAbstractListModel
  from ._q_abstract_meta_call_event import QAbstractMetaCallEvent
  from ._q_abstract_proxy_model_private import QAbstractProxyModelPrivate
  from ._q_abstract_table_model import QAbstractTableModel
  from ._q_adopted_thread import QAdoptedThread
  from ._q_animation_driver_private import QAnimationDriverPrivate
  from ._q_argument_type import QArgumentType
  from ._q_associative_iterable import QAssociativeIterable
  from ._q_bluetooth_permission import QBluetoothPermission
  from ._q_buffer import QBuffer
  from ._q_calendar_locale import QCalendarLocale
  from ._q_calendar_permission import QCalendarPermission
  from ._q_cbor_value_ref import QCborValueRef
  from ._q_chrono_timer import QChronoTimer
  from ._q_collator_private import QCollatorPrivate
  from ._q_concatenate_tables_proxy_model import QConcatenateTablesProxyModel
  from ._q_contacts_permission import QContactsPermission
  from ._q_cryptographic_hash import QCryptographicHash
  from ._q_ctf_lib import QCtfLib
  from ._q_daemon_thread import QDaemonThread
  from ._q_date_pattern import QDatePattern
  from ._q_date_time_pattern import QDateTimePattern
  from ._q_date_time_private import QDateTimePrivate
  from ._q_debug_state_saver import QDebugStateSaver
  from ._q_deferred_delete_event import QDeferredDeleteEvent
  from ._q_dir_listing import QDirListing
  from ._q_dynamic_meta_object_data import QDynamicMetaObjectData
  from ._q_dynamic_property_change_event import QDynamicPropertyChangeEvent
  from ._q_event_dispatcher_glib_private import QEventDispatcherGlibPrivate
  from ._q_event_dispatcher_u_n_i_x_private import QEventDispatcherUNIXPrivate
  from ._q_event_loop_locker import QEventLoopLocker
  from ._q_event_loop_private import QEventLoopPrivate
  from ._q_file_device import QFileDevice
  from ._q_file_device_private import QFileDevicePrivate
  from ._q_file_selector import QFileSelector
  from ._q_file_selector_private import QFileSelectorPrivate
  from ._q_file_system_watcher import QFileSystemWatcher
  from ._q_file_system_watcher_engine import QFileSystemWatcherEngine
  from ._q_future_call_out_event import QFutureCallOutEvent
  from ._q_future_watcher_base import QFutureWatcherBase
  from ._q_i_o_operation import QIOOperation
  from ._q_i_o_operation_private import QIOOperationPrivate
  from ._q_item_selection_range import QItemSelectionRange
  from ._q_json_value_const_ref import QJsonValueConstRef
  from ._q_library import QLibrary
  from ._q_library_info import QLibraryInfo
  from ._q_location_permission import QLocationPermission
  from ._q_meta_enum import QMetaEnum
  from ._q_meta_method_invoker import QMetaMethodInvoker
  from ._q_mime_type import QMimeType
  from ._q_mime_type_parser_base import QMimeTypeParserBase
  from ._q_native_ipc_key import QNativeIpcKey
  from ._q_no_debug import QNoDebug
  from ._q_non_contiguous_byte_device import QNonContiguousByteDevice
  from ._q_object_cleanup_handler import QObjectCleanupHandler
  from ._q_permission import QPermission
  from ._q_post_event import QPostEvent
  from ._q_process import QProcess
  from ._q_random_access_async_file import QRandomAccessAsyncFile
  from ._q_resource import QResource
  from ._q_scoped_scope_level_counter import QScopedScopeLevelCounter
  from ._q_sequential_iterable import QSequentialIterable
  from ._q_settings import QSettings
  from ._q_signal_blocker import QSignalBlocker
  from ._q_signal_mapper import QSignalMapper
  from ._q_single_shot_timer import QSingleShotTimer
  from ._q_standard_paths import QStandardPaths
  from ._q_system_locale import QSystemLocale
  from ._q_text_stream_private import QTextStreamPrivate
  from ._q_thread_pool import QThreadPool
  from ._q_thread_pool_private import QThreadPoolPrivate
  from ._q_time_line import QTimeLine
  from ._q_time_pattern import QTimePattern
  from ._q_timer import QTimer
  from ._q_timer_info import QTimerInfo
  from ._q_translator import QTranslator
  from ._q_untyped_property_binding import QUntypedPropertyBinding
  from ._q_variant_const_pointer import QVariantConstPointer
  from ._q_windows_file_system_watcher_engine_thread import QWindowsFileSystemWatcherEngineThread
  from ._q_xml_stream_reader import QXmlStreamReader
  from ._q_zip_reader import QZipReader
  from ._q_abstract_dynamic_meta_object import QAbstractDynamicMetaObject
  from ._q_animation_driver import QAnimationDriver
  from ._q_animation_group_private import QAnimationGroupPrivate
  from ._q_animation_timer import QAnimationTimer
  from ._q_byte_device_wrapping_io_device import QByteDeviceWrappingIoDevice
  from ._q_calendar_backend import QCalendarBackend
  from ._q_event_dispatcher_glib import QEventDispatcherGlib
  from ._q_event_dispatcher_u_n_i_x import QEventDispatcherUNIX
  from ._q_factory_loader import QFactoryLoader
  from ._q_file import QFile
  from ._q_file_private import QFilePrivate
  from ._q_file_system_watcher_private import QFileSystemWatcherPrivate
  from ._q_future_call_out_interface import QFutureCallOutInterface
  from ._q_i_o_read_write_operation_base import QIOReadWriteOperationBase
  from ._q_i_o_ring import QIORing
  from ._q_identity_proxy_model_private import QIdentityProxyModelPrivate
  from ._q_inotify_file_system_watcher_engine import QInotifyFileSystemWatcherEngine
  from ._q_item_selection import QItemSelection
  from ._q_item_selection_model import QItemSelectionModel
  from ._q_item_selection_model_private import QItemSelectionModelPrivate
  from ._q_json_value_ref import QJsonValueRef
  from ._q_kqueue_file_system_watcher_engine import QKqueueFileSystemWatcherEngine
  from ._q_library_info_private import QLibraryInfoPrivate
  from ._q_library_private import QLibraryPrivate
  from ._q_message_authentication_code import QMessageAuthenticationCode
  from ._q_meta_call_event import QMetaCallEvent
  from ._q_meta_object_builder import QMetaObjectBuilder
  from ._q_meta_object_private import QMetaObjectPrivate
  from ._q_native_ipc_key_private import QNativeIpcKeyPrivate
  from ._q_non_contiguous_byte_device_byte_array_impl import QNonContiguousByteDeviceByteArrayImpl
  from ._q_non_contiguous_byte_device_factory import QNonContiguousByteDeviceFactory
  from ._q_non_contiguous_byte_device_io_device_impl import QNonContiguousByteDeviceIoDeviceImpl
  from ._q_non_contiguous_byte_device_ring_buffer_impl import QNonContiguousByteDeviceRingBufferImpl
  from ._q_pause_animation import QPauseAnimation
  from ._q_permission_plugin import QPermissionPlugin
  from ._q_plugin_loader import QPluginLoader
  from ._q_polling_file_system_watcher_engine import QPollingFileSystemWatcherEngine
  from ._q_post_event_list import QPostEventList
  from ._q_process_private import QProcessPrivate
  from ._q_property_binding_private import QPropertyBindingPrivate
  from ._q_property_observer import QPropertyObserver
  from ._q_property_binding_data_pointer import QPropertyBindingDataPointer
  from ._q_property_observer_pointer import QPropertyObserverPointer
  from ._q_random_access_async_file_backend import QRandomAccessAsyncFileBackend
  from ._q_random_access_async_file_private import QRandomAccessAsyncFilePrivate
  from ._q_range_model import QRangeModel
  from ._q_range_model_impl_base import QRangeModelImplBase
  from ._q_save_file import QSaveFile
  from ._q_save_file_private import QSaveFilePrivate
  from ._q_settings_private import QSettingsPrivate
  from ._q_shared_memory import QSharedMemory
  from ._q_string_list_model import QStringListModel
  from ._q_system_semaphore import QSystemSemaphore
  from ._q_timer_info_list import QTimerInfoList
  from ._q_timer_private import QTimerPrivate
  from ._q_transpose_proxy_model_private import QTransposeProxyModelPrivate
  from ._q_variant_animation import QVariantAnimation
  from ._q_variant_animation_private import QVariantAnimationPrivate
  from ._q_windows_file_system_watcher_engine import QWindowsFileSystemWatcherEngine
  from ._q_xml_stream_reader_private import QXmlStreamReaderPrivate
  from ._q_xml_stream_writer import QXmlStreamWriter
  from ._q_abstract_file_engine import QAbstractFileEngine
  from ._q_abstract_file_engine_private import QAbstractFileEnginePrivate
  from ._q_abstract_proxy_model import QAbstractProxyModel
  from ._q_animation_group import QAnimationGroup
  from ._q_binding_observer_ptr import QBindingObserverPtr
  from ._q_conf_file_settings_private import QConfFileSettingsPrivate
  from ._q_core_application_private import QCoreApplicationPrivate
  from ._q_dir import QDir
  from ._q_dir_private import QDirPrivate
  from ._q_future_watcher_base_private import QFutureWatcherBasePrivate
  from ._q_hijri_calendar import QHijriCalendar
  from ._q_i_o_read_operation import QIOReadOperation
  from ._q_i_o_vectored_read_operation import QIOVectoredReadOperation
  from ._q_i_o_vectored_write_operation import QIOVectoredWriteOperation
  from ._q_i_o_write_operation import QIOWriteOperation
  from ._q_jalali_calendar import QJalaliCalendar
  from ._q_meta_enum_builder import QMetaEnumBuilder
  from ._q_meta_method_builder import QMetaMethodBuilder
  from ._q_parallel_animation_group_private import QParallelAnimationGroupPrivate
  from ._q_property_animation import QPropertyAnimation
  from ._q_property_animation_private import QPropertyAnimationPrivate
  from ._q_property_notifier import QPropertyNotifier
  from ._q_property_observer_node_protector import QPropertyObserverNodeProtector
  from ._q_queued_meta_call_event import QQueuedMetaCallEvent
  from ._q_random_access_async_file_thread_pool_backend import QRandomAccessAsyncFileThreadPoolBackend
  from ._q_roman_calendar import QRomanCalendar
  from ._q_sequential_animation_group_private import QSequentialAnimationGroupPrivate
  from ._q_shared_memory_locker import QSharedMemoryLocker
  from ._q_system_semaphore_private import QSystemSemaphorePrivate
  from ._q_temporary_file import QTemporaryFile
  from ._q_temporary_file_private import QTemporaryFilePrivate
  from ._q_unified_timer import QUnifiedTimer
  from ._q_untyped_bindable import QUntypedBindable
  from ._q_zip_writer import QZipWriter
  from ._q_abstract_file_engine_iterator import QAbstractFileEngineIterator
  from ._q_core_application import QCoreApplication
  from ._q_date_time_parser import QDateTimeParser
  from ._q_default_animation_driver import QDefaultAnimationDriver
  from ._q_dir_iterator import QDirIterator
  from ._q_file_system_iterator import QFileSystemIterator
  from ._q_file_system_meta_data import QFileSystemMetaData
  from ._q_future_interface_base import QFutureInterfaceBase
  from ._q_gregorian_calendar import QGregorianCalendar
  from ._q_identity_proxy_model import QIdentityProxyModel
  from ._q_islamic_civil_calendar import QIslamicCivilCalendar
  from ._q_julian_calendar import QJulianCalendar
  from ._q_meta_property_builder import QMetaPropertyBuilder
  from ._q_milankovic_calendar import QMilankovicCalendar
  from ._q_parallel_animation_group import QParallelAnimationGroup
  from ._q_resource_file_engine import QResourceFileEngine
  from ._q_sequential_animation_group import QSequentialAnimationGroup
  from ._q_shared_memory_private import QSharedMemoryPrivate
  from ._q_sort_filter_proxy_model import QSortFilterProxyModel
  from ._q_storage_info import QStorageInfo
  from ._q_system_semaphore_posix import QSystemSemaphorePosix
  from ._q_system_semaphore_system_v import QSystemSemaphoreSystemV
  from ._q_system_semaphore_win32 import QSystemSemaphoreWin32
  from ._q_transpose_proxy_model import QTransposeProxyModel
  from ._q_untyped_bindable_private import QUntypedBindablePrivate
  from ._q_wasm_animation_driver import QWasmAnimationDriver
  from ._q_command_line_parser import QCommandLineParser
  from ._q_f_s_file_engine_iterator import QFSFileEngineIterator
  from ._q_f_s_file_engine_private import QFSFileEnginePrivate
  from ._q_file_info import QFileInfo
  from ._q_file_info_private import QFileInfoPrivate
  from ._q_file_system_engine import QFileSystemEngine
  from ._q_future_interface_base_private import QFutureInterfaceBasePrivate
  from ._q_resource_file_engine_iterator import QResourceFileEngineIterator
  from ._q_shared_memory_posix import QSharedMemoryPosix
  from ._q_shared_memory_system_v import QSharedMemorySystemV
  from ._q_shared_memory_win32 import QSharedMemoryWin32
  from ._q_dir_entry_info import QDirEntryInfo
  from ._q_f_s_file_engine import QFSFileEngine
  from ._q_mime_database import QMimeDatabase
  from ._q_mime_database_private import QMimeDatabasePrivate
  from ._q_temporary_file_engine import QTemporaryFileEngine
  from ._q_mime_provider_base import QMimeProviderBase
  from ._q_mime_binary_provider import QMimeBinaryProvider
  from ._q_mime_x_m_l_provider import QMimeXMLProvider
  from ._q_mime_type_parser import QMimeTypeParser
  from ._q_byte_array_view import QSSGUserShaderFragmentOutputs
  from ._q_xml_stream_entity_declaration import QXmlStreamEntityDeclarations
  from ._q_xml_stream_notation_declaration import QXmlStreamNotationDeclarations
  from ._q_byte_array import QByteArrayList
  from ._q_byte_array import QIntHash
  from ._q_xml_stream_namespace_declaration import QXmlStreamNamespaceDeclarations
  from ._q_object import QObjectList
  from ._q_model_index import QModelIndexList
  from ._q_variant import QVariantList
  from ._q_variant import QVariantHash
  from ._q_variant import QVariantMap
  from ._q_file_info import QFileInfoList
  from . import QHashPrivate
  from . import QHooks
  from . import QJsonPrivate
  from . import QLocalTime
  from . import QOhosAppContext
  from . import QRangeModelDetails
  from . import QTest
  from . import QUnicodeTables
  from . import QUnicodeTools
  from . import Qt
  from . import QtCbor
  from . import QtFuture
  from . import QtGlobalStatic
  from . import QtIpcCommon
  from . import QtMetaContainerPrivate
  from . import QtMetaTypePrivate
  from . import QtMocConstants
  from . import QtMocHelpers
  from . import QtOrderingPrivate
  from . import QtParseCommon
  from . import QtParseQtTemporalFormat
  from . import QtParseTemporal
  from . import QtParseTimeZone
  from . import QtPrivate
  from . import QtSharedPointer
  from . import QtTemporalPattern
  from . import QtUniqueHandleTraits
  from . import q20
  from . import q23
  from . import qxp
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QList': '_q_list',
      'QStringList': '_q_string_list',
      'QMap': '_q_map',
      'QHash': '_q_hash',
      'CalculateGrowingBlockSizeResult': '_calculate_growing_block_size_result',
      'DecodedArchRequirements': '_decoded_arch_requirements',
      'ProcessOpenModeResult': '_process_open_mode_result',
      'QAbstractDeclarativeData': '_q_abstract_declarative_data',
      'QAdoptSharedDataTag': '_q_adopt_shared_data_tag',
      'QArrayData': '_q_array_data',
      'QAtomicInt': '_q_atomic_int',
      'QBindingStatus': '_q_binding_status',
      'QByteArrayView': '_q_byte_array_view',
      'QCameraPermission': '_q_camera_permission',
      'QCborParserError': '_q_cbor_parser_error',
      'QChar': '_q_char',
      'QCharAttributes': '_q_char_attributes',
      'QContiguousCacheData': '_q_contiguous_cache_data',
      'QDeadlineTimer': '_q_deadline_timer',
      'QElapsedTimer': '_q_elapsed_timer',
      'QException': '_q_exception',
      'QFactoryInterface': '_q_factory_interface',
      'QFileSelectorSharedData': '_q_file_selector_shared_data',
      'QFlag': '_q_flag',
      'QFreeListDefaultConstants': '_q_free_list_default_constants',
      'QGenericArgument': '_q_generic_argument',
      'QHashDummyValue': '_q_hash_dummy_value',
      'QHashSeed': '_q_hash_seed',
      'QIODeviceBase': '_q_i_o_device_base',
      'QIORingRequestEmptyBase': '_q_i_o_ring_request_empty_base',
      'QIncompatibleFlag': '_q_incompatible_flag',
      'QInternal': '_q_internal',
      'QJsonParseError': '_q_json_parse_error',
      'QKeyCombination': '_q_key_combination',
      'QLatch': '_q_latch',
      'QLatin1Char': '_q_latin1_char',
      'QLibraryScanResult': '_q_library_scan_result',
      'QMargins': '_q_margins',
      'QMessageLogContext': '_q_message_log_context',
      'QMetaClassInfo': '_q_meta_class_info',
      'QMetaMethodArgument': '_q_meta_method_argument',
      'QMetaMethodReturnArgument': '_q_meta_method_return_argument',
      'QMetaTypeModuleHelper': '_q_meta_type_module_helper',
      'QMethodRawArguments': '_q_method_raw_arguments',
      'QMicrophonePermission': '_q_microphone_permission',
      'QMimeMagicResult': '_q_mime_magic_result',
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
      'QSignalSpyCallbackSet': '_q_signal_spy_callback_set',
      'QSocketDescriptor': '_q_socket_descriptor',
      'QSocketNotifierSetUNIX': '_q_socket_notifier_set_u_n_i_x',
      'QStaticByteArrayMatcherBase': '_q_static_byte_array_matcher_base',
      'QStaticPlugin': '_q_static_plugin',
      'QStringConverterBase': '_q_string_converter_base',
      'QStringTokenizerBaseBase': '_q_string_tokenizer_base_base',
      'QSysInfo': '_q_sys_info',
      'QSystemError': '_q_system_error',
      'QThreadPipe': '_q_thread_pipe',
      'QThreadStorageData': '_q_thread_storage_data',
      'QTypeRevision': '_q_type_revision',
      'QUntypedPropertyData': '_q_untyped_property_data',
      'QUtf8BaseTraits': '_q_utf8_base_traits',
      'QVLABaseBase': '_q_v_l_a_base_base',
      'QXmlStream': '_q_xml_stream',
      'QXmlStreamEntityDeclaration': '_q_xml_stream_entity_declaration',
      'QXmlStreamGrammar': '_q_xml_stream_grammar',
      'QXmlStreamNotationDeclaration': '_q_xml_stream_notation_declaration',
      'qfloat16': '_qfloat16',
      'qt_semun': '_qt_semun',
      'QAbstractConcatenable': '_q_abstract_concatenable',
      'QBasicMutex': '_q_basic_mutex',
      'QBindingStorage': '_q_binding_storage',
      'QBitArray': '_q_bit_array',
      'QByteArray': '_q_byte_array',
      'QCollatorSortKeyPrivate': '_q_collator_sort_key_private',
      'QGenericReturnArgument': '_q_generic_return_argument',
      'QIORingRequestOffsetFdBase': '_q_i_o_ring_request_offset_fd_base',
      'QLine': '_q_line',
      'QMarginsF': '_q_margins_f',
      'QMetaContainer': '_q_meta_container',
      'QModelRoleDataSpan': '_q_model_role_data_span',
      'QMutexPrivate': '_q_mutex_private',
      'QOperatingSystemVersionUnexported': '_q_operating_system_version_unexported',
      'QPartialOrdering': '_q_partial_ordering',
      'QPointF': '_q_point_f',
      'QPropertyBindingErrorPrivate': '_q_property_binding_error_private',
      'QRandomGenerator64': '_q_random_generator64',
      'QReadWriteLockPrivate': '_q_read_write_lock_private',
      'QRecursiveMutex': '_q_recursive_mutex',
      'QSemaphore': '_q_semaphore',
      'QSize': '_q_size',
      'QUnhandledException': '_q_unhandled_exception',
      'QUtf8BaseTraitsNoAscii': '_q_utf8_base_traits_no_ascii',
      'QueuePage': '_queue_page',
      'QAbstractNativeEventFilter': '_q_abstract_native_event_filter',
      'QRegularExpressionMatch': '_q_regular_expression_match',
      'QStringView': '_q_string_view',
      'QAnyStringView': '_q_any_string_view',
      'QRegularExpression': '_q_regular_expression',
      'QString': '_q_string',
      'QBasicReadWriteLock': '_q_basic_read_write_lock',
      'QBitRef': '_q_bit_ref',
      'QByteArrayMatcher': '_q_byte_array_matcher',
      'QCollatorSortKey': '_q_collator_sort_key',
      'QLineF': '_q_line_f',
      'QMetaAssociation': '_q_meta_association',
      'QMetaSequence': '_q_meta_sequence',
      'QMetaStringTable': '_q_meta_string_table',
      'QMutex': '_q_mutex',
      'QOperatingSystemVersion': '_q_operating_system_version',
      'QOrderedMutexLocker': '_q_ordered_mutex_locker',
      'QRect': '_q_rect',
      'QRingBuffer': '_q_ring_buffer',
      'QRingChunk': '_q_ring_chunk',
      'QSemaphoreReleaser': '_q_semaphore_releaser',
      'QSizeF': '_q_size_f',
      'QAbstractFileEngineHandler': '_q_abstract_file_engine_handler',
      'QAssociativeConstIterator': '_q_associative_const_iterator',
      'QAssociativeIterator': '_q_associative_iterator',
      'QCommandLineOption': '_q_command_line_option',
      'QConfFile': '_q_conf_file',
      'QCtfTracePointProvider': '_q_ctf_trace_point_provider',
      'QElfParser': '_q_elf_parser',
      'QFileSystemEntry': '_q_file_system_entry',
      'QFileSystemWatcherPathKey': '_q_file_system_watcher_path_key',
      'QLatin1String': '_q_latin1_string',
      'QLatin1StringMatcher': '_q_latin1_string_matcher',
      'QLocaleId': '_q_locale_id',
      'QLockFile': '_q_lock_file',
      'QLoggingCategory': '_q_logging_category',
      'QLoggingRule': '_q_logging_rule',
      'QLoggingSettingsParser': '_q_logging_settings_parser',
      'QMimeGlobMatchResult': '_q_mime_glob_match_result',
      'QMimeGlobPattern': '_q_mime_glob_pattern',
      'QMimeMagicRule': '_q_mime_magic_rule',
      'QMimeTypePrivate': '_q_mime_type_private',
      'QMimeTypeXMLData': '_q_mime_type_x_m_l_data',
      'QPluginParsedMetaData': '_q_plugin_parsed_meta_data',
      'QProcEnvValue': '_q_proc_env_value',
      'QProcessEnvironment': '_q_process_environment',
      'QProcessEnvironmentPrivate': '_q_process_environment_private',
      'QPropertyBindingError': '_q_property_binding_error',
      'QReadWriteLock': '_q_read_write_lock',
      'QRectF': '_q_rect_f',
      'QSequentialConstIterator': '_q_sequential_const_iterator',
      'QSequentialIterator': '_q_sequential_iterator',
      'QSettingsGroup': '_q_settings_group',
      'QSettingsKey': '_q_settings_key',
      'QStorageInfoPrivate': '_q_storage_info_private',
      'QStringConverter': '_q_string_converter',
      'QStringIterator': '_q_string_iterator',
      'QStringMatcher': '_q_string_matcher',
      'QTemporaryDir': '_q_temporary_dir',
      'QTemporaryFileName': '_q_temporary_file_name',
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
      'QXmlStreamPrivateTagStack': '_q_xml_stream_private_tag_stack',
      'QXmlUtils': '_q_xml_utils',
      'QMetaObject': '_q_meta_object',
      'QObject': '_q_object',
      'QIODevice': '_q_i_o_device',
      'QDataStream': '_q_data_stream',
      'QModelIndex': '_q_model_index',
      'QDateTime': '_q_date_time',
      'QLocale': '_q_locale',
      'QEvent': '_q_event',
      'QCborContainerPrivate': '_q_cbor_container_private',
      'QJsonArray': '_q_json_array',
      'QJsonObject': '_q_json_object',
      'QCborStreamWriter': '_q_cbor_stream_writer',
      'QDebug': '_q_debug',
      'QMetaType': '_q_meta_type',
      'QPersistentModelIndex': '_q_persistent_model_index',
      'QVariant': '_q_variant',
      'QBasicTimer': '_q_basic_timer',
      'QCborStreamReader': '_q_cbor_stream_reader',
      'QCborValue': '_q_cbor_value',
      'QCollator': '_q_collator',
      'QEventLoop': '_q_event_loop',
      'QLocaleData': '_q_locale_data',
      'QMetaMethod': '_q_meta_method',
      'QMetaProperty': '_q_meta_property',
      'QMimeData': '_q_mime_data',
      'QPersistentModelIndexData': '_q_persistent_model_index_data',
      'QSocketNotifier': '_q_socket_notifier',
      'QTextStream': '_q_text_stream',
      'QThread': '_q_thread',
      'QThreadData': '_q_thread_data',
      'QTimeZone': '_q_time_zone',
      'QAbstractEventDispatcher': '_q_abstract_event_dispatcher',
      'QAbstractItemModel': '_q_abstract_item_model',
      'QCalendar': '_q_calendar',
      'QCborArray': '_q_cbor_array',
      'QCborError': '_q_cbor_error',
      'QCborMap': '_q_cbor_map',
      'QCborValueConstRef': '_q_cbor_value_const_ref',
      'QChildEvent': '_q_child_event',
      'QDate': '_q_date',
      'QEasingCurve': '_q_easing_curve',
      'QJsonDocument': '_q_json_document',
      'QJsonValue': '_q_json_value',
      'QLocalePrivate': '_q_locale_private',
      'QObjectPrivate': '_q_object_private',
      'QAbstractEventDispatcherPrivate': '_q_abstract_event_dispatcher_private',
      'QAbstractItemModelPrivate': '_q_abstract_item_model_private',
      'QIODevicePrivate': '_q_i_o_device_private',
      'QTextStreamManipulator': '_q_text_stream_manipulator',
      'QThreadPrivate': '_q_thread_private',
      'QTimerEvent': '_q_timer_event',
      'QCtfTraceMetadata': '_q_ctf_trace_metadata',
      'QCtfTracePointEvent': '_q_ctf_trace_point_event',
      'QInternalMessageLogContext': '_q_internal_message_log_context',
      'QLatin1': '_q_latin1',
      'QLocal8Bit': '_q_local8_bit',
      'QLockFilePrivate': '_q_lock_file_private',
      'QLoggingCategoryWithEnvironmentOverride': '_q_logging_category_with_environment_override',
      'QLoggingRegistry': '_q_logging_registry',
      'QMessageLogger': '_q_message_logger',
      'QMimeAllGlobPatterns': '_q_mime_all_glob_patterns',
      'QMimeGlobPatternList': '_q_mime_glob_pattern_list',
      'QMimeMagicRuleMatcher': '_q_mime_magic_rule_matcher',
      'QReadLocker': '_q_read_locker',
      'QStringDecoder': '_q_string_decoder',
      'QStringEncoder': '_q_string_encoder',
      'QUtf16': '_q_utf16',
      'QUtf32': '_q_utf32',
      'QUtf8': '_q_utf8',
      'QWaitCondition': '_q_wait_condition',
      'QWriteLocker': '_q_write_locker',
      'QAbstractAnimation': '_q_abstract_animation',
      'QAbstractAnimationPrivate': '_q_abstract_animation_private',
      'QAbstractAnimationTimer': '_q_abstract_animation_timer',
      'QAbstractEventDispatcherV2': '_q_abstract_event_dispatcher_v2',
      'QAbstractListModel': '_q_abstract_list_model',
      'QAbstractMetaCallEvent': '_q_abstract_meta_call_event',
      'QAbstractProxyModelPrivate': '_q_abstract_proxy_model_private',
      'QAbstractTableModel': '_q_abstract_table_model',
      'QAdoptedThread': '_q_adopted_thread',
      'QAnimationDriverPrivate': '_q_animation_driver_private',
      'QArgumentType': '_q_argument_type',
      'QAssociativeIterable': '_q_associative_iterable',
      'QBluetoothPermission': '_q_bluetooth_permission',
      'QBuffer': '_q_buffer',
      'QCalendarLocale': '_q_calendar_locale',
      'QCalendarPermission': '_q_calendar_permission',
      'QCborValueRef': '_q_cbor_value_ref',
      'QChronoTimer': '_q_chrono_timer',
      'QCollatorPrivate': '_q_collator_private',
      'QConcatenateTablesProxyModel': '_q_concatenate_tables_proxy_model',
      'QContactsPermission': '_q_contacts_permission',
      'QCryptographicHash': '_q_cryptographic_hash',
      'QCtfLib': '_q_ctf_lib',
      'QDaemonThread': '_q_daemon_thread',
      'QDatePattern': '_q_date_pattern',
      'QDateTimePattern': '_q_date_time_pattern',
      'QDateTimePrivate': '_q_date_time_private',
      'QDebugStateSaver': '_q_debug_state_saver',
      'QDeferredDeleteEvent': '_q_deferred_delete_event',
      'QDirListing': '_q_dir_listing',
      'QDynamicMetaObjectData': '_q_dynamic_meta_object_data',
      'QDynamicPropertyChangeEvent': '_q_dynamic_property_change_event',
      'QEventDispatcherGlibPrivate': '_q_event_dispatcher_glib_private',
      'QEventDispatcherUNIXPrivate': '_q_event_dispatcher_u_n_i_x_private',
      'QEventLoopLocker': '_q_event_loop_locker',
      'QEventLoopPrivate': '_q_event_loop_private',
      'QFileDevice': '_q_file_device',
      'QFileDevicePrivate': '_q_file_device_private',
      'QFileSelector': '_q_file_selector',
      'QFileSelectorPrivate': '_q_file_selector_private',
      'QFileSystemWatcher': '_q_file_system_watcher',
      'QFileSystemWatcherEngine': '_q_file_system_watcher_engine',
      'QFutureCallOutEvent': '_q_future_call_out_event',
      'QFutureWatcherBase': '_q_future_watcher_base',
      'QIOOperation': '_q_i_o_operation',
      'QIOOperationPrivate': '_q_i_o_operation_private',
      'QItemSelectionRange': '_q_item_selection_range',
      'QJsonValueConstRef': '_q_json_value_const_ref',
      'QLibrary': '_q_library',
      'QLibraryInfo': '_q_library_info',
      'QLocationPermission': '_q_location_permission',
      'QMetaEnum': '_q_meta_enum',
      'QMetaMethodInvoker': '_q_meta_method_invoker',
      'QMimeType': '_q_mime_type',
      'QMimeTypeParserBase': '_q_mime_type_parser_base',
      'QNativeIpcKey': '_q_native_ipc_key',
      'QNoDebug': '_q_no_debug',
      'QNonContiguousByteDevice': '_q_non_contiguous_byte_device',
      'QObjectCleanupHandler': '_q_object_cleanup_handler',
      'QPermission': '_q_permission',
      'QPostEvent': '_q_post_event',
      'QProcess': '_q_process',
      'QRandomAccessAsyncFile': '_q_random_access_async_file',
      'QResource': '_q_resource',
      'QScopedScopeLevelCounter': '_q_scoped_scope_level_counter',
      'QSequentialIterable': '_q_sequential_iterable',
      'QSettings': '_q_settings',
      'QSignalBlocker': '_q_signal_blocker',
      'QSignalMapper': '_q_signal_mapper',
      'QSingleShotTimer': '_q_single_shot_timer',
      'QStandardPaths': '_q_standard_paths',
      'QSystemLocale': '_q_system_locale',
      'QTextStreamPrivate': '_q_text_stream_private',
      'QThreadPool': '_q_thread_pool',
      'QThreadPoolPrivate': '_q_thread_pool_private',
      'QTimeLine': '_q_time_line',
      'QTimePattern': '_q_time_pattern',
      'QTimer': '_q_timer',
      'QTimerInfo': '_q_timer_info',
      'QTranslator': '_q_translator',
      'QUntypedPropertyBinding': '_q_untyped_property_binding',
      'QVariantConstPointer': '_q_variant_const_pointer',
      'QWindowsFileSystemWatcherEngineThread': '_q_windows_file_system_watcher_engine_thread',
      'QXmlStreamReader': '_q_xml_stream_reader',
      'QZipReader': '_q_zip_reader',
      'QAbstractDynamicMetaObject': '_q_abstract_dynamic_meta_object',
      'QAnimationDriver': '_q_animation_driver',
      'QAnimationGroupPrivate': '_q_animation_group_private',
      'QAnimationTimer': '_q_animation_timer',
      'QByteDeviceWrappingIoDevice': '_q_byte_device_wrapping_io_device',
      'QCalendarBackend': '_q_calendar_backend',
      'QEventDispatcherGlib': '_q_event_dispatcher_glib',
      'QEventDispatcherUNIX': '_q_event_dispatcher_u_n_i_x',
      'QFactoryLoader': '_q_factory_loader',
      'QFile': '_q_file',
      'QFilePrivate': '_q_file_private',
      'QFileSystemWatcherPrivate': '_q_file_system_watcher_private',
      'QFutureCallOutInterface': '_q_future_call_out_interface',
      'QIOReadWriteOperationBase': '_q_i_o_read_write_operation_base',
      'QIORing': '_q_i_o_ring',
      'QIdentityProxyModelPrivate': '_q_identity_proxy_model_private',
      'QInotifyFileSystemWatcherEngine': '_q_inotify_file_system_watcher_engine',
      'QItemSelection': '_q_item_selection',
      'QItemSelectionModel': '_q_item_selection_model',
      'QItemSelectionModelPrivate': '_q_item_selection_model_private',
      'QJsonValueRef': '_q_json_value_ref',
      'QKqueueFileSystemWatcherEngine': '_q_kqueue_file_system_watcher_engine',
      'QLibraryInfoPrivate': '_q_library_info_private',
      'QLibraryPrivate': '_q_library_private',
      'QMessageAuthenticationCode': '_q_message_authentication_code',
      'QMetaCallEvent': '_q_meta_call_event',
      'QMetaObjectBuilder': '_q_meta_object_builder',
      'QMetaObjectPrivate': '_q_meta_object_private',
      'QNativeIpcKeyPrivate': '_q_native_ipc_key_private',
      'QNonContiguousByteDeviceByteArrayImpl': '_q_non_contiguous_byte_device_byte_array_impl',
      'QNonContiguousByteDeviceFactory': '_q_non_contiguous_byte_device_factory',
      'QNonContiguousByteDeviceIoDeviceImpl': '_q_non_contiguous_byte_device_io_device_impl',
      'QNonContiguousByteDeviceRingBufferImpl': '_q_non_contiguous_byte_device_ring_buffer_impl',
      'QPauseAnimation': '_q_pause_animation',
      'QPermissionPlugin': '_q_permission_plugin',
      'QPluginLoader': '_q_plugin_loader',
      'QPollingFileSystemWatcherEngine': '_q_polling_file_system_watcher_engine',
      'QPostEventList': '_q_post_event_list',
      'QProcessPrivate': '_q_process_private',
      'QPropertyBindingPrivate': '_q_property_binding_private',
      'QPropertyObserver': '_q_property_observer',
      'QPropertyBindingDataPointer': '_q_property_binding_data_pointer',
      'QPropertyObserverPointer': '_q_property_observer_pointer',
      'QRandomAccessAsyncFileBackend': '_q_random_access_async_file_backend',
      'QRandomAccessAsyncFilePrivate': '_q_random_access_async_file_private',
      'QRangeModel': '_q_range_model',
      'QRangeModelImplBase': '_q_range_model_impl_base',
      'QSaveFile': '_q_save_file',
      'QSaveFilePrivate': '_q_save_file_private',
      'QSettingsPrivate': '_q_settings_private',
      'QSharedMemory': '_q_shared_memory',
      'QStringListModel': '_q_string_list_model',
      'QSystemSemaphore': '_q_system_semaphore',
      'QTimerInfoList': '_q_timer_info_list',
      'QTimerPrivate': '_q_timer_private',
      'QTransposeProxyModelPrivate': '_q_transpose_proxy_model_private',
      'QVariantAnimation': '_q_variant_animation',
      'QVariantAnimationPrivate': '_q_variant_animation_private',
      'QWindowsFileSystemWatcherEngine': '_q_windows_file_system_watcher_engine',
      'QXmlStreamReaderPrivate': '_q_xml_stream_reader_private',
      'QXmlStreamWriter': '_q_xml_stream_writer',
      'QAbstractFileEngine': '_q_abstract_file_engine',
      'QAbstractFileEnginePrivate': '_q_abstract_file_engine_private',
      'QAbstractProxyModel': '_q_abstract_proxy_model',
      'QAnimationGroup': '_q_animation_group',
      'QBindingObserverPtr': '_q_binding_observer_ptr',
      'QConfFileSettingsPrivate': '_q_conf_file_settings_private',
      'QCoreApplicationPrivate': '_q_core_application_private',
      'QDir': '_q_dir',
      'QDirPrivate': '_q_dir_private',
      'QFutureWatcherBasePrivate': '_q_future_watcher_base_private',
      'QHijriCalendar': '_q_hijri_calendar',
      'QIOReadOperation': '_q_i_o_read_operation',
      'QIOVectoredReadOperation': '_q_i_o_vectored_read_operation',
      'QIOVectoredWriteOperation': '_q_i_o_vectored_write_operation',
      'QIOWriteOperation': '_q_i_o_write_operation',
      'QJalaliCalendar': '_q_jalali_calendar',
      'QMetaEnumBuilder': '_q_meta_enum_builder',
      'QMetaMethodBuilder': '_q_meta_method_builder',
      'QParallelAnimationGroupPrivate': '_q_parallel_animation_group_private',
      'QPropertyAnimation': '_q_property_animation',
      'QPropertyAnimationPrivate': '_q_property_animation_private',
      'QPropertyNotifier': '_q_property_notifier',
      'QPropertyObserverNodeProtector': '_q_property_observer_node_protector',
      'QQueuedMetaCallEvent': '_q_queued_meta_call_event',
      'QRandomAccessAsyncFileThreadPoolBackend': '_q_random_access_async_file_thread_pool_backend',
      'QRomanCalendar': '_q_roman_calendar',
      'QSequentialAnimationGroupPrivate': '_q_sequential_animation_group_private',
      'QSharedMemoryLocker': '_q_shared_memory_locker',
      'QSystemSemaphorePrivate': '_q_system_semaphore_private',
      'QTemporaryFile': '_q_temporary_file',
      'QTemporaryFilePrivate': '_q_temporary_file_private',
      'QUnifiedTimer': '_q_unified_timer',
      'QUntypedBindable': '_q_untyped_bindable',
      'QZipWriter': '_q_zip_writer',
      'QAbstractFileEngineIterator': '_q_abstract_file_engine_iterator',
      'QCoreApplication': '_q_core_application',
      'QDateTimeParser': '_q_date_time_parser',
      'QDefaultAnimationDriver': '_q_default_animation_driver',
      'QDirIterator': '_q_dir_iterator',
      'QFileSystemIterator': '_q_file_system_iterator',
      'QFileSystemMetaData': '_q_file_system_meta_data',
      'QFutureInterfaceBase': '_q_future_interface_base',
      'QGregorianCalendar': '_q_gregorian_calendar',
      'QIdentityProxyModel': '_q_identity_proxy_model',
      'QIslamicCivilCalendar': '_q_islamic_civil_calendar',
      'QJulianCalendar': '_q_julian_calendar',
      'QMetaPropertyBuilder': '_q_meta_property_builder',
      'QMilankovicCalendar': '_q_milankovic_calendar',
      'QParallelAnimationGroup': '_q_parallel_animation_group',
      'QResourceFileEngine': '_q_resource_file_engine',
      'QSequentialAnimationGroup': '_q_sequential_animation_group',
      'QSharedMemoryPrivate': '_q_shared_memory_private',
      'QSortFilterProxyModel': '_q_sort_filter_proxy_model',
      'QStorageInfo': '_q_storage_info',
      'QSystemSemaphorePosix': '_q_system_semaphore_posix',
      'QSystemSemaphoreSystemV': '_q_system_semaphore_system_v',
      'QSystemSemaphoreWin32': '_q_system_semaphore_win32',
      'QTransposeProxyModel': '_q_transpose_proxy_model',
      'QUntypedBindablePrivate': '_q_untyped_bindable_private',
      'QWasmAnimationDriver': '_q_wasm_animation_driver',
      'QCommandLineParser': '_q_command_line_parser',
      'QFSFileEngineIterator': '_q_f_s_file_engine_iterator',
      'QFSFileEnginePrivate': '_q_f_s_file_engine_private',
      'QFileInfo': '_q_file_info',
      'QFileInfoPrivate': '_q_file_info_private',
      'QFileSystemEngine': '_q_file_system_engine',
      'QFutureInterfaceBasePrivate': '_q_future_interface_base_private',
      'QResourceFileEngineIterator': '_q_resource_file_engine_iterator',
      'QSharedMemoryPosix': '_q_shared_memory_posix',
      'QSharedMemorySystemV': '_q_shared_memory_system_v',
      'QSharedMemoryWin32': '_q_shared_memory_win32',
      'QDirEntryInfo': '_q_dir_entry_info',
      'QFSFileEngine': '_q_f_s_file_engine',
      'QMimeDatabase': '_q_mime_database',
      'QMimeDatabasePrivate': '_q_mime_database_private',
      'QTemporaryFileEngine': '_q_temporary_file_engine',
      'QMimeProviderBase': '_q_mime_provider_base',
      'QMimeBinaryProvider': '_q_mime_binary_provider',
      'QMimeXMLProvider': '_q_mime_x_m_l_provider',
      'QMimeTypeParser': '_q_mime_type_parser',
      'QSSGUserShaderFragmentOutputs': '_q_byte_array_view',
      'QXmlStreamEntityDeclarations': '_q_xml_stream_entity_declaration',
      'QXmlStreamNotationDeclarations': '_q_xml_stream_notation_declaration',
      'QByteArrayList': '_q_byte_array',
      'QIntHash': '_q_byte_array',
      'QXmlStreamNamespaceDeclarations': '_q_xml_stream_namespace_declaration',
      'QObjectList': '_q_object',
      'QModelIndexList': '_q_model_index',
      'QVariantList': '_q_variant',
      'QVariantHash': '_q_variant',
      'QVariantMap': '_q_variant',
      'QFileInfoList': '_q_file_info',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QHashPrivate', 'QHooks', 'QJsonPrivate', 'QLocalTime', 'QOhosAppContext', 'QRangeModelDetails', 'QTest', 'QUnicodeTables', 'QUnicodeTools', 'Qt', 'QtCbor', 'QtFuture', 'QtGlobalStatic', 'QtIpcCommon', 'QtMetaContainerPrivate', 'QtMetaTypePrivate', 'QtMocConstants', 'QtMocHelpers', 'QtOrderingPrivate', 'QtParseCommon', 'QtParseQtTemporalFormat', 'QtParseTemporal', 'QtParseTimeZone', 'QtPrivate', 'QtSharedPointer', 'QtTemporalPattern', 'QtUniqueHandleTraits', 'q20', 'q23', 'qxp',)


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
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
      globals()[name] = value
      return value
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
