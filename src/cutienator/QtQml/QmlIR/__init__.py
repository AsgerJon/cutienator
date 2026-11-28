"""
The namespace 'QmlIR' of Qt, a package of 'cutienator.QtQml':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQml import QmlIR
  QmlIR.CompiledFunctionOrExpression

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
    'CompiledFunctionOrExpression',
    'Enum',
    'Function',
    'Pragma',
    'QmlUnitGenerator',
    'Alias',
    'EnumValue',
    'InlineComponent',
    'Property',
    'RequiredPropertyExtraData',
    'Document',
    'Parameter',
    'Binding',
    'IRBuilder',
    'Object',
    'ScriptDirectivesCollector',
    'Signal',
    'JSCodeGen',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qml_i_r__compiled_function_or_expression import CompiledFunctionOrExpression
  from .._qml_i_r__enum import Enum
  from .._qml_i_r__function import Function
  from .._qml_i_r__pragma import Pragma
  from .._qml_i_r__qml_unit_generator import QmlUnitGenerator
  from .._qml_i_r__alias import Alias
  from .._qml_i_r__enum_value import EnumValue
  from .._qml_i_r__inline_component import InlineComponent
  from .._qml_i_r__property import Property
  from .._qml_i_r__required_property_extra_data import RequiredPropertyExtraData
  from .._qml_i_r__document import Document
  from .._qml_i_r__parameter import Parameter
  from .._qml_i_r__binding import Binding
  from .._qml_i_r__i_r_builder import IRBuilder
  from .._qml_i_r__object import Object
  from .._qml_i_r__script_directives_collector import ScriptDirectivesCollector
  from .._qml_i_r__signal import Signal
  from .._qml_i_r__j_s_code_gen import JSCodeGen
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'CompiledFunctionOrExpression': '_qml_i_r__compiled_function_or_expression',
      'Enum': '_qml_i_r__enum',
      'Function': '_qml_i_r__function',
      'Pragma': '_qml_i_r__pragma',
      'QmlUnitGenerator': '_qml_i_r__qml_unit_generator',
      'Alias': '_qml_i_r__alias',
      'EnumValue': '_qml_i_r__enum_value',
      'InlineComponent': '_qml_i_r__inline_component',
      'Property': '_qml_i_r__property',
      'RequiredPropertyExtraData': '_qml_i_r__required_property_extra_data',
      'Document': '_qml_i_r__document',
      'Parameter': '_qml_i_r__parameter',
      'Binding': '_qml_i_r__binding',
      'IRBuilder': '_qml_i_r__i_r_builder',
      'Object': '_qml_i_r__object',
      'ScriptDirectivesCollector': '_qml_i_r__script_directives_collector',
      'Signal': '_qml_i_r__signal',
      'JSCodeGen': '_qml_i_r__j_s_code_gen',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QmlIR.CompiledFunctionOrExpression'. Python calls this
    for a name the package does not hold yet, and what it gives is kept here
    for the next time.

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
    return [*__all__]
