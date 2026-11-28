"""
The namespace 'QV4::Heap' of Qt, a package of 'cutienator.QtQml':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQml import QV4
  QV4.Heap.ArgumentsObjectData

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
    'ArgumentsObjectData',
    'ArgumentsObjectOffsetStruct',
    'ArrayDataData',
    'ArrayDataOffsetStruct',
    'ArrayIteratorObjectData',
    'ArrayIteratorObjectOffsetStruct',
    'BoundFunctionData',
    'BoundFunctionOffsetStruct',
    'CallContextData',
    'CallContextOffsetStruct',
    'CapabilitiesExecutorWrapperData',
    'CapabilitiesExecutorWrapperOffsetStruct',
    'ConstructorFunctionData',
    'ConstructorFunctionOffsetStruct',
    'DataViewData',
    'DataViewOffsetStruct',
    'DateObjectData',
    'DateObjectOffsetStruct',
    'DefaultClassConstructorFunctionData',
    'DefaultClassConstructorFunctionOffsetStruct',
    'DynamicFunctionObjectData',
    'DynamicFunctionObjectOffsetStruct',
    'ErrorObjectData',
    'ErrorObjectOffsetStruct',
    'ExecutionContextData',
    'ExecutionContextOffsetStruct',
    'ForInIteratorObjectData',
    'ForInIteratorObjectOffsetStruct',
    'FunctionObjectData',
    'FunctionObjectOffsetStruct',
    'GeneratorObjectData',
    'GeneratorObjectOffsetStruct',
    'JavaScriptFunctionObjectData',
    'JavaScriptFunctionObjectOffsetStruct',
    'MapIteratorObjectData',
    'MapIteratorObjectOffsetStruct',
    'MemberDataData',
    'MemberDataOffsetStruct',
    'MemberFunctionData',
    'MemberFunctionOffsetStruct',
    'ModuleData',
    'ModuleOffsetStruct',
    'ObjectData',
    'ObjectOffsetStruct',
    'PromiseCapabilityData',
    'PromiseCapabilityOffsetStruct',
    'PromiseExecutionStateData',
    'PromiseExecutionStateOffsetStruct',
    'PromiseObjectData',
    'PromiseObjectOffsetStruct',
    'PromiseReactionData',
    'PromiseReactionOffsetStruct',
    'ProxyData',
    'ProxyObjectData',
    'ProxyObjectOffsetStruct',
    'ProxyOffsetStruct',
    'QObjectMethodData',
    'QObjectMethodOffsetStruct',
    'QQmlBindingFunctionData',
    'QQmlBindingFunctionOffsetStruct',
    'QQmlContextWrapperData',
    'QQmlContextWrapperOffsetStruct',
    'QQmlValueTypeWrapperData',
    'QQmlValueTypeWrapperOffsetStruct',
    'QmlContextData',
    'QmlContextOffsetStruct',
    'ReferenceObjectData',
    'ReferenceObjectOffsetStruct',
    'RegExpCtorData',
    'RegExpCtorOffsetStruct',
    'RegExpObjectData',
    'RegExpObjectOffsetStruct',
    'RejectWrapperData',
    'RejectWrapperOffsetStruct',
    'ResolveElementWrapperData',
    'ResolveElementWrapperOffsetStruct',
    'ResolveWrapperData',
    'ResolveWrapperOffsetStruct',
    'ScriptFunctionData',
    'ScriptFunctionOffsetStruct',
    'SetIteratorObjectData',
    'SetIteratorObjectOffsetStruct',
    'StrictArgumentsObjectData',
    'StrictArgumentsObjectOffsetStruct',
    'StringIteratorObjectData',
    'StringIteratorObjectOffsetStruct',
    'StringObjectData',
    'StringObjectOffsetStruct',
    'SymbolObjectData',
    'SymbolObjectOffsetStruct',
    'TypedArrayData',
    'TypedArrayOffsetStruct',
    'UrlObjectData',
    'UrlObjectOffsetStruct',
    'UrlSearchParamsObjectData',
    'UrlSearchParamsObjectOffsetStruct',
    'VariantAssociationObjectData',
    'VariantAssociationObjectOffsetStruct',
    'Base',
    'ArrayData',
    'ArrayDataSizeStruct',
    'ExecutionContext',
    'ExecutionContextSizeStruct',
    'MemberData',
    'MemberDataSizeStruct',
    'Object',
    'ObjectSizeStruct',
    'StringOrSymbol',
    'ArgumentsObject',
    'ArgumentsObjectSizeStruct',
    'ArrayIteratorObjectSizeStruct',
    'ArrayObject',
    'Atomics',
    'BooleanObject',
    'CallContext',
    'CallContextSizeStruct',
    'ConsoleObject',
    'DataView',
    'DataViewSizeStruct',
    'ErrorObject',
    'ErrorObjectSizeStruct',
    'ForInIteratorObjectSizeStruct',
    'FunctionObjectSizeStruct',
    'GeneratorObject',
    'GeneratorObjectSizeStruct',
    'IntrinsicTypedArrayPrototype',
    'JsonObject',
    'MapIteratorObjectSizeStruct',
    'MapObject',
    'MathObject',
    'Module',
    'ModuleSizeStruct',
    'NumberObject',
    'PromiseCapability',
    'PromiseCapabilitySizeStruct',
    'PromiseObjectSizeStruct',
    'PromiseReactionSizeStruct',
    'QQmlContextWrapperSizeStruct',
    'QQmlEnumWrapper',
    'QmlContextSizeStruct',
    'ReferenceObjectSizeStruct',
    'Reflect',
    'RegExpObject',
    'RegExpObjectSizeStruct',
    'SetIteratorObjectSizeStruct',
    'SetObject',
    'SharedArrayBuffer',
    'SimpleArrayData',
    'SparseArrayData',
    'StrictArgumentsObject',
    'StrictArgumentsObjectSizeStruct',
    'String',
    'StringIteratorObjectSizeStruct',
    'StringObjectSizeStruct',
    'Symbol',
    'SymbolObjectSizeStruct',
    'TypedArray',
    'TypedArrayPrototype',
    'TypedArraySizeStruct',
    'UrlObject',
    'UrlObjectSizeStruct',
    'UrlSearchParamsObject',
    'UrlSearchParamsObjectSizeStruct',
    'ArrayBuffer',
    'ComplexString',
    'EvalErrorObject',
    'QObjectWrapper',
    'QmlListWrapper',
    'QmlSignalHandler',
    'RangeErrorObject',
    'ReferenceErrorObject',
    'StringObject',
    'SymbolObject',
    'SyntaxErrorObject',
    'TypeErrorObject',
    'URIErrorObject',
    'VariantObject',
    'PromiseObject',
    'ArrayIteratorObject',
    'ForInIteratorObject',
    'FunctionObject',
    'InternalClass',
    'MapIteratorObject',
    'PromiseReaction',
    'QQmlContextWrapper',
    'ReferenceObject',
    'ReferenceObjectEndpoint',
    'SetIteratorObject',
    'StringIteratorObject',
    'ArrayCtor',
    'BooleanCtor',
    'CapabilitiesExecutorWrapper',
    'CapabilitiesExecutorWrapperSizeStruct',
    'DataViewCtor',
    'DateCtor',
    'DateObject',
    'DateObjectSizeStruct',
    'DefaultClassConstructorFunction',
    'DefaultClassConstructorFunctionSizeStruct',
    'DynamicFunctionObject',
    'DynamicFunctionObjectSizeStruct',
    'ErrorCtor',
    'EvalFunction',
    'FunctionCtor',
    'FunctionPrototype',
    'GeneratorFunctionCtor',
    'GeneratorPrototype',
    'IntrinsicTypedArrayCtor',
    'JavaScriptFunctionObject',
    'JavaScriptFunctionObjectSizeStruct',
    'NumberCtor',
    'ObjectCtor',
    'PromiseCtor',
    'PromiseExecutionState',
    'PromiseExecutionStateSizeStruct',
    'Proxy',
    'ProxyObject',
    'ProxyObjectSizeStruct',
    'ProxySizeStruct',
    'QMetaObjectWrapper',
    'QObjectMethod',
    'QObjectMethodSizeStruct',
    'QQmlTypeWrapper',
    'QQmlValueTypeWrapper',
    'QQmlValueTypeWrapperSizeStruct',
    'QmlContext',
    'RegExpCtor',
    'RegExpCtorSizeStruct',
    'RejectWrapper',
    'RejectWrapperSizeStruct',
    'ResolveElementWrapper',
    'ResolveElementWrapperSizeStruct',
    'ResolveWrapper',
    'ResolveWrapperSizeStruct',
    'Sequence',
    'SharedArrayBufferCtor',
    'StringCtor',
    'SymbolCtor',
    'TypedArrayCtor',
    'UrlCtor',
    'UrlSearchParamsCtor',
    'VariantAssociationObject',
    'VariantAssociationObjectSizeStruct',
    'WeakMapCtor',
    'WeakSetCtor',
    'ArrayBufferCtor',
    'ArrowFunction',
    'BoundFunction',
    'BoundFunctionSizeStruct',
    'EvalErrorCtor',
    'IndexedBuiltinFunction',
    'MapCtor',
    'ProxyFunctionObject',
    'QQmlBindingFunction',
    'QQmlBindingFunctionSizeStruct',
    'RangeErrorCtor',
    'ReferenceErrorCtor',
    'SetCtor',
    'SyntaxErrorCtor',
    'TypeErrorCtor',
    'URIErrorCtor',
    'BoundConstructor',
    'GeneratorFunction',
    'MemberFunction',
    'MemberFunctionSizeStruct',
    'ProxyConstructorObject',
    'ScriptFunction',
    'ScriptFunctionSizeStruct',
    'ConstructorFunction',
    'ConstructorFunctionSizeStruct',
    'MemberGeneratorFunction',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ..._q_v4__heap__arguments_object_data import ArgumentsObjectData
  from ..._q_v4__heap__arguments_object_offset_struct import ArgumentsObjectOffsetStruct
  from ..._q_v4__heap__array_data_data import ArrayDataData
  from ..._q_v4__heap__array_data_offset_struct import ArrayDataOffsetStruct
  from ..._q_v4__heap__array_iterator_object_data import ArrayIteratorObjectData
  from ..._q_v4__heap__array_iterator_object_offset_struct import ArrayIteratorObjectOffsetStruct
  from ..._q_v4__heap__bound_function_data import BoundFunctionData
  from ..._q_v4__heap__bound_function_offset_struct import BoundFunctionOffsetStruct
  from ..._q_v4__heap__call_context_data import CallContextData
  from ..._q_v4__heap__call_context_offset_struct import CallContextOffsetStruct
  from ..._q_v4__heap__capabilities_executor_wrapper_data import CapabilitiesExecutorWrapperData
  from ..._q_v4__heap__capabilities_executor_wrapper_offset_struct import CapabilitiesExecutorWrapperOffsetStruct
  from ..._q_v4__heap__constructor_function_data import ConstructorFunctionData
  from ..._q_v4__heap__constructor_function_offset_struct import ConstructorFunctionOffsetStruct
  from ..._q_v4__heap__data_view_data import DataViewData
  from ..._q_v4__heap__data_view_offset_struct import DataViewOffsetStruct
  from ..._q_v4__heap__date_object_data import DateObjectData
  from ..._q_v4__heap__date_object_offset_struct import DateObjectOffsetStruct
  from ..._q_v4__heap__default_class_constructor_function_data import DefaultClassConstructorFunctionData
  from ..._q_v4__heap__default_class_constructor_function_offset_struct import DefaultClassConstructorFunctionOffsetStruct
  from ..._q_v4__heap__dynamic_function_object_data import DynamicFunctionObjectData
  from ..._q_v4__heap__dynamic_function_object_offset_struct import DynamicFunctionObjectOffsetStruct
  from ..._q_v4__heap__error_object_data import ErrorObjectData
  from ..._q_v4__heap__error_object_offset_struct import ErrorObjectOffsetStruct
  from ..._q_v4__heap__execution_context_data import ExecutionContextData
  from ..._q_v4__heap__execution_context_offset_struct import ExecutionContextOffsetStruct
  from ..._q_v4__heap__for_in_iterator_object_data import ForInIteratorObjectData
  from ..._q_v4__heap__for_in_iterator_object_offset_struct import ForInIteratorObjectOffsetStruct
  from ..._q_v4__heap__function_object_data import FunctionObjectData
  from ..._q_v4__heap__function_object_offset_struct import FunctionObjectOffsetStruct
  from ..._q_v4__heap__generator_object_data import GeneratorObjectData
  from ..._q_v4__heap__generator_object_offset_struct import GeneratorObjectOffsetStruct
  from ..._q_v4__heap__java_script_function_object_data import JavaScriptFunctionObjectData
  from ..._q_v4__heap__java_script_function_object_offset_struct import JavaScriptFunctionObjectOffsetStruct
  from ..._q_v4__heap__map_iterator_object_data import MapIteratorObjectData
  from ..._q_v4__heap__map_iterator_object_offset_struct import MapIteratorObjectOffsetStruct
  from ..._q_v4__heap__member_data_data import MemberDataData
  from ..._q_v4__heap__member_data_offset_struct import MemberDataOffsetStruct
  from ..._q_v4__heap__member_function_data import MemberFunctionData
  from ..._q_v4__heap__member_function_offset_struct import MemberFunctionOffsetStruct
  from ..._q_v4__heap__module_data import ModuleData
  from ..._q_v4__heap__module_offset_struct import ModuleOffsetStruct
  from ..._q_v4__heap__object_data import ObjectData
  from ..._q_v4__heap__object_offset_struct import ObjectOffsetStruct
  from ..._q_v4__heap__promise_capability_data import PromiseCapabilityData
  from ..._q_v4__heap__promise_capability_offset_struct import PromiseCapabilityOffsetStruct
  from ..._q_v4__heap__promise_execution_state_data import PromiseExecutionStateData
  from ..._q_v4__heap__promise_execution_state_offset_struct import PromiseExecutionStateOffsetStruct
  from ..._q_v4__heap__promise_object_data import PromiseObjectData
  from ..._q_v4__heap__promise_object_offset_struct import PromiseObjectOffsetStruct
  from ..._q_v4__heap__promise_reaction_data import PromiseReactionData
  from ..._q_v4__heap__promise_reaction_offset_struct import PromiseReactionOffsetStruct
  from ..._q_v4__heap__proxy_data import ProxyData
  from ..._q_v4__heap__proxy_object_data import ProxyObjectData
  from ..._q_v4__heap__proxy_object_offset_struct import ProxyObjectOffsetStruct
  from ..._q_v4__heap__proxy_offset_struct import ProxyOffsetStruct
  from ..._q_v4__heap__q_object_method_data import QObjectMethodData
  from ..._q_v4__heap__q_object_method_offset_struct import QObjectMethodOffsetStruct
  from ..._q_v4__heap__q_qml_binding_function_data import QQmlBindingFunctionData
  from ..._q_v4__heap__q_qml_binding_function_offset_struct import QQmlBindingFunctionOffsetStruct
  from ..._q_v4__heap__q_qml_context_wrapper_data import QQmlContextWrapperData
  from ..._q_v4__heap__q_qml_context_wrapper_offset_struct import QQmlContextWrapperOffsetStruct
  from ..._q_v4__heap__q_qml_value_type_wrapper_data import QQmlValueTypeWrapperData
  from ..._q_v4__heap__q_qml_value_type_wrapper_offset_struct import QQmlValueTypeWrapperOffsetStruct
  from ..._q_v4__heap__qml_context_data import QmlContextData
  from ..._q_v4__heap__qml_context_offset_struct import QmlContextOffsetStruct
  from ..._q_v4__heap__reference_object_data import ReferenceObjectData
  from ..._q_v4__heap__reference_object_offset_struct import ReferenceObjectOffsetStruct
  from ..._q_v4__heap__reg_exp_ctor_data import RegExpCtorData
  from ..._q_v4__heap__reg_exp_ctor_offset_struct import RegExpCtorOffsetStruct
  from ..._q_v4__heap__reg_exp_object_data import RegExpObjectData
  from ..._q_v4__heap__reg_exp_object_offset_struct import RegExpObjectOffsetStruct
  from ..._q_v4__heap__reject_wrapper_data import RejectWrapperData
  from ..._q_v4__heap__reject_wrapper_offset_struct import RejectWrapperOffsetStruct
  from ..._q_v4__heap__resolve_element_wrapper_data import ResolveElementWrapperData
  from ..._q_v4__heap__resolve_element_wrapper_offset_struct import ResolveElementWrapperOffsetStruct
  from ..._q_v4__heap__resolve_wrapper_data import ResolveWrapperData
  from ..._q_v4__heap__resolve_wrapper_offset_struct import ResolveWrapperOffsetStruct
  from ..._q_v4__heap__script_function_data import ScriptFunctionData
  from ..._q_v4__heap__script_function_offset_struct import ScriptFunctionOffsetStruct
  from ..._q_v4__heap__set_iterator_object_data import SetIteratorObjectData
  from ..._q_v4__heap__set_iterator_object_offset_struct import SetIteratorObjectOffsetStruct
  from ..._q_v4__heap__strict_arguments_object_data import StrictArgumentsObjectData
  from ..._q_v4__heap__strict_arguments_object_offset_struct import StrictArgumentsObjectOffsetStruct
  from ..._q_v4__heap__string_iterator_object_data import StringIteratorObjectData
  from ..._q_v4__heap__string_iterator_object_offset_struct import StringIteratorObjectOffsetStruct
  from ..._q_v4__heap__string_object_data import StringObjectData
  from ..._q_v4__heap__string_object_offset_struct import StringObjectOffsetStruct
  from ..._q_v4__heap__symbol_object_data import SymbolObjectData
  from ..._q_v4__heap__symbol_object_offset_struct import SymbolObjectOffsetStruct
  from ..._q_v4__heap__typed_array_data import TypedArrayData
  from ..._q_v4__heap__typed_array_offset_struct import TypedArrayOffsetStruct
  from ..._q_v4__heap__url_object_data import UrlObjectData
  from ..._q_v4__heap__url_object_offset_struct import UrlObjectOffsetStruct
  from ..._q_v4__heap__url_search_params_object_data import UrlSearchParamsObjectData
  from ..._q_v4__heap__url_search_params_object_offset_struct import UrlSearchParamsObjectOffsetStruct
  from ..._q_v4__heap__variant_association_object_data import VariantAssociationObjectData
  from ..._q_v4__heap__variant_association_object_offset_struct import VariantAssociationObjectOffsetStruct
  from ..._q_v4__heap__base import Base
  from ..._q_v4__heap__array_data import ArrayData
  from ..._q_v4__heap__array_data_size_struct import ArrayDataSizeStruct
  from ..._q_v4__heap__execution_context import ExecutionContext
  from ..._q_v4__heap__execution_context_size_struct import ExecutionContextSizeStruct
  from ..._q_v4__heap__member_data import MemberData
  from ..._q_v4__heap__member_data_size_struct import MemberDataSizeStruct
  from ..._q_v4__heap__object import Object
  from ..._q_v4__heap__object_size_struct import ObjectSizeStruct
  from ..._q_v4__heap__string_or_symbol import StringOrSymbol
  from ..._q_v4__heap__arguments_object import ArgumentsObject
  from ..._q_v4__heap__arguments_object_size_struct import ArgumentsObjectSizeStruct
  from ..._q_v4__heap__array_iterator_object_size_struct import ArrayIteratorObjectSizeStruct
  from ..._q_v4__heap__array_object import ArrayObject
  from ..._q_v4__heap__atomics import Atomics
  from ..._q_v4__heap__boolean_object import BooleanObject
  from ..._q_v4__heap__call_context import CallContext
  from ..._q_v4__heap__call_context_size_struct import CallContextSizeStruct
  from ..._q_v4__heap__console_object import ConsoleObject
  from ..._q_v4__heap__data_view import DataView
  from ..._q_v4__heap__data_view_size_struct import DataViewSizeStruct
  from ..._q_v4__heap__error_object import ErrorObject
  from ..._q_v4__heap__error_object_size_struct import ErrorObjectSizeStruct
  from ..._q_v4__heap__for_in_iterator_object_size_struct import ForInIteratorObjectSizeStruct
  from ..._q_v4__heap__function_object_size_struct import FunctionObjectSizeStruct
  from ..._q_v4__heap__generator_object import GeneratorObject
  from ..._q_v4__heap__generator_object_size_struct import GeneratorObjectSizeStruct
  from ..._q_v4__heap__intrinsic_typed_array_prototype import IntrinsicTypedArrayPrototype
  from ..._q_v4__heap__json_object import JsonObject
  from ..._q_v4__heap__map_iterator_object_size_struct import MapIteratorObjectSizeStruct
  from ..._q_v4__heap__map_object import MapObject
  from ..._q_v4__heap__math_object import MathObject
  from ..._q_v4__heap__module import Module
  from ..._q_v4__heap__module_size_struct import ModuleSizeStruct
  from ..._q_v4__heap__number_object import NumberObject
  from ..._q_v4__heap__promise_capability import PromiseCapability
  from ..._q_v4__heap__promise_capability_size_struct import PromiseCapabilitySizeStruct
  from ..._q_v4__heap__promise_object_size_struct import PromiseObjectSizeStruct
  from ..._q_v4__heap__promise_reaction_size_struct import PromiseReactionSizeStruct
  from ..._q_v4__heap__q_qml_context_wrapper_size_struct import QQmlContextWrapperSizeStruct
  from ..._q_v4__heap__q_qml_enum_wrapper import QQmlEnumWrapper
  from ..._q_v4__heap__qml_context_size_struct import QmlContextSizeStruct
  from ..._q_v4__heap__reference_object_size_struct import ReferenceObjectSizeStruct
  from ..._q_v4__heap__reflect import Reflect
  from ..._q_v4__heap__reg_exp_object import RegExpObject
  from ..._q_v4__heap__reg_exp_object_size_struct import RegExpObjectSizeStruct
  from ..._q_v4__heap__set_iterator_object_size_struct import SetIteratorObjectSizeStruct
  from ..._q_v4__heap__set_object import SetObject
  from ..._q_v4__heap__shared_array_buffer import SharedArrayBuffer
  from ..._q_v4__heap__simple_array_data import SimpleArrayData
  from ..._q_v4__heap__sparse_array_data import SparseArrayData
  from ..._q_v4__heap__strict_arguments_object import StrictArgumentsObject
  from ..._q_v4__heap__strict_arguments_object_size_struct import StrictArgumentsObjectSizeStruct
  from ..._q_v4__heap__string import String
  from ..._q_v4__heap__string_iterator_object_size_struct import StringIteratorObjectSizeStruct
  from ..._q_v4__heap__string_object_size_struct import StringObjectSizeStruct
  from ..._q_v4__heap__symbol import Symbol
  from ..._q_v4__heap__symbol_object_size_struct import SymbolObjectSizeStruct
  from ..._q_v4__heap__typed_array import TypedArray
  from ..._q_v4__heap__typed_array_prototype import TypedArrayPrototype
  from ..._q_v4__heap__typed_array_size_struct import TypedArraySizeStruct
  from ..._q_v4__heap__url_object import UrlObject
  from ..._q_v4__heap__url_object_size_struct import UrlObjectSizeStruct
  from ..._q_v4__heap__url_search_params_object import UrlSearchParamsObject
  from ..._q_v4__heap__url_search_params_object_size_struct import UrlSearchParamsObjectSizeStruct
  from ..._q_v4__heap__array_buffer import ArrayBuffer
  from ..._q_v4__heap__complex_string import ComplexString
  from ..._q_v4__heap__eval_error_object import EvalErrorObject
  from ..._q_v4__heap__q_object_wrapper import QObjectWrapper
  from ..._q_v4__heap__qml_list_wrapper import QmlListWrapper
  from ..._q_v4__heap__qml_signal_handler import QmlSignalHandler
  from ..._q_v4__heap__range_error_object import RangeErrorObject
  from ..._q_v4__heap__reference_error_object import ReferenceErrorObject
  from ..._q_v4__heap__string_object import StringObject
  from ..._q_v4__heap__symbol_object import SymbolObject
  from ..._q_v4__heap__syntax_error_object import SyntaxErrorObject
  from ..._q_v4__heap__type_error_object import TypeErrorObject
  from ..._q_v4__heap__u_r_i_error_object import URIErrorObject
  from ..._q_v4__heap__variant_object import VariantObject
  from ..._q_v4__heap__promise_object import PromiseObject
  from ..._q_v4__heap__array_iterator_object import ArrayIteratorObject
  from ..._q_v4__heap__for_in_iterator_object import ForInIteratorObject
  from ..._q_v4__heap__function_object import FunctionObject
  from ..._q_v4__heap__internal_class import InternalClass
  from ..._q_v4__heap__map_iterator_object import MapIteratorObject
  from ..._q_v4__heap__promise_reaction import PromiseReaction
  from ..._q_v4__heap__q_qml_context_wrapper import QQmlContextWrapper
  from ..._q_v4__heap__reference_object import ReferenceObject
  from ..._q_v4__heap__reference_object_endpoint import ReferenceObjectEndpoint
  from ..._q_v4__heap__set_iterator_object import SetIteratorObject
  from ..._q_v4__heap__string_iterator_object import StringIteratorObject
  from ..._q_v4__heap__array_ctor import ArrayCtor
  from ..._q_v4__heap__boolean_ctor import BooleanCtor
  from ..._q_v4__heap__capabilities_executor_wrapper import CapabilitiesExecutorWrapper
  from ..._q_v4__heap__capabilities_executor_wrapper_size_struct import CapabilitiesExecutorWrapperSizeStruct
  from ..._q_v4__heap__data_view_ctor import DataViewCtor
  from ..._q_v4__heap__date_ctor import DateCtor
  from ..._q_v4__heap__date_object import DateObject
  from ..._q_v4__heap__date_object_size_struct import DateObjectSizeStruct
  from ..._q_v4__heap__default_class_constructor_function import DefaultClassConstructorFunction
  from ..._q_v4__heap__default_class_constructor_function_size_struct import DefaultClassConstructorFunctionSizeStruct
  from ..._q_v4__heap__dynamic_function_object import DynamicFunctionObject
  from ..._q_v4__heap__dynamic_function_object_size_struct import DynamicFunctionObjectSizeStruct
  from ..._q_v4__heap__error_ctor import ErrorCtor
  from ..._q_v4__heap__eval_function import EvalFunction
  from ..._q_v4__heap__function_ctor import FunctionCtor
  from ..._q_v4__heap__function_prototype import FunctionPrototype
  from ..._q_v4__heap__generator_function_ctor import GeneratorFunctionCtor
  from ..._q_v4__heap__generator_prototype import GeneratorPrototype
  from ..._q_v4__heap__intrinsic_typed_array_ctor import IntrinsicTypedArrayCtor
  from ..._q_v4__heap__java_script_function_object import JavaScriptFunctionObject
  from ..._q_v4__heap__java_script_function_object_size_struct import JavaScriptFunctionObjectSizeStruct
  from ..._q_v4__heap__number_ctor import NumberCtor
  from ..._q_v4__heap__object_ctor import ObjectCtor
  from ..._q_v4__heap__promise_ctor import PromiseCtor
  from ..._q_v4__heap__promise_execution_state import PromiseExecutionState
  from ..._q_v4__heap__promise_execution_state_size_struct import PromiseExecutionStateSizeStruct
  from ..._q_v4__heap__proxy import Proxy
  from ..._q_v4__heap__proxy_object import ProxyObject
  from ..._q_v4__heap__proxy_object_size_struct import ProxyObjectSizeStruct
  from ..._q_v4__heap__proxy_size_struct import ProxySizeStruct
  from ..._q_v4__heap__q_meta_object_wrapper import QMetaObjectWrapper
  from ..._q_v4__heap__q_object_method import QObjectMethod
  from ..._q_v4__heap__q_object_method_size_struct import QObjectMethodSizeStruct
  from ..._q_v4__heap__q_qml_type_wrapper import QQmlTypeWrapper
  from ..._q_v4__heap__q_qml_value_type_wrapper import QQmlValueTypeWrapper
  from ..._q_v4__heap__q_qml_value_type_wrapper_size_struct import QQmlValueTypeWrapperSizeStruct
  from ..._q_v4__heap__qml_context import QmlContext
  from ..._q_v4__heap__reg_exp_ctor import RegExpCtor
  from ..._q_v4__heap__reg_exp_ctor_size_struct import RegExpCtorSizeStruct
  from ..._q_v4__heap__reject_wrapper import RejectWrapper
  from ..._q_v4__heap__reject_wrapper_size_struct import RejectWrapperSizeStruct
  from ..._q_v4__heap__resolve_element_wrapper import ResolveElementWrapper
  from ..._q_v4__heap__resolve_element_wrapper_size_struct import ResolveElementWrapperSizeStruct
  from ..._q_v4__heap__resolve_wrapper import ResolveWrapper
  from ..._q_v4__heap__resolve_wrapper_size_struct import ResolveWrapperSizeStruct
  from ..._q_v4__heap__sequence import Sequence
  from ..._q_v4__heap__shared_array_buffer_ctor import SharedArrayBufferCtor
  from ..._q_v4__heap__string_ctor import StringCtor
  from ..._q_v4__heap__symbol_ctor import SymbolCtor
  from ..._q_v4__heap__typed_array_ctor import TypedArrayCtor
  from ..._q_v4__heap__url_ctor import UrlCtor
  from ..._q_v4__heap__url_search_params_ctor import UrlSearchParamsCtor
  from ..._q_v4__heap__variant_association_object import VariantAssociationObject
  from ..._q_v4__heap__variant_association_object_size_struct import VariantAssociationObjectSizeStruct
  from ..._q_v4__heap__weak_map_ctor import WeakMapCtor
  from ..._q_v4__heap__weak_set_ctor import WeakSetCtor
  from ..._q_v4__heap__array_buffer_ctor import ArrayBufferCtor
  from ..._q_v4__heap__arrow_function import ArrowFunction
  from ..._q_v4__heap__bound_function import BoundFunction
  from ..._q_v4__heap__bound_function_size_struct import BoundFunctionSizeStruct
  from ..._q_v4__heap__eval_error_ctor import EvalErrorCtor
  from ..._q_v4__heap__indexed_builtin_function import IndexedBuiltinFunction
  from ..._q_v4__heap__map_ctor import MapCtor
  from ..._q_v4__heap__proxy_function_object import ProxyFunctionObject
  from ..._q_v4__heap__q_qml_binding_function import QQmlBindingFunction
  from ..._q_v4__heap__q_qml_binding_function_size_struct import QQmlBindingFunctionSizeStruct
  from ..._q_v4__heap__range_error_ctor import RangeErrorCtor
  from ..._q_v4__heap__reference_error_ctor import ReferenceErrorCtor
  from ..._q_v4__heap__set_ctor import SetCtor
  from ..._q_v4__heap__syntax_error_ctor import SyntaxErrorCtor
  from ..._q_v4__heap__type_error_ctor import TypeErrorCtor
  from ..._q_v4__heap__u_r_i_error_ctor import URIErrorCtor
  from ..._q_v4__heap__bound_constructor import BoundConstructor
  from ..._q_v4__heap__generator_function import GeneratorFunction
  from ..._q_v4__heap__member_function import MemberFunction
  from ..._q_v4__heap__member_function_size_struct import MemberFunctionSizeStruct
  from ..._q_v4__heap__proxy_constructor_object import ProxyConstructorObject
  from ..._q_v4__heap__script_function import ScriptFunction
  from ..._q_v4__heap__script_function_size_struct import ScriptFunctionSizeStruct
  from ..._q_v4__heap__constructor_function import ConstructorFunction
  from ..._q_v4__heap__constructor_function_size_struct import ConstructorFunctionSizeStruct
  from ..._q_v4__heap__member_generator_function import MemberGeneratorFunction
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'ArgumentsObjectData': '_q_v4__heap__arguments_object_data',
      'ArgumentsObjectOffsetStruct': '_q_v4__heap__arguments_object_offset_struct',
      'ArrayDataData': '_q_v4__heap__array_data_data',
      'ArrayDataOffsetStruct': '_q_v4__heap__array_data_offset_struct',
      'ArrayIteratorObjectData': '_q_v4__heap__array_iterator_object_data',
      'ArrayIteratorObjectOffsetStruct': '_q_v4__heap__array_iterator_object_offset_struct',
      'BoundFunctionData': '_q_v4__heap__bound_function_data',
      'BoundFunctionOffsetStruct': '_q_v4__heap__bound_function_offset_struct',
      'CallContextData': '_q_v4__heap__call_context_data',
      'CallContextOffsetStruct': '_q_v4__heap__call_context_offset_struct',
      'CapabilitiesExecutorWrapperData': '_q_v4__heap__capabilities_executor_wrapper_data',
      'CapabilitiesExecutorWrapperOffsetStruct': '_q_v4__heap__capabilities_executor_wrapper_offset_struct',
      'ConstructorFunctionData': '_q_v4__heap__constructor_function_data',
      'ConstructorFunctionOffsetStruct': '_q_v4__heap__constructor_function_offset_struct',
      'DataViewData': '_q_v4__heap__data_view_data',
      'DataViewOffsetStruct': '_q_v4__heap__data_view_offset_struct',
      'DateObjectData': '_q_v4__heap__date_object_data',
      'DateObjectOffsetStruct': '_q_v4__heap__date_object_offset_struct',
      'DefaultClassConstructorFunctionData': '_q_v4__heap__default_class_constructor_function_data',
      'DefaultClassConstructorFunctionOffsetStruct': '_q_v4__heap__default_class_constructor_function_offset_struct',
      'DynamicFunctionObjectData': '_q_v4__heap__dynamic_function_object_data',
      'DynamicFunctionObjectOffsetStruct': '_q_v4__heap__dynamic_function_object_offset_struct',
      'ErrorObjectData': '_q_v4__heap__error_object_data',
      'ErrorObjectOffsetStruct': '_q_v4__heap__error_object_offset_struct',
      'ExecutionContextData': '_q_v4__heap__execution_context_data',
      'ExecutionContextOffsetStruct': '_q_v4__heap__execution_context_offset_struct',
      'ForInIteratorObjectData': '_q_v4__heap__for_in_iterator_object_data',
      'ForInIteratorObjectOffsetStruct': '_q_v4__heap__for_in_iterator_object_offset_struct',
      'FunctionObjectData': '_q_v4__heap__function_object_data',
      'FunctionObjectOffsetStruct': '_q_v4__heap__function_object_offset_struct',
      'GeneratorObjectData': '_q_v4__heap__generator_object_data',
      'GeneratorObjectOffsetStruct': '_q_v4__heap__generator_object_offset_struct',
      'JavaScriptFunctionObjectData': '_q_v4__heap__java_script_function_object_data',
      'JavaScriptFunctionObjectOffsetStruct': '_q_v4__heap__java_script_function_object_offset_struct',
      'MapIteratorObjectData': '_q_v4__heap__map_iterator_object_data',
      'MapIteratorObjectOffsetStruct': '_q_v4__heap__map_iterator_object_offset_struct',
      'MemberDataData': '_q_v4__heap__member_data_data',
      'MemberDataOffsetStruct': '_q_v4__heap__member_data_offset_struct',
      'MemberFunctionData': '_q_v4__heap__member_function_data',
      'MemberFunctionOffsetStruct': '_q_v4__heap__member_function_offset_struct',
      'ModuleData': '_q_v4__heap__module_data',
      'ModuleOffsetStruct': '_q_v4__heap__module_offset_struct',
      'ObjectData': '_q_v4__heap__object_data',
      'ObjectOffsetStruct': '_q_v4__heap__object_offset_struct',
      'PromiseCapabilityData': '_q_v4__heap__promise_capability_data',
      'PromiseCapabilityOffsetStruct': '_q_v4__heap__promise_capability_offset_struct',
      'PromiseExecutionStateData': '_q_v4__heap__promise_execution_state_data',
      'PromiseExecutionStateOffsetStruct': '_q_v4__heap__promise_execution_state_offset_struct',
      'PromiseObjectData': '_q_v4__heap__promise_object_data',
      'PromiseObjectOffsetStruct': '_q_v4__heap__promise_object_offset_struct',
      'PromiseReactionData': '_q_v4__heap__promise_reaction_data',
      'PromiseReactionOffsetStruct': '_q_v4__heap__promise_reaction_offset_struct',
      'ProxyData': '_q_v4__heap__proxy_data',
      'ProxyObjectData': '_q_v4__heap__proxy_object_data',
      'ProxyObjectOffsetStruct': '_q_v4__heap__proxy_object_offset_struct',
      'ProxyOffsetStruct': '_q_v4__heap__proxy_offset_struct',
      'QObjectMethodData': '_q_v4__heap__q_object_method_data',
      'QObjectMethodOffsetStruct': '_q_v4__heap__q_object_method_offset_struct',
      'QQmlBindingFunctionData': '_q_v4__heap__q_qml_binding_function_data',
      'QQmlBindingFunctionOffsetStruct': '_q_v4__heap__q_qml_binding_function_offset_struct',
      'QQmlContextWrapperData': '_q_v4__heap__q_qml_context_wrapper_data',
      'QQmlContextWrapperOffsetStruct': '_q_v4__heap__q_qml_context_wrapper_offset_struct',
      'QQmlValueTypeWrapperData': '_q_v4__heap__q_qml_value_type_wrapper_data',
      'QQmlValueTypeWrapperOffsetStruct': '_q_v4__heap__q_qml_value_type_wrapper_offset_struct',
      'QmlContextData': '_q_v4__heap__qml_context_data',
      'QmlContextOffsetStruct': '_q_v4__heap__qml_context_offset_struct',
      'ReferenceObjectData': '_q_v4__heap__reference_object_data',
      'ReferenceObjectOffsetStruct': '_q_v4__heap__reference_object_offset_struct',
      'RegExpCtorData': '_q_v4__heap__reg_exp_ctor_data',
      'RegExpCtorOffsetStruct': '_q_v4__heap__reg_exp_ctor_offset_struct',
      'RegExpObjectData': '_q_v4__heap__reg_exp_object_data',
      'RegExpObjectOffsetStruct': '_q_v4__heap__reg_exp_object_offset_struct',
      'RejectWrapperData': '_q_v4__heap__reject_wrapper_data',
      'RejectWrapperOffsetStruct': '_q_v4__heap__reject_wrapper_offset_struct',
      'ResolveElementWrapperData': '_q_v4__heap__resolve_element_wrapper_data',
      'ResolveElementWrapperOffsetStruct': '_q_v4__heap__resolve_element_wrapper_offset_struct',
      'ResolveWrapperData': '_q_v4__heap__resolve_wrapper_data',
      'ResolveWrapperOffsetStruct': '_q_v4__heap__resolve_wrapper_offset_struct',
      'ScriptFunctionData': '_q_v4__heap__script_function_data',
      'ScriptFunctionOffsetStruct': '_q_v4__heap__script_function_offset_struct',
      'SetIteratorObjectData': '_q_v4__heap__set_iterator_object_data',
      'SetIteratorObjectOffsetStruct': '_q_v4__heap__set_iterator_object_offset_struct',
      'StrictArgumentsObjectData': '_q_v4__heap__strict_arguments_object_data',
      'StrictArgumentsObjectOffsetStruct': '_q_v4__heap__strict_arguments_object_offset_struct',
      'StringIteratorObjectData': '_q_v4__heap__string_iterator_object_data',
      'StringIteratorObjectOffsetStruct': '_q_v4__heap__string_iterator_object_offset_struct',
      'StringObjectData': '_q_v4__heap__string_object_data',
      'StringObjectOffsetStruct': '_q_v4__heap__string_object_offset_struct',
      'SymbolObjectData': '_q_v4__heap__symbol_object_data',
      'SymbolObjectOffsetStruct': '_q_v4__heap__symbol_object_offset_struct',
      'TypedArrayData': '_q_v4__heap__typed_array_data',
      'TypedArrayOffsetStruct': '_q_v4__heap__typed_array_offset_struct',
      'UrlObjectData': '_q_v4__heap__url_object_data',
      'UrlObjectOffsetStruct': '_q_v4__heap__url_object_offset_struct',
      'UrlSearchParamsObjectData': '_q_v4__heap__url_search_params_object_data',
      'UrlSearchParamsObjectOffsetStruct': '_q_v4__heap__url_search_params_object_offset_struct',
      'VariantAssociationObjectData': '_q_v4__heap__variant_association_object_data',
      'VariantAssociationObjectOffsetStruct': '_q_v4__heap__variant_association_object_offset_struct',
      'Base': '_q_v4__heap__base',
      'ArrayData': '_q_v4__heap__array_data',
      'ArrayDataSizeStruct': '_q_v4__heap__array_data_size_struct',
      'ExecutionContext': '_q_v4__heap__execution_context',
      'ExecutionContextSizeStruct': '_q_v4__heap__execution_context_size_struct',
      'MemberData': '_q_v4__heap__member_data',
      'MemberDataSizeStruct': '_q_v4__heap__member_data_size_struct',
      'Object': '_q_v4__heap__object',
      'ObjectSizeStruct': '_q_v4__heap__object_size_struct',
      'StringOrSymbol': '_q_v4__heap__string_or_symbol',
      'ArgumentsObject': '_q_v4__heap__arguments_object',
      'ArgumentsObjectSizeStruct': '_q_v4__heap__arguments_object_size_struct',
      'ArrayIteratorObjectSizeStruct': '_q_v4__heap__array_iterator_object_size_struct',
      'ArrayObject': '_q_v4__heap__array_object',
      'Atomics': '_q_v4__heap__atomics',
      'BooleanObject': '_q_v4__heap__boolean_object',
      'CallContext': '_q_v4__heap__call_context',
      'CallContextSizeStruct': '_q_v4__heap__call_context_size_struct',
      'ConsoleObject': '_q_v4__heap__console_object',
      'DataView': '_q_v4__heap__data_view',
      'DataViewSizeStruct': '_q_v4__heap__data_view_size_struct',
      'ErrorObject': '_q_v4__heap__error_object',
      'ErrorObjectSizeStruct': '_q_v4__heap__error_object_size_struct',
      'ForInIteratorObjectSizeStruct': '_q_v4__heap__for_in_iterator_object_size_struct',
      'FunctionObjectSizeStruct': '_q_v4__heap__function_object_size_struct',
      'GeneratorObject': '_q_v4__heap__generator_object',
      'GeneratorObjectSizeStruct': '_q_v4__heap__generator_object_size_struct',
      'IntrinsicTypedArrayPrototype': '_q_v4__heap__intrinsic_typed_array_prototype',
      'JsonObject': '_q_v4__heap__json_object',
      'MapIteratorObjectSizeStruct': '_q_v4__heap__map_iterator_object_size_struct',
      'MapObject': '_q_v4__heap__map_object',
      'MathObject': '_q_v4__heap__math_object',
      'Module': '_q_v4__heap__module',
      'ModuleSizeStruct': '_q_v4__heap__module_size_struct',
      'NumberObject': '_q_v4__heap__number_object',
      'PromiseCapability': '_q_v4__heap__promise_capability',
      'PromiseCapabilitySizeStruct': '_q_v4__heap__promise_capability_size_struct',
      'PromiseObjectSizeStruct': '_q_v4__heap__promise_object_size_struct',
      'PromiseReactionSizeStruct': '_q_v4__heap__promise_reaction_size_struct',
      'QQmlContextWrapperSizeStruct': '_q_v4__heap__q_qml_context_wrapper_size_struct',
      'QQmlEnumWrapper': '_q_v4__heap__q_qml_enum_wrapper',
      'QmlContextSizeStruct': '_q_v4__heap__qml_context_size_struct',
      'ReferenceObjectSizeStruct': '_q_v4__heap__reference_object_size_struct',
      'Reflect': '_q_v4__heap__reflect',
      'RegExpObject': '_q_v4__heap__reg_exp_object',
      'RegExpObjectSizeStruct': '_q_v4__heap__reg_exp_object_size_struct',
      'SetIteratorObjectSizeStruct': '_q_v4__heap__set_iterator_object_size_struct',
      'SetObject': '_q_v4__heap__set_object',
      'SharedArrayBuffer': '_q_v4__heap__shared_array_buffer',
      'SimpleArrayData': '_q_v4__heap__simple_array_data',
      'SparseArrayData': '_q_v4__heap__sparse_array_data',
      'StrictArgumentsObject': '_q_v4__heap__strict_arguments_object',
      'StrictArgumentsObjectSizeStruct': '_q_v4__heap__strict_arguments_object_size_struct',
      'String': '_q_v4__heap__string',
      'StringIteratorObjectSizeStruct': '_q_v4__heap__string_iterator_object_size_struct',
      'StringObjectSizeStruct': '_q_v4__heap__string_object_size_struct',
      'Symbol': '_q_v4__heap__symbol',
      'SymbolObjectSizeStruct': '_q_v4__heap__symbol_object_size_struct',
      'TypedArray': '_q_v4__heap__typed_array',
      'TypedArrayPrototype': '_q_v4__heap__typed_array_prototype',
      'TypedArraySizeStruct': '_q_v4__heap__typed_array_size_struct',
      'UrlObject': '_q_v4__heap__url_object',
      'UrlObjectSizeStruct': '_q_v4__heap__url_object_size_struct',
      'UrlSearchParamsObject': '_q_v4__heap__url_search_params_object',
      'UrlSearchParamsObjectSizeStruct': '_q_v4__heap__url_search_params_object_size_struct',
      'ArrayBuffer': '_q_v4__heap__array_buffer',
      'ComplexString': '_q_v4__heap__complex_string',
      'EvalErrorObject': '_q_v4__heap__eval_error_object',
      'QObjectWrapper': '_q_v4__heap__q_object_wrapper',
      'QmlListWrapper': '_q_v4__heap__qml_list_wrapper',
      'QmlSignalHandler': '_q_v4__heap__qml_signal_handler',
      'RangeErrorObject': '_q_v4__heap__range_error_object',
      'ReferenceErrorObject': '_q_v4__heap__reference_error_object',
      'StringObject': '_q_v4__heap__string_object',
      'SymbolObject': '_q_v4__heap__symbol_object',
      'SyntaxErrorObject': '_q_v4__heap__syntax_error_object',
      'TypeErrorObject': '_q_v4__heap__type_error_object',
      'URIErrorObject': '_q_v4__heap__u_r_i_error_object',
      'VariantObject': '_q_v4__heap__variant_object',
      'PromiseObject': '_q_v4__heap__promise_object',
      'ArrayIteratorObject': '_q_v4__heap__array_iterator_object',
      'ForInIteratorObject': '_q_v4__heap__for_in_iterator_object',
      'FunctionObject': '_q_v4__heap__function_object',
      'InternalClass': '_q_v4__heap__internal_class',
      'MapIteratorObject': '_q_v4__heap__map_iterator_object',
      'PromiseReaction': '_q_v4__heap__promise_reaction',
      'QQmlContextWrapper': '_q_v4__heap__q_qml_context_wrapper',
      'ReferenceObject': '_q_v4__heap__reference_object',
      'ReferenceObjectEndpoint': '_q_v4__heap__reference_object_endpoint',
      'SetIteratorObject': '_q_v4__heap__set_iterator_object',
      'StringIteratorObject': '_q_v4__heap__string_iterator_object',
      'ArrayCtor': '_q_v4__heap__array_ctor',
      'BooleanCtor': '_q_v4__heap__boolean_ctor',
      'CapabilitiesExecutorWrapper': '_q_v4__heap__capabilities_executor_wrapper',
      'CapabilitiesExecutorWrapperSizeStruct': '_q_v4__heap__capabilities_executor_wrapper_size_struct',
      'DataViewCtor': '_q_v4__heap__data_view_ctor',
      'DateCtor': '_q_v4__heap__date_ctor',
      'DateObject': '_q_v4__heap__date_object',
      'DateObjectSizeStruct': '_q_v4__heap__date_object_size_struct',
      'DefaultClassConstructorFunction': '_q_v4__heap__default_class_constructor_function',
      'DefaultClassConstructorFunctionSizeStruct': '_q_v4__heap__default_class_constructor_function_size_struct',
      'DynamicFunctionObject': '_q_v4__heap__dynamic_function_object',
      'DynamicFunctionObjectSizeStruct': '_q_v4__heap__dynamic_function_object_size_struct',
      'ErrorCtor': '_q_v4__heap__error_ctor',
      'EvalFunction': '_q_v4__heap__eval_function',
      'FunctionCtor': '_q_v4__heap__function_ctor',
      'FunctionPrototype': '_q_v4__heap__function_prototype',
      'GeneratorFunctionCtor': '_q_v4__heap__generator_function_ctor',
      'GeneratorPrototype': '_q_v4__heap__generator_prototype',
      'IntrinsicTypedArrayCtor': '_q_v4__heap__intrinsic_typed_array_ctor',
      'JavaScriptFunctionObject': '_q_v4__heap__java_script_function_object',
      'JavaScriptFunctionObjectSizeStruct': '_q_v4__heap__java_script_function_object_size_struct',
      'NumberCtor': '_q_v4__heap__number_ctor',
      'ObjectCtor': '_q_v4__heap__object_ctor',
      'PromiseCtor': '_q_v4__heap__promise_ctor',
      'PromiseExecutionState': '_q_v4__heap__promise_execution_state',
      'PromiseExecutionStateSizeStruct': '_q_v4__heap__promise_execution_state_size_struct',
      'Proxy': '_q_v4__heap__proxy',
      'ProxyObject': '_q_v4__heap__proxy_object',
      'ProxyObjectSizeStruct': '_q_v4__heap__proxy_object_size_struct',
      'ProxySizeStruct': '_q_v4__heap__proxy_size_struct',
      'QMetaObjectWrapper': '_q_v4__heap__q_meta_object_wrapper',
      'QObjectMethod': '_q_v4__heap__q_object_method',
      'QObjectMethodSizeStruct': '_q_v4__heap__q_object_method_size_struct',
      'QQmlTypeWrapper': '_q_v4__heap__q_qml_type_wrapper',
      'QQmlValueTypeWrapper': '_q_v4__heap__q_qml_value_type_wrapper',
      'QQmlValueTypeWrapperSizeStruct': '_q_v4__heap__q_qml_value_type_wrapper_size_struct',
      'QmlContext': '_q_v4__heap__qml_context',
      'RegExpCtor': '_q_v4__heap__reg_exp_ctor',
      'RegExpCtorSizeStruct': '_q_v4__heap__reg_exp_ctor_size_struct',
      'RejectWrapper': '_q_v4__heap__reject_wrapper',
      'RejectWrapperSizeStruct': '_q_v4__heap__reject_wrapper_size_struct',
      'ResolveElementWrapper': '_q_v4__heap__resolve_element_wrapper',
      'ResolveElementWrapperSizeStruct': '_q_v4__heap__resolve_element_wrapper_size_struct',
      'ResolveWrapper': '_q_v4__heap__resolve_wrapper',
      'ResolveWrapperSizeStruct': '_q_v4__heap__resolve_wrapper_size_struct',
      'Sequence': '_q_v4__heap__sequence',
      'SharedArrayBufferCtor': '_q_v4__heap__shared_array_buffer_ctor',
      'StringCtor': '_q_v4__heap__string_ctor',
      'SymbolCtor': '_q_v4__heap__symbol_ctor',
      'TypedArrayCtor': '_q_v4__heap__typed_array_ctor',
      'UrlCtor': '_q_v4__heap__url_ctor',
      'UrlSearchParamsCtor': '_q_v4__heap__url_search_params_ctor',
      'VariantAssociationObject': '_q_v4__heap__variant_association_object',
      'VariantAssociationObjectSizeStruct': '_q_v4__heap__variant_association_object_size_struct',
      'WeakMapCtor': '_q_v4__heap__weak_map_ctor',
      'WeakSetCtor': '_q_v4__heap__weak_set_ctor',
      'ArrayBufferCtor': '_q_v4__heap__array_buffer_ctor',
      'ArrowFunction': '_q_v4__heap__arrow_function',
      'BoundFunction': '_q_v4__heap__bound_function',
      'BoundFunctionSizeStruct': '_q_v4__heap__bound_function_size_struct',
      'EvalErrorCtor': '_q_v4__heap__eval_error_ctor',
      'IndexedBuiltinFunction': '_q_v4__heap__indexed_builtin_function',
      'MapCtor': '_q_v4__heap__map_ctor',
      'ProxyFunctionObject': '_q_v4__heap__proxy_function_object',
      'QQmlBindingFunction': '_q_v4__heap__q_qml_binding_function',
      'QQmlBindingFunctionSizeStruct': '_q_v4__heap__q_qml_binding_function_size_struct',
      'RangeErrorCtor': '_q_v4__heap__range_error_ctor',
      'ReferenceErrorCtor': '_q_v4__heap__reference_error_ctor',
      'SetCtor': '_q_v4__heap__set_ctor',
      'SyntaxErrorCtor': '_q_v4__heap__syntax_error_ctor',
      'TypeErrorCtor': '_q_v4__heap__type_error_ctor',
      'URIErrorCtor': '_q_v4__heap__u_r_i_error_ctor',
      'BoundConstructor': '_q_v4__heap__bound_constructor',
      'GeneratorFunction': '_q_v4__heap__generator_function',
      'MemberFunction': '_q_v4__heap__member_function',
      'MemberFunctionSizeStruct': '_q_v4__heap__member_function_size_struct',
      'ProxyConstructorObject': '_q_v4__heap__proxy_constructor_object',
      'ScriptFunction': '_q_v4__heap__script_function',
      'ScriptFunctionSizeStruct': '_q_v4__heap__script_function_size_struct',
      'ConstructorFunction': '_q_v4__heap__constructor_function',
      'ConstructorFunctionSizeStruct': '_q_v4__heap__constructor_function_size_struct',
      'MemberGeneratorFunction': '_q_v4__heap__member_generator_function',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QV4.Heap.ArgumentsObjectData'. Python calls this for a
    name the package does not hold yet, and what it gives is kept here for
    the next time.

    Raises
    ------

    AttributeError
      The namespace has nothing of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
    else:
      try:
        fileName = __class_files__[name]
      except KeyError:
        infoSpec = """module '%s' has no attribute '%s'"""
        raise AttributeError(infoSpec % (__name__, name)) from None
      module = importlib.import_module('...%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__]
