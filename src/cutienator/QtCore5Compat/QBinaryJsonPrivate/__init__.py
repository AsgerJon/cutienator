"""
The namespace 'QBinaryJsonPrivate' of Qt, a package of 'cutienator.QtCore5Compat':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtCore5Compat import QBinaryJsonPrivate
  QBinaryJsonPrivate.Base

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
    'Base',
    'ConstData',
    'Header',
    'IsValidFrame',
    'Array',
    'DocumentFrame',
    'Entry',
    'Latin1String',
    'Object',
    'String',
    'MutableData',
    'Value',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_binary_json_private__base import Base
  from .._q_binary_json_private__const_data import ConstData
  from .._q_binary_json_private__header import Header
  from .._q_binary_json_private__is_valid_frame import IsValidFrame
  from .._q_binary_json_private__array import Array
  from .._q_binary_json_private__document_frame import DocumentFrame
  from .._q_binary_json_private__entry import Entry
  from .._q_binary_json_private__latin1_string import Latin1String
  from .._q_binary_json_private__object import Object
  from .._q_binary_json_private__string import String
  from .._q_binary_json_private__mutable_data import MutableData
  from .._q_binary_json_private__value import Value
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'Base': '_q_binary_json_private__base',
      'ConstData': '_q_binary_json_private__const_data',
      'Header': '_q_binary_json_private__header',
      'IsValidFrame': '_q_binary_json_private__is_valid_frame',
      'Array': '_q_binary_json_private__array',
      'DocumentFrame': '_q_binary_json_private__document_frame',
      'Entry': '_q_binary_json_private__entry',
      'Latin1String': '_q_binary_json_private__latin1_string',
      'Object': '_q_binary_json_private__object',
      'String': '_q_binary_json_private__string',
      'MutableData': '_q_binary_json_private__mutable_data',
      'Value': '_q_binary_json_private__value',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QBinaryJsonPrivate.Base'. Python calls this for a name
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
    return [*__all__]
