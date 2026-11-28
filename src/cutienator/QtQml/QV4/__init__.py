"""
The namespace 'QV4' of Qt, a package of 'cutienator.QtQml':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQml import QV4
  QV4.ArrayElementLessThan

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from .._q_v4 import QV4 as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'ArrayElementLessThan',
    'ArrayVTable',
    'BitVector',
    'BlockAllocator',
    'CallData',
    'Chunk',
    'CompilationUnitRuntimeData',
    'CppStackFrameBase',
    'ESTable',
    'Encode',
    'EngineBase',
    'ExecutableAllocator',
    'FunctionData',
    'GCData',
    'GCIteratorStorage',
    'GlobalFunctions',
    'HeapItem',
    'HugeItemAllocator',
    'IdentifierHashData',
    'IdentifierHashEntry',
    'InternalClassEntry',
    'InternalClassTransition',
    'JSCallArguments',
    'JSCallData',
    'Lookup',
    'ObjectIterator',
    'OptionalReturnedValue',
    'OwnPropertyKeyIterator',
    'PersistentValue',
    'PersistentValueStorage',
    'Property',
    'PropertyAttributes',
    'PropertyHash',
    'PropertyHashData',
    'PropertyIndex',
    'PropertyKey',
    'Runtime',
    'Scope',
    'ScopedProperty',
    'ScopedPropertyKey',
    'ScopedStackFrame',
    'ScopedValue',
    'SparseArray',
    'SparseArrayNode',
    'StackFrame',
    'StackProperties',
    'StaticValue',
    'TypedArrayOperations',
    'VTable',
    'VTableBase',
    'WeakValue',
    'WriteBarrier',
    'CppStackFrame',
    'MarkStack',
    'MemoryManager',
    'ObjectOwnPropertyKeyIterator',
    'Value',
    'JSTypesStackFrame',
    'Managed',
    'ArrayData',
    'ExecutionContext',
    'IdentifierHash',
    'InternalClass',
    'JsonParser',
    'RuntimeHelpers',
    'StringOrSymbol',
    'CallContext',
    'SimpleArrayData',
    'SparseArrayData',
    'String',
    'Symbol',
    'CompilationUnitMapper',
    'ComplexString',
    'Date',
    'ExecutableCompilationUnit',
    'Function',
    'GCStateMachine',
    'IdentifierTable',
    'MetaTypesStackFrame',
    'MultiplyWrappedQObjectMap',
    'NumberLocale',
    'Script',
    'RuntimeCodegen',
    'ExecutionEngine',
    'QmlContext',
    'ResolvedTypeReference',
    'Object',
    'FunctionObject',
    'PromiseCapability',
    'ArgumentsObject',
    'ArrayCtor',
    'ArrayIteratorObject',
    'ArrayIteratorPrototype',
    'ArrayObject',
    'Atomics',
    'BooleanCtor',
    'BooleanObject',
    'CapabilitiesExecutorWrapper',
    'ConsoleObject',
    'DataView',
    'DataViewCtor',
    'DataViewPrototype',
    'DateCtor',
    'DatePrototype',
    'DefaultClassConstructorFunction',
    'DynamicFunctionObject',
    'ErrorCtor',
    'ErrorObject',
    'ErrorPrototype',
    'EvalErrorPrototype',
    'EvalFunction',
    'ForInIteratorObject',
    'ForInIteratorPrototype',
    'FunctionCtor',
    'FunctionPrototype',
    'GeneratorObject',
    'GeneratorPrototype',
    'GlobalExtensions',
    'IntrinsicTypedArrayCtor',
    'IntrinsicTypedArrayPrototype',
    'IteratorPrototype',
    'JavaScriptFunctionObject',
    'JsonObject',
    'MapIteratorObject',
    'MapIteratorPrototype',
    'MapObject',
    'MathObject',
    'MemberData',
    'Module',
    'NumberCtor',
    'NumberObject',
    'ObjectCtor',
    'ObjectItem',
    'ObjectPrototype',
    'PromiseCtor',
    'PromiseExecutionState',
    'PromiseObject',
    'PromisePrototype',
    'PromiseReaction',
    'PropertyListPrototype',
    'Proxy',
    'ProxyObject',
    'QMetaObjectWrapper',
    'QObjectMethod',
    'QObjectWrapper',
    'QQmlContextWrapper',
    'QQmlEnumWrapper',
    'QQmlTypeWrapper',
    'QmlListWrapper',
    'QmlSignalHandler',
    'RangeErrorPrototype',
    'ReferenceErrorPrototype',
    'ReferenceObject',
    'Reflect',
    'RegExpCtor',
    'RegExpObject',
    'RegExpPrototype',
    'RejectWrapper',
    'ResolveElementWrapper',
    'ResolveWrapper',
    'SequencePrototype',
    'SetIteratorObject',
    'SetIteratorPrototype',
    'SetObject',
    'SharedArrayBuffer',
    'SharedArrayBufferCtor',
    'SharedArrayBufferPrototype',
    'StrictArgumentsObject',
    'StringCtor',
    'StringIteratorObject',
    'StringIteratorPrototype',
    'StringObject',
    'SymbolCtor',
    'SymbolObject',
    'SymbolPrototype',
    'SyntaxErrorPrototype',
    'TypeErrorPrototype',
    'TypedArray',
    'TypedArrayCtor',
    'TypedArrayPrototype',
    'URIErrorPrototype',
    'UrlCtor',
    'UrlObject',
    'UrlPrototype',
    'UrlSearchParamsCtor',
    'UrlSearchParamsObject',
    'UrlSearchParamsPrototype',
    'VariantAssociationPrototype',
    'VariantObject',
    'WeakMapCtor',
    'WeakMapPrototype',
    'WeakSetCtor',
    'WeakSetPrototype',
    'ArrayBuffer',
    'ArrayBufferCtor',
    'ArrayBufferPrototype',
    'ArrayPrototype',
    'ArrowFunction',
    'BooleanPrototype',
    'BoundFunction',
    'DateObject',
    'EvalErrorCtor',
    'EvalErrorObject',
    'GeneratorFunctionCtor',
    'IndexedBuiltinFunction',
    'MapCtor',
    'MapPrototype',
    'NumberPrototype',
    'ProxyFunctionObject',
    'QQmlBindingFunction',
    'QQmlTypeConstructor',
    'QQmlValueTypeWrapper',
    'RangeErrorCtor',
    'RangeErrorObject',
    'ReferenceErrorCtor',
    'ReferenceErrorObject',
    'Sequence',
    'SetCtor',
    'SetPrototype',
    'StringPrototype',
    'SyntaxErrorCtor',
    'SyntaxErrorObject',
    'TypeErrorCtor',
    'TypeErrorObject',
    'URIErrorCtor',
    'URIErrorObject',
    'VariantAssociationObject',
    'VariantPrototype',
    'BoundConstructor',
    'GeneratorFunction',
    'MemberFunction',
    'ProxyConstructorObject',
    'ScriptFunction',
    'ConstructorFunction',
    'MemberGeneratorFunction',
    'CompiledData',
    'Compiler',
    'Debugging',
    'Heap',
    'JIT',
    'Moth',
    'Profiling',
    'Promise',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_v4__array_element_less_than import ArrayElementLessThan
  from .._q_v4__array_v_table import ArrayVTable
  from .._q_v4__bit_vector import BitVector
  from .._q_v4__block_allocator import BlockAllocator
  from .._q_v4__call_data import CallData
  from .._q_v4__chunk import Chunk
  from .._q_v4__compilation_unit_runtime_data import CompilationUnitRuntimeData
  from .._q_v4__cpp_stack_frame_base import CppStackFrameBase
  from .._q_v4__e_s_table import ESTable
  from .._q_v4__encode import Encode
  from .._q_v4__engine_base import EngineBase
  from .._q_v4__executable_allocator import ExecutableAllocator
  from .._q_v4__function_data import FunctionData
  from .._q_v4__g_c_data import GCData
  from .._q_v4__g_c_iterator_storage import GCIteratorStorage
  from .._q_v4__global_functions import GlobalFunctions
  from .._q_v4__heap_item import HeapItem
  from .._q_v4__huge_item_allocator import HugeItemAllocator
  from .._q_v4__identifier_hash_data import IdentifierHashData
  from .._q_v4__identifier_hash_entry import IdentifierHashEntry
  from .._q_v4__internal_class_entry import InternalClassEntry
  from .._q_v4__internal_class_transition import InternalClassTransition
  from .._q_v4__j_s_call_arguments import JSCallArguments
  from .._q_v4__j_s_call_data import JSCallData
  from .._q_v4__lookup import Lookup
  from .._q_v4__object_iterator import ObjectIterator
  from .._q_v4__optional_returned_value import OptionalReturnedValue
  from .._q_v4__own_property_key_iterator import OwnPropertyKeyIterator
  from .._q_v4__persistent_value import PersistentValue
  from .._q_v4__persistent_value_storage import PersistentValueStorage
  from .._q_v4__property import Property
  from .._q_v4__property_attributes import PropertyAttributes
  from .._q_v4__property_hash import PropertyHash
  from .._q_v4__property_hash_data import PropertyHashData
  from .._q_v4__property_index import PropertyIndex
  from .._q_v4__property_key import PropertyKey
  from .._q_v4__runtime import Runtime
  from .._q_v4__scope import Scope
  from .._q_v4__scoped_property import ScopedProperty
  from .._q_v4__scoped_property_key import ScopedPropertyKey
  from .._q_v4__scoped_stack_frame import ScopedStackFrame
  from .._q_v4__scoped_value import ScopedValue
  from .._q_v4__sparse_array import SparseArray
  from .._q_v4__sparse_array_node import SparseArrayNode
  from .._q_v4__stack_frame import StackFrame
  from .._q_v4__stack_properties import StackProperties
  from .._q_v4__static_value import StaticValue
  from .._q_v4__typed_array_operations import TypedArrayOperations
  from .._q_v4__v_table import VTable
  from .._q_v4__v_table_base import VTableBase
  from .._q_v4__weak_value import WeakValue
  from .._q_v4__write_barrier import WriteBarrier
  from .._q_v4__cpp_stack_frame import CppStackFrame
  from .._q_v4__mark_stack import MarkStack
  from .._q_v4__memory_manager import MemoryManager
  from .._q_v4__object_own_property_key_iterator import ObjectOwnPropertyKeyIterator
  from .._q_v4__value import Value
  from .._q_v4__j_s_types_stack_frame import JSTypesStackFrame
  from .._q_v4__managed import Managed
  from .._q_v4__array_data import ArrayData
  from .._q_v4__execution_context import ExecutionContext
  from .._q_v4__identifier_hash import IdentifierHash
  from .._q_v4__internal_class import InternalClass
  from .._q_v4__json_parser import JsonParser
  from .._q_v4__runtime_helpers import RuntimeHelpers
  from .._q_v4__string_or_symbol import StringOrSymbol
  from .._q_v4__call_context import CallContext
  from .._q_v4__simple_array_data import SimpleArrayData
  from .._q_v4__sparse_array_data import SparseArrayData
  from .._q_v4__string import String
  from .._q_v4__symbol import Symbol
  from .._q_v4__compilation_unit_mapper import CompilationUnitMapper
  from .._q_v4__complex_string import ComplexString
  from .._q_v4__date import Date
  from .._q_v4__executable_compilation_unit import ExecutableCompilationUnit
  from .._q_v4__function import Function
  from .._q_v4__g_c_state_machine import GCStateMachine
  from .._q_v4__identifier_table import IdentifierTable
  from .._q_v4__meta_types_stack_frame import MetaTypesStackFrame
  from .._q_v4__multiply_wrapped_q_object_map import MultiplyWrappedQObjectMap
  from .._q_v4__number_locale import NumberLocale
  from .._q_v4__script import Script
  from .._q_v4__runtime_codegen import RuntimeCodegen
  from .._q_v4__execution_engine import ExecutionEngine
  from .._q_v4__qml_context import QmlContext
  from .._q_v4__resolved_type_reference import ResolvedTypeReference
  from .._q_v4__object import Object
  from .._q_v4__function_object import FunctionObject
  from .._q_v4__promise_capability import PromiseCapability
  from .._q_v4__arguments_object import ArgumentsObject
  from .._q_v4__array_ctor import ArrayCtor
  from .._q_v4__array_iterator_object import ArrayIteratorObject
  from .._q_v4__array_iterator_prototype import ArrayIteratorPrototype
  from .._q_v4__array_object import ArrayObject
  from .._q_v4__atomics import Atomics
  from .._q_v4__boolean_ctor import BooleanCtor
  from .._q_v4__boolean_object import BooleanObject
  from .._q_v4__capabilities_executor_wrapper import CapabilitiesExecutorWrapper
  from .._q_v4__console_object import ConsoleObject
  from .._q_v4__data_view import DataView
  from .._q_v4__data_view_ctor import DataViewCtor
  from .._q_v4__data_view_prototype import DataViewPrototype
  from .._q_v4__date_ctor import DateCtor
  from .._q_v4__date_prototype import DatePrototype
  from .._q_v4__default_class_constructor_function import DefaultClassConstructorFunction
  from .._q_v4__dynamic_function_object import DynamicFunctionObject
  from .._q_v4__error_ctor import ErrorCtor
  from .._q_v4__error_object import ErrorObject
  from .._q_v4__error_prototype import ErrorPrototype
  from .._q_v4__eval_error_prototype import EvalErrorPrototype
  from .._q_v4__eval_function import EvalFunction
  from .._q_v4__for_in_iterator_object import ForInIteratorObject
  from .._q_v4__for_in_iterator_prototype import ForInIteratorPrototype
  from .._q_v4__function_ctor import FunctionCtor
  from .._q_v4__function_prototype import FunctionPrototype
  from .._q_v4__generator_object import GeneratorObject
  from .._q_v4__generator_prototype import GeneratorPrototype
  from .._q_v4__global_extensions import GlobalExtensions
  from .._q_v4__intrinsic_typed_array_ctor import IntrinsicTypedArrayCtor
  from .._q_v4__intrinsic_typed_array_prototype import IntrinsicTypedArrayPrototype
  from .._q_v4__iterator_prototype import IteratorPrototype
  from .._q_v4__java_script_function_object import JavaScriptFunctionObject
  from .._q_v4__json_object import JsonObject
  from .._q_v4__map_iterator_object import MapIteratorObject
  from .._q_v4__map_iterator_prototype import MapIteratorPrototype
  from .._q_v4__map_object import MapObject
  from .._q_v4__math_object import MathObject
  from .._q_v4__member_data import MemberData
  from .._q_v4__module import Module
  from .._q_v4__number_ctor import NumberCtor
  from .._q_v4__number_object import NumberObject
  from .._q_v4__object_ctor import ObjectCtor
  from .._q_v4__object_item import ObjectItem
  from .._q_v4__object_prototype import ObjectPrototype
  from .._q_v4__promise_ctor import PromiseCtor
  from .._q_v4__promise_execution_state import PromiseExecutionState
  from .._q_v4__promise_object import PromiseObject
  from .._q_v4__promise_prototype import PromisePrototype
  from .._q_v4__promise_reaction import PromiseReaction
  from .._q_v4__property_list_prototype import PropertyListPrototype
  from .._q_v4__proxy import Proxy
  from .._q_v4__proxy_object import ProxyObject
  from .._q_v4__q_meta_object_wrapper import QMetaObjectWrapper
  from .._q_v4__q_object_method import QObjectMethod
  from .._q_v4__q_object_wrapper import QObjectWrapper
  from .._q_v4__q_qml_context_wrapper import QQmlContextWrapper
  from .._q_v4__q_qml_enum_wrapper import QQmlEnumWrapper
  from .._q_v4__q_qml_type_wrapper import QQmlTypeWrapper
  from .._q_v4__qml_list_wrapper import QmlListWrapper
  from .._q_v4__qml_signal_handler import QmlSignalHandler
  from .._q_v4__range_error_prototype import RangeErrorPrototype
  from .._q_v4__reference_error_prototype import ReferenceErrorPrototype
  from .._q_v4__reference_object import ReferenceObject
  from .._q_v4__reflect import Reflect
  from .._q_v4__reg_exp_ctor import RegExpCtor
  from .._q_v4__reg_exp_object import RegExpObject
  from .._q_v4__reg_exp_prototype import RegExpPrototype
  from .._q_v4__reject_wrapper import RejectWrapper
  from .._q_v4__resolve_element_wrapper import ResolveElementWrapper
  from .._q_v4__resolve_wrapper import ResolveWrapper
  from .._q_v4__sequence_prototype import SequencePrototype
  from .._q_v4__set_iterator_object import SetIteratorObject
  from .._q_v4__set_iterator_prototype import SetIteratorPrototype
  from .._q_v4__set_object import SetObject
  from .._q_v4__shared_array_buffer import SharedArrayBuffer
  from .._q_v4__shared_array_buffer_ctor import SharedArrayBufferCtor
  from .._q_v4__shared_array_buffer_prototype import SharedArrayBufferPrototype
  from .._q_v4__strict_arguments_object import StrictArgumentsObject
  from .._q_v4__string_ctor import StringCtor
  from .._q_v4__string_iterator_object import StringIteratorObject
  from .._q_v4__string_iterator_prototype import StringIteratorPrototype
  from .._q_v4__string_object import StringObject
  from .._q_v4__symbol_ctor import SymbolCtor
  from .._q_v4__symbol_object import SymbolObject
  from .._q_v4__symbol_prototype import SymbolPrototype
  from .._q_v4__syntax_error_prototype import SyntaxErrorPrototype
  from .._q_v4__type_error_prototype import TypeErrorPrototype
  from .._q_v4__typed_array import TypedArray
  from .._q_v4__typed_array_ctor import TypedArrayCtor
  from .._q_v4__typed_array_prototype import TypedArrayPrototype
  from .._q_v4__u_r_i_error_prototype import URIErrorPrototype
  from .._q_v4__url_ctor import UrlCtor
  from .._q_v4__url_object import UrlObject
  from .._q_v4__url_prototype import UrlPrototype
  from .._q_v4__url_search_params_ctor import UrlSearchParamsCtor
  from .._q_v4__url_search_params_object import UrlSearchParamsObject
  from .._q_v4__url_search_params_prototype import UrlSearchParamsPrototype
  from .._q_v4__variant_association_prototype import VariantAssociationPrototype
  from .._q_v4__variant_object import VariantObject
  from .._q_v4__weak_map_ctor import WeakMapCtor
  from .._q_v4__weak_map_prototype import WeakMapPrototype
  from .._q_v4__weak_set_ctor import WeakSetCtor
  from .._q_v4__weak_set_prototype import WeakSetPrototype
  from .._q_v4__array_buffer import ArrayBuffer
  from .._q_v4__array_buffer_ctor import ArrayBufferCtor
  from .._q_v4__array_buffer_prototype import ArrayBufferPrototype
  from .._q_v4__array_prototype import ArrayPrototype
  from .._q_v4__arrow_function import ArrowFunction
  from .._q_v4__boolean_prototype import BooleanPrototype
  from .._q_v4__bound_function import BoundFunction
  from .._q_v4__date_object import DateObject
  from .._q_v4__eval_error_ctor import EvalErrorCtor
  from .._q_v4__eval_error_object import EvalErrorObject
  from .._q_v4__generator_function_ctor import GeneratorFunctionCtor
  from .._q_v4__indexed_builtin_function import IndexedBuiltinFunction
  from .._q_v4__map_ctor import MapCtor
  from .._q_v4__map_prototype import MapPrototype
  from .._q_v4__number_prototype import NumberPrototype
  from .._q_v4__proxy_function_object import ProxyFunctionObject
  from .._q_v4__q_qml_binding_function import QQmlBindingFunction
  from .._q_v4__q_qml_type_constructor import QQmlTypeConstructor
  from .._q_v4__q_qml_value_type_wrapper import QQmlValueTypeWrapper
  from .._q_v4__range_error_ctor import RangeErrorCtor
  from .._q_v4__range_error_object import RangeErrorObject
  from .._q_v4__reference_error_ctor import ReferenceErrorCtor
  from .._q_v4__reference_error_object import ReferenceErrorObject
  from .._q_v4__sequence import Sequence
  from .._q_v4__set_ctor import SetCtor
  from .._q_v4__set_prototype import SetPrototype
  from .._q_v4__string_prototype import StringPrototype
  from .._q_v4__syntax_error_ctor import SyntaxErrorCtor
  from .._q_v4__syntax_error_object import SyntaxErrorObject
  from .._q_v4__type_error_ctor import TypeErrorCtor
  from .._q_v4__type_error_object import TypeErrorObject
  from .._q_v4__u_r_i_error_ctor import URIErrorCtor
  from .._q_v4__u_r_i_error_object import URIErrorObject
  from .._q_v4__variant_association_object import VariantAssociationObject
  from .._q_v4__variant_prototype import VariantPrototype
  from .._q_v4__bound_constructor import BoundConstructor
  from .._q_v4__generator_function import GeneratorFunction
  from .._q_v4__member_function import MemberFunction
  from .._q_v4__proxy_constructor_object import ProxyConstructorObject
  from .._q_v4__script_function import ScriptFunction
  from .._q_v4__constructor_function import ConstructorFunction
  from .._q_v4__member_generator_function import MemberGeneratorFunction
  from . import CompiledData
  from . import Compiler
  from . import Debugging
  from . import Heap
  from . import JIT
  from . import Moth
  from . import Profiling
  from . import Promise
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'ArrayElementLessThan': '_q_v4__array_element_less_than',
      'ArrayVTable': '_q_v4__array_v_table',
      'BitVector': '_q_v4__bit_vector',
      'BlockAllocator': '_q_v4__block_allocator',
      'CallData': '_q_v4__call_data',
      'Chunk': '_q_v4__chunk',
      'CompilationUnitRuntimeData': '_q_v4__compilation_unit_runtime_data',
      'CppStackFrameBase': '_q_v4__cpp_stack_frame_base',
      'ESTable': '_q_v4__e_s_table',
      'Encode': '_q_v4__encode',
      'EngineBase': '_q_v4__engine_base',
      'ExecutableAllocator': '_q_v4__executable_allocator',
      'FunctionData': '_q_v4__function_data',
      'GCData': '_q_v4__g_c_data',
      'GCIteratorStorage': '_q_v4__g_c_iterator_storage',
      'GlobalFunctions': '_q_v4__global_functions',
      'HeapItem': '_q_v4__heap_item',
      'HugeItemAllocator': '_q_v4__huge_item_allocator',
      'IdentifierHashData': '_q_v4__identifier_hash_data',
      'IdentifierHashEntry': '_q_v4__identifier_hash_entry',
      'InternalClassEntry': '_q_v4__internal_class_entry',
      'InternalClassTransition': '_q_v4__internal_class_transition',
      'JSCallArguments': '_q_v4__j_s_call_arguments',
      'JSCallData': '_q_v4__j_s_call_data',
      'Lookup': '_q_v4__lookup',
      'ObjectIterator': '_q_v4__object_iterator',
      'OptionalReturnedValue': '_q_v4__optional_returned_value',
      'OwnPropertyKeyIterator': '_q_v4__own_property_key_iterator',
      'PersistentValue': '_q_v4__persistent_value',
      'PersistentValueStorage': '_q_v4__persistent_value_storage',
      'Property': '_q_v4__property',
      'PropertyAttributes': '_q_v4__property_attributes',
      'PropertyHash': '_q_v4__property_hash',
      'PropertyHashData': '_q_v4__property_hash_data',
      'PropertyIndex': '_q_v4__property_index',
      'PropertyKey': '_q_v4__property_key',
      'Runtime': '_q_v4__runtime',
      'Scope': '_q_v4__scope',
      'ScopedProperty': '_q_v4__scoped_property',
      'ScopedPropertyKey': '_q_v4__scoped_property_key',
      'ScopedStackFrame': '_q_v4__scoped_stack_frame',
      'ScopedValue': '_q_v4__scoped_value',
      'SparseArray': '_q_v4__sparse_array',
      'SparseArrayNode': '_q_v4__sparse_array_node',
      'StackFrame': '_q_v4__stack_frame',
      'StackProperties': '_q_v4__stack_properties',
      'StaticValue': '_q_v4__static_value',
      'TypedArrayOperations': '_q_v4__typed_array_operations',
      'VTable': '_q_v4__v_table',
      'VTableBase': '_q_v4__v_table_base',
      'WeakValue': '_q_v4__weak_value',
      'WriteBarrier': '_q_v4__write_barrier',
      'CppStackFrame': '_q_v4__cpp_stack_frame',
      'MarkStack': '_q_v4__mark_stack',
      'MemoryManager': '_q_v4__memory_manager',
      'ObjectOwnPropertyKeyIterator': '_q_v4__object_own_property_key_iterator',
      'Value': '_q_v4__value',
      'JSTypesStackFrame': '_q_v4__j_s_types_stack_frame',
      'Managed': '_q_v4__managed',
      'ArrayData': '_q_v4__array_data',
      'ExecutionContext': '_q_v4__execution_context',
      'IdentifierHash': '_q_v4__identifier_hash',
      'InternalClass': '_q_v4__internal_class',
      'JsonParser': '_q_v4__json_parser',
      'RuntimeHelpers': '_q_v4__runtime_helpers',
      'StringOrSymbol': '_q_v4__string_or_symbol',
      'CallContext': '_q_v4__call_context',
      'SimpleArrayData': '_q_v4__simple_array_data',
      'SparseArrayData': '_q_v4__sparse_array_data',
      'String': '_q_v4__string',
      'Symbol': '_q_v4__symbol',
      'CompilationUnitMapper': '_q_v4__compilation_unit_mapper',
      'ComplexString': '_q_v4__complex_string',
      'Date': '_q_v4__date',
      'ExecutableCompilationUnit': '_q_v4__executable_compilation_unit',
      'Function': '_q_v4__function',
      'GCStateMachine': '_q_v4__g_c_state_machine',
      'IdentifierTable': '_q_v4__identifier_table',
      'MetaTypesStackFrame': '_q_v4__meta_types_stack_frame',
      'MultiplyWrappedQObjectMap': '_q_v4__multiply_wrapped_q_object_map',
      'NumberLocale': '_q_v4__number_locale',
      'Script': '_q_v4__script',
      'RuntimeCodegen': '_q_v4__runtime_codegen',
      'ExecutionEngine': '_q_v4__execution_engine',
      'QmlContext': '_q_v4__qml_context',
      'ResolvedTypeReference': '_q_v4__resolved_type_reference',
      'Object': '_q_v4__object',
      'FunctionObject': '_q_v4__function_object',
      'PromiseCapability': '_q_v4__promise_capability',
      'ArgumentsObject': '_q_v4__arguments_object',
      'ArrayCtor': '_q_v4__array_ctor',
      'ArrayIteratorObject': '_q_v4__array_iterator_object',
      'ArrayIteratorPrototype': '_q_v4__array_iterator_prototype',
      'ArrayObject': '_q_v4__array_object',
      'Atomics': '_q_v4__atomics',
      'BooleanCtor': '_q_v4__boolean_ctor',
      'BooleanObject': '_q_v4__boolean_object',
      'CapabilitiesExecutorWrapper': '_q_v4__capabilities_executor_wrapper',
      'ConsoleObject': '_q_v4__console_object',
      'DataView': '_q_v4__data_view',
      'DataViewCtor': '_q_v4__data_view_ctor',
      'DataViewPrototype': '_q_v4__data_view_prototype',
      'DateCtor': '_q_v4__date_ctor',
      'DatePrototype': '_q_v4__date_prototype',
      'DefaultClassConstructorFunction': '_q_v4__default_class_constructor_function',
      'DynamicFunctionObject': '_q_v4__dynamic_function_object',
      'ErrorCtor': '_q_v4__error_ctor',
      'ErrorObject': '_q_v4__error_object',
      'ErrorPrototype': '_q_v4__error_prototype',
      'EvalErrorPrototype': '_q_v4__eval_error_prototype',
      'EvalFunction': '_q_v4__eval_function',
      'ForInIteratorObject': '_q_v4__for_in_iterator_object',
      'ForInIteratorPrototype': '_q_v4__for_in_iterator_prototype',
      'FunctionCtor': '_q_v4__function_ctor',
      'FunctionPrototype': '_q_v4__function_prototype',
      'GeneratorObject': '_q_v4__generator_object',
      'GeneratorPrototype': '_q_v4__generator_prototype',
      'GlobalExtensions': '_q_v4__global_extensions',
      'IntrinsicTypedArrayCtor': '_q_v4__intrinsic_typed_array_ctor',
      'IntrinsicTypedArrayPrototype': '_q_v4__intrinsic_typed_array_prototype',
      'IteratorPrototype': '_q_v4__iterator_prototype',
      'JavaScriptFunctionObject': '_q_v4__java_script_function_object',
      'JsonObject': '_q_v4__json_object',
      'MapIteratorObject': '_q_v4__map_iterator_object',
      'MapIteratorPrototype': '_q_v4__map_iterator_prototype',
      'MapObject': '_q_v4__map_object',
      'MathObject': '_q_v4__math_object',
      'MemberData': '_q_v4__member_data',
      'Module': '_q_v4__module',
      'NumberCtor': '_q_v4__number_ctor',
      'NumberObject': '_q_v4__number_object',
      'ObjectCtor': '_q_v4__object_ctor',
      'ObjectItem': '_q_v4__object_item',
      'ObjectPrototype': '_q_v4__object_prototype',
      'PromiseCtor': '_q_v4__promise_ctor',
      'PromiseExecutionState': '_q_v4__promise_execution_state',
      'PromiseObject': '_q_v4__promise_object',
      'PromisePrototype': '_q_v4__promise_prototype',
      'PromiseReaction': '_q_v4__promise_reaction',
      'PropertyListPrototype': '_q_v4__property_list_prototype',
      'Proxy': '_q_v4__proxy',
      'ProxyObject': '_q_v4__proxy_object',
      'QMetaObjectWrapper': '_q_v4__q_meta_object_wrapper',
      'QObjectMethod': '_q_v4__q_object_method',
      'QObjectWrapper': '_q_v4__q_object_wrapper',
      'QQmlContextWrapper': '_q_v4__q_qml_context_wrapper',
      'QQmlEnumWrapper': '_q_v4__q_qml_enum_wrapper',
      'QQmlTypeWrapper': '_q_v4__q_qml_type_wrapper',
      'QmlListWrapper': '_q_v4__qml_list_wrapper',
      'QmlSignalHandler': '_q_v4__qml_signal_handler',
      'RangeErrorPrototype': '_q_v4__range_error_prototype',
      'ReferenceErrorPrototype': '_q_v4__reference_error_prototype',
      'ReferenceObject': '_q_v4__reference_object',
      'Reflect': '_q_v4__reflect',
      'RegExpCtor': '_q_v4__reg_exp_ctor',
      'RegExpObject': '_q_v4__reg_exp_object',
      'RegExpPrototype': '_q_v4__reg_exp_prototype',
      'RejectWrapper': '_q_v4__reject_wrapper',
      'ResolveElementWrapper': '_q_v4__resolve_element_wrapper',
      'ResolveWrapper': '_q_v4__resolve_wrapper',
      'SequencePrototype': '_q_v4__sequence_prototype',
      'SetIteratorObject': '_q_v4__set_iterator_object',
      'SetIteratorPrototype': '_q_v4__set_iterator_prototype',
      'SetObject': '_q_v4__set_object',
      'SharedArrayBuffer': '_q_v4__shared_array_buffer',
      'SharedArrayBufferCtor': '_q_v4__shared_array_buffer_ctor',
      'SharedArrayBufferPrototype': '_q_v4__shared_array_buffer_prototype',
      'StrictArgumentsObject': '_q_v4__strict_arguments_object',
      'StringCtor': '_q_v4__string_ctor',
      'StringIteratorObject': '_q_v4__string_iterator_object',
      'StringIteratorPrototype': '_q_v4__string_iterator_prototype',
      'StringObject': '_q_v4__string_object',
      'SymbolCtor': '_q_v4__symbol_ctor',
      'SymbolObject': '_q_v4__symbol_object',
      'SymbolPrototype': '_q_v4__symbol_prototype',
      'SyntaxErrorPrototype': '_q_v4__syntax_error_prototype',
      'TypeErrorPrototype': '_q_v4__type_error_prototype',
      'TypedArray': '_q_v4__typed_array',
      'TypedArrayCtor': '_q_v4__typed_array_ctor',
      'TypedArrayPrototype': '_q_v4__typed_array_prototype',
      'URIErrorPrototype': '_q_v4__u_r_i_error_prototype',
      'UrlCtor': '_q_v4__url_ctor',
      'UrlObject': '_q_v4__url_object',
      'UrlPrototype': '_q_v4__url_prototype',
      'UrlSearchParamsCtor': '_q_v4__url_search_params_ctor',
      'UrlSearchParamsObject': '_q_v4__url_search_params_object',
      'UrlSearchParamsPrototype': '_q_v4__url_search_params_prototype',
      'VariantAssociationPrototype': '_q_v4__variant_association_prototype',
      'VariantObject': '_q_v4__variant_object',
      'WeakMapCtor': '_q_v4__weak_map_ctor',
      'WeakMapPrototype': '_q_v4__weak_map_prototype',
      'WeakSetCtor': '_q_v4__weak_set_ctor',
      'WeakSetPrototype': '_q_v4__weak_set_prototype',
      'ArrayBuffer': '_q_v4__array_buffer',
      'ArrayBufferCtor': '_q_v4__array_buffer_ctor',
      'ArrayBufferPrototype': '_q_v4__array_buffer_prototype',
      'ArrayPrototype': '_q_v4__array_prototype',
      'ArrowFunction': '_q_v4__arrow_function',
      'BooleanPrototype': '_q_v4__boolean_prototype',
      'BoundFunction': '_q_v4__bound_function',
      'DateObject': '_q_v4__date_object',
      'EvalErrorCtor': '_q_v4__eval_error_ctor',
      'EvalErrorObject': '_q_v4__eval_error_object',
      'GeneratorFunctionCtor': '_q_v4__generator_function_ctor',
      'IndexedBuiltinFunction': '_q_v4__indexed_builtin_function',
      'MapCtor': '_q_v4__map_ctor',
      'MapPrototype': '_q_v4__map_prototype',
      'NumberPrototype': '_q_v4__number_prototype',
      'ProxyFunctionObject': '_q_v4__proxy_function_object',
      'QQmlBindingFunction': '_q_v4__q_qml_binding_function',
      'QQmlTypeConstructor': '_q_v4__q_qml_type_constructor',
      'QQmlValueTypeWrapper': '_q_v4__q_qml_value_type_wrapper',
      'RangeErrorCtor': '_q_v4__range_error_ctor',
      'RangeErrorObject': '_q_v4__range_error_object',
      'ReferenceErrorCtor': '_q_v4__reference_error_ctor',
      'ReferenceErrorObject': '_q_v4__reference_error_object',
      'Sequence': '_q_v4__sequence',
      'SetCtor': '_q_v4__set_ctor',
      'SetPrototype': '_q_v4__set_prototype',
      'StringPrototype': '_q_v4__string_prototype',
      'SyntaxErrorCtor': '_q_v4__syntax_error_ctor',
      'SyntaxErrorObject': '_q_v4__syntax_error_object',
      'TypeErrorCtor': '_q_v4__type_error_ctor',
      'TypeErrorObject': '_q_v4__type_error_object',
      'URIErrorCtor': '_q_v4__u_r_i_error_ctor',
      'URIErrorObject': '_q_v4__u_r_i_error_object',
      'VariantAssociationObject': '_q_v4__variant_association_object',
      'VariantPrototype': '_q_v4__variant_prototype',
      'BoundConstructor': '_q_v4__bound_constructor',
      'GeneratorFunction': '_q_v4__generator_function',
      'MemberFunction': '_q_v4__member_function',
      'ProxyConstructorObject': '_q_v4__proxy_constructor_object',
      'ScriptFunction': '_q_v4__script_function',
      'ConstructorFunction': '_q_v4__constructor_function',
      'MemberGeneratorFunction': '_q_v4__member_generator_function',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('CompiledData', 'Compiler', 'Debugging', 'Heap', 'JIT', 'Moth', 'Profiling', 'Promise',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QV4.ArrayElementLessThan'. Python calls this for a name
    the package does not hold yet, and what it gives is kept here for the
    next time.

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
      module = importlib.import_module('..%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
