"""
The namespace 'QtPrivate' of Qt, a package of 'cutienator.QtCore':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtCore import QtPrivate
  QtPrivate.ArgBase

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from .._qt_private import QtPrivate as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'ArgBase',
    'BindingFunctionVTable',
    'CompareAgainstLiteralZero',
    'Deprecated_t',
    'EnableInternalData',
    'FunctorCallBase',
    'MSVCWorkAround',
    'QBindableInterface',
    'QBindingStatusAccessToken',
    'QCaseInsensitiveLatin1Hash',
    'QCaseSensitiveLatin1Hash',
    'QContainerImplHelper',
    'QHashCombineCommutativeMixer',
    'QHashCombineMixer',
    'QMetaTypeInterface',
    'QPropertyBindingFunction',
    'QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel',
    'QTypeNormalizer',
    'QVersionTag',
    'ReadWriteExtra',
    'RefCount',
    'RefCounted',
    'ResultItem',
    'ResultIteratorBase',
    'ResultStoreBase',
    'SlotObjSharedPtr',
    'UnwrapHandler',
    'hide_char8_t',
    'wrap_char',
    'AlignedQArrayData',
    'CompatPropertySafePoint',
    'CurrentCompatPropertyThief',
    'ExceptionStore',
    'QLatin1StringArg',
    'QRegularExpressionMatchIteratorRangeBasedForIterator',
    'QIOOperationDataStorage',
    'QAnyStringArg',
    'QStringViewArg',
    'QXmlString',
    'XmlStringRef',
    'QSlotObjectBase',
    'BindingStatusOrList',
    'QModelIndexWrapper',
    'QPropertyAdaptorSlotObject',
    'QVariantTypeCoercer',
    'StreamStateSaver',
    'BindingEvaluationState',
    'QPropertyBindingData',
    'BindableWarnings',
    'QCheckedIntegers',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt_private__arg_base import ArgBase
  from .._qt_private__binding_function_v_table import BindingFunctionVTable
  from .._qt_private__compare_against_literal_zero import CompareAgainstLiteralZero
  from .._qt_private__deprecated_t import Deprecated_t
  from .._qt_private__enable_internal_data import EnableInternalData
  from .._qt_private__functor_call_base import FunctorCallBase
  from .._qt_private__m_s_v_c_work_around import MSVCWorkAround
  from .._qt_private__q_bindable_interface import QBindableInterface
  from .._qt_private__q_binding_status_access_token import QBindingStatusAccessToken
  from .._qt_private__q_case_insensitive_latin1_hash import QCaseInsensitiveLatin1Hash
  from .._qt_private__q_case_sensitive_latin1_hash import QCaseSensitiveLatin1Hash
  from .._qt_private__q_container_impl_helper import QContainerImplHelper
  from .._qt_private__q_hash_combine_commutative_mixer import QHashCombineCommutativeMixer
  from .._qt_private__q_hash_combine_mixer import QHashCombineMixer
  from .._qt_private__q_meta_type_interface import QMetaTypeInterface
  from .._qt_private__q_property_binding_function import QPropertyBindingFunction
  from .._qt_private__q_regular_expression_match_iterator_range_based_for_iterator_sentinel import QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel
  from .._qt_private__q_type_normalizer import QTypeNormalizer
  from .._qt_private__q_version_tag import QVersionTag
  from .._qt_private__read_write_extra import ReadWriteExtra
  from .._qt_private__ref_count import RefCount
  from .._qt_private__ref_counted import RefCounted
  from .._qt_private__result_item import ResultItem
  from .._qt_private__result_iterator_base import ResultIteratorBase
  from .._qt_private__result_store_base import ResultStoreBase
  from .._qt_private__slot_obj_shared_ptr import SlotObjSharedPtr
  from .._qt_private__unwrap_handler import UnwrapHandler
  from .._qt_private__hide_char8_t import hide_char8_t
  from .._qt_private__wrap_char import wrap_char
  from .._qt_private__aligned_q_array_data import AlignedQArrayData
  from .._qt_private__compat_property_safe_point import CompatPropertySafePoint
  from .._qt_private__current_compat_property_thief import CurrentCompatPropertyThief
  from .._qt_private__exception_store import ExceptionStore
  from .._qt_private__q_latin1_string_arg import QLatin1StringArg
  from .._qt_private__q_regular_expression_match_iterator_range_based_for_iterator import QRegularExpressionMatchIteratorRangeBasedForIterator
  from .._qt_private__q_i_o_operation_data_storage import QIOOperationDataStorage
  from .._qt_private__q_any_string_arg import QAnyStringArg
  from .._qt_private__q_string_view_arg import QStringViewArg
  from .._qt_private__q_xml_string import QXmlString
  from .._qt_private__xml_string_ref import XmlStringRef
  from .._qt_private__q_slot_object_base import QSlotObjectBase
  from .._qt_private__binding_status_or_list import BindingStatusOrList
  from .._qt_private__q_model_index_wrapper import QModelIndexWrapper
  from .._qt_private__q_property_adaptor_slot_object import QPropertyAdaptorSlotObject
  from .._qt_private__q_variant_type_coercer import QVariantTypeCoercer
  from .._qt_private__stream_state_saver import StreamStateSaver
  from .._qt_private__binding_evaluation_state import BindingEvaluationState
  from .._qt_private__q_property_binding_data import QPropertyBindingData
  from . import BindableWarnings
  from . import QCheckedIntegers
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'ArgBase': '_qt_private__arg_base',
      'BindingFunctionVTable': '_qt_private__binding_function_v_table',
      'CompareAgainstLiteralZero': '_qt_private__compare_against_literal_zero',
      'Deprecated_t': '_qt_private__deprecated_t',
      'EnableInternalData': '_qt_private__enable_internal_data',
      'FunctorCallBase': '_qt_private__functor_call_base',
      'MSVCWorkAround': '_qt_private__m_s_v_c_work_around',
      'QBindableInterface': '_qt_private__q_bindable_interface',
      'QBindingStatusAccessToken': '_qt_private__q_binding_status_access_token',
      'QCaseInsensitiveLatin1Hash': '_qt_private__q_case_insensitive_latin1_hash',
      'QCaseSensitiveLatin1Hash': '_qt_private__q_case_sensitive_latin1_hash',
      'QContainerImplHelper': '_qt_private__q_container_impl_helper',
      'QHashCombineCommutativeMixer': '_qt_private__q_hash_combine_commutative_mixer',
      'QHashCombineMixer': '_qt_private__q_hash_combine_mixer',
      'QMetaTypeInterface': '_qt_private__q_meta_type_interface',
      'QPropertyBindingFunction': '_qt_private__q_property_binding_function',
      'QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel': '_qt_private__q_regular_expression_match_iterator_range_based_for_iterator_sentinel',
      'QTypeNormalizer': '_qt_private__q_type_normalizer',
      'QVersionTag': '_qt_private__q_version_tag',
      'ReadWriteExtra': '_qt_private__read_write_extra',
      'RefCount': '_qt_private__ref_count',
      'RefCounted': '_qt_private__ref_counted',
      'ResultItem': '_qt_private__result_item',
      'ResultIteratorBase': '_qt_private__result_iterator_base',
      'ResultStoreBase': '_qt_private__result_store_base',
      'SlotObjSharedPtr': '_qt_private__slot_obj_shared_ptr',
      'UnwrapHandler': '_qt_private__unwrap_handler',
      'hide_char8_t': '_qt_private__hide_char8_t',
      'wrap_char': '_qt_private__wrap_char',
      'AlignedQArrayData': '_qt_private__aligned_q_array_data',
      'CompatPropertySafePoint': '_qt_private__compat_property_safe_point',
      'CurrentCompatPropertyThief': '_qt_private__current_compat_property_thief',
      'ExceptionStore': '_qt_private__exception_store',
      'QLatin1StringArg': '_qt_private__q_latin1_string_arg',
      'QRegularExpressionMatchIteratorRangeBasedForIterator': '_qt_private__q_regular_expression_match_iterator_range_based_for_iterator',
      'QIOOperationDataStorage': '_qt_private__q_i_o_operation_data_storage',
      'QAnyStringArg': '_qt_private__q_any_string_arg',
      'QStringViewArg': '_qt_private__q_string_view_arg',
      'QXmlString': '_qt_private__q_xml_string',
      'XmlStringRef': '_qt_private__xml_string_ref',
      'QSlotObjectBase': '_qt_private__q_slot_object_base',
      'BindingStatusOrList': '_qt_private__binding_status_or_list',
      'QModelIndexWrapper': '_qt_private__q_model_index_wrapper',
      'QPropertyAdaptorSlotObject': '_qt_private__q_property_adaptor_slot_object',
      'QVariantTypeCoercer': '_qt_private__q_variant_type_coercer',
      'StreamStateSaver': '_qt_private__stream_state_saver',
      'BindingEvaluationState': '_qt_private__binding_evaluation_state',
      'QPropertyBindingData': '_qt_private__q_property_binding_data',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('BindableWarnings', 'QCheckedIntegers',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QtPrivate.ArgBase'. Python calls this for a name the
    package does not hold yet, and what it gives is kept here for the next
    time.

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
