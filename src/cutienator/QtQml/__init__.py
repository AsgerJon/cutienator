"""
The namespace '' of Qt, a package of 'cutienator.QtQml':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQml import 
  .QQmlTriviallyDestructibleDebuggingEnabler

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
    'AliasToRequiredInfo',
    'DeferredQPropertyBinding',
    'ParserStatus',
    'QInheritedListNode',
    'QIntrusiveListNode',
    'QJSListForInIterator',
    'QJSListForOfIterator',
    'QJSListIndexClamp',
    'QJSNumberCoercion',
    'QJSPrimitiveNull',
    'QJSPrimitiveUndefined',
    'QQmlComponentAndAliasResolverBase',
    'QQmlEnumData',
    'QQmlFinalizerHook',
    'QQmlImportRef',
    'QQmlIncubationController',
    'QQmlModuleRegistration',
    'QQmlObjectCreatorSharedState',
    'QQmlParserStatus',
    'QQmlProfilerDefinitions',
    'QQmlPropertyCacheMethodArguments',
    'QQmlPropertyIndex',
    'QQmlRefCount',
    'QQmlTriviallyDestructibleDebuggingEnabler',
    'QQmlTypeLoaderConfiguredData',
    'QQmlTypeLoaderNetworkAccessManagerData',
    'QQmlTypeLoaderSharedData',
    'QQmlTypeLoaderThreadData',
    'QQmlTypesExtensionInterface',
    'QQmlVME',
    'QRecursionNode',
    'QmltcTypeData',
    'RequiredProperties',
    'RequiredPropertyInfo',
    'SelfDeletable',
    'QHashedCStringRef',
    'QQmlInstantiationInterrupt',
    'QQmlProfilerData',
    'QQmlListMetaTypeInterface',
    'QQmlMetaTypeInterface',
    'QQmlThread',
    'QHashedString',
    'QHashedStringRef',
    'QQmlDebuggingEnabler',
    'QQmlDirParser',
    'QQmlEnumValue',
    'QQmlPropertyResolver',
    'QQmlSignalNames',
    'QQmlSourceLocation',
    'QQmlTranslation',
    'QQmlAbstractUrlInterceptor',
    'QQmlBindingInstantiationContext',
    'DayOfWeekList',
    'QAbstractAnimationJob',
    'QAnimationJobChangeListener',
    'QBoolStdVectorForeign',
    'QDoubleStdVectorForeign',
    'QFloatStdVectorForeign',
    'QIntStdVectorForeign',
    'QJSPrimitiveValue',
    'QQmlAbstractProfilerAdapterFactory',
    'QQmlAnyStringViewForeign',
    'QQmlApplicationPrivate',
    'QQmlBoolForeign',
    'QQmlCharForeign',
    'QQmlColorProvider',
    'QQmlComponentAttached',
    'QQmlComponentForeign',
    'QQmlDateForeign',
    'QQmlDebugConnectorFactory',
    'QQmlDebugServerConnectionFactory',
    'QQmlDebugServiceFactory',
    'QQmlDoubleForeign',
    'QQmlEasing',
    'QQmlError',
    'QQmlFileSelectorPrivate',
    'QQmlFloatForeign',
    'QQmlGuardImpl',
    'QQmlGuiProvider',
    'QQmlImageProviderBase',
    'QQmlIncubator',
    'QQmlInfo',
    'QQmlInt16TForeign',
    'QQmlInt32TForeign',
    'QQmlInt64TForeign',
    'QQmlInt8TForeign',
    'QQmlIntForeign',
    'QQmlLocaleValueType',
    'QQmlLoggingCategoryBase',
    'QQmlLongForeign',
    'QQmlMarginsFValueType',
    'QQmlMarginsValueType',
    'QQmlMetaObjectPointer',
    'QQmlNetworkAccessManagerFactory',
    'QQmlNullForeign',
    'QQmlPlatform',
    'QQmlPointFValueType',
    'QQmlPointValueType',
    'QQmlPropertyCacheCreatorBase',
    'QQmlPropertyData',
    'QQmlPropertyMap',
    'QQmlQByteArrayForeign',
    'QQmlQByteArrayListForeign',
    'QQmlQCharForeign',
    'QQmlQDateForeign',
    'QQmlQJSValueForeign',
    'QQmlQJsonArrayForeign',
    'QQmlQJsonObjectForeign',
    'QQmlQJsonValueForeign',
    'QQmlQListQObjectForeign',
    'QQmlQObjectListForeign',
    'QQmlQRealForeign',
    'QQmlQStringListForeign',
    'QQmlQTimeForeign',
    'QQmlQVariantHashForeign',
    'QQmlQVariantListForeign',
    'QQmlQVariantMapForeign',
    'QQmlQint16Foreign',
    'QQmlQint32Foreign',
    'QQmlQint64Foreign',
    'QQmlQint8Foreign',
    'QQmlQlonglongForeign',
    'QQmlQtObjectForeign',
    'QQmlQuint16Foreign',
    'QQmlQuint32Foreign',
    'QQmlQuint64Foreign',
    'QQmlQuint8Foreign',
    'QQmlQulonglongForeign',
    'QQmlRectFValueType',
    'QQmlRectValueType',
    'QQmlRegexpForeign',
    'QQmlScriptStringForeign',
    'QQmlShortForeign',
    'QQmlSizeFValueType',
    'QQmlSizeValueType',
    'QQmlStringForeign',
    'QQmlTypeNotAvailable',
    'QQmlUcharForeign',
    'QQmlUint16TForeign',
    'QQmlUint32TForeign',
    'QQmlUint64TForeign',
    'QQmlUint8TForeign',
    'QQmlUintForeign',
    'QQmlUlongForeign',
    'QQmlUrlForeign',
    'QQmlUshortForeign',
    'QQmlV4ExecutionEnginePtrForeign',
    'QQmlV4FunctionPtrForeign',
    'QQmlVMEResolvedList',
    'QQmlVarForeign',
    'QQmlVoidForeign',
    'QQmltcObjectCreationHelper',
    'QRealListForeign',
    'QRealStdVectorForeign',
    'QStringHashBase',
    'QStringHashNode',
    'QStringStdVectorForeign',
    'QUrlStdVectorForeign',
    'RequiredPropertiesAndTarget',
    'QAnimationGroupJob',
    'QPauseAnimationJob',
    'QQmlAnimationTimer',
    'QQmlApplication',
    'QQmlCppBinding',
    'QQmlEasingValueType',
    'QQmlFileSelectorInterceptor',
    'QQmlIRLoader',
    'QQmlMetaObject',
    'QQmlProxyMetaObject',
    'QQmlTranslationPropertyBindingFunctorBase',
    'QQmlTypeLoaderQmldirContent',
    'QQmlValueType',
    'QStringHashData',
    'RequiredPropertyKey',
    'QContinuingAnimationGroupJob',
    'QParallelAnimationGroupJob',
    'QQmlObjectOrGadget',
    'QQmlPropertyBindingBase',
    'QQmlTranslationPropertyBinding',
    'QQmlTranslationPropertyBindingFunctor',
    'QQmlTranslationPropertyTranslationDataFunctor',
    'QSequentialAnimationGroupJob',
    'QQmlOpenMetaObjectType',
    'QQmlOpenMetaObject',
    'QQmlTypeLoader',
    'QQmlType',
    'QQmlContext',
    'QQmlContextData',
    'QQmlDataBlob',
    'QQmlImportNamespace',
    'QQmlProperty',
    'QJSValue',
    'QJSEngine',
    'QQmlEngine',
    'QQmlAbstractBinding',
    'QQmlComponent',
    'QQmlData',
    'QQmlImportInstance',
    'QQmlImports',
    'QQmlIncubatorPrivate',
    'QQmlTypeNameCache',
    'QQmlTypePrivate',
    'QQmlMetaType',
    'QJSEnginePrivate',
    'QQmlEnginePrivate',
    'QJSManagedValue',
    'QQmlContextPrivate',
    'QQmlEngineExtensionInterface',
    'QQmlExtensionInterface',
    'QQmlJavaScriptExpression',
    'QQmlBoundSignalExpression',
    'QQmlPropertyPrivate',
    'QQmlObjectCreator',
    'QQmlNotifier',
    'QQmlNotifierEndpoint',
    'QQmlProfiler',
    'QQmlComponentPrivate',
    'QQmlNotifyingBlob',
    'QQmlScriptBlob',
    'QQmlQmldirData',
    'QQmlTypeData',
    'LoadHelper',
    'ObjectInCreationGCAnchorList',
    'QJSManagedValuePrivate',
    'QJSValueIterator',
    'QJSValueIteratorPrivate',
    'QJSValuePrivate',
    'QPropertyChangeTrigger',
    'QQmlApplicationEngine',
    'QQmlApplicationEnginePrivate',
    'QQmlBoundSignal',
    'QQmlCustomParser',
    'QQmlDateExtension',
    'QQmlDebugService',
    'QQmlDebugStatesDelegate',
    'QQmlDelayedCallQueue',
    'QQmlDelayedError',
    'QQmlEngineExtensionPlugin',
    'QQmlExtensionPlugin',
    'QQmlFile',
    'QQmlFileSelector',
    'QQmlGadgetPtrWrapper',
    'QQmlGuardedContextData',
    'QQmlJavaScriptExpressionGuard',
    'QQmlListReference',
    'QQmlLocale',
    'QQmlNotifyList',
    'QQmlNumberExtension',
    'QQmlObjectCreationProfiler',
    'QQmlObjectCreatorRecursionWatcher',
    'QQmlPluginImporter',
    'QQmlProfilerHelper',
    'QQmlPropertyBindingJS',
    'QQmlPropertyObserver',
    'QQmlPropertyToBindablePropertyBinding',
    'QQmlPropertyToPropertyBinding',
    'QQmlPropertyToUnbindablePropertyBinding',
    'QQmlPropertyValidator',
    'QQmlPropertyValueInterceptor',
    'QQmlPropertyValueSource',
    'QQmlScriptData',
    'QQmlScriptString',
    'QQmlTypeCompiler',
    'QQmlTypeLoaderLockedData',
    'QQmlTypeLoaderNetworkReplyProxy',
    'QQmlTypeLoaderThread',
    'QQmlTypeModule',
    'QQmlV4Function',
    'QQmlVMEGuard',
    'QQmlValueTypeProvider',
    'QQmlValueTypeProxyBinding',
    'QQmlVmeProfiler',
    'QV4Include',
    'QtObject',
    'TranslationBindingInformation',
    'QDebugMessageService',
    'QQmlAbstractProfilerAdapter',
    'QQmlProfilerService',
    'QQmlAnyBinding',
    'QQmlBindableToBindablePropertyBinding',
    'QQmlBindableToUnbindablePropertyBinding',
    'QQmlBindingProfiler',
    'QQmlCompilePass',
    'QQmlCompilingProfiler',
    'QQmlCppOnAssignmentHelper',
    'QQmlDebugConnector',
    'QQmlDebugTranslationService',
    'QQmlEngineControlService',
    'QQmlEngineDebugService',
    'QQmlExpression',
    'QQmlExpressionPrivate',
    'QQmlExtensionPluginPrivate',
    'QQmlHandlingSignalProfiler',
    'QQmlInterceptorMetaObject',
    'QQmlListReferencePrivate',
    'QQmlMetaTypeData',
    'QQmlNativeDebugService',
    'QQmlNetworkAccessManagerFactoryPtr',
    'QQmlObjectCompletionProfiler',
    'QQmlPropertyBindingJSForBoundFunction',
    'QQmlScriptStringPrivate',
    'QQmlTypeModuleVersion',
    'QQmlUnbindableToBindablePropertyBinding',
    'QQmlUnbindableToUnbindablePropertyBinding',
    'QQuickEventReplayService',
    'QV4DebugService',
    'TriggerList',
    'QQmlAliasAnnotator',
    'QQmlBinding',
    'QQmlCustomParserScriptIndexer',
    'QQmlDebugServer',
    'QQmlDeferredAndCustomParserBindingScanner',
    'QQmlEnumTypeResolver',
    'QQmlInspectorService',
    'QQmlPropertyBinding',
    'QQmlScriptStringScanner',
    'QQmlVMEMetaObject',
    'SignalHandlerResolver',
    'QQmlDebugServerConnection',
    'QQmlPropertyCache',
    'QQmlVMEVariantQObjectPtr',
    'QQmlPropertyCacheVector',
    'QQmlPropertyCapture',
    'QQmlPendingGroupPropertyBindings',
    'QQmlProperties',
    'QJSValueList',
    'OverrideSemantics',
    'QQml',
    'QQmlDebugTranslation',
    'QQmlImport',
    'QQmlJS',
    'QQmlPrivate',
    'QSOperator',
    'QV4',
    'QmlIR',
    'icutils',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._alias_to_required_info import AliasToRequiredInfo
  from ._deferred_q_property_binding import DeferredQPropertyBinding
  from ._parser_status import ParserStatus
  from ._q_inherited_list_node import QInheritedListNode
  from ._q_intrusive_list_node import QIntrusiveListNode
  from ._q_j_s_list_for_in_iterator import QJSListForInIterator
  from ._q_j_s_list_for_of_iterator import QJSListForOfIterator
  from ._q_j_s_list_index_clamp import QJSListIndexClamp
  from ._q_j_s_number_coercion import QJSNumberCoercion
  from ._q_j_s_primitive_null import QJSPrimitiveNull
  from ._q_j_s_primitive_undefined import QJSPrimitiveUndefined
  from ._q_qml_component_and_alias_resolver_base import QQmlComponentAndAliasResolverBase
  from ._q_qml_enum_data import QQmlEnumData
  from ._q_qml_finalizer_hook import QQmlFinalizerHook
  from ._q_qml_import_ref import QQmlImportRef
  from ._q_qml_incubation_controller import QQmlIncubationController
  from ._q_qml_module_registration import QQmlModuleRegistration
  from ._q_qml_object_creator_shared_state import QQmlObjectCreatorSharedState
  from ._q_qml_parser_status import QQmlParserStatus
  from ._q_qml_profiler_definitions import QQmlProfilerDefinitions
  from ._q_qml_property_cache_method_arguments import QQmlPropertyCacheMethodArguments
  from ._q_qml_property_index import QQmlPropertyIndex
  from ._q_qml_ref_count import QQmlRefCount
  from ._q_qml_trivially_destructible_debugging_enabler import QQmlTriviallyDestructibleDebuggingEnabler
  from ._q_qml_type_loader_configured_data import QQmlTypeLoaderConfiguredData
  from ._q_qml_type_loader_network_access_manager_data import QQmlTypeLoaderNetworkAccessManagerData
  from ._q_qml_type_loader_shared_data import QQmlTypeLoaderSharedData
  from ._q_qml_type_loader_thread_data import QQmlTypeLoaderThreadData
  from ._q_qml_types_extension_interface import QQmlTypesExtensionInterface
  from ._q_qml_v_m_e import QQmlVME
  from ._q_recursion_node import QRecursionNode
  from ._qmltc_type_data import QmltcTypeData
  from ._required_properties import RequiredProperties
  from ._required_property_info import RequiredPropertyInfo
  from ._self_deletable import SelfDeletable
  from ._q_hashed_c_string_ref import QHashedCStringRef
  from ._q_qml_instantiation_interrupt import QQmlInstantiationInterrupt
  from ._q_qml_profiler_data import QQmlProfilerData
  from ._q_qml_list_meta_type_interface import QQmlListMetaTypeInterface
  from ._q_qml_meta_type_interface import QQmlMetaTypeInterface
  from ._q_qml_thread import QQmlThread
  from ._q_hashed_string import QHashedString
  from ._q_hashed_string_ref import QHashedStringRef
  from ._q_qml_debugging_enabler import QQmlDebuggingEnabler
  from ._q_qml_dir_parser import QQmlDirParser
  from ._q_qml_enum_value import QQmlEnumValue
  from ._q_qml_property_resolver import QQmlPropertyResolver
  from ._q_qml_signal_names import QQmlSignalNames
  from ._q_qml_source_location import QQmlSourceLocation
  from ._q_qml_translation import QQmlTranslation
  from ._q_qml_abstract_url_interceptor import QQmlAbstractUrlInterceptor
  from ._q_qml_binding_instantiation_context import QQmlBindingInstantiationContext
  from ._day_of_week_list import DayOfWeekList
  from ._q_abstract_animation_job import QAbstractAnimationJob
  from ._q_animation_job_change_listener import QAnimationJobChangeListener
  from ._q_bool_std_vector_foreign import QBoolStdVectorForeign
  from ._q_double_std_vector_foreign import QDoubleStdVectorForeign
  from ._q_float_std_vector_foreign import QFloatStdVectorForeign
  from ._q_int_std_vector_foreign import QIntStdVectorForeign
  from ._q_j_s_primitive_value import QJSPrimitiveValue
  from ._q_qml_abstract_profiler_adapter_factory import QQmlAbstractProfilerAdapterFactory
  from ._q_qml_any_string_view_foreign import QQmlAnyStringViewForeign
  from ._q_qml_application_private import QQmlApplicationPrivate
  from ._q_qml_bool_foreign import QQmlBoolForeign
  from ._q_qml_char_foreign import QQmlCharForeign
  from ._q_qml_color_provider import QQmlColorProvider
  from ._q_qml_component_attached import QQmlComponentAttached
  from ._q_qml_component_foreign import QQmlComponentForeign
  from ._q_qml_date_foreign import QQmlDateForeign
  from ._q_qml_debug_connector_factory import QQmlDebugConnectorFactory
  from ._q_qml_debug_server_connection_factory import QQmlDebugServerConnectionFactory
  from ._q_qml_debug_service_factory import QQmlDebugServiceFactory
  from ._q_qml_double_foreign import QQmlDoubleForeign
  from ._q_qml_easing import QQmlEasing
  from ._q_qml_error import QQmlError
  from ._q_qml_file_selector_private import QQmlFileSelectorPrivate
  from ._q_qml_float_foreign import QQmlFloatForeign
  from ._q_qml_guard_impl import QQmlGuardImpl
  from ._q_qml_gui_provider import QQmlGuiProvider
  from ._q_qml_image_provider_base import QQmlImageProviderBase
  from ._q_qml_incubator import QQmlIncubator
  from ._q_qml_info import QQmlInfo
  from ._q_qml_int16_t_foreign import QQmlInt16TForeign
  from ._q_qml_int32_t_foreign import QQmlInt32TForeign
  from ._q_qml_int64_t_foreign import QQmlInt64TForeign
  from ._q_qml_int8_t_foreign import QQmlInt8TForeign
  from ._q_qml_int_foreign import QQmlIntForeign
  from ._q_qml_locale_value_type import QQmlLocaleValueType
  from ._q_qml_logging_category_base import QQmlLoggingCategoryBase
  from ._q_qml_long_foreign import QQmlLongForeign
  from ._q_qml_margins_f_value_type import QQmlMarginsFValueType
  from ._q_qml_margins_value_type import QQmlMarginsValueType
  from ._q_qml_meta_object_pointer import QQmlMetaObjectPointer
  from ._q_qml_network_access_manager_factory import QQmlNetworkAccessManagerFactory
  from ._q_qml_null_foreign import QQmlNullForeign
  from ._q_qml_platform import QQmlPlatform
  from ._q_qml_point_f_value_type import QQmlPointFValueType
  from ._q_qml_point_value_type import QQmlPointValueType
  from ._q_qml_property_cache_creator_base import QQmlPropertyCacheCreatorBase
  from ._q_qml_property_data import QQmlPropertyData
  from ._q_qml_property_map import QQmlPropertyMap
  from ._q_qml_q_byte_array_foreign import QQmlQByteArrayForeign
  from ._q_qml_q_byte_array_list_foreign import QQmlQByteArrayListForeign
  from ._q_qml_q_char_foreign import QQmlQCharForeign
  from ._q_qml_q_date_foreign import QQmlQDateForeign
  from ._q_qml_q_j_s_value_foreign import QQmlQJSValueForeign
  from ._q_qml_q_json_array_foreign import QQmlQJsonArrayForeign
  from ._q_qml_q_json_object_foreign import QQmlQJsonObjectForeign
  from ._q_qml_q_json_value_foreign import QQmlQJsonValueForeign
  from ._q_qml_q_list_q_object_foreign import QQmlQListQObjectForeign
  from ._q_qml_q_object_list_foreign import QQmlQObjectListForeign
  from ._q_qml_q_real_foreign import QQmlQRealForeign
  from ._q_qml_q_string_list_foreign import QQmlQStringListForeign
  from ._q_qml_q_time_foreign import QQmlQTimeForeign
  from ._q_qml_q_variant_hash_foreign import QQmlQVariantHashForeign
  from ._q_qml_q_variant_list_foreign import QQmlQVariantListForeign
  from ._q_qml_q_variant_map_foreign import QQmlQVariantMapForeign
  from ._q_qml_qint16_foreign import QQmlQint16Foreign
  from ._q_qml_qint32_foreign import QQmlQint32Foreign
  from ._q_qml_qint64_foreign import QQmlQint64Foreign
  from ._q_qml_qint8_foreign import QQmlQint8Foreign
  from ._q_qml_qlonglong_foreign import QQmlQlonglongForeign
  from ._q_qml_qt_object_foreign import QQmlQtObjectForeign
  from ._q_qml_quint16_foreign import QQmlQuint16Foreign
  from ._q_qml_quint32_foreign import QQmlQuint32Foreign
  from ._q_qml_quint64_foreign import QQmlQuint64Foreign
  from ._q_qml_quint8_foreign import QQmlQuint8Foreign
  from ._q_qml_qulonglong_foreign import QQmlQulonglongForeign
  from ._q_qml_rect_f_value_type import QQmlRectFValueType
  from ._q_qml_rect_value_type import QQmlRectValueType
  from ._q_qml_regexp_foreign import QQmlRegexpForeign
  from ._q_qml_script_string_foreign import QQmlScriptStringForeign
  from ._q_qml_short_foreign import QQmlShortForeign
  from ._q_qml_size_f_value_type import QQmlSizeFValueType
  from ._q_qml_size_value_type import QQmlSizeValueType
  from ._q_qml_string_foreign import QQmlStringForeign
  from ._q_qml_type_not_available import QQmlTypeNotAvailable
  from ._q_qml_uchar_foreign import QQmlUcharForeign
  from ._q_qml_uint16_t_foreign import QQmlUint16TForeign
  from ._q_qml_uint32_t_foreign import QQmlUint32TForeign
  from ._q_qml_uint64_t_foreign import QQmlUint64TForeign
  from ._q_qml_uint8_t_foreign import QQmlUint8TForeign
  from ._q_qml_uint_foreign import QQmlUintForeign
  from ._q_qml_ulong_foreign import QQmlUlongForeign
  from ._q_qml_url_foreign import QQmlUrlForeign
  from ._q_qml_ushort_foreign import QQmlUshortForeign
  from ._q_qml_v4_execution_engine_ptr_foreign import QQmlV4ExecutionEnginePtrForeign
  from ._q_qml_v4_function_ptr_foreign import QQmlV4FunctionPtrForeign
  from ._q_qml_v_m_e_resolved_list import QQmlVMEResolvedList
  from ._q_qml_var_foreign import QQmlVarForeign
  from ._q_qml_void_foreign import QQmlVoidForeign
  from ._q_qmltc_object_creation_helper import QQmltcObjectCreationHelper
  from ._q_real_list_foreign import QRealListForeign
  from ._q_real_std_vector_foreign import QRealStdVectorForeign
  from ._q_string_hash_base import QStringHashBase
  from ._q_string_hash_node import QStringHashNode
  from ._q_string_std_vector_foreign import QStringStdVectorForeign
  from ._q_url_std_vector_foreign import QUrlStdVectorForeign
  from ._required_properties_and_target import RequiredPropertiesAndTarget
  from ._q_animation_group_job import QAnimationGroupJob
  from ._q_pause_animation_job import QPauseAnimationJob
  from ._q_qml_animation_timer import QQmlAnimationTimer
  from ._q_qml_application import QQmlApplication
  from ._q_qml_cpp_binding import QQmlCppBinding
  from ._q_qml_easing_value_type import QQmlEasingValueType
  from ._q_qml_file_selector_interceptor import QQmlFileSelectorInterceptor
  from ._q_qml_i_r_loader import QQmlIRLoader
  from ._q_qml_meta_object import QQmlMetaObject
  from ._q_qml_proxy_meta_object import QQmlProxyMetaObject
  from ._q_qml_translation_property_binding_functor_base import QQmlTranslationPropertyBindingFunctorBase
  from ._q_qml_type_loader_qmldir_content import QQmlTypeLoaderQmldirContent
  from ._q_qml_value_type import QQmlValueType
  from ._q_string_hash_data import QStringHashData
  from ._required_property_key import RequiredPropertyKey
  from ._q_continuing_animation_group_job import QContinuingAnimationGroupJob
  from ._q_parallel_animation_group_job import QParallelAnimationGroupJob
  from ._q_qml_object_or_gadget import QQmlObjectOrGadget
  from ._q_qml_property_binding_base import QQmlPropertyBindingBase
  from ._q_qml_translation_property_binding import QQmlTranslationPropertyBinding
  from ._q_qml_translation_property_binding_functor import QQmlTranslationPropertyBindingFunctor
  from ._q_qml_translation_property_translation_data_functor import QQmlTranslationPropertyTranslationDataFunctor
  from ._q_sequential_animation_group_job import QSequentialAnimationGroupJob
  from ._q_qml_open_meta_object_type import QQmlOpenMetaObjectType
  from ._q_qml_open_meta_object import QQmlOpenMetaObject
  from ._q_qml_type_loader import QQmlTypeLoader
  from ._q_qml_type import QQmlType
  from ._q_qml_context import QQmlContext
  from ._q_qml_context_data import QQmlContextData
  from ._q_qml_data_blob import QQmlDataBlob
  from ._q_qml_import_namespace import QQmlImportNamespace
  from ._q_qml_property import QQmlProperty
  from ._q_j_s_value import QJSValue
  from ._q_j_s_engine import QJSEngine
  from ._q_qml_engine import QQmlEngine
  from ._q_qml_abstract_binding import QQmlAbstractBinding
  from ._q_qml_component import QQmlComponent
  from ._q_qml_data import QQmlData
  from ._q_qml_import_instance import QQmlImportInstance
  from ._q_qml_imports import QQmlImports
  from ._q_qml_incubator_private import QQmlIncubatorPrivate
  from ._q_qml_type_name_cache import QQmlTypeNameCache
  from ._q_qml_type_private import QQmlTypePrivate
  from ._q_qml_meta_type import QQmlMetaType
  from ._q_j_s_engine_private import QJSEnginePrivate
  from ._q_qml_engine_private import QQmlEnginePrivate
  from ._q_j_s_managed_value import QJSManagedValue
  from ._q_qml_context_private import QQmlContextPrivate
  from ._q_qml_engine_extension_interface import QQmlEngineExtensionInterface
  from ._q_qml_extension_interface import QQmlExtensionInterface
  from ._q_qml_java_script_expression import QQmlJavaScriptExpression
  from ._q_qml_bound_signal_expression import QQmlBoundSignalExpression
  from ._q_qml_property_private import QQmlPropertyPrivate
  from ._q_qml_object_creator import QQmlObjectCreator
  from ._q_qml_notifier import QQmlNotifier
  from ._q_qml_notifier_endpoint import QQmlNotifierEndpoint
  from ._q_qml_profiler import QQmlProfiler
  from ._q_qml_component_private import QQmlComponentPrivate
  from ._q_qml_notifying_blob import QQmlNotifyingBlob
  from ._q_qml_script_blob import QQmlScriptBlob
  from ._q_qml_qmldir_data import QQmlQmldirData
  from ._q_qml_type_data import QQmlTypeData
  from ._load_helper import LoadHelper
  from ._object_in_creation_g_c_anchor_list import ObjectInCreationGCAnchorList
  from ._q_j_s_managed_value_private import QJSManagedValuePrivate
  from ._q_j_s_value_iterator import QJSValueIterator
  from ._q_j_s_value_iterator_private import QJSValueIteratorPrivate
  from ._q_j_s_value_private import QJSValuePrivate
  from ._q_property_change_trigger import QPropertyChangeTrigger
  from ._q_qml_application_engine import QQmlApplicationEngine
  from ._q_qml_application_engine_private import QQmlApplicationEnginePrivate
  from ._q_qml_bound_signal import QQmlBoundSignal
  from ._q_qml_custom_parser import QQmlCustomParser
  from ._q_qml_date_extension import QQmlDateExtension
  from ._q_qml_debug_service import QQmlDebugService
  from ._q_qml_debug_states_delegate import QQmlDebugStatesDelegate
  from ._q_qml_delayed_call_queue import QQmlDelayedCallQueue
  from ._q_qml_delayed_error import QQmlDelayedError
  from ._q_qml_engine_extension_plugin import QQmlEngineExtensionPlugin
  from ._q_qml_extension_plugin import QQmlExtensionPlugin
  from ._q_qml_file import QQmlFile
  from ._q_qml_file_selector import QQmlFileSelector
  from ._q_qml_gadget_ptr_wrapper import QQmlGadgetPtrWrapper
  from ._q_qml_guarded_context_data import QQmlGuardedContextData
  from ._q_qml_java_script_expression_guard import QQmlJavaScriptExpressionGuard
  from ._q_qml_list_reference import QQmlListReference
  from ._q_qml_locale import QQmlLocale
  from ._q_qml_notify_list import QQmlNotifyList
  from ._q_qml_number_extension import QQmlNumberExtension
  from ._q_qml_object_creation_profiler import QQmlObjectCreationProfiler
  from ._q_qml_object_creator_recursion_watcher import QQmlObjectCreatorRecursionWatcher
  from ._q_qml_plugin_importer import QQmlPluginImporter
  from ._q_qml_profiler_helper import QQmlProfilerHelper
  from ._q_qml_property_binding_j_s import QQmlPropertyBindingJS
  from ._q_qml_property_observer import QQmlPropertyObserver
  from ._q_qml_property_to_bindable_property_binding import QQmlPropertyToBindablePropertyBinding
  from ._q_qml_property_to_property_binding import QQmlPropertyToPropertyBinding
  from ._q_qml_property_to_unbindable_property_binding import QQmlPropertyToUnbindablePropertyBinding
  from ._q_qml_property_validator import QQmlPropertyValidator
  from ._q_qml_property_value_interceptor import QQmlPropertyValueInterceptor
  from ._q_qml_property_value_source import QQmlPropertyValueSource
  from ._q_qml_script_data import QQmlScriptData
  from ._q_qml_script_string import QQmlScriptString
  from ._q_qml_type_compiler import QQmlTypeCompiler
  from ._q_qml_type_loader_locked_data import QQmlTypeLoaderLockedData
  from ._q_qml_type_loader_network_reply_proxy import QQmlTypeLoaderNetworkReplyProxy
  from ._q_qml_type_loader_thread import QQmlTypeLoaderThread
  from ._q_qml_type_module import QQmlTypeModule
  from ._q_qml_v4_function import QQmlV4Function
  from ._q_qml_v_m_e_guard import QQmlVMEGuard
  from ._q_qml_value_type_provider import QQmlValueTypeProvider
  from ._q_qml_value_type_proxy_binding import QQmlValueTypeProxyBinding
  from ._q_qml_vme_profiler import QQmlVmeProfiler
  from ._q_v4_include import QV4Include
  from ._qt_object import QtObject
  from ._translation_binding_information import TranslationBindingInformation
  from ._q_debug_message_service import QDebugMessageService
  from ._q_qml_abstract_profiler_adapter import QQmlAbstractProfilerAdapter
  from ._q_qml_profiler_service import QQmlProfilerService
  from ._q_qml_any_binding import QQmlAnyBinding
  from ._q_qml_bindable_to_bindable_property_binding import QQmlBindableToBindablePropertyBinding
  from ._q_qml_bindable_to_unbindable_property_binding import QQmlBindableToUnbindablePropertyBinding
  from ._q_qml_binding_profiler import QQmlBindingProfiler
  from ._q_qml_compile_pass import QQmlCompilePass
  from ._q_qml_compiling_profiler import QQmlCompilingProfiler
  from ._q_qml_cpp_on_assignment_helper import QQmlCppOnAssignmentHelper
  from ._q_qml_debug_connector import QQmlDebugConnector
  from ._q_qml_debug_translation_service import QQmlDebugTranslationService
  from ._q_qml_engine_control_service import QQmlEngineControlService
  from ._q_qml_engine_debug_service import QQmlEngineDebugService
  from ._q_qml_expression import QQmlExpression
  from ._q_qml_expression_private import QQmlExpressionPrivate
  from ._q_qml_extension_plugin_private import QQmlExtensionPluginPrivate
  from ._q_qml_handling_signal_profiler import QQmlHandlingSignalProfiler
  from ._q_qml_interceptor_meta_object import QQmlInterceptorMetaObject
  from ._q_qml_list_reference_private import QQmlListReferencePrivate
  from ._q_qml_meta_type_data import QQmlMetaTypeData
  from ._q_qml_native_debug_service import QQmlNativeDebugService
  from ._q_qml_network_access_manager_factory_ptr import QQmlNetworkAccessManagerFactoryPtr
  from ._q_qml_object_completion_profiler import QQmlObjectCompletionProfiler
  from ._q_qml_property_binding_j_s_for_bound_function import QQmlPropertyBindingJSForBoundFunction
  from ._q_qml_script_string_private import QQmlScriptStringPrivate
  from ._q_qml_type_module_version import QQmlTypeModuleVersion
  from ._q_qml_unbindable_to_bindable_property_binding import QQmlUnbindableToBindablePropertyBinding
  from ._q_qml_unbindable_to_unbindable_property_binding import QQmlUnbindableToUnbindablePropertyBinding
  from ._q_quick_event_replay_service import QQuickEventReplayService
  from ._q_v4_debug_service import QV4DebugService
  from ._trigger_list import TriggerList
  from ._q_qml_alias_annotator import QQmlAliasAnnotator
  from ._q_qml_binding import QQmlBinding
  from ._q_qml_custom_parser_script_indexer import QQmlCustomParserScriptIndexer
  from ._q_qml_debug_server import QQmlDebugServer
  from ._q_qml_deferred_and_custom_parser_binding_scanner import QQmlDeferredAndCustomParserBindingScanner
  from ._q_qml_enum_type_resolver import QQmlEnumTypeResolver
  from ._q_qml_inspector_service import QQmlInspectorService
  from ._q_qml_property_binding import QQmlPropertyBinding
  from ._q_qml_script_string_scanner import QQmlScriptStringScanner
  from ._q_qml_v_m_e_meta_object import QQmlVMEMetaObject
  from ._signal_handler_resolver import SignalHandlerResolver
  from ._q_qml_debug_server_connection import QQmlDebugServerConnection
  from ._q_qml_property_cache import QQmlPropertyCache
  from ._q_qml_v_m_e_variant_q_object_ptr import QQmlVMEVariantQObjectPtr
  from ._q_qml_property_cache_vector import QQmlPropertyCacheVector
  from ._q_qml_property_capture import QQmlPropertyCapture
  from ._q_qml_pending_group_property_bindings import QQmlPendingGroupPropertyBindings
  from ._q_qml_property import QQmlProperties
  from ._q_j_s_value import QJSValueList
  from . import OverrideSemantics
  from . import QQml
  from . import QQmlDebugTranslation
  from . import QQmlImport
  from . import QQmlJS
  from . import QQmlPrivate
  from . import QSOperator
  from . import QV4
  from . import QmlIR
  from . import icutils
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'AliasToRequiredInfo': '_alias_to_required_info',
      'DeferredQPropertyBinding': '_deferred_q_property_binding',
      'ParserStatus': '_parser_status',
      'QInheritedListNode': '_q_inherited_list_node',
      'QIntrusiveListNode': '_q_intrusive_list_node',
      'QJSListForInIterator': '_q_j_s_list_for_in_iterator',
      'QJSListForOfIterator': '_q_j_s_list_for_of_iterator',
      'QJSListIndexClamp': '_q_j_s_list_index_clamp',
      'QJSNumberCoercion': '_q_j_s_number_coercion',
      'QJSPrimitiveNull': '_q_j_s_primitive_null',
      'QJSPrimitiveUndefined': '_q_j_s_primitive_undefined',
      'QQmlComponentAndAliasResolverBase': '_q_qml_component_and_alias_resolver_base',
      'QQmlEnumData': '_q_qml_enum_data',
      'QQmlFinalizerHook': '_q_qml_finalizer_hook',
      'QQmlImportRef': '_q_qml_import_ref',
      'QQmlIncubationController': '_q_qml_incubation_controller',
      'QQmlModuleRegistration': '_q_qml_module_registration',
      'QQmlObjectCreatorSharedState': '_q_qml_object_creator_shared_state',
      'QQmlParserStatus': '_q_qml_parser_status',
      'QQmlProfilerDefinitions': '_q_qml_profiler_definitions',
      'QQmlPropertyCacheMethodArguments': '_q_qml_property_cache_method_arguments',
      'QQmlPropertyIndex': '_q_qml_property_index',
      'QQmlRefCount': '_q_qml_ref_count',
      'QQmlTriviallyDestructibleDebuggingEnabler': '_q_qml_trivially_destructible_debugging_enabler',
      'QQmlTypeLoaderConfiguredData': '_q_qml_type_loader_configured_data',
      'QQmlTypeLoaderNetworkAccessManagerData': '_q_qml_type_loader_network_access_manager_data',
      'QQmlTypeLoaderSharedData': '_q_qml_type_loader_shared_data',
      'QQmlTypeLoaderThreadData': '_q_qml_type_loader_thread_data',
      'QQmlTypesExtensionInterface': '_q_qml_types_extension_interface',
      'QQmlVME': '_q_qml_v_m_e',
      'QRecursionNode': '_q_recursion_node',
      'QmltcTypeData': '_qmltc_type_data',
      'RequiredProperties': '_required_properties',
      'RequiredPropertyInfo': '_required_property_info',
      'SelfDeletable': '_self_deletable',
      'QHashedCStringRef': '_q_hashed_c_string_ref',
      'QQmlInstantiationInterrupt': '_q_qml_instantiation_interrupt',
      'QQmlProfilerData': '_q_qml_profiler_data',
      'QQmlListMetaTypeInterface': '_q_qml_list_meta_type_interface',
      'QQmlMetaTypeInterface': '_q_qml_meta_type_interface',
      'QQmlThread': '_q_qml_thread',
      'QHashedString': '_q_hashed_string',
      'QHashedStringRef': '_q_hashed_string_ref',
      'QQmlDebuggingEnabler': '_q_qml_debugging_enabler',
      'QQmlDirParser': '_q_qml_dir_parser',
      'QQmlEnumValue': '_q_qml_enum_value',
      'QQmlPropertyResolver': '_q_qml_property_resolver',
      'QQmlSignalNames': '_q_qml_signal_names',
      'QQmlSourceLocation': '_q_qml_source_location',
      'QQmlTranslation': '_q_qml_translation',
      'QQmlAbstractUrlInterceptor': '_q_qml_abstract_url_interceptor',
      'QQmlBindingInstantiationContext': '_q_qml_binding_instantiation_context',
      'DayOfWeekList': '_day_of_week_list',
      'QAbstractAnimationJob': '_q_abstract_animation_job',
      'QAnimationJobChangeListener': '_q_animation_job_change_listener',
      'QBoolStdVectorForeign': '_q_bool_std_vector_foreign',
      'QDoubleStdVectorForeign': '_q_double_std_vector_foreign',
      'QFloatStdVectorForeign': '_q_float_std_vector_foreign',
      'QIntStdVectorForeign': '_q_int_std_vector_foreign',
      'QJSPrimitiveValue': '_q_j_s_primitive_value',
      'QQmlAbstractProfilerAdapterFactory': '_q_qml_abstract_profiler_adapter_factory',
      'QQmlAnyStringViewForeign': '_q_qml_any_string_view_foreign',
      'QQmlApplicationPrivate': '_q_qml_application_private',
      'QQmlBoolForeign': '_q_qml_bool_foreign',
      'QQmlCharForeign': '_q_qml_char_foreign',
      'QQmlColorProvider': '_q_qml_color_provider',
      'QQmlComponentAttached': '_q_qml_component_attached',
      'QQmlComponentForeign': '_q_qml_component_foreign',
      'QQmlDateForeign': '_q_qml_date_foreign',
      'QQmlDebugConnectorFactory': '_q_qml_debug_connector_factory',
      'QQmlDebugServerConnectionFactory': '_q_qml_debug_server_connection_factory',
      'QQmlDebugServiceFactory': '_q_qml_debug_service_factory',
      'QQmlDoubleForeign': '_q_qml_double_foreign',
      'QQmlEasing': '_q_qml_easing',
      'QQmlError': '_q_qml_error',
      'QQmlFileSelectorPrivate': '_q_qml_file_selector_private',
      'QQmlFloatForeign': '_q_qml_float_foreign',
      'QQmlGuardImpl': '_q_qml_guard_impl',
      'QQmlGuiProvider': '_q_qml_gui_provider',
      'QQmlImageProviderBase': '_q_qml_image_provider_base',
      'QQmlIncubator': '_q_qml_incubator',
      'QQmlInfo': '_q_qml_info',
      'QQmlInt16TForeign': '_q_qml_int16_t_foreign',
      'QQmlInt32TForeign': '_q_qml_int32_t_foreign',
      'QQmlInt64TForeign': '_q_qml_int64_t_foreign',
      'QQmlInt8TForeign': '_q_qml_int8_t_foreign',
      'QQmlIntForeign': '_q_qml_int_foreign',
      'QQmlLocaleValueType': '_q_qml_locale_value_type',
      'QQmlLoggingCategoryBase': '_q_qml_logging_category_base',
      'QQmlLongForeign': '_q_qml_long_foreign',
      'QQmlMarginsFValueType': '_q_qml_margins_f_value_type',
      'QQmlMarginsValueType': '_q_qml_margins_value_type',
      'QQmlMetaObjectPointer': '_q_qml_meta_object_pointer',
      'QQmlNetworkAccessManagerFactory': '_q_qml_network_access_manager_factory',
      'QQmlNullForeign': '_q_qml_null_foreign',
      'QQmlPlatform': '_q_qml_platform',
      'QQmlPointFValueType': '_q_qml_point_f_value_type',
      'QQmlPointValueType': '_q_qml_point_value_type',
      'QQmlPropertyCacheCreatorBase': '_q_qml_property_cache_creator_base',
      'QQmlPropertyData': '_q_qml_property_data',
      'QQmlPropertyMap': '_q_qml_property_map',
      'QQmlQByteArrayForeign': '_q_qml_q_byte_array_foreign',
      'QQmlQByteArrayListForeign': '_q_qml_q_byte_array_list_foreign',
      'QQmlQCharForeign': '_q_qml_q_char_foreign',
      'QQmlQDateForeign': '_q_qml_q_date_foreign',
      'QQmlQJSValueForeign': '_q_qml_q_j_s_value_foreign',
      'QQmlQJsonArrayForeign': '_q_qml_q_json_array_foreign',
      'QQmlQJsonObjectForeign': '_q_qml_q_json_object_foreign',
      'QQmlQJsonValueForeign': '_q_qml_q_json_value_foreign',
      'QQmlQListQObjectForeign': '_q_qml_q_list_q_object_foreign',
      'QQmlQObjectListForeign': '_q_qml_q_object_list_foreign',
      'QQmlQRealForeign': '_q_qml_q_real_foreign',
      'QQmlQStringListForeign': '_q_qml_q_string_list_foreign',
      'QQmlQTimeForeign': '_q_qml_q_time_foreign',
      'QQmlQVariantHashForeign': '_q_qml_q_variant_hash_foreign',
      'QQmlQVariantListForeign': '_q_qml_q_variant_list_foreign',
      'QQmlQVariantMapForeign': '_q_qml_q_variant_map_foreign',
      'QQmlQint16Foreign': '_q_qml_qint16_foreign',
      'QQmlQint32Foreign': '_q_qml_qint32_foreign',
      'QQmlQint64Foreign': '_q_qml_qint64_foreign',
      'QQmlQint8Foreign': '_q_qml_qint8_foreign',
      'QQmlQlonglongForeign': '_q_qml_qlonglong_foreign',
      'QQmlQtObjectForeign': '_q_qml_qt_object_foreign',
      'QQmlQuint16Foreign': '_q_qml_quint16_foreign',
      'QQmlQuint32Foreign': '_q_qml_quint32_foreign',
      'QQmlQuint64Foreign': '_q_qml_quint64_foreign',
      'QQmlQuint8Foreign': '_q_qml_quint8_foreign',
      'QQmlQulonglongForeign': '_q_qml_qulonglong_foreign',
      'QQmlRectFValueType': '_q_qml_rect_f_value_type',
      'QQmlRectValueType': '_q_qml_rect_value_type',
      'QQmlRegexpForeign': '_q_qml_regexp_foreign',
      'QQmlScriptStringForeign': '_q_qml_script_string_foreign',
      'QQmlShortForeign': '_q_qml_short_foreign',
      'QQmlSizeFValueType': '_q_qml_size_f_value_type',
      'QQmlSizeValueType': '_q_qml_size_value_type',
      'QQmlStringForeign': '_q_qml_string_foreign',
      'QQmlTypeNotAvailable': '_q_qml_type_not_available',
      'QQmlUcharForeign': '_q_qml_uchar_foreign',
      'QQmlUint16TForeign': '_q_qml_uint16_t_foreign',
      'QQmlUint32TForeign': '_q_qml_uint32_t_foreign',
      'QQmlUint64TForeign': '_q_qml_uint64_t_foreign',
      'QQmlUint8TForeign': '_q_qml_uint8_t_foreign',
      'QQmlUintForeign': '_q_qml_uint_foreign',
      'QQmlUlongForeign': '_q_qml_ulong_foreign',
      'QQmlUrlForeign': '_q_qml_url_foreign',
      'QQmlUshortForeign': '_q_qml_ushort_foreign',
      'QQmlV4ExecutionEnginePtrForeign': '_q_qml_v4_execution_engine_ptr_foreign',
      'QQmlV4FunctionPtrForeign': '_q_qml_v4_function_ptr_foreign',
      'QQmlVMEResolvedList': '_q_qml_v_m_e_resolved_list',
      'QQmlVarForeign': '_q_qml_var_foreign',
      'QQmlVoidForeign': '_q_qml_void_foreign',
      'QQmltcObjectCreationHelper': '_q_qmltc_object_creation_helper',
      'QRealListForeign': '_q_real_list_foreign',
      'QRealStdVectorForeign': '_q_real_std_vector_foreign',
      'QStringHashBase': '_q_string_hash_base',
      'QStringHashNode': '_q_string_hash_node',
      'QStringStdVectorForeign': '_q_string_std_vector_foreign',
      'QUrlStdVectorForeign': '_q_url_std_vector_foreign',
      'RequiredPropertiesAndTarget': '_required_properties_and_target',
      'QAnimationGroupJob': '_q_animation_group_job',
      'QPauseAnimationJob': '_q_pause_animation_job',
      'QQmlAnimationTimer': '_q_qml_animation_timer',
      'QQmlApplication': '_q_qml_application',
      'QQmlCppBinding': '_q_qml_cpp_binding',
      'QQmlEasingValueType': '_q_qml_easing_value_type',
      'QQmlFileSelectorInterceptor': '_q_qml_file_selector_interceptor',
      'QQmlIRLoader': '_q_qml_i_r_loader',
      'QQmlMetaObject': '_q_qml_meta_object',
      'QQmlProxyMetaObject': '_q_qml_proxy_meta_object',
      'QQmlTranslationPropertyBindingFunctorBase': '_q_qml_translation_property_binding_functor_base',
      'QQmlTypeLoaderQmldirContent': '_q_qml_type_loader_qmldir_content',
      'QQmlValueType': '_q_qml_value_type',
      'QStringHashData': '_q_string_hash_data',
      'RequiredPropertyKey': '_required_property_key',
      'QContinuingAnimationGroupJob': '_q_continuing_animation_group_job',
      'QParallelAnimationGroupJob': '_q_parallel_animation_group_job',
      'QQmlObjectOrGadget': '_q_qml_object_or_gadget',
      'QQmlPropertyBindingBase': '_q_qml_property_binding_base',
      'QQmlTranslationPropertyBinding': '_q_qml_translation_property_binding',
      'QQmlTranslationPropertyBindingFunctor': '_q_qml_translation_property_binding_functor',
      'QQmlTranslationPropertyTranslationDataFunctor': '_q_qml_translation_property_translation_data_functor',
      'QSequentialAnimationGroupJob': '_q_sequential_animation_group_job',
      'QQmlOpenMetaObjectType': '_q_qml_open_meta_object_type',
      'QQmlOpenMetaObject': '_q_qml_open_meta_object',
      'QQmlTypeLoader': '_q_qml_type_loader',
      'QQmlType': '_q_qml_type',
      'QQmlContext': '_q_qml_context',
      'QQmlContextData': '_q_qml_context_data',
      'QQmlDataBlob': '_q_qml_data_blob',
      'QQmlImportNamespace': '_q_qml_import_namespace',
      'QQmlProperty': '_q_qml_property',
      'QJSValue': '_q_j_s_value',
      'QJSEngine': '_q_j_s_engine',
      'QQmlEngine': '_q_qml_engine',
      'QQmlAbstractBinding': '_q_qml_abstract_binding',
      'QQmlComponent': '_q_qml_component',
      'QQmlData': '_q_qml_data',
      'QQmlImportInstance': '_q_qml_import_instance',
      'QQmlImports': '_q_qml_imports',
      'QQmlIncubatorPrivate': '_q_qml_incubator_private',
      'QQmlTypeNameCache': '_q_qml_type_name_cache',
      'QQmlTypePrivate': '_q_qml_type_private',
      'QQmlMetaType': '_q_qml_meta_type',
      'QJSEnginePrivate': '_q_j_s_engine_private',
      'QQmlEnginePrivate': '_q_qml_engine_private',
      'QJSManagedValue': '_q_j_s_managed_value',
      'QQmlContextPrivate': '_q_qml_context_private',
      'QQmlEngineExtensionInterface': '_q_qml_engine_extension_interface',
      'QQmlExtensionInterface': '_q_qml_extension_interface',
      'QQmlJavaScriptExpression': '_q_qml_java_script_expression',
      'QQmlBoundSignalExpression': '_q_qml_bound_signal_expression',
      'QQmlPropertyPrivate': '_q_qml_property_private',
      'QQmlObjectCreator': '_q_qml_object_creator',
      'QQmlNotifier': '_q_qml_notifier',
      'QQmlNotifierEndpoint': '_q_qml_notifier_endpoint',
      'QQmlProfiler': '_q_qml_profiler',
      'QQmlComponentPrivate': '_q_qml_component_private',
      'QQmlNotifyingBlob': '_q_qml_notifying_blob',
      'QQmlScriptBlob': '_q_qml_script_blob',
      'QQmlQmldirData': '_q_qml_qmldir_data',
      'QQmlTypeData': '_q_qml_type_data',
      'LoadHelper': '_load_helper',
      'ObjectInCreationGCAnchorList': '_object_in_creation_g_c_anchor_list',
      'QJSManagedValuePrivate': '_q_j_s_managed_value_private',
      'QJSValueIterator': '_q_j_s_value_iterator',
      'QJSValueIteratorPrivate': '_q_j_s_value_iterator_private',
      'QJSValuePrivate': '_q_j_s_value_private',
      'QPropertyChangeTrigger': '_q_property_change_trigger',
      'QQmlApplicationEngine': '_q_qml_application_engine',
      'QQmlApplicationEnginePrivate': '_q_qml_application_engine_private',
      'QQmlBoundSignal': '_q_qml_bound_signal',
      'QQmlCustomParser': '_q_qml_custom_parser',
      'QQmlDateExtension': '_q_qml_date_extension',
      'QQmlDebugService': '_q_qml_debug_service',
      'QQmlDebugStatesDelegate': '_q_qml_debug_states_delegate',
      'QQmlDelayedCallQueue': '_q_qml_delayed_call_queue',
      'QQmlDelayedError': '_q_qml_delayed_error',
      'QQmlEngineExtensionPlugin': '_q_qml_engine_extension_plugin',
      'QQmlExtensionPlugin': '_q_qml_extension_plugin',
      'QQmlFile': '_q_qml_file',
      'QQmlFileSelector': '_q_qml_file_selector',
      'QQmlGadgetPtrWrapper': '_q_qml_gadget_ptr_wrapper',
      'QQmlGuardedContextData': '_q_qml_guarded_context_data',
      'QQmlJavaScriptExpressionGuard': '_q_qml_java_script_expression_guard',
      'QQmlListReference': '_q_qml_list_reference',
      'QQmlLocale': '_q_qml_locale',
      'QQmlNotifyList': '_q_qml_notify_list',
      'QQmlNumberExtension': '_q_qml_number_extension',
      'QQmlObjectCreationProfiler': '_q_qml_object_creation_profiler',
      'QQmlObjectCreatorRecursionWatcher': '_q_qml_object_creator_recursion_watcher',
      'QQmlPluginImporter': '_q_qml_plugin_importer',
      'QQmlProfilerHelper': '_q_qml_profiler_helper',
      'QQmlPropertyBindingJS': '_q_qml_property_binding_j_s',
      'QQmlPropertyObserver': '_q_qml_property_observer',
      'QQmlPropertyToBindablePropertyBinding': '_q_qml_property_to_bindable_property_binding',
      'QQmlPropertyToPropertyBinding': '_q_qml_property_to_property_binding',
      'QQmlPropertyToUnbindablePropertyBinding': '_q_qml_property_to_unbindable_property_binding',
      'QQmlPropertyValidator': '_q_qml_property_validator',
      'QQmlPropertyValueInterceptor': '_q_qml_property_value_interceptor',
      'QQmlPropertyValueSource': '_q_qml_property_value_source',
      'QQmlScriptData': '_q_qml_script_data',
      'QQmlScriptString': '_q_qml_script_string',
      'QQmlTypeCompiler': '_q_qml_type_compiler',
      'QQmlTypeLoaderLockedData': '_q_qml_type_loader_locked_data',
      'QQmlTypeLoaderNetworkReplyProxy': '_q_qml_type_loader_network_reply_proxy',
      'QQmlTypeLoaderThread': '_q_qml_type_loader_thread',
      'QQmlTypeModule': '_q_qml_type_module',
      'QQmlV4Function': '_q_qml_v4_function',
      'QQmlVMEGuard': '_q_qml_v_m_e_guard',
      'QQmlValueTypeProvider': '_q_qml_value_type_provider',
      'QQmlValueTypeProxyBinding': '_q_qml_value_type_proxy_binding',
      'QQmlVmeProfiler': '_q_qml_vme_profiler',
      'QV4Include': '_q_v4_include',
      'QtObject': '_qt_object',
      'TranslationBindingInformation': '_translation_binding_information',
      'QDebugMessageService': '_q_debug_message_service',
      'QQmlAbstractProfilerAdapter': '_q_qml_abstract_profiler_adapter',
      'QQmlProfilerService': '_q_qml_profiler_service',
      'QQmlAnyBinding': '_q_qml_any_binding',
      'QQmlBindableToBindablePropertyBinding': '_q_qml_bindable_to_bindable_property_binding',
      'QQmlBindableToUnbindablePropertyBinding': '_q_qml_bindable_to_unbindable_property_binding',
      'QQmlBindingProfiler': '_q_qml_binding_profiler',
      'QQmlCompilePass': '_q_qml_compile_pass',
      'QQmlCompilingProfiler': '_q_qml_compiling_profiler',
      'QQmlCppOnAssignmentHelper': '_q_qml_cpp_on_assignment_helper',
      'QQmlDebugConnector': '_q_qml_debug_connector',
      'QQmlDebugTranslationService': '_q_qml_debug_translation_service',
      'QQmlEngineControlService': '_q_qml_engine_control_service',
      'QQmlEngineDebugService': '_q_qml_engine_debug_service',
      'QQmlExpression': '_q_qml_expression',
      'QQmlExpressionPrivate': '_q_qml_expression_private',
      'QQmlExtensionPluginPrivate': '_q_qml_extension_plugin_private',
      'QQmlHandlingSignalProfiler': '_q_qml_handling_signal_profiler',
      'QQmlInterceptorMetaObject': '_q_qml_interceptor_meta_object',
      'QQmlListReferencePrivate': '_q_qml_list_reference_private',
      'QQmlMetaTypeData': '_q_qml_meta_type_data',
      'QQmlNativeDebugService': '_q_qml_native_debug_service',
      'QQmlNetworkAccessManagerFactoryPtr': '_q_qml_network_access_manager_factory_ptr',
      'QQmlObjectCompletionProfiler': '_q_qml_object_completion_profiler',
      'QQmlPropertyBindingJSForBoundFunction': '_q_qml_property_binding_j_s_for_bound_function',
      'QQmlScriptStringPrivate': '_q_qml_script_string_private',
      'QQmlTypeModuleVersion': '_q_qml_type_module_version',
      'QQmlUnbindableToBindablePropertyBinding': '_q_qml_unbindable_to_bindable_property_binding',
      'QQmlUnbindableToUnbindablePropertyBinding': '_q_qml_unbindable_to_unbindable_property_binding',
      'QQuickEventReplayService': '_q_quick_event_replay_service',
      'QV4DebugService': '_q_v4_debug_service',
      'TriggerList': '_trigger_list',
      'QQmlAliasAnnotator': '_q_qml_alias_annotator',
      'QQmlBinding': '_q_qml_binding',
      'QQmlCustomParserScriptIndexer': '_q_qml_custom_parser_script_indexer',
      'QQmlDebugServer': '_q_qml_debug_server',
      'QQmlDeferredAndCustomParserBindingScanner': '_q_qml_deferred_and_custom_parser_binding_scanner',
      'QQmlEnumTypeResolver': '_q_qml_enum_type_resolver',
      'QQmlInspectorService': '_q_qml_inspector_service',
      'QQmlPropertyBinding': '_q_qml_property_binding',
      'QQmlScriptStringScanner': '_q_qml_script_string_scanner',
      'QQmlVMEMetaObject': '_q_qml_v_m_e_meta_object',
      'SignalHandlerResolver': '_signal_handler_resolver',
      'QQmlDebugServerConnection': '_q_qml_debug_server_connection',
      'QQmlPropertyCache': '_q_qml_property_cache',
      'QQmlVMEVariantQObjectPtr': '_q_qml_v_m_e_variant_q_object_ptr',
      'QQmlPropertyCacheVector': '_q_qml_property_cache_vector',
      'QQmlPropertyCapture': '_q_qml_property_capture',
      'QQmlPendingGroupPropertyBindings': '_q_qml_pending_group_property_bindings',
      'QQmlProperties': '_q_qml_property',
      'QJSValueList': '_q_j_s_value',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('OverrideSemantics', 'QQml', 'QQmlDebugTranslation', 'QQmlImport', 'QQmlJS', 'QQmlPrivate', 'QSOperator', 'QV4', 'QmlIR', 'icutils',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQml import QJSValueList'. Python calls
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
