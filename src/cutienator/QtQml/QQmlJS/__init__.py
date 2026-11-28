"""
The namespace 'QQmlJS' of Qt, a package of 'cutienator.QtQml':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQml import QQmlJS
  QQmlJS.DiagnosticMessage

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
    'DiagnosticMessage',
    'Managed',
    'Directives',
    'Engine',
    'MemoryPool',
    'SourceLocation',
    'AST',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_qml_j_s__diagnostic_message import DiagnosticMessage
  from .._q_qml_j_s__managed import Managed
  from .._q_qml_j_s__directives import Directives
  from .._q_qml_j_s__engine import Engine
  from .._q_qml_j_s__memory_pool import MemoryPool
  from .._q_qml_j_s__source_location import SourceLocation
  from . import AST
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'DiagnosticMessage': '_q_qml_j_s__diagnostic_message',
      'Managed': '_q_qml_j_s__managed',
      'Directives': '_q_qml_j_s__directives',
      'Engine': '_q_qml_j_s__engine',
      'MemoryPool': '_q_qml_j_s__memory_pool',
      'SourceLocation': '_q_qml_j_s__source_location',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('AST',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QQmlJS.DiagnosticMessage'. Python calls this for a name
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
