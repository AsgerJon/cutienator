"""
The namespace 'QV4::CompiledData' of Qt, a package of 'cutienator.QtQml':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQml import QV4
  QV4.CompiledData.Alias

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from ..._q_v4__compiled_data import CompiledData as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'Alias',
    'Block',
    'Class',
    'CodeOffsetToLineAndStatement',
    'Enum',
    'EnumValue',
    'ExportEntry',
    'Function',
    'Import',
    'ImportEntry',
    'InlineComponent',
    'JSClass',
    'JSClassMember',
    'Location',
    'Lookup',
    'Method',
    'Object',
    'Parameter',
    'ParameterType',
    'Property',
    'QmlUnit',
    'RegExp',
    'RequiredPropertyExtraData',
    'Signal',
    'TemplateObject',
    'TranslationData',
    'TypeReference',
    'TypeReferenceMap',
    'Binding',
    'SaveableUnitPointer',
    'String',
    'Unit',
    'ResolvedTypeReferenceMap',
    'CompilationUnit',
    'InlineComponentData',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ..._q_v4__compiled_data__alias import Alias
  from ..._q_v4__compiled_data__block import Block
  from ..._q_v4__compiled_data__class import Class
  from ..._q_v4__compiled_data__code_offset_to_line_and_statement import CodeOffsetToLineAndStatement
  from ..._q_v4__compiled_data__enum import Enum
  from ..._q_v4__compiled_data__enum_value import EnumValue
  from ..._q_v4__compiled_data__export_entry import ExportEntry
  from ..._q_v4__compiled_data__function import Function
  from ..._q_v4__compiled_data__import import Import
  from ..._q_v4__compiled_data__import_entry import ImportEntry
  from ..._q_v4__compiled_data__inline_component import InlineComponent
  from ..._q_v4__compiled_data__j_s_class import JSClass
  from ..._q_v4__compiled_data__j_s_class_member import JSClassMember
  from ..._q_v4__compiled_data__location import Location
  from ..._q_v4__compiled_data__lookup import Lookup
  from ..._q_v4__compiled_data__method import Method
  from ..._q_v4__compiled_data__object import Object
  from ..._q_v4__compiled_data__parameter import Parameter
  from ..._q_v4__compiled_data__parameter_type import ParameterType
  from ..._q_v4__compiled_data__property import Property
  from ..._q_v4__compiled_data__qml_unit import QmlUnit
  from ..._q_v4__compiled_data__reg_exp import RegExp
  from ..._q_v4__compiled_data__required_property_extra_data import RequiredPropertyExtraData
  from ..._q_v4__compiled_data__signal import Signal
  from ..._q_v4__compiled_data__template_object import TemplateObject
  from ..._q_v4__compiled_data__translation_data import TranslationData
  from ..._q_v4__compiled_data__type_reference import TypeReference
  from ..._q_v4__compiled_data__type_reference_map import TypeReferenceMap
  from ..._q_v4__compiled_data__binding import Binding
  from ..._q_v4__compiled_data__saveable_unit_pointer import SaveableUnitPointer
  from ..._q_v4__compiled_data__string import String
  from ..._q_v4__compiled_data__unit import Unit
  from ..._q_v4__compiled_data__resolved_type_reference_map import ResolvedTypeReferenceMap
  from ..._q_v4__compiled_data__compilation_unit import CompilationUnit
  from ..._q_v4__compiled_data__inline_component_data import InlineComponentData
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'Alias': '_q_v4__compiled_data__alias',
      'Block': '_q_v4__compiled_data__block',
      'Class': '_q_v4__compiled_data__class',
      'CodeOffsetToLineAndStatement': '_q_v4__compiled_data__code_offset_to_line_and_statement',
      'Enum': '_q_v4__compiled_data__enum',
      'EnumValue': '_q_v4__compiled_data__enum_value',
      'ExportEntry': '_q_v4__compiled_data__export_entry',
      'Function': '_q_v4__compiled_data__function',
      'Import': '_q_v4__compiled_data__import',
      'ImportEntry': '_q_v4__compiled_data__import_entry',
      'InlineComponent': '_q_v4__compiled_data__inline_component',
      'JSClass': '_q_v4__compiled_data__j_s_class',
      'JSClassMember': '_q_v4__compiled_data__j_s_class_member',
      'Location': '_q_v4__compiled_data__location',
      'Lookup': '_q_v4__compiled_data__lookup',
      'Method': '_q_v4__compiled_data__method',
      'Object': '_q_v4__compiled_data__object',
      'Parameter': '_q_v4__compiled_data__parameter',
      'ParameterType': '_q_v4__compiled_data__parameter_type',
      'Property': '_q_v4__compiled_data__property',
      'QmlUnit': '_q_v4__compiled_data__qml_unit',
      'RegExp': '_q_v4__compiled_data__reg_exp',
      'RequiredPropertyExtraData': '_q_v4__compiled_data__required_property_extra_data',
      'Signal': '_q_v4__compiled_data__signal',
      'TemplateObject': '_q_v4__compiled_data__template_object',
      'TranslationData': '_q_v4__compiled_data__translation_data',
      'TypeReference': '_q_v4__compiled_data__type_reference',
      'TypeReferenceMap': '_q_v4__compiled_data__type_reference_map',
      'Binding': '_q_v4__compiled_data__binding',
      'SaveableUnitPointer': '_q_v4__compiled_data__saveable_unit_pointer',
      'String': '_q_v4__compiled_data__string',
      'Unit': '_q_v4__compiled_data__unit',
      'ResolvedTypeReferenceMap': '_q_v4__compiled_data__resolved_type_reference_map',
      'CompilationUnit': '_q_v4__compiled_data__compilation_unit',
      'InlineComponentData': '_q_v4__compiled_data__inline_component_data',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QV4.CompiledData.Alias'. Python calls this for a name
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
      module = importlib.import_module('...%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
